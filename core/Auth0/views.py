import json
from authlib.integrations.django_client import OAuth
from config import *
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

oauth = OAuth()
from os.path import join, dirname
with open(join(dirname(__file__), "config.txt")) as f:
    id, secret, domain=f.read().strip().split("\n")

oauth.register(
    "auth0",
    client_id=id,
    client_secret=secret,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{domain}/.well-known/openid-configuration",
)


def index(request):

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{domain}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": id,
            },
            quote_via=quote_plus,
        ),
    )
import json
from authlib.integrations.django_client import OAuth
from config import *
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

# TODO: Remove hardcoded urls, replace with reverse()


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
    print(request.build_absolute_uri(reverse("index")))
    return render(
        request,
        "home.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


def callback(request):
    print(request.build_absolute_uri(reverse("index")))
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect('http://127.0.0.1:8000/')


def login(request):
    print(request.build_absolute_uri(reverse("callback")))
    return oauth.auth0.authorize_redirect(
        request, 'https://127.0.0.1:8000/auth/callback')


def logout(request):
    print(request.build_absolute_uri(reverse("logout")))
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
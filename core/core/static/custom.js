function collapse() {
    var elements = document.getElementsByName('expandable');
    for(var i = 0; i < elements.length; i++) {
        elements[i].classList.toggle('expanded');
    }
}
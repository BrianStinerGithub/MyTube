function collapse() {
    const elements = document.getElementsByName('expandable');
    for(let i = 0; i < elements.length; i++) {
        elements[i].classList.toggle('expanded');
    }
}
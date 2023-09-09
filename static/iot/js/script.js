// meu_script.js

document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById("menu-icon");
    const menu = document.getElementById("menu");

    menuIcon.addEventListener("click", () => {
        menu.classList.toggle("hidden");
    });
});

// meu_script.js

document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById("menu-icon");
    const menu = document.getElementById("menu");

    menuIcon.addEventListener("click", () => {
        menu.classList.toggle("hidden");
    });
});

var mySwiper = new Swiper('.swiper-container', {
    // Configurações do carrossel
    slidesPerView: 1, // Exibe apenas 1 slide por vez
    spaceBetween: 10,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});



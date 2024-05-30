var swiper = new Swiper(".mySwiper", {
    onSlideChangeStart: function() {
        $('.swiper-container').height($(mySwiper.activeSlide()).height())
    },
    pagination: {
        el: ".swiper-pagination",
        type: "progressbar",
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

function calculateSlideHeights() {
    const slides = document.querySelectorAll('.swiper-slide');
    slides.forEach((slide, index) => {
        console.log(`Height of slide ${index + 1}: ${slide.clientHeight}px`);
    });
}
calculateSlideHeights();

document.getElementById('recalculate-height').addEventListener('click', function() {
    calculateSlideHeights();
});
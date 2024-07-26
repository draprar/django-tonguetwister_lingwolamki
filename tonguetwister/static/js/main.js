var mainSwiper = new Swiper(".mySwiper", {
    onSlideChangeStart: function() {
        $('.swiper-container').height($(mainSwiper.activeSlide()).height());
    },
    pagination: {
        el: ".swiper-pagination",
        type: "progressbar",
    },
});

var textSwiper = new Swiper('.textSwiper', {
    autoplay: {
        delay: 10000,
    },
    loop: true,
    pagination: {
        el: '.textSwiper-pagination',
        clickable: true,
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

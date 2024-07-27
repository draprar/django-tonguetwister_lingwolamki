document.addEventListener('DOMContentLoaded', function() {
    var textSwiper = new bootstrap.Carousel('#textSwiper', {
        interval: 3000,
        ride: 'carousel'
    });

    var mainSwiper = new Swiper(".mySwiper", {
        on: {
            init: function () {
                adjustMainSwiperHeight();
            },
            slideChange: function () {
                adjustMainSwiperHeight();
            }
        },
        pagination: {
            el: ".swiper-pagination",
            type: "progressbar",
        },
    });

    function adjustMainSwiperHeight() {
        let activeSlide = document.querySelector('.mySwiper .swiper-slide-active');
        if (activeSlide) {
            document.querySelector('.mySwiper').style.height = activeSlide.offsetHeight + 'px';
        }
    }

    function calculateSlideHeights() {
        const slides = document.querySelectorAll('.swiper-slide');
        slides.forEach((slide, index) => {
            console.log(`Height of slide ${index + 1}: ${slide.clientHeight}px`);
        });
    }

    adjustMainSwiperHeight();

    document.getElementById('recalculate-height').addEventListener('click', function() {
        calculateSlideHeights();
    });
});

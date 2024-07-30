document.addEventListener('DOMContentLoaded', function() {
    var textSwiper = new bootstrap.Carousel('#textSwiper', {
        interval: 5000,
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
        });
    }

    adjustMainSwiperHeight();

    document.getElementById('recalculate-height').addEventListener('click', function() {
        calculateSlideHeights();
    });
});

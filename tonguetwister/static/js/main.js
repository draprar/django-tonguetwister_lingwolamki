document.addEventListener('DOMContentLoaded', function() {
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

    function handleButtonClick() {
        if (navigator.vibrate) {
            navigator.vibrate(50);
        }
    }

    document.querySelectorAll('button').forEach(function(button) {
        button.addEventListener('click', handleButtonClick);
    });

});

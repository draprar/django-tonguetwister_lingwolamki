document.addEventListener('DOMContentLoaded', function() {
    var mainSwiper = new Swiper(".mySwiper", {
        on: {
            init: function () {
                calculateSlideHeights();
            },
            slideChange: function () {
                calculateSlideHeights();
            }
        },
        pagination: {
            el: ".swiper-pagination",
            type: "progressbar",
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        }
    });

    function calculateSlideHeights() {
        const slides = document.querySelectorAll('.swiper-slide');
        slides.forEach((slide) => {
            slide.style.height = 'auto';
            const slideHeight = slide.scrollHeight;
            slide.style.height = slideHeight + 'px';
        });

        const activeSlide = document.querySelector('.mySwiper .swiper-slide-active');
        if (activeSlide) {
            document.querySelector('.mySwiper').style.height = activeSlide.scrollHeight + 'px';
        }
    }

    const dynamicContentTriggers = [
        '.toggle-articulator-btn',
        '#load-more-btn',
        '#mirror-btn',
        '.toggle-exercise-btn',
        '#load-more-exercises-btn',
        '.toggle-twister-btn',
        '#load-more-twisters-btn',
        '#load-more-trivia-btn',
        '#load-more-facts-btn'
    ];

    dynamicContentTriggers.forEach(function(selector) {
        document.querySelectorAll(selector).forEach(function(button) {
            button.addEventListener('click', function() {
                setTimeout(calculateSlideHeights, 100);
            });
        });
    });

    const elementsToObserve = [
        '#video-container',
        '#card-articulator',
        '#card-exercises',
        '#card-twister',
        '#trivia-container',
        '#facts-container',
        '#congratulations-modal'
    ];

    elementsToObserve.forEach(function(selector) {
        const element = document.querySelector(selector);
        if (element) {
            const observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    if (mutation.attributeName === 'style' && element.style.display !== 'none') {
                        setTimeout(calculateSlideHeights, 100);
                    }
                });
            });
            observer.observe(element, { attributes: true });
        }
    });

    document.addEventListener('ajaxContentLoaded', function() {
        setTimeout(calculateSlideHeights, 100);
    });

    document.querySelectorAll('button').forEach(function(button) {
        button.addEventListener('click', function() {
            setTimeout(calculateSlideHeights, 100);
        });
    });

    calculateSlideHeights();
});

document.addEventListener('DOMContentLoaded', function () {
    const userAuthenticated = document.body.getAttribute('data-user-authenticated') === 'true';

    if (!userAuthenticated) {
        var beaverImg = document.getElementById('beaver-img');
        var speechBubble = document.getElementById('beaver-speech-bubble');
        var closeBubble = document.getElementById('close-speech-bubble');
        var beaverText = document.getElementById('beaver-text');
        var screenDim = document.getElementById('screen-dim');
        var beaverOptions = document.createElement('div');
        var currentStep = 0;

        screenDim.style.display = 'block';

        var steps = [
            { selector: ['#login', '#login-mobile'], text: 'Tu możesz się zarejestrować, aby stworzyć swój profil i spersonalizować swoją naukę 😎' },
            { selector: ['#contact', '#contact-mobile'], text: 'Tu możesz się z nami skontaktować, a ja zamienię się w chatbota 🧐' },
            { selector: ['#mic-btn', '#mic-btn-mobile'], text: 'Jeżeli tu klikniesz - rozpoczniesz nagrywanie swojego głosu 🎤' },
            { selector: '#mirror-btn-exercises', text: 'Dzięki tej opcji, możesz odpalić lusterko 🎥' },
            { selector: '#load-more-exercises-btn', text: 'A tutaj wygenerujesz nowe ćwiczenie do praktyki 💡' },
            { selector: 'body', text: 'Zaczynamy? Zamknij tę chmurkę, aby przejść do rozgrzewki 🚀', final: true }
        ];

        function getTargetElement(step) {
            let selector;

            switch (step) {
                case 0:
                    selector = window.innerWidth <= 991 ? '#login-mobile' : '#login';
                    break;
                case 1:
                    selector = window.innerWidth <= 991 ? '#contact-mobile' : '#contact';
                    break;
                case 2:
                    selector = window.innerWidth <= 991 ? '#mic-btn-mobile' : '#mic-btn';
                    break;
                default:
                    selector = steps[step].selector;
                    break;
            }

            return document.querySelector(selector);
        }


        function moveToStep(step) {
            if (step >= steps.length) return;

            var stepInfo = steps[step];
            var targetElement = getTargetElement(step);

            if (!targetElement) {
                console.error('Target element not found for step:', step);
                return;
            }

            var targetRect = targetElement.getBoundingClientRect();
            var viewportWidth = window.innerWidth;
            var viewportHeight = window.innerHeight;

            beaverImg.style.left = (viewportWidth / 4 - beaverImg.offsetWidth / 2) + 'px';
            beaverImg.style.top = (viewportHeight / 2 - beaverImg.offsetHeight / 2) + 'px';

            updateSpeechBubblePosition();
            beaverText.innerHTML = stepInfo.text;

            beaverOptions.innerHTML = '';
            var nextButton = document.createElement('button');
            nextButton.className = 'btn btn-dark';

            if (stepInfo.final) {
                nextButton.innerText = 'ZAMKNIJ';
                nextButton.addEventListener('click', function () {
                    var swiperInstance = document.querySelector('.mySwiper').swiper;
                    if (swiperInstance) {
                        swiperInstance.slideTo(0, 500);

                        swiperInstance.on('slideChangeTransitionEnd', function () {
                            closeTutorialAndShowPolishBeaver();
                        });
                    } else {
                        closeTutorialAndShowPolishBeaver();
                    }
                });
            } else {
                nextButton.innerText = 'DALEJ';
                nextButton.addEventListener('click', function () {
                    if (step === 2) {
                        var swiperInstance = document.querySelector('.mySwiper').swiper;
                        if (swiperInstance) {
                            swiperInstance.slideTo(2, 500);

                            swiperInstance.on('slideChangeTransitionEnd', function () {
                                moveToStep(step + 1);
                            });
                        } else {
                            moveToStep(step + 1);
                        }
                    } else {
                        moveToStep(step + 1);
                    }
                });
            }

            beaverOptions.appendChild(nextButton);
            speechBubble.appendChild(beaverOptions);
            speechBubble.style.display = 'block';

            removePulseEffectFromAllSteps();

            if (targetElement) {
                console.log(targetElement)
                targetElement.classList.add('highlight'); // Apply pulse effect
            }
            console.log(targetElement);
        }

        function removePulseEffectFromAllSteps() {
            steps.forEach((step, index) => {
                var target = getTargetElement(index);
                if (target) {
                    target.classList.remove('highlight');
                }
            });
        }

        function closeTutorialAndShowPolishBeaver() {
            closeTutorial();
            showPolishBeaver();
        }

        function closeTutorial() {
            speechBubble.style.display = 'none';
            screenDim.style.display = 'none';
            beaverImg.style.display = 'none';
            removePulseEffectFromAllSteps();
        }

        function startTutorial() {
            document.getElementById('beaver-yes').style.display = 'none';
            document.getElementById('beaver-no').style.display = 'none';

            screenDim.style.display = 'block';
            moveToStep(0);
        }

        function updateSpeechBubblePosition() {
            var beaverRect = beaverImg.getBoundingClientRect();
            speechBubble.style.left = (beaverRect.right + 20) + 'px';
            speechBubble.style.top = (beaverRect.top - speechBubble.offsetHeight - 20) + 'px';
        }

        var isDragging = false;
        var startX, startY;
        var offsetX, offsetY;

        beaverImg.addEventListener('mousedown', startDrag);
        document.addEventListener('mousemove', doDrag);
        document.addEventListener('mouseup', stopDrag);

        beaverImg.addEventListener('touchstart', startDrag);
        document.addEventListener('touchmove', doDrag);
        document.addEventListener('touchend', stopDrag);

        function startDrag(e) {
            startX = e.clientX || e.touches[0].clientX;
            startY = e.clientY || e.touches[0].clientY;
            offsetX = startX - beaverImg.getBoundingClientRect().left;
            offsetY = startY - beaverImg.getBoundingClientRect().top;
            isDragging = true;
            e.preventDefault();
        }

        function doDrag(e) {
            if (isDragging) {
                var x = (e.clientX || e.touches[0].clientX) - offsetX;
                var y = (e.clientY || e.touches[0].clientY) - offsetY;
                beaverImg.style.left = x + 'px';
                beaverImg.style.top = y + 'px';

                updateSpeechBubblePosition();
            }
        }

        function stopDrag() {
            if (isDragging) {
                isDragging = false;
            }
        }

        document.getElementById('beaver-yes').addEventListener('click', function () {
            startTutorial();
        });

        document.getElementById('beaver-no').addEventListener('click', function () {
            closeTutorialAndShowPolishBeaver();
        });

        closeBubble.addEventListener('click', function () {
            closeTutorialAndShowPolishBeaver();
        });

        var viewportWidth = window.innerWidth;
        beaverImg.style.left = (viewportWidth / 4 - beaverImg.offsetWidth / 2) + 'px';
        beaverImg.style.top = (window.innerHeight / 2 - beaverImg.offsetHeight / 2) + 'px';

        updateSpeechBubblePosition();
    } else {
        showPolishBeaver();
    }

    // --- POLISH BEAVER ---
    function showPolishBeaver() {
        var polishBeaverContainer = document.getElementById('polish-beaver-container');
        polishBeaverContainer.style.display = 'block';

        var speechBubble = document.getElementById('beaver-speech-bubble');
        speechBubble.style.display = 'none';
        var beaverImg = document.getElementById('beaver-img');
        beaverImg.style.display = 'none';

        var closeBubble = document.getElementById('close-speech-bubble');
        closeBubble.style.display = 'none';

        var beaverText = document.getElementById('beaver-text');
        beaverText.style.display = 'none';

        var polishBeaverImg = document.getElementById('polish-beaver-img');
        var polishSpeechBubble = document.getElementById('polish-beaver-speech-bubble');
        var polishCloseBubble = document.getElementById('polish-close-speech-bubble');
        var polishBeaverText = document.getElementById('polish-beaver-text');

        var offset = 0;
        var isDragging = false;
        var startX, startY;
        var offsetX, offsetY;
        var moved = false;
        var bubbleClosedManually = false;

        function randomizePosition() {
            var viewportWidth = window.innerWidth;
            var viewportHeight = window.innerHeight;
            var imgWidth = polishBeaverImg.offsetWidth;
            var imgHeight = polishBeaverImg.offsetHeight;

            var randomLeft = Math.random() * (viewportWidth - imgWidth);
            var randomTop = Math.random() * (viewportHeight - imgHeight);

            polishBeaverImg.style.left = randomLeft + 'px';
            polishBeaverImg.style.top = randomTop + 'px';

            updatePolishSpeechBubblePosition();
        }

        function updatePolishSpeechBubblePosition() {
            var beaverRect = polishBeaverImg.getBoundingClientRect();
            polishSpeechBubble.style.left = beaverRect.right + 'px';
            polishSpeechBubble.style.top = (beaverRect.top - polishSpeechBubble.offsetHeight - 20) + 'px';
        }

        randomizePosition();

        function fetchNewRecord() {
            fetch(`/load-more-old-polish/?offset=${offset}`)
                .then(response => response.json())
                .then(data => {
                    if (data.length > 0) {
                        var record = data[0];
                        polishBeaverText.innerHTML = `Czy wiesz, że staropolskie <strong>${record.old_text}</strong> to dziś <strong>${record.new_text}</strong>?`;
                    } else {
                        polishBeaverText.innerHTML = 'Brawo! Baza danych wyczyszczona 😲';
                    }
                    polishSpeechBubble.style.display = 'block';
                    offset++;
                })
                .catch(error => {
                    polishBeaverText.innerHTML = 'Error loading data.';
                    polishSpeechBubble.style.display = 'block';
                });
        }

        function startDrag(e) {
            startX = e.clientX || e.touches[0].clientX;
            startY = e.clientY || e.touches[0].clientY;
            offsetX = startX - polishBeaverImg.getBoundingClientRect().left;
            offsetY = startY - polishBeaverImg.getBoundingClientRect().top;
            isDragging = true;
            moved = false;
            e.preventDefault();
        }

        function doDrag(e) {
            if (isDragging) {
                var x = (e.clientX || e.touches[0].clientX) - offsetX;
                var y = (e.clientY || e.touches[0].clientY) - offsetY;
                polishBeaverImg.style.left = x + 'px';
                polishBeaverImg.style.top = y + 'px';
                moved = true;

                updatePolishSpeechBubblePosition();
            }
        }

        function stopDrag() {
            if (isDragging) {
                if (!moved && !bubbleClosedManually) {
                    fetchNewRecord();
                }
                isDragging = false;
            }
        }

        polishBeaverImg.addEventListener('mousedown', startDrag);
        document.addEventListener('mousemove', doDrag);
        document.addEventListener('mouseup', stopDrag);

        polishBeaverImg.addEventListener('touchstart', startDrag);
        document.addEventListener('touchmove', doDrag);
        document.addEventListener('touchend', stopDrag);

        polishCloseBubble.addEventListener('click', function () {
            polishSpeechBubble.style.display = 'none';
            polishBeaverImg.style.display = 'none';
            bubbleClosedManually = true;
        });

        polishBeaverImg.addEventListener('click', function () {
            if (bubbleClosedManually && !moved) {
                fetchNewRecord();
                bubbleClosedManually = false;
            }
        });
    }
});

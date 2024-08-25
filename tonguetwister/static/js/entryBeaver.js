document.addEventListener('DOMContentLoaded', function () {
    var beaverImg = document.getElementById('beaver-img');
    var speechBubble = document.getElementById('beaver-speech-bubble');
    var closeBubble = document.getElementById('close-speech-bubble');
    var beaverText = document.getElementById('beaver-text');
    var screenDim = document.getElementById('screen-dim');
    var beaverOptions = document.createElement('div');
    var arrow = document.createElement('div');
    var currentStep = 0;

    // Hide the buttons initially
    document.getElementById('beaver-yes').style.display = 'inline-block';
    document.getElementById('beaver-no').style.display = 'inline-block';

    // Dim the screen when the DOM is loaded
    screenDim.style.display = 'block';

    // Arrow styling
    arrow.id = 'beaver-arrow';
    arrow.style.position = 'absolute';
    arrow.style.width = '0';
    arrow.style.height = '0';
    arrow.style.borderLeft = '10px solid transparent';
    arrow.style.borderRight = '10px solid transparent';
    arrow.style.borderBottom = '20px solid black';
    arrow.style.display = 'none';
    document.body.appendChild(arrow);

    var steps = [
        { selector: '#login', text: 'Kliknij, aby się zarejestrować' },
        { selector: '#contact', text: 'Kliknij, aby się z nami skontaktować' },
        { selector: '#mic-btn', text: 'Kliknij, aby nagrać swój głos' },
        { selector: '#mirror-btn-articulators', text: 'Kliknij, aby włączyć podgląd' },
        { selector: '#load-more-btn', text: 'Kliknij, aby zmienić ćwiczenie' },
        { selector: 'body', text: 'Ekstra! Skończyliśmy nasz krótki przewodnik, pora na przygodę? :)', final: true }
    ];

    function moveToStep(step) {
        if (step >= steps.length) return;

        var stepInfo = steps[step];
        var targetElement = document.querySelector(stepInfo.selector);

        if (!targetElement) return;

        // Position the arrow pointing to the target element
        var targetRect = targetElement.getBoundingClientRect();
        var viewportWidth = window.innerWidth;
        var viewportHeight = window.innerHeight;

        arrow.style.left = (targetRect.left + targetRect.width / 2 - 10) + 'px';
        arrow.style.top = (targetRect.top - 30) + 'px';
        arrow.style.display = 'block';

        // Center the beaver on the screen
        beaverImg.style.left = (viewportWidth / 2 - beaverImg.offsetWidth / 2) + 'px';
        beaverImg.style.top = (viewportHeight / 2 - beaverImg.offsetHeight / 2) + 'px';

        updateSpeechBubblePosition();
        beaverText.innerHTML = stepInfo.text;

        // Adjust the buttons in the beaverOptions div
        beaverOptions.innerHTML = '';
        var nextButton = document.createElement('button');
        nextButton.className = 'btn btn-success';

        if (stepInfo.final) {
            nextButton.innerText = 'ZAMKNIJ';
            nextButton.addEventListener('click', function () {
                closeTutorial();
            });
        } else {
            nextButton.innerText = 'DALEJ';
            nextButton.addEventListener('click', function () {
                moveToStep(step + 1);
            });
        }

        beaverOptions.appendChild(nextButton);

        if (step >= 0) {
            var prevButton = document.createElement('button');
            prevButton.className = 'btn btn-danger';
            prevButton.innerText = 'WRÓĆ';
            prevButton.addEventListener('click', function () {
                moveToStep(step - 1);
            });
            beaverOptions.appendChild(prevButton);
        }

        speechBubble.appendChild(beaverOptions);
        speechBubble.style.display = 'block';
    }

    function closeTutorial() {
        speechBubble.style.display = 'none';
        screenDim.style.display = 'none';
        beaverImg.style.display = 'none';
        arrow.style.display = 'none';
    }

    function startTutorial() {
        // Hide "TAK" and "NIE" buttons
        document.getElementById('beaver-yes').style.display = 'none';
        document.getElementById('beaver-no').style.display = 'none';

        screenDim.style.display = 'block';
        moveToStep(0);
    }

    function updateSpeechBubblePosition() {
        var beaverRect = beaverImg.getBoundingClientRect();
        speechBubble.style.left = beaverRect.right + 'px';
        speechBubble.style.top = (beaverRect.top - speechBubble.offsetHeight - 20) + 'px';
    }

    // Initialize the tutorial when the user clicks "TAK"
    document.getElementById('beaver-yes').addEventListener('click', function () {
        startTutorial();
    });

    // Ensure the "NIE" button works like closing the beaver
    document.getElementById('beaver-no').addEventListener('click', function () {
        closeTutorial();
    });

    // Ensure the close button works
    closeBubble.addEventListener('click', function () {
        closeTutorial();
    });

    // Center the beaver initially
    var viewportWidth = window.innerWidth;
    var viewportHeight = window.innerHeight;
    beaverImg.style.left = (viewportWidth / 2 - beaverImg.offsetWidth / 2) + 'px';
    beaverImg.style.top = (viewportHeight / 2 - beaverImg.offsetHeight / 2) + 'px';

    updateSpeechBubblePosition();
});

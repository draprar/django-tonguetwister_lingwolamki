document.addEventListener('DOMContentLoaded', function () {
    var beaverImg = document.getElementById('beaver-img');
    var speechBubble = document.getElementById('beaver-speech-bubble');
    var closeBubble = document.getElementById('close-speech-bubble');
    var beaverText = document.getElementById('beaver-text');

    speechBubble.style.display = 'block';

    var offset = 0;
    var isDragging = false;
    var startX, startY;
    var offsetX, offsetY;
    var moved = false;
    var bubbleClosedManually = false;

    function randomizePosition() {
        var viewportWidth = window.innerWidth;
        var viewportHeight = window.innerHeight;
        var imgWidth = beaverImg.offsetWidth;
        var imgHeight = beaverImg.offsetHeight;

        var randomLeft = Math.random() * (viewportWidth - imgWidth);
        var randomTop = Math.random() * (viewportHeight - imgHeight);

        beaverImg.style.left = randomLeft + 'px';
        beaverImg.style.top = randomTop + 'px';

        updateSpeechBubblePosition();
    }

    function updateSpeechBubblePosition() {
        var beaverRect = beaverImg.getBoundingClientRect();
        speechBubble.style.left = beaverRect.right + 'px';
        speechBubble.style.top = (beaverRect.top - speechBubble.offsetHeight - 20) + 'px';
    }

    randomizePosition();

    function fetchNewRecord() {
        fetch(`/load-more-old-polish/?offset=${offset}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    var record = data[0];
                    beaverText.innerHTML = `Czy wiesz, że staropolskie <strong>${record.old_text}</strong> to dziś <strong>${record.new_text}</strong>?`;
                } else {
                    beaverText.innerHTML = 'Brawo! Baza danych wyczyszczona 😲';
                }
                speechBubble.style.display = 'block';
                offset++;
            })
            .catch(error => {
                console.error('Error fetching new record:', error);
                beaverText.innerHTML = 'Error loading data.';
                speechBubble.style.display = 'block';
            });
    }

    function startDrag(e) {
        startX = e.clientX || e.touches[0].clientX;
        startY = e.clientY || e.touches[0].clientY;
        offsetX = startX - beaverImg.getBoundingClientRect().left;
        offsetY = startY - beaverImg.getBoundingClientRect().top;
        isDragging = true;
        moved = false;
        e.preventDefault();
    }

    function doDrag(e) {
        if (isDragging) {
            var x = (e.clientX || e.touches[0].clientX) - offsetX;
            var y = (e.clientY || e.touches[0].clientY) - offsetY;
            beaverImg.style.left = x + 'px';
            beaverImg.style.top = y + 'px';
            moved = true;

            updateSpeechBubblePosition();
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

    beaverImg.addEventListener('mousedown', startDrag);
    document.addEventListener('mousemove', doDrag);
    document.addEventListener('mouseup', stopDrag);

    beaverImg.addEventListener('touchstart', startDrag);
    document.addEventListener('touchmove', doDrag);
    document.addEventListener('touchend', stopDrag);

    closeBubble.addEventListener('click', function () {
        speechBubble.style.display = 'none';
        bubbleClosedManually = true;
    });

    beaverImg.addEventListener('click', function () {
        if (bubbleClosedManually && !moved) {
        fetchNewRecord();
        bubbleClosedManually = false;
        }
    })
});
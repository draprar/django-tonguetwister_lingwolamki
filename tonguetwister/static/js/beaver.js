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

    function randomizePosition() {
        var viewportWidth = window.innerWidth;
        var viewportHeight = window.innerHeight;
        var imgWidth = beaverImg.offsetWidth;
        var imgHeight = beaverImg.offsetHeight;

        var randomLeft = Math.random() * (viewportWidth - imgWidth);
        var randomTop = Math.random() * (viewportHeight - imgHeight);

        beaverImg.style.left = randomLeft + 'px';
        beaverImg.style.top = randomTop + 'px';
    }

    randomizePosition();

    beaverImg.addEventListener('mousedown', function (e) {
        startX = e.clientX;
        startY = e.clientY;
        offsetX = e.clientX - beaverImg.getBoundingClientRect().left;
        offsetY = e.clientY - beaverImg.getBoundingClientRect().top;
        isDragging = true;
        moved = false;
        e.preventDefault();
    });

    document.addEventListener('mousemove', function (e) {
        if (isDragging) {
            var deltaX = e.clientX - startX;
            var deltaY = e.clientY - startY;

            if (Math.abs(deltaX) > 3 || Math.abs(deltaY) > 3) {
                moved = true;
                var x = e.clientX - offsetX;
                var y = e.clientY - offsetY;
                beaverImg.style.left = x + 'px';
                beaverImg.style.top = y + 'px';
            }
        }
    });

    document.addEventListener('mouseup', function () {
        if (isDragging && !moved) {
            fetch(`/load-more-old-polish/?offset=${offset}`)
                .then(response => response.json())
                .then(data => {
                    if (data.length > 0) {
                        var record = data[0];
                        beaverText.innerHTML = `Czy wiesz, że staropolskie <strong>${record.old_text}</strong> to dziś <strong>${record.new_text}</strong>?`;
                    } else {
                        beaverText.innerHTML = 'Brak danych.';
                    }
                    speechBubble.style.display = 'block';
                    offset++;
                })
                .catch(error => {
                    console.error('Error fetching new record:', error);
                    beaverText.innerHTML = 'Wystąpił błąd przy ładowaniu danych.';
                    speechBubble.style.display = 'block';
                });
        }
        isDragging = false;
    });

    closeBubble.addEventListener('click', function () {
        speechBubble.style.display = 'none';
    });
});

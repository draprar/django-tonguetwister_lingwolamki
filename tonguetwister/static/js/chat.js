document.addEventListener('DOMContentLoaded', function () {
    const beaverImg = document.getElementById('chat-beaver-img');
    const speechBubble = document.getElementById('chat-speech-bubble');
    const beaverContainer = document.getElementById('chat-beaver-container');

    let isDragging = false;
    let offsetX, offsetY;

    function startDrag(e) {
        isDragging = true;
        const rect = beaverContainer.getBoundingClientRect();
        offsetX = (e.clientX || e.touches[0].clientX) - rect.left;
        offsetY = (e.clientY || e.touches[0].clientY) - rect.top;
        e.preventDefault();
    }

    function doDrag(e) {
        if (isDragging) {
            const x = (e.clientX || e.touches[0].clientX) - offsetX;
            const y = (e.clientY || e.touches[0].clientY) - offsetY;
            beaverContainer.style.left = x + 'px';
            beaverContainer.style.top = y + 'px';
        }
    }

    function stopDrag() {
        isDragging = false;
    }

    beaverContainer.addEventListener('mousedown', startDrag);
    document.addEventListener('mousemove', doDrag);
    document.addEventListener('mouseup', stopDrag);

    beaverContainer.addEventListener('touchstart', startDrag);
    document.addEventListener('touchmove', doDrag);
    document.addEventListener('touchend', stopDrag);

    document.getElementById('chat-send-button').addEventListener('click', function () {
        var userMessage = document.getElementById('chat-user-input').value;
        fetch('/chatbot/?message=' + encodeURIComponent(userMessage))
            .then(response => response.json())
            .then(data => {
                document.getElementById('chat-chat-text').innerText = data.response;
                document.getElementById('chat-user-input').value = '';
            });
    });

    });
});
document.addEventListener('DOMContentLoaded', () => {
    const mirrorBtn = document.getElementById('mirror-btn-exercises');
    const videoContainer = document.getElementById('video-container-exercises');
    const videoPreview = document.getElementById('video-preview-exercises');

    let stream;

    mirrorBtn.addEventListener('click', () => {
        if (!videoContainer.style.display || videoContainer.style.display === 'none') {
            startVideoStream();
        } else {
            stopVideoStream();
        }
    });

    function startVideoStream() {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' }, audio: false })
            .then(mediaStream => {
                stream = mediaStream;
                videoPreview.srcObject = stream;
                videoContainer.style.display = 'block';
                mirrorBtn.textContent = '🛑 Zatrzymaj lusterko';
            })
            .catch(error => {
                console.error('Error accessing media devices.', error);
            });
    }

    function stopVideoStream() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            videoPreview.srcObject = null;
            videoContainer.style.display = 'none';
            mirrorBtn.textContent = '📷 Otwórz lusterko';
        }
    }
});

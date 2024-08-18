document.addEventListener('DOMContentLoaded', () => {
    const micBtn = document.getElementById('mic-btn');
    const micBtnMobile = document.getElementById('mic-btn-mobile');
    const micImg = document.getElementById('mic-img');

    let mediaRecorder;
    let audioChunks = [];
    let recordingAudio = false;
    let currentStream;

    micBtn.addEventListener('click', () => {
        if (!recordingAudio) {
            startAudioRecording();
        } else {
            stopAudioRecording();
        }
    });

    micBtnMobile.addEventListener('click', () => {
        if (!recordingAudio) {
            startAudioRecording();
        } else {
            stopAudioRecording();
        }
    });

    function startAudioRecording() {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                recordingAudio = true;
                currentStream = stream;
                micBtn.textContent = '🛑 Zatrzymaj nagranie';
                micImg.src = micOffSrc;
                micImg.alt = "mic-off";

                audioChunks = [];
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();

                mediaRecorder.addEventListener('dataavailable', event => {
                    audioChunks.push(event.data);
                });

                mediaRecorder.addEventListener('stop', () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                    confirmSave(audioBlob, 'audio.wav');
                    recordingAudio = false;
                    resetButton();
                    stopMediaStream();
                });
            })
            .catch(err => {
                console.error('Error accessing audio stream:', err);
                alert('Błąd przy próbie dostępu do mikrofonu. Proszę sprawdzić uprawnienia.');
            });
    }

    function stopAudioRecording() {
        if (mediaRecorder && recordingAudio) {
            mediaRecorder.stop();
        }
    }

    function stopMediaStream() {
        if (currentStream) {
            currentStream.getTracks().forEach(track => track.stop());
            currentStream = null;
        }
    }

    function confirmSave(blob, filename) {
        const save = confirm("Czy chcesz zapisać nagranie?");
        if (save) {
            downloadBlob(blob, filename);
        }
    }

    function downloadBlob(blob, filename) {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(() => {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 100);
    }

    function resetButton() {
        micBtn.textContent = '🎙️ Nagraj swój głos';
        micImg.src = micOnSrc;
        micImg.alt = "mic-on";
    }
});

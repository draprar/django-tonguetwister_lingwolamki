document.addEventListener('DOMContentLoaded', () => {
    const micBtn = document.getElementById('mic-btn');
    const micBtnMobile = document.getElementById('mic-btn-mobile');
    const micImg = document.getElementById('mic-img');

    let mediaRecorder;
    let audioChunks = [];
    let recordingAudio = false;
    let currentStream;

    async function startAudioRecording() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            recordingAudio = true;
            currentStream = stream;

            updateUIForRecording(true);

            audioChunks = [];
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            mediaRecorder.addEventListener('dataavailable', event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener('stop', () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                confirmSave(audioBlob, 'audio.wav');
                resetRecordingState();
            });

        } catch (err) {
            console.error('Error accessing audio stream:', err);
            alert('Błąd przy próbie dostępu do mikrofonu. Proszę sprawdzić uprawnienia.');
        }
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
        if (confirm("Czy chcesz zapisać nagranie?")) {
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
            URL.revokeObjectURL(url);
        }, 100);
    }

    function updateUIForRecording(isRecording) {
        if (isRecording) {
            micBtn.textContent = '🛑 Zatrzymaj nagranie';
            micImg.src = micOffSrc;
            micImg.alt = "mic-off";
        } else {
            micBtn.textContent = '🎙️ Nagraj swój głos';
            micImg.src = micOnSrc;
            micImg.alt = "mic-on";
        }
    }

    function resetRecordingState() {
        recordingAudio = false;
        stopMediaStream();
        updateUIForRecording(false);
    }

    micBtn.addEventListener('click', () => {
        recordingAudio ? stopAudioRecording() : startAudioRecording();
    });

    micBtnMobile.addEventListener('click', () => {
        recordingAudio ? stopAudioRecording() : startAudioRecording();
    });
});

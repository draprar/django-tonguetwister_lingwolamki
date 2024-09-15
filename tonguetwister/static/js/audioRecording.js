document.addEventListener('DOMContentLoaded', () => {
    const micBtn = document.getElementById('mic-btn');
    const micBtnMobile = document.getElementById('mic-btn-mobile');
    const micImg = document.getElementById('mic-img');
    const micOnSrc = window.micConfig.micOnSrc;
    const micOffSrc = window.micConfig.micOffSrc;

    let audioContext;
    let mediaRecorder;
    let audioChunks = [];
    let recordingAudio = false;
    let currentStream;

    async function startAudioRecording() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            recordingAudio = true;
            currentStream = stream;

            audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const source = audioContext.createMediaStreamSource(stream);
            const processor = audioContext.createScriptProcessor(4096, 1, 1);

            processor.onaudioprocess = function(e) {
                const inputData = e.inputBuffer.getChannelData(0);
                const buffer = new Int16Array(inputData.length);

                for (let i = 0; i < inputData.length; i++) {
                    buffer[i] = Math.max(-1, Math.min(1, inputData[i])) * 0x7FFF;
                }
                audioChunks.push(buffer);
            };

            source.connect(processor);
            processor.connect(audioContext.destination);

            updateUIForRecording(true);
        } catch (err) {
            console.error('Error accessing audio stream:', err);
            alert('Błąd przy próbie dostępu do mikrofonu. Proszę sprawdzić uprawnienia.');
        }
    }

    function stopAudioRecording() {
        if (recordingAudio) {
            recordingAudio = false;
            audioContext.close();

            const mp3Blob = exportMP3(audioChunks);
            audioChunks = [];
            confirmSave(mp3Blob, 'audio.mp3');
            resetRecordingState();
        }
    }

    function exportMP3(chunks) {
        const mp3Encoder = new lamejs.Mp3Encoder(1, 44100, 128);
        const mp3Data = [];

        chunks.forEach(chunk => {
            const mp3buf = mp3Encoder.encodeBuffer(chunk);
            if (mp3buf.length > 0) {
                mp3Data.push(new Int8Array(mp3buf));
            }
        });

        const mp3buf = mp3Encoder.flush();
        if (mp3buf.length > 0) {
            mp3Data.push(new Int8Array(mp3buf));
        }

        return new Blob(mp3Data, { type: 'audio/mp3' });
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

    function toggleRecording() {
        recordingAudio ? stopAudioRecording() : startAudioRecording();
    }

    micBtn.addEventListener('click', toggleRecording);
    micBtnMobile.addEventListener('click', toggleRecording);

    window.addEventListener('beforeunload', () => {
        if (currentStream) {
            currentStream.getTracks().forEach(track => track.stop());
        }
        micBtn.removeEventListener('click', toggleRecording);
        micBtnMobile.removeEventListener('click', toggleRecording);
    })
});

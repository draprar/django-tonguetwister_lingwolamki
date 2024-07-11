document.addEventListener('htmx:afterSettle', function(evt) {
    let records = document.querySelectorAll('#twisters-container .twister');

    if (records.length > 1) {
        records[records.length - 2].remove();
    }

    let loadMoreBtn = document.getElementById('recalculate-height');
    if (!loadMoreBtn) {
        let loadMoreContainer = document.getElementById('load-more');
        if (loadMoreContainer) {
            loadMoreContainer.style.display = 'none';
        }

        if (records.length > 0) {
            records[records.length - 1].style.display = 'none';
        }

        const successSound = document.getElementById('success-sound-twisters');
        if (successSound) {
            successSound.play().catch(error => {
                console.error('Error playing success sound:', error);
            });
        }
    }
});


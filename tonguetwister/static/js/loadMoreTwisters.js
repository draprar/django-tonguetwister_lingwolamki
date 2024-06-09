document.addEventListener('htmx:afterSettle', function(evt) {
    let records = document.querySelectorAll('#twisters-container .twister');

    if (records.length > 1) {
        records[records.length - 2].style.display = 'none';
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

        let cardTwisters = document.getElementById('card-twisters');
        if (cardTwisters) {
            cardTwisters.style.display = 'block';
        }
    }
});


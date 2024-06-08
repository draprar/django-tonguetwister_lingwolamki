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

        let endMessage = document.createElement('p');
        endMessage.className = 'col-md-16 fs-4 text-danger';
        endMessage.innerHTML = '<strong>Finisz bazy łamańców :o Chapeu bas!</strong>';
        document.getElementById('twisters-container').appendChild(endMessage);
    }
});


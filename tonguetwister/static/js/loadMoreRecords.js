document.addEventListener('DOMContentLoaded', function() {
    let loadMoreBtn = document.getElementById('load-more-btn');
    let offset = parseInt(loadMoreBtn.getAttribute('data-offset'));
    let url = loadMoreBtn.getAttribute('data-url');

    loadMoreBtn.addEventListener('click', function() {
        $.ajax({
            url: url,
            data: { 'offset': offset },
            dataType: 'json',
            success: function(data) {
                if (data.length > 0) {
                    for (let i = 0; i < data.length; i++) {
                        $('#records-container').append('<div class="record col-md-16 fs-4">' + data[i].text + '</div>');
                    }
                    offset += data.length;

                    let records = $('#records-container .record');
                    while (records.length > 1) {
                        records.first().remove();
                        records = $('#records-container .record');
                    }

                } else {
                    $('#load-more-btn').hide();
                    $('#records-container .record').hide();
                    $('.card').show();
                }
            }
        });
    });

    function changeRecordsButtonText() {
        var button = document.getElementById("load-more-btn");
        button.textContent = "Więcej";
    }
    document.getElementById("load-more-btn").onclick = changeRecordsButtonText;
});
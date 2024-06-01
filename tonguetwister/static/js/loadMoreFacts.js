document.addEventListener('DOMContentLoaded', function() {
    let loadMoreBtn = document.getElementById('load-more-funfacts-btn');
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
                        $('#trivia-container').append('<div class="one-trivia col-md-16 fs-4">' + data[i].text + '</div>');
                    }
                    offset += data.length;
                } else {
                    $('#load-more-funfacts-btnn').hide();
                }
            }
        });
    });

    function changeFactsButtonText() {
        var button = document.getElementById("load-more-funfacts-btn");
        button.textContent = "Więcej ciekawostek";
    }
    document.getElementById("load-more-funfacts-btn").onclick = changeFactsButtonText;
});
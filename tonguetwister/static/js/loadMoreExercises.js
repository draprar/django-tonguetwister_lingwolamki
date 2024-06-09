document.addEventListener('DOMContentLoaded', function() {
    let loadMoreBtn = document.getElementById('load-more-exercises-btn');
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
                        $('#exercises-container').append('<div class="exercise col-md-16 fs-4">' + data[i].text + '</div>');
                    }
                    offset += data.length;

                    let exercises = $('#exercises-container .exercise');
                    while (exercises.length > 1) {
                        exercises.first().remove();
                        exercises = $('#exercises-container .exercise');
                    }

                } else {
                    $('#card-exercises').show();
                    $('#load-more-exercises-btn').hide();
                    $('#exercises-container .exercise').hide();
                }
            }
        });
    });

    function changeExercisesButtonText() {
        var button = document.getElementById("load-more-exercises-btn");
        button.textContent = "Więcej";
    }
    document.getElementById("load-more-exercises-btn").onclick = changeExercisesButtonText;
});
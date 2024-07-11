document.addEventListener('DOMContentLoaded', function() {
    let triviaBtn = document.getElementById('load-more-trivia-btn');
    let triviaOffset = parseInt(triviaBtn.getAttribute('data-offset'));
    let triviaUrl = triviaBtn.getAttribute('data-url');

    let factsBtn = document.getElementById('load-more-facts-btn');
    let factsOffset = parseInt(factsBtn.getAttribute('data-offset'));
    let factsUrl = factsBtn.getAttribute('data-url');

    let triviaComplete = false;
    let factsComplete = false;

    triviaBtn.addEventListener('click', function() {
        $.ajax({
            url: triviaUrl,
            data: { 'offset': triviaOffset },
            dataType: 'json',
            success: function(data) {
                if (data.length > 0) {
                    $('#trivia-container').empty();
                    $('#facts-container').empty();
                    for (let i = 0; i < data.length; i++) {
                        $('#trivia-container').append('<div class="trivia col-md-16 fs-4">' + data[i].text + '</div>');
                    }
                    triviaOffset += data.length;

                } else {
                    triviaComplete = true;
                    $('#load-more-trivia-btn').hide();
                    $('#trivia-container .trivia').hide();
                    checkCompletion();
                }
            }
        });
    });

    factsBtn.addEventListener('click', function() {
        $.ajax({
            url: factsUrl,
            data: { 'offset': factsOffset },
            dataType: 'json',
            success: function(data) {
                if (data.length > 0) {
                    $('#facts-container').empty();
                    $('#trivia-container').empty();
                    for (let i = 0; i < data.length; i++) {
                        $('#facts-container').append('<br><div class="fact col-md-16 fs-4">' + data[i].text + '</div>');
                    }
                    factsOffset += data.length;

                } else {
                    factsComplete = true;
                    $('#load-more-facts-btn').hide();
                    $('#facts-container .fact').hide();
                    checkCompletion();
                }
            }
        });
    });

    function checkCompletion() {
        if (triviaComplete && factsComplete) {
            showCongratulationsModal();
        }
    }

    function showCongratulationsModal() {
        let modal = document.getElementById('congratulations-modal');
        let span = modal.getElementsByClassName('close')[0];

        modal.style.display = 'block';

        span.onclick = function() {
            modal.style.display = 'none';
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        }

        const successSound = document.getElementById('success-sound-end');
        successSound.play();
    }

    function changeTriviaButtonText() {
        var button = document.getElementById("load-more-trivia-btn");
        button.textContent = "Więcej porad";
    }
    document.getElementById("load-more-trivia-btn").onclick = changeTriviaButtonText;

    function changeFactsButtonText() {
        var button = document.getElementById("load-more-facts-btn");
        button.textContent = "Więcej ciekawostek";
    }
    document.getElementById("load-more-facts-btn").onclick = changeFactsButtonText;

});

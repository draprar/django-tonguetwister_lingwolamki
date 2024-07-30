document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    function handleToggleButtonClick(event) {
        const button = event.target.closest('.toggle-twister-btn');
        if (!button || button.disabled) return;

        const twisterId = button.dataset.id;
        const action = button.textContent.trim();
        button.disabled = true;

        if (action === 'Dodaj do powtórek') {
            fetch(`/add-twister/${twisterId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                button.disabled = false;
                if (data.status === 'Twister added') {
                    button.disabled = true;
                    button.textContent = 'W powtórkach 😄';
                    button.classList.replace('btn-success', 'btn-secondary');
                }
            })
            .catch(error => {
                button.disabled = false;
            });
        } else if (action === 'W powtórkach 😄') {
            button.disabled = true;
        }
    }

    function addTwisterToDOM(twister, isAuthenticated) {
        if (document.getElementById(`twister-${twister.id}`)) {
            return;
        }

        const twisterContainer = document.createElement('div');
        twisterContainer.id = `twisters-container-${twister.id}`;
        twisterContainer.classList.add('twisters-container', 'col-md-16', 'fs-4');

        const twisterDiv = document.createElement('div');
        twisterDiv.classList.add('twister');
        twisterDiv.textContent = twister.text;
        twisterDiv.id = `twister-${twister.id}`;

        twisterContainer.appendChild(twisterDiv);

        if (isAuthenticated) {
            const button = document.createElement('button');
            button.classList.add('btn', 'toggle-twister-btn');
            button.dataset.id = twister.id;
            button.textContent = twister.is_added ? 'W powtórkach 😄' : 'Dodaj do powtórek';
            button.classList.add(twister.is_added ? 'btn-secondary' : 'btn-success');
            button.disabled = twister.is_added;

            button.addEventListener('click', handleToggleButtonClick);

            twisterContainer.appendChild(button);
        }

        document.getElementById('twisters-container').appendChild(twisterContainer);
    }

    const twistersContainer = document.getElementById('twisters-container');
    if (twistersContainer) {
        twistersContainer.addEventListener('click', function(event) {
            if (event.target.matches('.toggle-twister-btn')) {
                handleToggleButtonClick(event);
            }
        });
    }

    let loadMoreBtn = document.getElementById('load-more-twisters-btn');
    let offset, url;
    if (loadMoreBtn) {
        offset = parseInt(loadMoreBtn.getAttribute('data-offset'));
        url = loadMoreBtn.getAttribute('data-url');
        const isAuthenticated = loadMoreBtn.getAttribute('data-authenticated') === 'true';

        loadMoreBtn.addEventListener('click', function() {
            fetch(`${url}?offset=${offset}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                document.getElementById('twisters-container').innerHTML = '';

                if (data.length > 0) {
                    data.forEach(twister => addTwisterToDOM(twister, isAuthenticated));
                    offset += data.length;
                    loadMoreBtn.setAttribute('data-offset', offset.toString());
                } else {
                    document.getElementById('card-twister').style.display = 'block';
                    loadMoreBtn.style.display = 'none';

                    const successSound = document.getElementById('success-sound-twisters');
                    successSound.play();
                }
            })
            .catch(error => {
            });
        });
    } else {
        document.querySelectorAll('.delete-twister-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                const twisterId = this.getAttribute('data-id');
                fetch(`/delete-twister/${twisterId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json'
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'Twister deleted') {
                        location.reload();
                    }
                })
                .catch(error => {
                });
            });
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    function handleToggleButtonClick(event) {
        const button = event.target.closest('.toggle-articulator-btn');
        if (!button || button.disabled) return;

        const articulatorId = button.dataset.id;
        const action = button.textContent.trim();
        button.disabled = true;

        if (action === 'Dodaj do powtórek') {
            fetch(`/add-articulator/${articulatorId}/`, {
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
                if (data.status === 'Articulator added') {
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

    function addArticulatorToDOM(articulator, isAuthenticated) {
        if (document.getElementById(`articulator-${articulator.id}`)) {
            return;
        }

        const articulatorContainer = document.createElement('div');
        articulatorContainer.id = `articulators-container-${articulator.id}`;
        articulatorContainer.classList.add('articulators-container', 'col-md-16', 'fs-4');

        const articulatorDiv = document.createElement('div');
        articulatorDiv.classList.add('articulator');
        articulatorDiv.textContent = articulator.text;
        articulatorDiv.id = `articulator-${articulator.id}`;

        articulatorContainer.appendChild(articulatorDiv);

        if (isAuthenticated) {
            const button = document.createElement('button');
            button.classList.add('btn', 'toggle-articulator-btn');
            button.dataset.id = articulator.id;
            button.textContent = articulator.is_added ? 'W powtórkach 😄' : 'Dodaj do powtórek';
            button.classList.add(articulator.is_added ? 'btn-secondary' : 'btn-success');
            button.disabled = articulator.is_added;

            button.addEventListener('click', handleToggleButtonClick);

            articulatorContainer.appendChild(button);
        }

        document.getElementById('articulators-container').appendChild(articulatorContainer);
    }

    const articulatorsContainer = document.getElementById('articulators-container');
    if (articulatorsContainer) {
        articulatorsContainer.addEventListener('click', function(event) {
            if (event.target.matches('.toggle-articulator-btn')) {
                handleToggleButtonClick(event);
            }
        });
    }

    let loadMoreBtn = document.getElementById('load-more-btn');
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
                document.getElementById('articulators-container').innerHTML = '';

                if (data.length > 0) {
                    data.forEach(articulator => addArticulatorToDOM(articulator, isAuthenticated));
                    offset += data.length;
                    loadMoreBtn.setAttribute('data-offset', offset.toString());
                } else {
                    document.getElementById('card-articulator').style.display = 'block';
                    loadMoreBtn.style.display = 'none';

                    const successSound = document.getElementById('success-sound-articulators');
                    successSound.play();

                    if (navigator.vibrate) {
                        navigator.vibrate(200);
                    }

                }
            })
            .catch(error => {
            });
        });
    } else {
        document.querySelectorAll('.delete-articulator-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                const articulatorId = this.getAttribute('data-id');
                fetch(`/delete-articulator/${articulatorId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json'
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'Articulator deleted') {
                        location.reload();
                    }
                })
                .catch(error => {
                });
            });
        });
    }
});
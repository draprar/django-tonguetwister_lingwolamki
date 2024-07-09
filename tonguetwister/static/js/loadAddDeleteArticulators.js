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
                console.log('Response data for adding:', data);
                button.disabled = false;
                if (data.status === 'Articulator added') {
                    button.textContent = 'W powtórkach 😄';
                    button.classList.replace('btn-success', 'btn-secondary');
                } else if (data.status === 'Duplicate articulator') {
                    alert('This articulator is already added.');
                } else {
                    alert('Error adding articulator: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error adding articulator:', error);
                button.disabled = false;
            });
        } else if (action === 'W powtórkach 😄') {
            button.disabled = true;
        }
    }

    function addArticulatorToDOM(articulator) {
        if (document.getElementById(`articulator-${articulator.id}`)) {
            console.log(`Articulator ${articulator.id} already exists`);
            return;
        }

        const articulatorContainer = document.createElement('div');
        articulatorContainer.id = `articulator-container-${articulator.id}`;
        articulatorContainer.classList.add('articulator-container', 'col-md-16', 'fs-4');

        const articulatorDiv = document.createElement('div');
        articulatorDiv.classList.add('articulator');
        articulatorDiv.textContent = articulator.text;
        articulatorDiv.id = `articulator-${articulator.id}`;

        const button = document.createElement('button');
        button.classList.add('btn', 'toggle-articulator-btn');
        button.dataset.id = articulator.id;

        button.textContent = articulator.is_added ? 'W powtórkach 😄' : 'Dodaj do powtórek';
        button.classList.add(articulator.is_added ? 'btn-secondary' : 'btn-success');
        button.disabled = articulator.is_added;

        button.addEventListener('click', handleToggleButtonClick);

        articulatorContainer.appendChild(articulatorDiv);
        articulatorContainer.appendChild(button);

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
                    data.forEach(articulator => addArticulatorToDOM(articulator));
                    offset += data.length;
                    loadMoreBtn.setAttribute('data-offset', offset.toString());
                } else {
                    document.getElementById('card-articulator').style.display = 'block';
                    loadMoreBtn.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error fetching articulators. Please try again.');
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
                    } else {
                        alert('Error: ' + data.message);
                    }
                })
                .catch(error => console.error('Error:', error));
            });
        });
    }
});
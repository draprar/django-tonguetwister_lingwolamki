document.addEventListener('DOMContentLoaded', function() {
    let loadMoreBtn = document.getElementById('load-more-btn');
    let offset = parseInt(loadMoreBtn.getAttribute('data-offset'));
    let url = loadMoreBtn.getAttribute('data-url');

    // Function to handle button clicks for both add and remove
    function handleToggleButtonClick(event) {
        const button = event.target.closest('.toggle-articulator-btn');
        if (!button || button.disabled) return;

        const articulatorId = button.dataset.id;
        const action = button.textContent.trim();

        console.log(`Button clicked: ${action} for articulator ${articulatorId}`);

        button.disabled = true; // Disable the button immediately

        if (action === '+') {
            fetch(`/add-articulator/${articulatorId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
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
                button.disabled = false; // Re-enable the button
                if (data.status === 'Articulator added') {
                    button.textContent = '-';
                    button.classList.remove('btn-success');
                    button.classList.add('btn-danger');
                } else if (data.status === 'Duplicate articulator') {
                    alert('This articulator is already added.');
                } else {
                    alert('Error adding articulator: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error adding articulator:', error);
                alert('Error adding articulator. Please try again.');
                button.disabled = false; // Re-enable the button on error
            });
        } else if (action === '-') {
            fetch(`/delete-articulator/${articulatorId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
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
                console.log('Response data for deleting:', data);
                button.disabled = false; // Re-enable the button
                if (data.status === 'Articulator deleted') {
                    button.textContent = '+';
                    button.classList.remove('btn-danger');
                    button.classList.add('btn-success');
                    // Remove the articulator from the DOM
                    const articulatorContainer = document.getElementById(`articulator-container-${articulatorId}`);
                    if (articulatorContainer) {
                        articulatorContainer.remove();
                    }
                } else {
                    alert('Error deleting articulator: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error deleting articulator:', error);
                alert('Error deleting articulator. Please try again.');
                button.disabled = false; // Re-enable the button on error
            });
        }
    }

    // Function to add articulator and button elements to DOM
    function addArticulatorToDOM(articulator) {
        const existingArticulatorDiv = document.getElementById(`articulator-${articulator.id}`);
        if (existingArticulatorDiv) {
            console.log(`Articulator ${articulator.id} already exists`);
            return; // If articulator already exists, do not add again
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
        if (articulator.is_added) {
            button.textContent = '-';
            button.classList.add('btn-danger');
        } else {
            button.textContent = '+';
            button.classList.add('btn-success');
        }

        button.addEventListener('click', handleToggleButtonClick);

        articulatorContainer.appendChild(articulatorDiv);
        articulatorContainer.appendChild(button);

        document.getElementById('articulators-container').appendChild(articulatorContainer);

        console.log(`Added articulator ${articulator.id} to DOM`);
    }

    // Event listener for button clicks using event delegation
    document.getElementById('articulators-container').addEventListener('click', function(event) {
        if (event.target.matches('.toggle-articulator-btn')) {
            handleToggleButtonClick(event);
        }
    });

    // Event listener for load more button
    loadMoreBtn.addEventListener('click', function() {
        fetch(`${url}?offset=${offset}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Received data:', data);

            // Clear existing articulators and buttons
            document.getElementById('articulators-container').innerHTML = '';

            if (data.length > 0) {
                data.forEach(articulator => {
                    addArticulatorToDOM(articulator);
                });

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
});

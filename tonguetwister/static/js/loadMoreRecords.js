document.addEventListener('DOMContentLoaded', function() {
    // Initial setup
    let loadMoreBtn = document.getElementById('load-more-btn');
    let offset = parseInt(loadMoreBtn.getAttribute('data-offset'));
    let url = loadMoreBtn.getAttribute('data-url');

    // Function to attach button listeners
    function attachButtonListeners() {
        document.querySelectorAll('.add-articulator-btn').forEach(function(button) {
            button.removeEventListener('click', handleButtonClick); // Remove old listeners to avoid duplicates
            button.addEventListener('click', handleButtonClick);
        });
    }

    // Function to handle button clicks
    function handleButtonClick(event) {
        const button = this;
        const articulatorId = button.dataset.id;
        console.log('Clicked articulator ID:', articulatorId);

        // Disable the button and change text
        button.textContent = 'Dodane!';
        button.disabled = true;

        fetch(`/add-articulator/${articulatorId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'Articulator added') {
                // Optionally, update UI or handle success message if needed
            } else if (data.status === 'Duplicate articulator') {
                alert('This articulator is already added.');
                // Re-enable button on duplicate
                button.textContent = '+';
                button.disabled = false;
            } else {
                // Re-enable button on error
                button.textContent = '+';
                button.disabled = false;
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            // Re-enable button on error
            button.textContent = '+';
            button.disabled = false;
            console.error('Error:', error);
        });
    }

    // Attach button listeners initially
    attachButtonListeners();

    // Event listener for load more button
    loadMoreBtn.addEventListener('click', function() {
        fetch(`${url}?offset=${offset}`)
        .then(response => response.json())
        .then(data => {
            // Remove old articulator and '+' button
            const oldArticulator = document.querySelector('.articulator');
            const oldButton = document.querySelector('.add-articulator-btn');
            if (oldArticulator) {
                oldArticulator.remove();
            }
            if (oldButton) {
                oldButton.remove();
            }

            if (data.length > 0) {
                data.forEach((articulator, index) => {
                    const articulatorDiv = document.createElement('div');
                    articulatorDiv.classList.add('articulator', 'col-md-16', 'fs-4');
                    articulatorDiv.textContent = articulator.text;

                    const button = document.createElement('button');
                    button.classList.add('btn', 'btn-success', 'add-articulator-btn');
                    button.dataset.id = articulator.id;
                    button.textContent = '+';
                    button.addEventListener('click', handleButtonClick); // Add listener to new button

                    document.getElementById('articulators-container').appendChild(articulatorDiv);
                    document.getElementById('articulators-container').appendChild(button);
                });

                attachButtonListeners(); // Re-attach listeners to the new buttons

                offset += data.length;
                loadMoreBtn.setAttribute('data-offset', offset.toString());
            } else {
                document.getElementById('card-articulator').style.display = 'block';
                loadMoreBtn.style.display = 'none';
                document.querySelectorAll('#articulators-container .articulator').forEach(articulator => {
                    articulator.style.display = 'none';
                });
            }
        })
        .catch(error => console.error('Error:', error));
    });

});

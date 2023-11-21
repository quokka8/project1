// main.js

document.querySelectorAll('.add-to-reading-list-button').forEach(button => {
    button.addEventListener('click', function () {
        const bookId = this.getAttribute('data-book-id');
        
        fetch(`/add_to_reading_list/${bookId}/`)
            .then(response => response.json())
            .then(data => {
                alert(data.message);

            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});

document.querySelectorAll('.add-to-group-reading-button').forEach(button => {
    button.addEventListener('click', function () {
        const bookId = this.getAttribute('data-book-id');
        
        fetch(`/add_to_group_readings/${bookId}/`)
            .then(response => response.json())
            .then(data => {
                alert(data.message);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function removeFromReadingList(bookId) {
    fetch(`/remove_from_reading_list/${bookId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        // Check if the removal was successful
        if (data.success) {
            // Fetch the updated reading list from the server
            fetch('/reading_list_partial/')
                .then(response => response.text())
                .then(html => {
                    // Update the content of readingListContainer with the updated reading list
                    const readingListContainer = document.getElementById('reading-list-container');
                    readingListContainer.innerHTML = html;
                })
                .catch(error => {
                    console.error('Error fetching updated reading list:', error);
                });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function removeFromGroupReadings(bookId) {
    fetch(`/remove_from_group_readings/${bookId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        // Check if the removal was successful
        if (data.success) {
            // Fetch the updated reading list from the server
            fetch('/group_readings_partial/')
                .then(response => response.text())
                .then(html => {
                    // Update the content of readingListContainer with the updated reading list
                    const readingListContainer = document.getElementById('group-readings-container');
                    readingListContainer.innerHTML = html;
                })
                .catch(error => {
                    console.error('Error fetching updated reading list:', error);
                });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function readWithGroup(bookTitle, bookId) {
    // Отправить запрос на сервер для создания комнаты чата
    fetch(`/create_chat_room/${bookTitle}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
    .then(response => response.json())
    .then(data => {
        // Перенаправить пользователя на страницу чата для созданной комнаты
        window.location.href = `/chat/${data.room_name}/`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

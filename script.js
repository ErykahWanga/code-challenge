
function displayMessage(text) {
    const contentDiv = document.getElementById("content");
    
    
    contentDiv.innerHTML = "";

    
    const message = document.createElement("p");
    message.textContent = text;
    message.classList.add("message"); 

    contentDiv.appendChild(message);
}


document.getElementById("fetchDataBtn").addEventListener("click", () => {
    fetchData();
});


document.getElementById("postDataBtn").addEventListener("click", () => {
    sendData();
})
function fetchData() {
    const randomId = Math.floor(Math.random() * 100) + 1; 
    fetch(`https://jsonplaceholder.typicode.com/posts/${randomId}`)
        .then(response => response.json())
        .then(data => {
            displayMessage(`Fetched Post: ${data.title}`);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            displayMessage("Failed to fetch data.");
        });
}

function sendData() {
    const postData = {
        title: "New Post",
        body: "This is a test post",
        userId: 1
    };

    fetch("https://jsonplaceholder.typicode.com/posts", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(`Post Created: ${data.title}`);
    })
    .catch(error => {
        console.error("Error posting data:", error);
        displayMessage("Failed to send data.");
    });
}

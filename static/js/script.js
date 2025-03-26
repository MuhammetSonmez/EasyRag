const API_URL = "http://127.0.0.1:5000";
let socket;

function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        alert("Lütfen bir dosya seçin!");
        return;
    }
    
    document.getElementById("loader").style.display = "block";
    
    let formData = new FormData();
    formData.append("file", fileInput.files[0]);
    
    fetch(`${API_URL}/api/create_rag`, {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        document.getElementById("loader").style.display = "none";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("loader").style.display = "none";
    });
}

function sendQuestion() {
    let question = document.getElementById("questionInput").value;
    if (!question) {
        alert("Lütfen bir soru yazın!");
        return;
    }
    
    let responseBox = document.getElementById("liveResponseBox");
    responseBox.innerHTML = "";
    responseBox.style.display = "none";

    if (!socket || socket.readyState !== WebSocket.OPEN) {
        socket = new WebSocket(`ws://localhost:5000/ws`);

        socket.onopen = function () {
            socket.send(question);
        };

        socket.onmessage = function (event) {
            displayLiveResponse(event.data); 
        };

        socket.onclose = function () {
            console.log("WebSocket bağlantısı kapandı.");
        };
    } else {
        socket.send(question);
    }
}

function displayLiveResponse(text) {
    let responseBox = document.getElementById("liveResponseBox");
    responseBox.style.display = "block";
    responseBox.innerHTML += text;  
}


document.getElementById("check").addEventListener("click", function () {

    let email = document.getElementById("email").value;

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => {

        let resultBox = document.getElementById("resultBox");
        let resultText = document.getElementById("resultText");
        let confidenceText = document.getElementById("confidenceText");
        let confidenceBar = document.getElementById("confidenceBar");
        let reasonsText = document.getElementById("reasonsText");
        let urlText = document.getElementById("urlText");

        resultBox.classList.remove("hidden");

        resultText.innerText = data.result;
        confidenceText.innerText = "Confidence: " + data.confidence + "%";

        confidenceBar.style.width = data.confidence + "%";

        if (data.result === "Safe Email") {
            resultBox.className = "safe";
            confidenceBar.style.background = "green";
        } else {
            resultBox.className = "phish";
            confidenceBar.style.background = "red";
        }

        if (data.reasons.length > 0) {
            reasonsText.innerText = "Suspicious Keywords: " + data.reasons.join(", ");
        } else {
            reasonsText.innerText = "";
        }

        if (data.urls_found.length > 0) {
            urlText.innerText = "URLs Detected: \n" + data.urls_found.join("\n");
        } else {
            urlText.innerText = "";
        }

    })
    .catch(error => {
        document.getElementById("resultText").innerText = "Error connecting to API";
    });

});

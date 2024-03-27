document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;

    fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name, email: email })
    })
    .then(response => {
        if (response.ok) {
            alert("Data submitted successfully!");
            document.getElementById("myForm").reset();
        } else {
            alert("Error submitting data!");
        }
    })
    .catch(error => console.error("Error:", error));
});

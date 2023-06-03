document.addEventListener("DOMContentLoaded", function() {
    console.log("UI ready!");

    document.getElementById("shoe-button").addEventListener("click", function() {
        fetch("/api/shoes")
        .then(response => response.json())
        .then(data => {
            document.getElementById("content").textContent = JSON.stringify(data);
        });
    });

    document.getElementById("offers-button").addEventListener("click", function() {
        fetch("/api/offers")
        .then(response => response.json())
        .then(data => {
            document.getElementById("content").textContent = JSON.stringify(data);
        });
    });
});

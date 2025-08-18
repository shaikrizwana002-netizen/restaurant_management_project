<form id="contactForm">
 <label for="name">Name:</label>
 <input type="text"id="name" name="name" />

 <label for="email">Email:</label>
 <input type="email" id="email" name="email" />

 <button type="submit">Submit</button>
</form>

<script>
document.getElementById("contactForm").addEventListener("submit", function (event) {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();

    if (!name || !email) {
        alert("Please fill in  both name and email field.");
        event.preventDefault(); // Prevent form submission
    }
});
</script>
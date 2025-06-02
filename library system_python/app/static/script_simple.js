function validateForm() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const messageDiv = document.getElementById('book-message');
    
    // Simple feedback before submission
    if (username && password) {
        messageDiv.innerHTML = "Logging in..."; // Feedback message
        return true; // Allow the form to be submitted
    } else {
        messageDiv.innerHTML = "Please fill in both fields."; // Error message
        return false; // Prevent form submission
    }
}
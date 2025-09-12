const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
    signInButton.textContent = "Sign In";
    signUpButton.textContent = "Sign Up";
});

signInButton.addEventListener('click', () => {
    // Redirection logic
    window.location.href = 'index2.html';
});

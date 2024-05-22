document.addEventListener('DOMContentLoaded', function() {
    const seedLoginButton = document.getElementById('seedLoginButton');
    const userLoginButton = document.getElementById('userLoginButton');
    const seedLoginForm = document.getElementById('seedLoginForm');
    const userLoginForm = document.getElementById('userLoginForm');

    seedLoginButton.addEventListener('click', function() {
        seedLoginForm.classList.remove('hidden');
        userLoginForm.classList.add('hidden');
    });

    userLoginButton.addEventListener('click', function() {
        userLoginForm.classList.remove('hidden');
        seedLoginForm.classList.add('hidden');
    });
});

function submitSeedLogin() {
    const seed = document.getElementById('seed').value;
    // Realiza la verificación del inicio de sesión usando AJAX o fetch
    // y envía los datos al backend de Django para autenticación.
}

function submitUserLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Realiza la verificación del inicio de sesión usando AJAX o fetch
    // y envía los datos al backend de Django para autenticación.
}

document.addEventListener('DOMContentLoaded', function() {
    const registrationForm = document.getElementById('registrationForm');
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirmPassword');

    confirmPasswordField.addEventListener('input', function() {
        if (passwordField.value === confirmPasswordField.value) {
            // No es necesario generar la semilla aquí
        }
    });

    registrationForm.addEventListener('submit', function(event) {
        event.preventDefault();
        if (passwordField.value === confirmPasswordField.value) {
            const formData = new FormData(registrationForm);
            // Enviar los datos del formulario al backend de Django usando AJAX o Fetch
            fetch('/register/', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/login/'; // Redirigir a la página de inicio de sesión
                } else {
                    alert('Error al registrar el usuario');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al registrar el usuario');
            });
        } else {
            alert('Las contraseñas no coinciden');
        }
    });
});


document.addEventListener('DOMContentLoaded', () => {

    const $password = document.getElementById('password');

    document.getElementById('frm-password').addEventListener('submit', async event => {
        event.preventDefault();

        try {
            const res = await fetch('password', {
                method: 'POST',
                body: new FormData(event.target)
            });

            const json = await res.json();

            $password.innerText = json.password;

        } catch (error) {
            alert("ERROR: " + error);
        }
    });
});
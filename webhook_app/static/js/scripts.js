document.addEventListener('DOMContentLoaded', function() {
    const accountForm = document.getElementById('account-form');
    const destinationForm = document.getElementById('destination-form');

    accountForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const accountName = document.getElementById('account_name').value;
        const website = document.getElementById('website').value;

        fetch('/accounts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                account_name: accountName,
                website: website
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Account created:', data);
            // Add the new account to the accounts list
        })
        .catch(error => {
            console.error('Error creating account:', error);
        });
    });

    destinationForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const accountId = document.getElementById('account_id').value;
        const url = document.getElementById('url').value;
        const httpMethod = document.getElementById('http_method').value;
        const headers = document.getElementById('headers').value;

        fetch('/destinations/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                account: accountId,
                url: url,
                http_method: httpMethod,
                headers: JSON.parse(headers)
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Destination created:', data);
            // Add the new destination to the destinations list
        })
        .catch(error => {
            console.error('Error creating destination:', error);
        });
    });
});
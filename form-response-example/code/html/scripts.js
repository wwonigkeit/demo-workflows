/* Place your JavaScript in this file */
function getClustersFromHttp() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const checkedValues = [];

    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            checkedValues.push(checkbox.value);
        }
    });
    
    console.log(checkedValues);

    fetch('https://internal.direktiv.io/ns/demo-workflows/get-clusters', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ vcenters: checkedValues })
    })

    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Handle the response data here
    })
    .catch(error => {
        console.error('There was a problem with the request:', error);
    });                        
}


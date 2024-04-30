/* Place your JavaScript in this file */
function renderCheckBoxVcenters(arr) {
    // var arr = ["vcenter1", "vcenter2", "vcenter3", "vcenter4"];
    var returnStr = "";
    for (i = 0; i < arr.length; i++) {
        returnStr += '<input type="checkbox" class="checkbox-input" name="' + arr[i] + '" value="' + arr[i] + '" />' + arr[i] + '<br>';
    }
    returnStr += '<button class="button" type="button" onclick="getClustersFromHttp()">Get Checked Values</button>'
    document.getElementById("dell-vcenter").innerHTML=returnStr;
}


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
        document.getElementById("dell-clusters").innerHTML = JSON.stringify(data.clusters);
        //renderCheckBoxClusters(data.clusters)
    })
    .catch(error => {
        console.error('There was a problem with the request:', error);
    });
}

function renderCheckBoxClusters(jsonData) {
    // var arr = ["vcenter1", "vcenter2", "vcenter3", "vcenter4"];
    var returnStr = "";
    for (i = 0; i < arr.length; i++) {
        returnStr += '<input type="checkbox" class="checkbox-input" name="' + arr[i] + '" value="' + arr[i] + '" />' + arr[i] + '<br>';
    }
    returnStr += '<button class="button" type="button" onclick="getClustersFromHttp()">Get Checked Values</button>'
    document.getElementById("dell-vcenter").innerHTML=returnStr;
}
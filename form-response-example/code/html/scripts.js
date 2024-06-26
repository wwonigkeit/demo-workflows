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
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    var checkedValues = [];

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
        // console.log(data); // Handle the response data here
        // document.getElementById("dell-clusters").innerHTML = JSON.stringify(data.clusters);
        renderCheckBoxClusters(data)
    })
    .catch(error => {
        console.error('There was a problem with the request:', error);
    });
}

function renderCheckBoxClusters(vcenters) {
    var returnStr = "";
    vcenters.clusters.forEach(function(item) {
        // Iterate over each property in the current object
        for (var vcenter in item) {
            item[vcenter].forEach(function(cluster) { 
                returnStr += '<input type="checkbox" class="checkbox-input" name="' + cluster + '" value="' + cluster + '" />' + cluster + '<br>';
            })
        }
     })

    returnStr += '<button class="button" type="button" onclick="getVmsFromHttp()">Get Checked Values</button>'
    document.getElementById("dell-clusters").innerHTML=returnStr;
}

function getVmsFromHttp() {
    var element = document.getElementById('dell-clusters');
    var checkboxes = element.querySelectorAll('input[type="checkbox"]');
    // #const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    var checkedValues = [];

    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            checkedValues.push(checkbox.value);
        }
    });
    
    console.log(checkedValues);

    fetch('https://internal.direktiv.io/ns/demo-workflows/get-vms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ clusters: checkedValues })
    })

    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // console.log(data); // Handle the response data here
        // document.getElementById("dell-clusters").innerHTML = JSON.stringify(data.clusters);
        renderCheckBoxVms(data)
    })
    .catch(error => {
        console.error('There was a problem with the request:', error);
    });
}

function renderCheckBoxVms(data) {
    var returnStr = "";
    data.vms.forEach(function(cluster) {
        // Iterate over each property in the current object
        for (var key in cluster) {
            cluster[key].forEach(function(vm) {
                returnStr += '<input type="checkbox" class="checkbox-input" name="' + vm + '" value="' + vm + '" />' + vm + '<br>';
            })
        }
     })

    // returnStr += '<button class="button" type="button" onclick="getVmsFromHttp()">Get Checked Values</button>'
    document.getElementById("dell-vms").innerHTML=returnStr;
}
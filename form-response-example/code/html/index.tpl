<!doctype html>

<html>
    <header>
        <img src="dell_logo.svg" alt="Logo">
    </header>

    <head>
        <style>
            header {
                background-color: #000000;
                padding: 10px;
                text-align: center;
            }
            img {
                height: 50px; /* Adjust the height as needed */
            }
            .grid-container {
                display: grid;
                grid-template-columns: 1fr 1fr; /* Three columns with equal width */
                grid-gap: 10px; /* Gap between grid items */
            }

            .grid-item-black {
                background-color: black;
                padding: 20px;
                text-align: center;
                color: white;
                font-family: Arial, sans-serif;
            }

            .grid-item-white {
                background-color: white;
                padding: 20px;
                text-align: center;
                color: black;
                font-family: Arial, sans-serif;
            }

            .checkbox-container {
                display: flex;
                align-items: center;
            }
            
            .checkbox-input {
                margin-right: 10px;
                font-family: Arial, sans-serif;
            }

            input[type="checkbox"] {
                appearance: none;
                -webkit-appearance: none;
                -moz-appearance: none;
                width: 20px; /* Set custom width */
                height: 20px; /* Set custom height */
                border: 2px solid #333; /* Add border */
                border-radius: 5px; /* Rounded corners */
                background-color: #fff; /* Checkbox background color */
                cursor: pointer; /* Cursor on hover */
                vertical-align: middle;
            }

            /* Custom checkbox when checked */
            input[type="checkbox"]:checked {
                background-color: #4CAF50; /* Green background when checked */
            }

            .button {
                background-color: black;
                color: white;
                border: none;
                font-family: Arial, sans-serif;
                padding: 7px 16px;
                text-align: center;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
            }
        </style>

        <meta charset="utf-8">

        <title>Get Virtual Machine Information</title>

        <!-- Load external CSS styles -->
        <link rel="stylesheet" href="styles.css">

    </head>

    <body>

        <h1 font-family="Arial, sans-serif">Virtual Machine Details</h1>
        
        <!-- Load external JavaScript -->
        <script src="scripts.js"></script>
        
        <div class="grid-container">
            <div class="grid-item-black">Step 1: select vCenter:</div>
            <div class="grid-item-white" id="dell-vcenter">
                <form id="checkboxForm">
                    <script>
                        var a = document.getElementById("dell-vcenter");
                        var arr = {{{vcenters}}};
                        var returnStr = "";
                        for (i = 0; i < arr.length; i++) {
                            returnStr += '<input type="checkbox" class="checkbox-input" name="' + arr[i] + '" value="' + arr[i] + '" />' + arr[i] + '<br>';
                        }
                        //a.innerHTML = returnStr;
                        returnStr += '<button class="button" type="button" onclick="getClustersFromHttp()">Get Checked Values</button>'
                        document.getElementById("dell-vcenter").innerHTML=returnStr;
                    </script>
                </form>
                <script>
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
                </script>                
            </div>
            <div class="grid-item-black">Step 2: select Cluster:</div>
            <div class="grid-item-white">placeholder for clusters</div>
            <div class="grid-item-black">Step 3: select Virtual Machine:</div>
            <div class="grid-item-white">placeholder for vms</div>
        </div>
        
    </body>

</html>
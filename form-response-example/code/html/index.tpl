<!doctype html>

<html>
    <header>
        <img src="dell-logo.svg" alt="Logo">
    </header>

    <head>
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
                        renderCheckBoxVcenters({{{vcenters}}})
                    </script>
                </form>
            </div>
            <div class="grid-item-black">Step 2: select Cluster:</div>
            <div class="grid-item-white" id="dell-clusters"></div>
            <div class="grid-item-black">Step 3: select Virtual Machine:</div>
            <div class="grid-item-white" id="dell-vms"></div>
        </div>
        
    </body>

</html>
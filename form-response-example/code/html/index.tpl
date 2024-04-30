<!DOCTYPE html>
<html style="font-size: 16px;" lang="en"><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <title>Home</title>
    <link rel="stylesheet" href="nicepage.css" media="screen">
<link rel="stylesheet" href="home.css" media="screen">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "",
		"logo": "dell_logo.svg"
}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="Home">
    <meta property="og:type" content="website"></head>
  <body data-home-page="Home.html" data-home-page-title="Home" data-path-to-root="./" data-include-products="false" class="u-body u-xl-mode" data-lang="en"><header class="u-clearfix u-header u-header" id="sec-8e47"><div class="u-clearfix u-sheet u-sheet-1">
        <a href="#" class="u-image u-logo u-image-1" data-image-width="300" data-image-height="38">
          <img src="dell_logo.svg" class="u-logo-image u-logo-image-1">
        </a>
      </div></header>
    <section class="u-clearfix u-section-1" id="sec-0618">
      <div class="u-clearfix u-sheet u-sheet-1">
        <h3 class="u-text u-text-default u-text-1">Virtual Machine Details</h3>
        
        <h4 class="u-text u-text-default u-text-2" for="dell-vcenter">Step 1: select vCenter:</h4>
        <a href="#" class="u-btn u-btn-2">
          <select name="dell-vcenter" id="dell-vcenter"></select>
          <script>
             // var arr = ["Courses here","Frontend Training","Backend Training","Java Training","Ethical Hacking"];
             var arr = {{{vcenters}}};
             var options="";
             arr.map((op,i)=>{
                options+=`<option value="${op}" id="${i}" style="border-radius: 5px;"">${op}</option>`
             })
             document.getElementById("dell-vcenter").innerHTML=options;
          </script>          
        </a>

        <h4 class="u-text u-text-default u-text-3">Step 2: select Cluster:</h4>
        <a href="#" class="u-btn u-btn-round u-button-style u-hover-palette-1-light-1 u-palette-1-base u-radius u-text-body-alt-color u-text-hover-white u-btn-2">Wrong&nbsp;<span class="u-icon u-text-white u-icon-2"><svg class="u-svg-content" viewBox="0 0 490.677 490.677" x="0px" y="0px" style="width: 1em; height: 1em;"><path d="M489.272,37.339c-1.92-3.307-5.44-5.333-9.259-5.333H10.68c-3.819,0-7.339,2.027-9.259,5.333    c-1.899,3.307-1.899,7.36,0.021,10.667l234.667,405.333c1.899,3.307,5.419,5.333,9.237,5.333s7.339-2.027,9.237-5.333 L489.251,48.005C491.149,44.72,491.149,40.645,489.272,37.339z"></path></svg></span>
        </a>
        <h4 class="u-text u-text-default u-text-4">Step 3: select Virtual Machine:</h4>
        <a href="#" class="u-btn u-btn-round u-button-style u-hover-palette-1-light-1 u-palette-1-base u-radius u-text-body-alt-color u-text-hover-white u-btn-3">Button&nbsp;<span class="u-icon u-text-white u-icon-3"><svg class="u-svg-content" viewBox="0 0 490.677 490.677" x="0px" y="0px" style="width: 1em; height: 1em;"><path d="M489.272,37.339c-1.92-3.307-5.44-5.333-9.259-5.333H10.68c-3.819,0-7.339,2.027-9.259,5.333    c-1.899,3.307-1.899,7.36,0.021,10.667l234.667,405.333c1.899,3.307,5.419,5.333,9.237,5.333s7.339-2.027,9.237-5.333 L489.251,48.005C491.149,44.72,491.149,40.645,489.272,37.339z"></path></svg></span>
        </a>
      </div>
    </section>
  
</body></html>
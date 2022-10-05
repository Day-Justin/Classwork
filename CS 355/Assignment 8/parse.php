<!DOCTYPE html> <!-- parse.php -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Parse Request</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script src="config.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>


</head>
<body class="content" id="last_project">
<!-- NAVBAR BEGINS HERE-->
<nav id="navbar">
</nav>
<!--NAVBAR ENDS HERE-->
<h1><span>Parse Form</span></h1>
<section class="parse_form">
<form action="parsed.php" method="post">
    <p>Source Name:</p>
    <p><input type="text" name="source_name" required="true"></p>
    <p>URL:</p>
    <p><input type="text" name="source_url" required="true"></p>
    <p>Begining At (optional):</p>
    <p><input type="text" name="source_begin"></p>
    <p>Ending At (optional):</p>
    <p><input type="text" name="source_end"></p>
    <p><input type="submit" name="submit" value="Parse"/></p>
</form>
</section>

<?php
if (isset($_GET["error"])){
    if ($_GET["error"] === "invalurl"){
        echo "<p>Please enter a valid url.</p>";
    }
        if ($_GET["error"] === "notfound"){
        echo "<p>The stats weren't found. Please contact admin to resolve problem.</p>";
    }
}
?>

</body>
</html>
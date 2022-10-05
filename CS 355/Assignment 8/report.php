<!DOCTYPE html> <!-- parsed.php -->
<html lang="en">
<head>
    <title>Report</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="style.css">
    <script src="config.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>


</head>
<body class="content" id="last_project">
<!-- NAVBAR BEGINS HERE-->
<nav id="navbar">
</nav>
<!--NAVBAR ENDS HERE-->
<?php

$host = "mars.cs.qc.cuny.edu";
$user = "daju9399";
$db = "daju9399";

$filename = "password.txt";
$myfile = fopen($filename, "r");
if (!$myfile) {
   die("Unable to open $filename.");
}
$pwd = fread($myfile, filesize($filename));
fclose($myfile);
//echo "<p>$pwd</p>";
$conn = connect_to_db($host, $user, $pwd, $db);
//echo "<p>Connected<p>"

$query = "SELECT * FROM source;";
$stmt = mysqli_stmt_init($conn);
if(!mysqli_stmt_prepare($stmt, $query)){
    header("location: parse.php?error=notfound");
}
mysqli_stmt_execute($stmt);
$data = mysqli_stmt_get_result($stmt);

if($data){
  $data_array = array();
  while($row = mysqli_fetch_array($data, MYSQLI_ASSOC)){
    $data_array[] = $row;
    }
    echo "<h1><span>Reporting<span></h1>";
    create_table($data_array);
}
else{
  header("location: parse.php?error=notfound");
}

mysqli_stmt_close($stmt);
$conn -> close();

//---------------------------------------------------------------------------------------------------------------------------------------

function connect_to_db($host, $user, $pwd, $db){
  $conn = new mysqli($host, $user, $pwd, $db);
  if($conn->connect_errno){
    die("Failed to connect to MySQL:($conn->connect_errno)$conn->connect_error");
  }
  return $conn;
}

function create_table($array){
  usort($array, function ($a, $b) {
  $a_val = (int) $a['source_id'];
  $b_val = (int) $b['source_id'];

  if($a_val > $b_val) return 1;
  if($a_val < $b_val) return -1;
  return 0;
  });
  $name = "source_name";
  $url = "source_url";
  $begin = "source_begin";
  $end = "source_end";
  $dtm = "parsed_dtm";
  $output = "<table id=\"report_table\"> <tr> <th>Name</th> <th>Source URL</th><th>Where Parse Began</th> <th>Where Parse Ends</th><th>When first Parsed</th></tr>";
  foreach($array as $row){
  $output .= "<tr> <td>$row[$name]</td> <td>$row[$url]</td> <td>$row[$begin]</td> <td>$row[$end]</td><td>$row[$dtm]</td></tr>";
  //print_r($row);
  }
 $output .= "</table>";
 echo $output;
 } 

?>

</body>
</html>
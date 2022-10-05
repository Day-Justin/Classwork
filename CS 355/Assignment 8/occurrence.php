<!DOCTYPE html> <!-- parsed.php -->
<html lang="en">
<head>
    <title>Occurrence Table</title>
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
$source_id;
if (!isset($_GET["id"])){
    header("location: parse.php");
    exit();
}
else{
    $source_id = getData("id");
}


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

$query = "SELECT * FROM occurrence WHERE source_id = ?;";
$stmt = mysqli_stmt_init($conn);
if(!mysqli_stmt_prepare($stmt, $query)){
    header("location: parse.php?error=notfound");
}
mysqli_stmt_bind_param($stmt, "i", $source_id);
mysqli_stmt_execute($stmt);
$data = mysqli_stmt_get_result($stmt);

if($data){
  $data_array = array();
  while($row = mysqli_fetch_array($data, MYSQLI_ASSOC)){
    $data_array[] = $row;
    }
    echo "<h1><span>N U M B E R S</span></h1>";
    create_table($data_array);
}
else{
  header("location: parse.php?error=notfound");
}

mysqli_stmt_close($stmt);
$conn -> close();

//---------------------------------------------------------------------------------------------------------------------------------------

function getData($field) {
   if (!isset($_GET[$field])) {
      $data = "";
   }
   else {
      $data = trim($_GET[$field]);
      $data = htmlspecialchars($data);
   }
   return $data;
}

function connect_to_db($host, $user, $pwd, $db){
  $conn = new mysqli($host, $user, $pwd, $db);
  if($conn->connect_errno){
    die("Failed to connect to MySQL:($conn->connect_errno)$conn->connect_error");
  }
  return $conn;
}

function create_table($array){
  usort($array, function ($a, $b) {
  $a_val = (int) $a['freq'];
  $b_val = (int) $b['freq'];

  if($a_val < $b_val) return 1;
  if($a_val > $b_val) return -1;
  return 0;
  });
  $word = "word";
  $freq = "freq";
  $percentage = "percentage";
  $output = "<table id=\"occurrence_table\"> <tr> <th>Word</th> <th>Frequency</th><th>Percentage of Document</th> </tr>";
  foreach($array as $row){
  $output .= "<tr> <td>$row[$word]</td> <td>$row[$freq]</td> <td>$row[$percentage]</td> </tr>";
  //print_r($row);
  }
 $output .= "</table>";
 echo $output;
 } 

?>

</body>
</html>
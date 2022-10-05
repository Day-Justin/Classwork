<!DOCTYPE html> <!-- parsed.php -->
<html lang="en">
<head>
    <title>Parsed Table</title>
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
if (!isset($_POST["submit"])){
    header("location: parse.php");
    exit();
}

$source_name = getData("source_name");
$source_url = getData("source_url");
$source_begin = getData("source_begin");
$source_end = getData("source_end");

if(!filter_var($source_url, FILTER_VALIDATE_URL)){
    header("location: parse.php?error=invalurl");
    exit();
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

data_is_in:

$query = "SELECT * FROM source WHERE source_name = ? AND source_url = ? AND source_begin = ? AND source_end = ?;";
$stmt = mysqli_stmt_init($conn);
if(!mysqli_stmt_prepare($stmt, $query)){
    header("location: parse.php?error=invalurl");
}
mysqli_stmt_bind_param($stmt, "ssss", $source_name, $source_url, $source_begin, $source_end);
mysqli_stmt_execute($stmt);
$data = mysqli_stmt_get_result($stmt);

$source_id;
if($row = mysqli_fetch_assoc($data)){
  $source_id = $row["source_id"];
  $html = file_get_contents($source_url);
  input_occur(occurence_array(parse($html,$source_begin, $source_end)), $source_id, $conn);
  echo "<h1 class=\"parsed\"><span>What you have parsed<span></h1>";
  create_table($row, $source_id);
}
else{
  // echo "<p>not found</p>";
  $insert = "INSERT INTO source (source_name, source_url, source_begin, source_end) VALUES (?, ?, ?, ?);";
  $insert_stmt = mysqli_stmt_init($conn);
  if(!mysqli_stmt_prepare($insert_stmt, $insert)){
    header("location: parse.php?error=invalurl");
  }
  mysqli_stmt_bind_param($insert_stmt, "ssss", $source_name, $source_url, $source_begin, $source_end);
  mysqli_stmt_execute($insert_stmt);
  mysqli_stmt_close($insert_stmt);
  goto data_is_in;
}

mysqli_stmt_close($stmt);
$conn -> close();

//---------------------------------------------------------------------------------------------------------------------------------------

function getData($field) {
   if (!isset($_POST[$field])) {
      $data = "";
   }
   else {
      $data = trim($_POST[$field]);
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

function create_table($row, $source_id){
  $output = "<table id=\"parsed_table\"> <tr> <th>What</th> <th>What it is</th> </tr>";
  foreach($row as $key => $value){
  $output .= "<tr> <td>$key</td> <td>$value</td> </tr>";
  }
 $output .= "<tr> <td>Words</td> <td><a href=\"occurrence.php?id=$source_id\">Click here to see word stats</a></td> </tr></table>";
 echo $output;
 } 

function parse($html, $begin, $end){
  $html = preg_replace('/<style[\s\S]+?<\/style>/', '$1$3', $html); // rmv stlye
  $html = preg_replace('/<script[\s\S]+?<\/script>/', '$1$3', $html); //rmv script
  $html = htmlspecialchars(trim(strip_tags($html))); // rmv html
  
  if($begin_pos = strpos($html, $begin)){ // if $source_begin
    $html = substr($html, $begin_pos);
  }
  
  if($end_pos = strrpos($html, $end)){ // if $souce_end
    $html = substr($html, 0, $end_pos + strlen($end));
  }
  
  $html = preg_replace( '/[^\w\']+|\'(?!\w)|(?<!\w)\'/', ' ', $html); // rmv punct
  $html = strtoupper($html);
  $txt_array = explode(" ", $html);
 /*
  foreach($txt_array as $word){
   echo $word . "<br>";
  }
  */
  
  return $txt_array;
  
}

function occurence_array($txt_array){
  $occur_array = array();
  foreach($txt_array as $word){
    if(array_key_exists($word, $occur_array)){
      $occur_array[$word] += 1;
    }
    else{
    $occur_array[$word] = 1;
    }
  }
  arsort($occur_array);
  return $occur_array;
}

function input_occur($occur_array, $source_id, $conn){
  /*
  $query = "truncate table occurrence;"; // the tables only have 1000 limit so gotta make space somehow
  $stmt = mysqli_stmt_init($conn);
  if(!mysqli_stmt_prepare($stmt, $query)){
    die("bad request1<br>");
  }
  mysqli_stmt_execute($stmt);
  mysqli_stmt_close($stmt);
  */
  $total = total($occur_array);
  foreach($occur_array as $word => $freq){
    $percentage =  ((float)$freq/$total) * 100;
    $insert = "INSERT INTO occurrence (source_id, word, freq, percentage) VALUES (?, ?, ?, ?);";
    $insert_stmt = mysqli_stmt_init($conn);
    if(!mysqli_stmt_prepare($insert_stmt, $insert)){
      die("bad request2<br>");
    }
    mysqli_stmt_bind_param($insert_stmt, "isid", $source_id, $word, $freq, $percentage);
    mysqli_stmt_execute($insert_stmt);
    mysqli_stmt_close($insert_stmt);
  }

   mysqli_stmt_close($stmt);

}

function total($array){
  $sum = 0;
  foreach($array as $word => $freq){
  $sum += $freq;
  }
  return $sum;
}

/*
function validateURL($URL) {
      $pattern_1 = "/^(http|https|ftp):\/\/(([A-Z0-9][A-Z0-9_-]*)(\.[A-Z0-9][A-Z0-9_-]*)+.(com|org|net|dk|at|us|tv|info|uk|co.uk|biz|se)$)(:(\d+))?\/?/i";
      $pattern_2 = "/^(www)((\.[A-Z0-9][A-Z0-9_-]*)+.(com|org|net|dk|at|us|tv|info|uk|co.uk|biz|se)$)(:(\d+))?\/?/i";
      if(preg_match($pattern_1, $URL) || preg_match($pattern_2, $URL)){
        return true;
      } else{
        return false;
      }
    }

if(!validateURL($source_url)){
    header("location: parse.php?error=invalurl");
    exit();
    }
*/

?>

</body>
</html>
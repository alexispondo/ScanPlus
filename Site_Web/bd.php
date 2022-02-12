
<?php
  try
  {
    $bd = new PDO("mysql:host=localhost; dbname=test", "root", "");
  }catch(Exception $error)
  {
    die("UNE ERREURE:" .$error->getMessage());
  }
?>
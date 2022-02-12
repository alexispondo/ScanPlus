
<?php include("bd.php"); ?>


<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>IP</title>
</head>
<body>
    <a href="index.php">Return</a>
        <h2>Entrez votre IP</h2>
        <form method="POST" action="commande.php">
            <label>IP</label><br>
            <input type="text" name="ip"><br><br>

            <input type="submit" name="submit">
        </form>

        <div>

<?php 
if (isset($_POST['submit'])) {
    $ip = $_POST['ip'];
    $output = shell_exec( "ping -c 4 {$ip}");
    echo "<pre>{$output}</pre>\n" ;
}
?>
        </div>

</body>
</html>
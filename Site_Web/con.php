<?php include("bd.php"); ?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Connexion</title>
</head>
<body>
	<a href="index.php">Return</a>
		<h2>Connexion</h2>
		<form method="POST" action="con.php">
			<label>User</label><br>
			<input type="text" name="username"><br><br>

			<label>Pass</label><br>
			<input type="password" name="passw"><br><br>

			<input type="submit" name="submit">
		</form>

</body>
</html>

<?php 

if (isset($_POST['submit'])) {
	$username = $_POST['username'];
	$password = $_POST['passw'];

	$rec = $bd->prepare("SELECT * FROM etudiants WHERE Username = :u and passw = :p ");
    $rec->execute(array("u"=>$username, "p"=>$password));
    $donne = $rec->fetch(PDO::FETCH_OBJ);

	#$reponse = $bd->query("SELECT * FROM etudiants WHERE Username = "."$username"." and passw = "."$password"." ");
	#$reponse->execute();
    #$donne=$reponse->fetch(PDO::FETCH_OBJ);
    if (!$donne) {
      echo "Désolé";
    }else{
      echo "Félicitation ".$donne->Username;
    }
}



 ?>
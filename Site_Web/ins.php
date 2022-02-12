<?php include("bd.php"); ?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Inscription</title>
</head>
<body>
	<a href="index.php">Return</a>
		<h2>Inscription</h2>
		<form method="POST" action="ins.php">
			<label>User</label><br>
			<input type="text" name="username"><br><br>

			<label>Pass</label><br>
			<input type="password" name="passw"><br><br>

			<label>Email</label><br>
			<input type="email" name="email"><br><br>

			<label>Telephone</label><br>
			<input type="text" name="tel"><br><br>

			<label>Classe</label><br>
			<input type="text" name="classe"><br><br>

			<input type="submit" name="submit">
		</form>

</body>
</html>

<?php 

if (isset($_POST['submit'])) {
	$username = $_POST['username'];
	$password = $_POST['passw'];
	$email = $_POST['email'];
	$telephone = $_POST['tel'];
	$classe = $_POST['classe'];
	//echo $username;

	#$connection = $bd->query("INSERT INTO etudiants (Username, passw, email, tel, classe) VALUES ($username, $password, $email, $telephone, $classe)");
	#$connection->execute();
	//echo $bd;
	$inserer = $bd->prepare("INSERT INTO etudiants (Username, passw, email, tel, classe) VALUES (?, ?, ?, ?, ?) ");
	$inserer->execute(array($username, $password, $email, $telephone, $classe));
}



 ?>
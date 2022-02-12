<?php include("bd.php"); ?>


<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Commentaire</title>
</head>
<body>
	<a href="index.php">Return</a>
		<h2>Commentaire</h2>
		<form method="POST" action="commentaire.php">
			<label>Commentaire</label><br>
			<textarea name="commentaire" placeholder="Votre message..."></textarea><br><br>
			<input type="submit" name="submit">
		</form>

    	<div>

<?php 
if (isset($_POST['submit'])) {
	$comment = $_POST['commentaire'];
	$inserer = $bd->prepare("INSERT INTO commentaires (comment) VALUES (?) ");
	$inserer->execute(array($comment));
}
?>


<?php
	$rec = $bd->prepare("SELECT * FROM commentaires ");
    $rec->execute(array());
    $donne = $rec->fetchAll(PDO::FETCH_OBJ);

    foreach ($donne as $key => $value) {
    	?>
    		<b>User: </b> <label><?php echo $value->comment; ?></label><br>
    	<?php
    }
?>
    	</div>

</body>
</html>
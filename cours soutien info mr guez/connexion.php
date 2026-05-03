<?php
if(isset($_POST["bout"])){
    $mail = $_POST["mail"];
    $mdp = $_POST["mdp"];
    include 'connect.php';
    $req = "select * from user where mail='$mail' and mdp='$mdp'";
    $resultat = mysqli_query($id, $req);
    if(mysqli_num_rows($resultat)>0){
        header("location:chat");
    }else{
        echo "Erreur de login ou de mot de passe!!!!!";
    }
}
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
      <h1>Formulaire de connexion</h1>
      <form action="" method = "post">
          <input type="email" name="mail" placeholder="Login/Mail:" required><br><br>
          <input type="password" name="mdp" placeholder="Mot de passe:" required><br><br>
          <input type="submit" value= "connexion" name="bout" >
      </form>><hr>
</body>
</html>
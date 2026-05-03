<?php
if(isset($_POST["bout"])){
    $pseudo = $_POST["pseudo"];
    $message = $_POST["message"];
    $id = mysqli_connect("localhost","root","","chatozar");
    $req = "insert into msg (pseudo,message,date)
            values ('$pseudo','$message',now())";
    mysqli_query($id, $req);

}
?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale">
</head>
<body>
     <div class="container">
	 <header>
	     <h1>Chattez'en direct! Chatbox</h1>
	 </header>
	 <div class="message">
	     <ul>
		     <li class="message">2024-06-05 10:01:10 - Fred: azerty</li>
		     <li class="message">2024-06-05 10:01:10 - Fred: azerty<</li>
			 <li class="message">2024-06-05 10:01:10 - Fred: azerty<</li>
		 </ul>
	 </div>
     <div class ="formulaire">
        <form action="" method="post">
         <input type="text" name="pseudo" placeholder="Pseudo :"required>
         <input type="text" name="message" placeholder="Message :"required><br>
         <input type="submit" value="Envoyer" name="bout">
        </form>
     </div> 
</div>
</body>
</html>
<?php
// Informations de connexion
$host = 'localhost'; // ou l'adresse de votre serveur
$username = 'root';
$password = '';
$database = 'mon_agenda_db'; // Nom de votre base de données

// Établissement de la connexion
$lien_connexion = mysqli_connect($host, $username, $password, $database);

// Vérification de la connexion
if(!$lien_connexion) {
    die("Problème de connexion : " . mysqli_connect_error());
}
?>
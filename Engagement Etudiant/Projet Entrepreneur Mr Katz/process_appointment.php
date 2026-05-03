<?php
require_once 'connexion.php'; // Connexion à la base avec $lien_connexion

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Récupération et nettoyage des données envoyées via POST
    $professional = trim($_POST['professional'] ?? '');
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $appointment_date = trim($_POST['appointment_date'] ?? '');
    $description = trim($_POST['description'] ?? '');

    // Vérification que tous les champs sont remplis
    if ($professional && $name && $email && $appointment_date) {
        // Formater la date si nécessaire
        $appointment_date = str_replace('T', ' ', $appointment_date);

        // Préparation de la requête d'insertion
        $sql = "INSERT INTO rendezvous (professional, name, email, appointment_date, description) 
                VALUES (?, ?, ?, ?, ?)";

        // Préparation de la requête avec mysqli
        if ($stmt = mysqli_prepare($lien_connexion, $sql)) {
            // Liaison des paramètres
            mysqli_stmt_bind_param($stmt, 'sssss', $professional, $name, $email, $appointment_date, $description);

            // Exécution de la requête
            if (mysqli_stmt_execute($stmt)) {
                echo "Rendez-vous enregistré avec succès !";
            } else {
                echo "Erreur lors de l'enregistrement : " . mysqli_error($lien_connexion);
            }

            // Fermeture de la requête préparée
            mysqli_stmt_close($stmt);
        } else {
            echo "Erreur lors de la préparation de la requête : " . mysqli_error($lien_connexion);
        }
    } else {
        echo "Tous les champs doivent être remplis.";
    }
} else {
    echo "Méthode non autorisée.";
}

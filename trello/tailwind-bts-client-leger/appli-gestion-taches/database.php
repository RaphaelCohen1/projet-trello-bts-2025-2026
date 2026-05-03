<?php
try {
    // Création (ou ouverture) de la base de données SQLite
    $pdo = new PDO("sqlite:db/database.sqlite");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Requête pour créer la table si elle n'existe pas encore
    $sql = "CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        statut INTEGER DEFAULT 0
    )";

    // Exécution de la requête
    $pdo->exec($sql);

    echo "✅ Base de données et table créées avec succès !";
} catch (PDOException $e) {
    echo "❌ Erreur : " . $e->getMessage();
}
?>


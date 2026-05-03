<?php
require 'database.php';
if (!empty($_POST['nom'])) {
    $stmt = $pdo->prepare("INSERT INTO taches (nom) VALUES (?)");
    $stmt->execute([$_POST['nom']]);
}
header('Location: index.php');

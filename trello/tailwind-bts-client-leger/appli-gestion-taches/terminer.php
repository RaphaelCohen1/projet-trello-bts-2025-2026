<?php
require 'database.php';
$id = $_GET['id'];
$pdo->query("UPDATE taches SET statut = 1 WHERE id = $id");
header('Location: index.php');

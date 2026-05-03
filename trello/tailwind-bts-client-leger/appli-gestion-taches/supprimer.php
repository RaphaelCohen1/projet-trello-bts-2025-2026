<?php
require 'database.php';
$id = $_GET['id'];
$pdo->query("DELETE FROM taches WHERE id = $id");
header('Location: index.php');

<?php
require 'database.php';
$id = $_GET['id'];
$tache = $pdo->query("SELECT * FROM taches WHERE id = $id")->fetch();

if ($_POST) {
    $stmt = $pdo->prepare("UPDATE taches SET nom = ? WHERE id = ?");
    $stmt->execute([$_POST['nom'], $id]);
    header('Location: index.php');
}
?>

<form method="post">
    <input type="text" name="nom" value="<?= htmlspecialchars($tache['nom']) ?>" required>
    <button type="submit">Modifier</button>
</form>

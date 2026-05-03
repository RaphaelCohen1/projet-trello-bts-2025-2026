<?php
header('Content-Type: application/json');
ini_set('display_errors', 1);
error_reporting(E_ALL);

$dsn = "mysql:host=localhost;dbname=TOVMEOD";
$username = "root";
$password = "";

try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $action = $_REQUEST['action'] ?? '';

    if ($action === 'fetch') {
        $filter = $_GET['filter'] ?? '';
        $stmt = $pdo->prepare("SELECT * FROM T_ENTITE WHERE NOM_ENTITE LIKE ?");
        $stmt->execute(['%' . $filter . '%']);
        echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));

    } elseif ($action === 'add') {
        if (empty($_POST['nom'])) {
            echo json_encode(["error" => "Le nom ne peut pas être vide."]);
            exit;
        }
        $stmt = $pdo->prepare("INSERT INTO T_ENTITE (NOM_ENTITE) VALUES (?)");
        $stmt->execute([$_POST['nom']]);
        echo json_encode(["status" => "success"]);

    } elseif ($action === 'update') {
        if (empty($_POST['nom']) || empty($_POST['id'])) {
            echo json_encode(["error" => "Nom ou ID manquant."]);
            exit;
        }
        $stmt = $pdo->prepare("UPDATE T_ENTITE SET NOM_ENTITE = ? WHERE ID_ENTITE = ?");
        $stmt->execute([$_POST['nom'], $_POST['id']]);
        echo json_encode(["status" => "success"]);

    } elseif ($action === 'delete') {
        $stmt = $pdo->prepare("DELETE FROM T_ENTITE WHERE ID_ENTITE = ?");
        $stmt->execute([$_GET['id']]);
        echo json_encode(["status" => "success"]);

    } elseif ($action === 'edit') {
        $stmt = $pdo->prepare("SELECT * FROM T_ENTITE WHERE ID_ENTITE = ?");
        $stmt->execute([$_GET['id']]);
        echo json_encode($stmt->fetch(PDO::FETCH_ASSOC));

    } else {
        echo json_encode(["error" => "Action non reconnue"]);
    }
} catch (PDOException $e) {
    echo json_encode(["error" => $e->getMessage()]);
}
?>

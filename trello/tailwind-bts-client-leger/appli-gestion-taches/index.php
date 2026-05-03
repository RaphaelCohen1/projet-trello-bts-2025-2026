<?php
require 'database.php';
$taches = $pdo->query("SELECT * FROM taches")->fetchAll();
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Gestion des tâches</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex flex-col items-center py-10">

    <h1 class="text-3xl font-bold text-blue-600 mb-5">📝 Gestion des tâches</h1>

    <!-- Formulaire d'ajout -->
    <form action="ajouter.php" method="post" class="flex space-x-2 mb-5">
        <input type="text" name="nom" placeholder="Nouvelle tâche" required
            class="border p-2 rounded-lg shadow-sm focus:ring focus:ring-blue-300">
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-600">
            ➕ Ajouter
        </button>
    </form>

    <!-- Liste des tâches -->
    <div class="w-full max-w-lg bg-white p-5 shadow-lg rounded-lg">
        <ul class="divide-y divide-gray-200">
            <?php foreach ($taches as $tache): ?>
                <li class="flex justify-between items-center py-3">
                    <span class="<?= $tache['statut'] ? 'line-through text-gray-500' : 'text-gray-900' ?>">
                        <?= htmlspecialchars($tache['nom']) ?>
                    </span>
                    <div class="space-x-2">
                        <?php if (!$tache['statut']): ?>
                            <a href="terminer.php?id=<?= $tache['id'] ?>" class="text-green-500 hover:text-green-700">✅</a>
                        <?php endif; ?>
                        <a href="modifier.php?id=<?= $tache['id'] ?>" class="text-yellow-500 hover:text-yellow-700">✏️</a>
                        <a href="supprimer.php?id=<?= $tache['id'] ?>" class="text-red-500 hover:text-red-700">🗑️</a>
                    </div>
                </li>
            <?php endforeach; ?>
        </ul>
    </div>

</body>
</html>

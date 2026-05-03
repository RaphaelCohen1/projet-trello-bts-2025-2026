<?php
$host = 'localhost';
$dbname = 'metsouyan';
$username = 'root';
$password = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Charger les entités
    if ($_GET['action'] == 'chargerEntites') {
        $stmt = $pdo->query("SELECT ID_ENTITE, NOM_ENTITE FROM T_ENTITE ORDER BY NOM_ENTITE ASC");
        $entites = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode($entites);
    }

    // Générer les requêtes SQL pour les entités mère et fille
    if ($_GET['action'] == 'genererSQL' && isset($_GET['entiteMere']) && isset($_GET['entiteFille'])) {
        $entiteMere = $_GET['entiteMere'];
        $entiteFille = $_GET['entiteFille'];
        
        // Récupérer l'ID de l'entité mère et de l'entité fille par leur nom
        $stmt = $pdo->prepare("SELECT ID_ENTITE FROM T_ENTITE WHERE NOM_ENTITE = ?");
        $stmt->execute([$entiteMere]);
        $entiteMereData = $stmt->fetch(PDO::FETCH_ASSOC);

        $stmt->execute([$entiteFille]);
        $entiteFilleData = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if ($entiteMereData && $entiteFilleData) {
            $idEntiteMere = $entiteMereData['ID_ENTITE'];
            $idEntiteFille = $entiteFilleData['ID_ENTITE'];
            
            // Récupérer les propriétés de l'entité mère
            $stmt = $pdo->prepare("SELECT p.NOM_PROPRIETE, t.NOM_TYPE_PROPRIETE, p.OBLIGATOIRE, p.VALEUR_DEFAUT
                                   FROM T_PROPRIETE p
                                   JOIN T_TYPE_PROPRIETE t ON p.ID_TYPE_PROPRIETE = t.ID_TYPE_PROPRIETE
                                   WHERE p.ID_ENTITE = ?");
            $stmt->execute([$idEntiteMere]);
            $proprietesMere = $stmt->fetchAll(PDO::FETCH_ASSOC);
            
            // Récupérer les propriétés de l'entité fille
            $stmt->execute([$idEntiteFille]);
            $proprietesFille = $stmt->fetchAll(PDO::FETCH_ASSOC);
            
            // Générer la requête SQL pour l'entité mère
            $sqlMere = "CREATE TABLE T_" . strtoupper(str_replace(' ', '_', $entiteMere)) . " (\n";
            $sqlMere .= "ID_" . strtoupper(str_replace(' ', '_', $entiteMere)) . " INT AUTO_INCREMENT PRIMARY KEY,\n";
            
            foreach ($proprietesMere as $propriete) {
                $nomPropriete = strtoupper(str_replace(' ', '_', $propriete['NOM_PROPRIETE']));
                $typePropriete = mapTypeToSQL($propriete['NOM_TYPE_PROPRIETE']);
                $nullable = $propriete['OBLIGATOIRE'] == 1 ? "NOT NULL" : "NULL";
                $defaultValue = $propriete['VALEUR_DEFAUT'] ? "DEFAULT '" . $propriete['VALEUR_DEFAUT'] . "'" : '';
                
                $sqlMere .= "$nomPropriete $typePropriete $nullable $defaultValue,\n";
            }
            
            $sqlMere = rtrim($sqlMere, ",\n") . "\n);";
            
            // Générer la requête SQL pour l'entité fille
            $sqlFille = "CREATE TABLE T_" . strtoupper(str_replace(' ', '_', $entiteFille)) . " (\n";
            $sqlFille .= "ID_" . strtoupper(str_replace(' ', '_', $entiteFille)) . " INT AUTO_INCREMENT PRIMARY KEY,\n";
            $sqlFille .= "ID_" . strtoupper(str_replace(' ', '_', $entiteMere)) . " INT,\n";
            
            foreach ($proprietesFille as $propriete) {
                $nomPropriete = strtoupper(str_replace(' ', '_', $propriete['NOM_PROPRIETE']));
                $typePropriete = mapTypeToSQL($propriete['NOM_TYPE_PROPRIETE']);
                $nullable = $propriete['OBLIGATOIRE'] == 1 ? "NOT NULL" : "NULL";
                $defaultValue = $propriete['VALEUR_DEFAUT'] ? "DEFAULT '" . $propriete['VALEUR_DEFAUT'] . "'" : '';
                
                $sqlFille .= "$nomPropriete $typePropriete $nullable $defaultValue,\n";
            }
            
            $sqlFille = rtrim($sqlFille, ",\n") . "\n);";
            
            // Ajouter la clé étrangère dans la table de l'entité fille
            $sqlFille .= "\nALTER TABLE T_" . strtoupper(str_replace(' ', '_', $entiteFille)) . " ";
            $sqlFille .= "ADD CONSTRAINT FK_" . strtoupper(str_replace(' ', '_', $entiteMere)) . "_TO_" . strtoupper(str_replace(' ', '_', $entiteFille)) . " ";
            $sqlFille .= "FOREIGN KEY (ID_" . strtoupper(str_replace(' ', '_', $entiteMere)) . ") ";
            $sqlFille .= "REFERENCES T_" . strtoupper(str_replace(' ', '_', $entiteMere)) . "(ID_" . strtoupper(str_replace(' ', '_', $entiteMere)) . ");";
            
            // Retourner les deux requêtes SQL
            echo $sqlMere . "\n\n" . $sqlFille;
        }
    }

    if ($_GET['action'] == 'genererSelect') {
        $entiteMere = $_GET['entiteMere'] ?? null;
        $entiteFille = $_GET['entiteFille'] ?? null;
    
        // Fonction pour récupérer les champs d'une entité
        function getChamps($pdo, $entite) {
            $stmt = $pdo->prepare("
                SELECT p.NOM_PROPRIETE 
                FROM T_PROPRIETE p
                JOIN T_ENTITE e ON p.ID_ENTITE = e.ID_ENTITE
                WHERE e.NOM_ENTITE = ?
            ");
            $stmt->execute([$entite]);
            $champs = $stmt->fetchAll(PDO::FETCH_COLUMN);
            return $champs;
        }
    
        if ($entiteMere && !$entiteFille) {
            // Cas 1 : Une seule entité
            $champsMere = getChamps($pdo, $entiteMere);
            echo "SELECT " . implode(', ', $champsMere) . " FROM T_" . strtoupper(str_replace(' ', '_', $entiteMere)) . ";";
        } elseif ($entiteMere && $entiteFille) {
            // Cas 2 : Deux entités avec jointure
            $champsMere = getChamps($pdo, $entiteMere);
            $champsFille = getChamps($pdo, $entiteFille);
    
            echo "SELECT " . implode(', ', array_map(fn($c) => "T1.$c", $champsMere)) . ", " .
                 implode(', ', array_map(fn($c) => "T2.$c", $champsFille)) . " " .
                 "FROM T_" . strtoupper(str_replace(' ', '_', $entiteMere)) . " T1 " .
                 "JOIN T_" . strtoupper(str_replace(' ', '_', $entiteFille)) . " T2 " .
                 "ON T1.ID_" . strtoupper(str_replace(' ', '_', $entiteMere)) . 
                 " = T2.ID_" . strtoupper(str_replace(' ', '_', $entiteMere)) . ";";
        }
    }
  // Action : Générer une liste déroulante pour l'entité mère (seulement le HTML, pas les options)
if ($_GET['action'] == 'generateDropdown') {
    $entite = $_GET['entite'] ?? null;

    if ($entite) {
        // Générer le HTML de la liste déroulante avec un label pour l'entité mère
        $dropdown = "<label for=\"{$entite}_dropdown\">Sélectionner une {$entite}</label>\n";
        $dropdown .= "<select id=\"{$entite}_dropdown\" name=\"{$entite}_dropdown\">\n";
        
        // Option vide par défaut
        $dropdown .= "    <option value=\"\">Sélectionner une {$entite}</option>\n";
        
        // Fermer la balise <select>
        $dropdown .= "</select>\n";

        // Retourner le HTML généré
        echo $dropdown;
    }
}


// Action : Générer les balises HTML pour les propriétés de l'entité fille avec un formulaire
if ($_GET['action'] == 'generateHtml') {
        // Récupérer les entités mère et fille depuis les paramètres d'URL
        $entiteMere = $_GET['entiteMere'] ?? null;
        $entiteFille = $_GET['entiteFille'] ?? null;
        $entiteFille = strtolower(htmlspecialchars($entiteFille, ENT_QUOTES, 'UTF-8'));


    if ($entiteMere && $entiteFille) {
        // Récupérer les propriétés associées à l'entité fille
        $stmt = $pdo->prepare("
            SELECT 
                e.NOM_ENTITE,
                p.NOM_PROPRIETE, 
                p.OBLIGATOIRE, 
                p.VALEUR_DEFAUT, 
                tp.NOM_TYPE_PROPRIETE 
            FROM T_PROPRIETE p
            JOIN T_ENTITE e ON p.ID_ENTITE = e.ID_ENTITE
            JOIN T_TYPE_PROPRIETE tp ON p.ID_TYPE_PROPRIETE = tp.ID_TYPE_PROPRIETE
            WHERE e.NOM_ENTITE = ?
        ");
        $stmt->execute([$entiteFille]);
        $proprietes = $stmt->fetchAll(PDO::FETCH_ASSOC);


        $stmtMere = $pdo->prepare("
        SELECT 
            e.NOM_ENTITE,
            p.NOM_PROPRIETE, 
            p.OBLIGATOIRE, 
            p.VALEUR_DEFAUT, 
            tp.NOM_TYPE_PROPRIETE 
        FROM T_PROPRIETE p
        JOIN T_ENTITE e ON p.ID_ENTITE = e.ID_ENTITE
        JOIN T_TYPE_PROPRIETE tp ON p.ID_TYPE_PROPRIETE = tp.ID_TYPE_PROPRIETE
        WHERE e.NOM_ENTITE = ?
    ");
    $stmtMere->execute([$entiteMere]);
    $proprietesMere = $stmtMere->fetch(PDO::FETCH_ASSOC);
    $nomProprieteMere = $proprietesMere['NOM_PROPRIETE'];
       
       
// Convertir l'entité fille en minuscules pour les fichiers dynamiques
$fichierCss = strtolower(htmlspecialchars($entiteFille, ENT_QUOTES, 'UTF-8')) . '.css';
$fichierJs = strtolower(htmlspecialchars($entiteFille, ENT_QUOTES, 'UTF-8')) . '.js';

// Générer le document HTML avec head et body
$html = '<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>' . htmlspecialchars($entiteFille, ENT_QUOTES, 'UTF-8') . '</title>
    <link rel="stylesheet" href="' . $fichierCss . '">
    <link rel="stylesheet" href="TEST.css">  
</head>
<body>';

$html .= "\n";

// Ajouter la navigation
$html .= '
    <nav class="navbar">
        <ul>
            <li><a href="' . strtolower(htmlspecialchars($entiteFille, ENT_QUOTES, 'UTF-8')) . '.html">' . strtoupper(htmlspecialchars($entiteFille, ENT_QUOTES, 'UTF-8')) . '</a></li>
        </ul>
    </nav>';
    $html .= "\n";


        // Générer le formulaire encadrant les balises HTML pour les propriétés de l'entité fille
        $html .= '<div class="cadre_global">
                <div class="col_gauche">
                    <h2 class="titre_entite">Gestion ' . ucfirst(strtolower(htmlspecialchars($entiteFille))) . '</h2>
                    <form class="formulaire">';

                    // Ajouter les boutons de l'étape suivante du formulaire
                    $html .= '<div class="ligne_boutons_form">
                    <button class="bouton" type="button" id="ajouter" onclick="ajouter' . ucfirst(strtolower(htmlspecialchars($entiteFille))) . '()">Ajouter</button>
                    <button class="bouton" type="button" id="modifier" onclick="modifier' . ucfirst(strtolower(htmlspecialchars($entiteFille))) . '()">Modifier</button>
                    <button class="bouton" type="button" id="rechercher" onclick="rechercher' . ucfirst(strtolower(htmlspecialchars($entiteFille))) . '()">Rechercher</button>
                    <button class="bouton" type="button" onclick="rechercher' . ucfirst(strtolower(htmlspecialchars($entiteMere)))  . ucfirst(strtolower(htmlspecialchars($entiteFille))) . '()">Rechercher ' . ucfirst(strtolower(htmlspecialchars($entiteFille))) . "s " . ucfirst(strtolower(htmlspecialchars($entiteMere))) . '</button>

                   
                    </div>';



                     $html .= '
                        <div class="ligne_form">
                            <label for="ID_' . ucfirst(strtoupper(htmlspecialchars($entiteMere))) . '" class="label_liste_deroulante">' . ucfirst(strtolower(htmlspecialchars($entiteMere))) . '</label>
                            <select class="liste_deroulante saisie" id="ID_' . ucfirst(strtoupper(htmlspecialchars($entiteMere))) . '"></select>
                        </div>';

        // Générer les balises HTML pour chaque propriété de l'entité fille
        foreach ($proprietes as $propriete) {
            $nomPropriete = htmlspecialchars($propriete['NOM_PROPRIETE']);
            $typePropriete = htmlspecialchars($propriete['NOM_TYPE_PROPRIETE']);
            $obligatoire = $propriete['OBLIGATOIRE'] ? 'required' : '';
            $valeurDefaut = htmlspecialchars($propriete['VALEUR_DEFAUT'] ?? '');

            // Ajouter une ligne de formulaire selon le type de propriété
            $html .= "<div class=\"ligne_form\">\n";
            $html .= "<label for=\"{$nomPropriete}\" class=\"label_{$nomPropriete}\">{$nomPropriete}</label>\n";

            switch (strtolower($typePropriete)) {
                case 'text':
                    $html .= "<input class=\"saisie\" type=\"text\" id=\"{$nomPropriete}\" name=\"{$nomPropriete}\" value=\"{$valeurDefaut}\" {$obligatoire} class=\"input_text\">\n";
                    break;

                case 'number':
                    $html .= "<input class=\"saisie\" type=\"number\" id=\"{$nomPropriete}\" name=\"{$nomPropriete}\" value=\"{$valeurDefaut}\" {$obligatoire} class=\"input_number\">\n";
                    break;

                case 'checkbox':
                    $checked = ($valeurDefaut === '1' || strtolower($valeurDefaut) === 'true') ? 'checked' : '';
                    $html .= "<input class=\"saisie\" type=\"checkbox\" id=\"{$nomPropriete}\" name=\"{$nomPropriete}\" {$checked} {$obligatoire} class=\"input_checkbox\">\n";
                    break;

                case 'textarea':
                    $html .= "<textarea id=\"{$nomPropriete}\" name=\"{$nomPropriete}\" {$obligatoire} class=\"textarea_input\">{$valeurDefaut}</textarea>\n";
                    break;

                case 'date':
                    $html .= "<input class=\"saisie\" type=\"date\" id=\"{$nomPropriete}\" name=\"{$nomPropriete}\" value=\"{$valeurDefaut}\" {$obligatoire} class=\"input_date\">\n";
                    break;

                default:
                    $html .= "<!-- Type inconnu pour {$nomPropriete} -->\n";
                    break;
            }

            $html .= "</div>\n";  // Fermer la ligne du formulaire
        }

        $html .= '</form>
                    </div>';

                    $html .= '
                    <div class="table_affichage" id="table_container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Action</th>';
                                    $nomProprieteMere = htmlspecialchars($nomProprieteMere);
                                    $html .= "<th>{$nomProprieteMere}</th>";
                    foreach ($proprietes as $propriete) {
                        $nomPropriete = htmlspecialchars($propriete['NOM_PROPRIETE']);
                        $html .= "<th>{$nomPropriete}</th>";
                    }
                    $html .= '    </tr>
                            </thead>
                            <tbody id="table_body">
                            </tbody>
                        </table>
                    </div>
                </div>';
               
                // Convertir l'entité fille en minuscules

// Ajouter la balise script avec la variable
$html .= "
    <script src=\"{$fichierJs}\"></script>
    </body>
</html>
";
                

        // Afficher le HTML généré
        echo $html;
    }
}



} catch (PDOException $e) {
    echo 'Erreur de connexion : ' . $e->getMessage();
}

// Fonction pour mapper les types de propriété aux types SQL
function mapTypeToSQL($type) {
    switch ($type) {
        case 'TEXTE':
            return 'VARCHAR(255)';
        case 'ENTIER':
            return 'INT';
        case 'DATE':
            return 'DATE';
        case 'OUI_NON':
            return 'BOOLEAN';
        default:
            return 'VARCHAR(255)';
    }
}
?>

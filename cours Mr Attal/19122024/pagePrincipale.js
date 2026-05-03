document.addEventListener('DOMContentLoaded', function() {
    chargerEntites();
});

let entitesTraitees = new Set();  // Ensemble pour stocker les entités déjà traitées

async function chargerEntites() {
    try {
        const response = await fetch('pagePrincipale.php?action=chargerEntites');
        const data = await response.json();

        const tableBody = document.querySelector("#table_entites tbody");

        // Créer 20 lignes avec 2 listes déroulantes par ligne
        for (let i = 0; i < 20; i++) {
            const row = document.createElement('tr');

            const cell1 = document.createElement('td');
            const select1 = createSelect(data);
            cell1.appendChild(select1);

            const cell2 = document.createElement('td');
            const select2 = createSelect(data);
            cell2.appendChild(select2);

            row.appendChild(cell1);
            row.appendChild(cell2);
            tableBody.appendChild(row);
        }
    } catch (error) {
        console.error('Erreur lors du chargement des entités:', error);
    }
}

function createSelect(entites) {
    const select = document.createElement('select');
    // Créer l'option vide en premier
    const defaultOption = document.createElement('option');
    defaultOption.value = ''; // valeur vide pour la première option
    defaultOption.textContent = 'Sélectionner une entité';
    select.appendChild(defaultOption);

    entites.forEach(entite => {
        const option = document.createElement('option');
        option.value = entite.ID_ENTITE;
        option.textContent = entite.NOM_ENTITE;
        select.appendChild(option);
    });

    return select;
}

async function sqlCreate() {
    const selects = document.querySelectorAll('#table_entites select');
    let queries = '';

    // On récupère les valeurs de chaque ligne (colonne de gauche et colonne de droite)
    for (let i = 0; i < selects.length; i += 2) {
        const selectMere = selects[i];
        const selectFille = selects[i + 1];

        const entiteMere = selectMere.options[selectMere.selectedIndex].text;
        const entiteFille = selectFille.options[selectFille.selectedIndex].text;

        if (entiteMere !== 'Sélectionner une entité' && entiteMere !== '' && entiteFille !== 'Sélectionner une entité' && entiteFille !== '') {
            // Générer les requêtes SQL pour les entités sélectionnées
            if (!entitesTraitees.has(entiteMere)) {
                queries += await genererSQL(entiteMere, null) + '\n\n';
                entitesTraitees.add(entiteMere);  // Marquer l'entité mère comme traitée
            }

            if (!entitesTraitees.has(entiteFille)) {
                queries += await genererSQL(entiteFille, null) + '\n\n';
                entitesTraitees.add(entiteFille);  // Marquer l'entité fille comme traitée
            }

            // Générer la requête de relation entre les entités (clé étrangère)
            queries += await genererSQL(entiteMere, entiteFille) + '\n\n';
        }
    }

    document.getElementById('resultat').value = queries;
}

// Fonction pour générer la requête SQL pour les entités sélectionnées
async function genererSQL(entiteMere, entiteFille) {
    try {
        const response = await fetch(`pagePrincipale.php?action=genererSQL&entiteMere=${encodeURIComponent(entiteMere)}&entiteFille=${encodeURIComponent(entiteFille)}`);
        const data = await response.text();
        return data;  // Retourne la requête générée pour l'entité mère et fille
    } catch (error) {
        console.error('Erreur lors de la génération SQL:', error);
        return ''; // En cas d'erreur, retourner une chaîne vide
    }
}
async function sqlSelect() {
    const selects = document.querySelectorAll('#table_entites select');
    let queries = ''; // Variable pour accumuler les requêtes SQL

    for (let i = 0; i < selects.length; i += 2) {
        const selectMere = selects[i];
        const selectFille = selects[i + 1];

        const entiteMere = selectMere.options[selectMere.selectedIndex].text;
        const entiteFille = selectFille.options[selectFille.selectedIndex].text;

        // Cas 1 : Une seule entité (colonne de gauche uniquement)
        if (entiteMere !== 'Sélectionner une entité' && entiteMere !== '' &&
            (entiteFille === 'Sélectionner une entité' || entiteFille === '')) {
            queries += await genererSelect(entiteMere, null) + '\n\n';
        }

        // Cas 2 : Deux entités sélectionnées (mère et fille)
        if (entiteMere !== 'Sélectionner une entité' && entiteMere !== '' &&
            entiteFille !== 'Sélectionner une entité' && entiteFille !== '') {
            queries += await genererSelect(entiteMere, entiteFille) + '\n\n';
        }
    }

    // Afficher les requêtes générées dans la textarea
    document.getElementById('resultat').value = queries;
}

// Fonction pour générer une requête SELECT
async function genererSelect(entiteMere, entiteFille) {
    try {
        const response = await fetch(`pagePrincipale.php?action=genererSelect&entiteMere=${encodeURIComponent(entiteMere)}&entiteFille=${encodeURIComponent(entiteFille)}`);
        const data = await response.text();
        return data;
    } catch (error) {
        console.error('Erreur lors de la génération SELECT:', error);
        return ''; // En cas d'erreur, retourner une chaîne vide
    }
}
async function generateHtml() {
    const selects = document.querySelectorAll('#table_entites select');
    let htmlCode = '';

    for (let i = 0; i < selects.length; i += 2) {
        const selectMere = selects[i];
        const entiteMere = selectMere.options[selectMere.selectedIndex].text;

        if (entiteMere !== 'Sélectionner une entité' && entiteMere !== '') {
            // Récupération du code HTML pour l'entité mère
            htmlCode += await fetchHtml(entiteMere) + '\n\n';
        }
    }

    // Afficher le code HTML dans la zone de texte
    document.getElementById('resultat').value = htmlCode;
}

// Fonction pour récupérer le HTML généré pour une entité
async function fetchHtml(entiteMere, entiteFille) {
    try {
        // Construire l'URL avec les deux paramètres d'entités
        const url = `pagePrincipale.php?action=generateHtml&entiteMere=${encodeURIComponent(entiteMere)}&entiteFille=${encodeURIComponent(entiteFille)}`;

        // Faire la requête fetch avec l'URL modifiée
        const response = await fetch(url);
        
        // Vérifier si la réponse est OK
        if (!response.ok) {
            throw new Error('Erreur lors de la récupération des données.');
        }

        // Récupérer le texte HTML
        const data = await response.text();

        // Retourner le HTML généré
        return data;
    } catch (error) {
        console.error('Erreur lors de la génération du HTML:', error);
        return '';
    }
}

async function generateHtmlWithRelation() {
    const selects = document.querySelectorAll('#table_entites select');
    let htmlCode = '';

    for (let i = 0; i < selects.length; i += 2) {
        const selectMere = selects[i];
        const selectFille = selects[i + 1];

        const entiteMere = selectMere.options[selectMere.selectedIndex].text;
        const entiteFille = selectFille.options[selectFille.selectedIndex].text;

        if (entiteMere !== 'Sélectionner une entité' && entiteMere !== '' &&
            entiteFille !== 'Sélectionner une entité' && entiteFille !== '') {
            
            // Génération de la liste déroulante pour l'entité mère
         //   htmlCode += await fetchHtmlDropdown(entiteMere) + '\n\n';

            // Génération des balises HTML pour les propriétés de l'entité fille
            htmlCode += await fetchHtml(entiteMere,entiteFille) + '\n\n';
        }
    }

    // Afficher le code HTML dans la zone de texte
    document.getElementById('resultat').value = htmlCode;
}

// Fonction pour récupérer la liste déroulante d'une entité mère
async function fetchHtmlDropdown(entite) {
    try {
        const response = await fetch(`pagePrincipale.php?action=generateDropdown&entite=${encodeURIComponent(entite)}`);
        const data = await response.text();
        return data;
    } catch (error) {
        console.error('Erreur lors de la génération du dropdown HTML:', error);
        return '';
    }
}

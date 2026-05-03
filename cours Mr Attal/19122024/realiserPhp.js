async function generatePhpCode() {
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
            htmlCode += await listerLesProprietes(entiteMere,entiteFille) + '\n\n';
        }
    }

    // Afficher le code HTML dans la zone de texte
    document.getElementById('resultat').value = htmlCode;
}

// Fonction pour récupérer le HTML généré pour une entité
async function listerLesProprietes(entiteMere, entiteFille) {
    try {
        // Construire l'URL avec les deux paramètres d'entités
        const url = `realiserPhp.php?action=genererPhp&entiteMere=${encodeURIComponent(entiteMere)}&entiteFille=${encodeURIComponent(entiteFille)}`;

        // Faire la requête fetch avec l'URL modifiée
        const response = await fetch(url);
        
        // Vérifier si la réponse est OK
        if (!response.ok) {
            throw new Error('Erreur lors de la récupération des données.');
        }

        // Récupérer le texte php
        const data = await response.text();

        // Retourner le php généré
        return data;
    } catch (error) {
        console.error('Erreur lors de la génération du php:', error);
        return '';
    }
}

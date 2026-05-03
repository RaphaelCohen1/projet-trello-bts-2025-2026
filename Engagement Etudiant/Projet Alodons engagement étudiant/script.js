document.addEventListener('DOMContentLoaded', () => {
    let montantChoisi = null;

    const boutonsMontants = document.querySelectorAll('#montants-suggérés button');
    const champAutreMontant = document.getElementById('champ-autre-montant');
    const champMontant = document.getElementById('autre-montant');
    const boutonValider = document.getElementById('valider-don');

    if (boutonsMontants.length > 0) {
        boutonsMontants.forEach(btn => {
            btn.addEventListener('click', () => {
                const montant = btn.getAttribute('data-montant');

                if (montant === "autre" && champAutreMontant) {
                    champAutreMontant.style.display = "block";
                    montantChoisi = null;
                } else if (champAutreMontant) {
                    champAutreMontant.style.display = "none";
                    montantChoisi = parseInt(montant);
                }

                boutonsMontants.forEach(b => b.classList.remove('actif'));
                btn.classList.add('actif');
            });
        });
    }

    if (boutonValider) {
        boutonValider.addEventListener('click', () => {
            if (montantChoisi !== null) {
                alert(`Montant choisi : ${montantChoisi}€`);
            } else if (champMontant && champMontant.value) {
                alert(`Montant personnalisé : ${champMontant.value}€`);
            } else {
                alert("Veuillez choisir un montant.");
            }
        });
    }
});

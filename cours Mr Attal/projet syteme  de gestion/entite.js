document.addEventListener("DOMContentLoaded", () => {
    const url = "entite.php";

    const idField = document.getElementById("id_entite");
    const nomField = document.getElementById("nom_entite");
    const rechercheField = document.getElementById("recherche_entite");
    const tableBody = document.getElementById("table_body");

    const loadData = (filter = "") => {
        fetch(`${url}?action=fetch&filter=${filter}`)
            .then(response => response.json())
            .then(data => {
                tableBody.innerHTML = "";
                data.forEach(row => {
                    tableBody.innerHTML += `
                        <tr>
                            <td>
                                <button class="bouton_action_modif" onclick="editRow(${row.ID_ENTITE})">Modifier</button>
                                <button class="bouton_action_supprime" onclick="deleteRow(${row.ID_ENTITE})">Supprimer</button>
                            </td>
                            <td>${row.ID_ENTITE}</td>
                            <td>${row.NOM_ENTITE}</td>
                        </tr>`;
                });
            });
    };

    const addOrUpdate = (action) => {
        const formData = new FormData();
        formData.append("id", idField.value);
        formData.append("nom", nomField.value);
        formData.append("action", action);

        fetch(url, { method: "POST", body: formData })
            .then(response => response.json())
            .then(() => loadData());
    };

    window.editRow = (id) => {
        fetch(`${url}?action=edit&id=${id}`)
            .then(response => response.json())
            .then(data => {
                idField.value = data.ID_ENTITE;
                nomField.value = data.NOM_ENTITE;
            });
    };

    window.deleteRow = (id) => {
        if (confirm("Confirmer la suppression ?")) {
            fetch(`${url}?action=delete&id=${id}`)
                .then(() => loadData());
        }
    };

    document.getElementById("ajouter").addEventListener("click", () => addOrUpdate("add"));
    document.getElementById("modifier").addEventListener("click", () => addOrUpdate("update"));
    document.getElementById("rechercher").addEventListener("click", () => loadData(rechercheField.value));

    loadData();
});
// layout.js
import React from 'react';
const StyledParagraph = styled.p`
    color: blue;
    `;
//Présentation de la déclaration du composant
const Layout = () => {
    return (
/*Les éléments HTML sont retournés à l'intérieur d'un fragment ( <> </>),
 ce qui permet d'inclure plusieurs éléments sans ajouter de nœud supplémentaire dans le DOM.
  */
    <>
      <p>Bonjour</p>
      <p>Ca va ?</p>
      <p>Où va tu ?</p>  
            
      <table>
                <thead>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Gender</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Anom</td>
                        <td>19</td>
                        <td>Male</td>
                    </tr>
                    <tr>
                        <td>Megha</td>
                        <td>19</td>
                        <td>Female</td>
                    </tr>
                    <tr>
                        <td>Subham</td>
                        <td>25</td>
                        <td>Male</td>
                    </tr>
                </tbody>
            </table>
        </>
    );
};

//FonctionReactDOM.render :Permet d'afficher le composant Layoutdans le DOM. Utilisez l'élément HTML avec l'ID "root"comme point de montage.
ReactDOM.render(<Layout />, document.getElementById("root"));

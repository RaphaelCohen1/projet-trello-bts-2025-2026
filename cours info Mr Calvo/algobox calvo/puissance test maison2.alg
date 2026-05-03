<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER Produit" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2defaut="" F2para="" F2lignes="" F2etat="inactif"/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param arrondiAuto="vrai" epaisseurLigne="2" totalBoucles="5000000" epaisseurPoint="2" maxBoucle="500000" nbDecimales="8" totalAffichages="1000"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="nb EST_DU_TYPE NOMBRE" code="1#NOMBRE#nb"/>
        <item algoitem="i EST_DU_TYPE NOMBRE" code="1#NOMBRE#i"/>
        <item algoitem="Produit EST_DU_TYPE NOMBRE" code="1#NOMBRE#Produit"/>
        <item algoitem="Puissance EST_DU_TYPE NOMBRE" code="1#NOMBRE#Puissance"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="Produit PREND_LA_VALEUR 1" code="5#Produit#1#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrer un nombre entier&quot;" code="4#Entrer un nombre entier#0"/>
        <item algoitem="LIRE nb" code="2#nb#pasliste"/>
        <item algoitem="AFFICHER Puissance" code="3#Puissance#0#pasliste"/>
        <item algoitem="LIRE Puissance" code="2#Puissance#pasliste"/>
        <item algoitem="POUR i ALLANT_DE 1 A Puissance" code="12#i#1#Puissance">
            <item algoitem="DEBUT_POUR" code="13#debutpour"/>
            <item algoitem="Produit PREND_LA_VALEUR Produit*nb" code="5#Produit#Produit*nb#pasliste"/>
            <item algoitem="FIN_POUR" code="14#finpour"/>
        </item>
        <item algoitem="AFFICHER Produit" code="3#Produit#0#pasliste"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>

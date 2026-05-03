<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="POUR i ALLANT_DE 1 A puissance"/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2para="" F2etat="inactif" F2lignes="" F2defaut=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param epaisseurPoint="2" nbDecimales="8" epaisseurLigne="2" totalBoucles="5000000" totalAffichages="1000" arrondiAuto="vrai" maxBoucle="500000"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#nb" algoitem="nb EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#puissance" algoitem="puissance EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#i" algoitem="i EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#produit" algoitem="produit EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="5#produit#1#pasliste" algoitem="produit PREND_LA_VALEUR 1"/>
        <item code="4#entrer un nombre entier#1" algoitem="AFFICHER &quot;entrer un nombre entier&quot;"/>
        <item code="2#nb#pasliste" algoitem="LIRE nb"/>
        <item code="4#Puissance#1" algoitem="AFFICHER &quot;Puissance&quot;"/>
        <item code="2#puissance#pasliste" algoitem="LIRE puissance"/>
        <item code="12#i#1#puissance" algoitem="POUR i ALLANT_DE 1 A puissance">
            <item code="13#debutpour" algoitem="DEBUT_POUR"/>
            <item code="5#produit#produit*nb#pasliste" algoitem="produit PREND_LA_VALEUR produit*nb"/>
            <item code="14#finpour" algoitem="FIN_POUR"/>
        </item>
        <item code="3#produit#1#pasliste" algoitem="AFFICHER produit"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>

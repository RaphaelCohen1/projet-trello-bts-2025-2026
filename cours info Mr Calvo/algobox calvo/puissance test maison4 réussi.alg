<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="LIRE produit"/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2para="" F2defaut="" F2lignes="" F2etat="inactif"/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param arrondiAuto="vrai" epaisseurLigne="2" nbDecimales="8" epaisseurPoint="2" totalBoucles="5000000" totalAffichages="1000" maxBoucle="500000"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#nb" algoitem="nb EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#produit" algoitem="produit EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#i" algoitem="i EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#puissance" algoitem="puissance EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="5#produit#1#pasliste" algoitem="produit PREND_LA_VALEUR 1"/>
        <item code="4#Entrer un nombre#0" algoitem="AFFICHER &quot;Entrer un nombre&quot;"/>
        <item code="3#nb#0#pasliste" algoitem="AFFICHER nb"/>
        <item code="2#nb#pasliste" algoitem="LIRE nb"/>
        <item code="3#puissance#0#pasliste" algoitem="AFFICHER puissance"/>
        <item code="2#puissance#pasliste" algoitem="LIRE puissance"/>
        <item code="12#i#1#puissance" algoitem="POUR i ALLANT_DE 1 A puissance">
            <item code="13#debutpour" algoitem="DEBUT_POUR"/>
            <item code="20#produit*nb#0" algoitem="AFFICHERCALCUL produit*nb"/>
            <item code="14#finpour" algoitem="FIN_POUR"/>
        </item>
        <item code="2#produit#pasliste" algoitem="LIRE produit"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>

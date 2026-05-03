<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="SI ((NOMBRE_ENTIER%2==0)) ALORS"/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2lignes="" F2para="" F2etat="inactif" F2defaut=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param arrondiAuto="vrai" totalBoucles="5000000" epaisseurPoint="2" nbDecimales="8" epaisseurLigne="2" maxBoucle="500000" totalAffichages="1000"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#NOMBRE_ENTIER" algoitem="NOMBRE_ENTIER EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="4#Entrer un nombre#1" algoitem="AFFICHER &quot;Entrer un nombre&quot;"/>
        <item code="2#NOMBRE_ENTIER#pasliste" algoitem="LIRE NOMBRE_ENTIER"/>
        <item code="15#NOMBRE_ENTIER>=0" algoitem="TANT_QUE (NOMBRE_ENTIER>=0) FAIRE">
            <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
            <item code="6#(NOMBRE_ENTIER%2==0)" algoitem="SI ((NOMBRE_ENTIER%2==0)) ALORS">
                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                <item code="4#Le nombre est impaire#1" algoitem="AFFICHER &quot;Le nombre est impaire&quot;"/>
                <item code="8#finsi" algoitem="FIN_SI"/>
                <item code="9#sinon" algoitem="SINON">
                    <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                    <item code="4#Le nombre est impair#1" algoitem="AFFICHER &quot;Le nombre est impair&quot;"/>
                    <item code="11#finsinon" algoitem="FIN_SINON"/>
                </item>
            </item>
            <item code="4#Entrez un autre nombre#1" algoitem="AFFICHER &quot;Entrez un autre nombre&quot;"/>
            <item code="2#NOMBRE_ENTIER#pasliste" algoitem="LIRE NOMBRE_ENTIER"/>
            <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>

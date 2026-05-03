<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="SI ((age>=1  ET age &lt;=10)) ALORS"/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2etat="inactif" F2defaut="" F2lignes="" F2para=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param totalBoucles="5000000" totalAffichages="1000" maxBoucle="500000" epaisseurPoint="2" epaisseurLigne="2" nbDecimales="8" arrondiAuto="vrai"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#age" algoitem="age EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="4#Entrer votre Age:#1" algoitem="AFFICHER &quot;Entrer votre Age:&quot;"/>
        <item code="2#age#pasliste" algoitem="LIRE age"/>
        <item code="6#(age>=1  ET age &lt;=10)" algoitem="SI ((age>=1  ET age &lt;=10)) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="4#Tu est un Enfant#1" algoitem="AFFICHER &quot;Tu est un Enfant&quot;"/>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="4#Vous etes un adultes#0" algoitem="AFFICHER &quot;Vous etes un adultes&quot;"/>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>

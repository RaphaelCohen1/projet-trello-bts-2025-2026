<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="FONCTIONS_UTILISEES" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2etat="inactif" F2defaut="" F2para="" F2lignes=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param maxBoucle="500000" arrondiAuto="vrai" epaisseurLigne="2" totalBoucles="5000000" nbDecimales="8" totalAffichages="1000" epaisseurPoint="2"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#Age" algoitem="Age EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#Grand" algoitem="Grand EST_DU_TYPE CHAINE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="12#Age#1#3" algoitem="POUR Age ALLANT_DE 1 A 3">
            <item code="13#debutpour" algoitem="DEBUT_POUR"/>
            <item code="4#Votre age est de #1" algoitem="AFFICHER &quot;Votre age est de &quot;"/>
            <item code="2#Age#pasliste" algoitem="LIRE Age"/>
            <item code="6#(&quot;Age&lt;=3&quot;)" algoitem="SI ((&quot;Age&lt;=3&quot;)) ALORS">
                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                <item code="4#Je suis petit#1" algoitem="AFFICHER &quot;Je suis petit&quot;"/>
                <item code="8#finsi" algoitem="FIN_SI"/>
                <item code="9#sinon" algoitem="SINON">
                    <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                    <item code="4#Je suis grand#1" algoitem="AFFICHER &quot;Je suis grand&quot;"/>
                    <item code="11#finsinon" algoitem="FIN_SINON"/>
                </item>
            </item>
            <item code="6#&quot;(Age&lt;=3)&quot;" algoitem="SI (&quot;(Age&lt;=3)&quot;) ALORS">
                <item code="7#debutsi" algoitem="DEBUT_SI"/>
                <item code="4#Je suis petit#1" algoitem="AFFICHER &quot;Je suis petit&quot;"/>
                <item code="8#finsi" algoitem="FIN_SI"/>
                <item code="9#sinon" algoitem="SINON">
                    <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                    <item code="4#Je suis grand#1" algoitem="AFFICHER &quot;Je suis grand&quot;"/>
                    <item code="11#finsinon" algoitem="FIN_SINON"/>
                </item>
            </item>
            <item code="14#finpour" algoitem="FIN_POUR"/>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>

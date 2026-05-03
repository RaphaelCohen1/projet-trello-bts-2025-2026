<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER &quot;Entrer votre age:&quot;" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2etat="inactif" F2defaut="" F2lignes="" F2para=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param maxBoucle="500000" nbDecimales="8" arrondiAuto="vrai" epaisseurPoint="2" epaisseurLigne="2" totalAffichages="1000" totalBoucles="5000000"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#age" algoitem="age EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="4#Entrer votre age:#0" algoitem="AFFICHER &quot;Entrer votre age:&quot;"/>
        <item code="2#age#pasliste" algoitem="LIRE age"/>
        <item code="15#age&lt;=0" algoitem="TANT_QUE (age&lt;=0) FAIRE">
            <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
            <item code="4#erreur age négatif#0" algoitem="AFFICHER &quot;erreur age négatif&quot;"/>
            <item code="4#merci de rentrer un nombre positif#1" algoitem="AFFICHER &quot;merci de rentrer un nombre positif&quot;"/>
            <item code="2#age#pasliste" algoitem="LIRE age"/>
            <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
        </item>
        <item code="6#age&lt;11" algoitem="SI (age&lt;11) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="4#tu est un enfant#1" algoitem="AFFICHER &quot;tu est un enfant&quot;"/>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="6#age&lt;18" algoitem="SI (age&lt;18) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="4#tu est un ado#1" algoitem="AFFICHER &quot;tu est un ado&quot;"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                    <item code="9#sinon" algoitem="SINON">
                        <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                        <item code="4#tu est un adulte#0" algoitem="AFFICHER &quot;tu est un adulte&quot;"/>
                        <item code="11#finsinon" algoitem="FIN_SINON"/>
                    </item>
                </item>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>

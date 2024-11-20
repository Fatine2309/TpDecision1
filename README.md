# TpDecision1
Introduction


Ce rapport va expliquer le processus de nettoyage des données, la méthodologie pour préparer le dataset. les résultats obtenus avec un arbre de décision sur les données des collisions avec des oiseaux.


Méthodologie:


Chargement des Données:

Les données ont été extraites du fichier Bird_strikes.csv, en limitant l'importation à 40 lignes pour une démonstration rapide. 
Nettoyage des Données:

Le nettoyage a consisté à :


1.	Remplacement des valeurs manquantes par 0 :

   
   o	Les colonnes contenant des valeurs manquantes (NaN) ont été nettoyées avec la méthode fillna(0) pour éviter les erreurs lors des calculs.

   
2.	Conversion en valeurs numériques :
   
   o	Les colonnes suivantes ont été converties en valeurs numériques :
  		PeopleInjured : Nombre de personnes blessées
  		NumberStruckActual : Nombre d'oiseaux effectivement frappés.
  		Damage : Encodée en 0 pour "aucun dommage" et 1 pour "dommage causé".
  	  Engines : Nombre de moteurs de l'avion.
    
  	o	Les données non convertibles ont été remplacées par 0 via errors="coerce".
   


Conclusion


o Nettoyage des Données
Le nettoyage a permis d'obtenir un dataset prêt pour l'analyse en éliminant les valeurs manquantes et en transformant les colonnes catégoriques en valeurs numériques. Cela a évité des erreurs d'exécution et amélioré la compatibilité avec les algorithmes de machine learning.
•	Le choix de colonnes a permis d'avoir le nombre d'oiseaux frappés, les blessures humaines et les dommages structuraux sont des facteurs directement liés à la sécurité aérienne et à la conception des avions.

  	  
  	  



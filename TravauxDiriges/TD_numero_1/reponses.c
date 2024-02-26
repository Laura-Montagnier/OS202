/*Réponses aux questions

Question 1 :
Pourquoi changer l'ordre des boucles change le temps d'exécution alors que la complexité reste la même ?

C'est à cause de la complexité d'accès mémoire : de la hiérarchie des caches.
C'est un problème qui n'existait pas quand les processeurs n'avaient qu'un seul coeur.

L'information est stockée en colonnes, c'est donc plus rapide de parcourir les colonnes plutôt que les lignes :
parcourir les lignes implique un chemin NON CONTIGU, alors que parcourir les colonnes implique un chemin CONTIGU.
Il faut donc maximiser le parcours par colonnes :

    pour j in colonne
        pour k in colonne
            pour i in ligne


Question 2 :

...

Voir le pdf de réponse (il est plus complet, j'avais besoin d'ajouter des images et des tableaux).
*/

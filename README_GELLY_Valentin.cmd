
# Lancement programme

Après avoir lancé le programme il vous faut juste entrer le nom du fichier qui contient les données des Personnes.


# Infos complémentaire :

Un bus peut avoir 4 état :
    - le bus est à un arret sans rien faire
    - le bus est en train de faire un trajet
    - le bus est à un arret et est en train de charger des personnes
    - le bus est à un arret et en train de virer des personnes

Une personne peut avoir 2 état :
    - la personne est dans un bus
    - la personne est à un arret et attend un bus

# Complexité

    ## Complexite algo faire monter une personnes

       Cette algo permet de faire monter une personne dans un bus.
       Elle est de complexité O(n) avec n le nombre de personne qui est à un arret.

    ## Complexite algo faire descendre une personnes

       Cette algo permet de faire descendre une personne dans un bus.
       Elle est de complexité O(n) avec n le nombre de personne qui est dans un bus.


    ## Complexité algo définir le parcours d'un bus (ligne 106) / définir le parcours d'une personne (ligne 131)

        Cette algo permet de définir les différentes routes (step dans le programme) que le bus/personne va faire.
        Cette algo a pour complexité f(n) = nlog(n)+log(n)
        Cette algo fait donc partie de la famille O(nlog(n))



# Fonctionnalité programme

    ## Ce que le programme fait :
        Le programme permet de faire circuler les différentes personnes entre plusieurs points.
        si une personne a besoin d'aller à un arret non disponible en direct alors il descend pour faire une correspondance ( si prochaine étape de la personne n'est pas la meme que celle du bus alors il en descend)
        les trajet des bus est réalisé en fonction de la distance entre les différents points pour faire le plus petit voyage.
        Le trajet des personnes est défini pour faire le moins d'étape entre les deux points

    ## Ce que le programme ne fait pas :

        Il ne se base pas sur les temps d'attente pour faire les trajet des personnes.

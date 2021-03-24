"""
EXERCICE PYTHON
> creer un programme simulant un combat qui respecte les regles suivantes:
    - 2 joueurs qui choisiront leur pseudo, 250 pv chacun
    - 4 attaques alternants joueur1 et joueur2
    - chaque attaque est une tentative (si reussit le joueur inflige entre 0 et 100)
                                        (si echoue c'est au tour de l'autre)
    - a la fin le gagnant est celui avec le plus de pv
"""
import random
import time

class player:
    pv = 250
    def __init__(self, pseudo):
        self.name = pseudo


def swap(var1, var2):
    tmp = var1
    var1 = var2
    var2 = tmp


def combat(joueur1, joueur2):
    i = 0
    attaquant = joueur1
    adversaire = joueur2
    while i < 4:
        if random.choice([True, False]):
            adversaire.pv -= random.randint(0, 100)
        swap(attaquant, adversaire)
        i += 1


if __name__ == '__main__':
    print("START")
    joueur1 = player(str(input("Player 1 choose a pseudo : ")))
    print("Bonjour {} !".format(joueur1.name))
    joueur2 = player(str(input("Player 2 choose a pseudo : ")))
    print("Bonjour {} !".format(joueur2.name))
    print("\nCOMBAT...")
    time.sleep(5)
    combat(joueur1, joueur2)
    print("\nRESULT")
    if joueur1.pv == joueur2.pv:
        print("Vous etes à égalité avec {} pv chacun.".format(joueur2.pv))
        exit(0)
    elif joueur1.pv > joueur2.pv:
        winner = joueur1.name
    else:
        winner = joueur2.name
    print("Bravo {}, vous l'empoter à {} contre {}.".format(winner, joueur1.pv, joueur2.pv))
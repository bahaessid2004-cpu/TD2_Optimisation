import random


distances = [
    [0,14,15,13,22,17,9,21],
    [14,0,11,21,19,8,17,5],
    [15,11,0,20,18,15,10,13],
    [13,21,20,0,15,18,19,12],
    [22,19,18,15,0,15,18,11],
    [17,8,15,18,15,0,15,10],
    [9,17,10,19,18,15,0,13],
    [21,5,13,12,11,10,13,0]
]
def cout(route):
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]
    total += distances[route[-1]][route[0]]  # retour à la ville de départ
    return total


def tabou_tsp(iterations: int = 200, taille_tabou: int = 15):
    courant = list(range(8))  # villes 0 à 7
    meilleur = courant[:]
    liste_tabou = []

    for _ in range(iterations):
        voisins = []
        for i in range(8):
            for j in range(i + 1, 8):
                nouv = courant[:]
                nouv[i], nouv[j] = nouv[j], nouv[i]
                voisins.append(nouv)
        voisins = [v for v in voisins if v not in liste_tabou]
        suivant = min(voisins, key=cout)
        if cout(suivant) < cout(meilleur):
            meilleur = suivant
        liste_tabou.append(suivant)
        if len(liste_tabou) > taille_tabou:
            liste_tabou.pop(0)
        courant = suivant
    return meilleur, cout(meilleur)

meilleur_trajet, meilleur_cout = tabou_tsp()
print("Meilleur trajet trouvé :", meilleur_trajet)
print("Coût minimal :", meilleur_cout)

import random
couts = [[5, 4, 8],[6, 7, 9]]
demandes = [4, 5, 8]
capacites = [8, 9]

def cout_total(solution):
    cout = 0
    for d in range(len(couts)):
        for m in range(len(couts[0])):
            cout += couts[d][m] * solution[d][m]
    return cout

def solution_initiale():
    sol = [[0]*len(demandes) for _ in range(len(capacites))]
    reste = demandes[:]
    cap = capacites[:]
    for m in range(len(demandes)):
        for d in range(len(capacites)):
            if reste[m] > 0 and cap[d] > 0:
                x = min(reste[m], cap[d])
                sol[d][m] = x
                reste[m] -= x
                cap[d] -= x
    return sol


def voisins(sol):
    voisins = []
    for d in range(len(sol)):
        for m in range(len(sol[0])):
            nouv = [row[:] for row in sol]
            nouv[d][m] = max(0, sol[d][m] + random.choice([-1, 1]))
            voisins.append(nouv)
    return voisins


def recherche_tabou(iterations=100, taille_tabou=10):
    courant = solution_initiale()
    meilleur = courant
    liste_tabou = []
    for _ in range(iterations):
        voisins_possibles = voisins(courant)
        voisins_possibles = [v for v in voisins_possibles if v not in liste_tabou]
        if not voisins_possibles:
            break
        suivant = min(voisins_possibles, key=cout_total)
        if cout_total(suivant) < cout_total(meilleur):
            meilleur = suivant
        liste_tabou.append(suivant)
        if len(liste_tabou) > taille_tabou:
            liste_tabou.pop(0)
        courant = suivant
    return meilleur, cout_total(meilleur)

solution, cout = recherche_tabou()
print("Solution optimale :", solution)
print("Coût minimal :", cout)

import math, random

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
    return sum(distances[route[i]][route[i+1]] for i in range(len(route)-1)) + distances[route[-1]][route[0]]

def recuit_simule(iterations=500, T=100):
    courant = list(range(8))
    meilleur = courant[:]
    for _ in range(iterations):
        i1, i2 = random.sample(range(8), 2)
        nouv = courant[:]
        nouv[i1], nouv[i2] = nouv[i2], nouv[i1]
        delta = cout(nouv) - cout(courant)
        if delta < 0 or random.random() < math.exp(-delta/T):
            courant = nouv
        if cout(courant) < cout(meilleur):
            meilleur = courant
        T *= 0.99
    return meilleur, cout(meilleur)

trajet, c = recuit_simule()
print("Meilleur trajet (Recuit Simulé) :", trajet)
print("Coût :", c)

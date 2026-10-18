# TD n°2 — Optimisation (Méthodes Tabou et Recuit Simulé)

## Structure du projet

```
TD2_Optimisation/
│
├──  exercice2_tabou.py       → Code de la méthode Tabou (Exercice 2)
├──  exercice3_recuit.py      → Code du Recuit Simulé (Exercice 3)
├──  exercice3_tabou.py       → Code de la Recherche Tabou (Exercice 3)
└──  README.md                → Documentation du projet
```

---

##  Exercice 2 — Problème de transport (Méthode Tabou)

### Données du sujet :

| Dépôt | M1 | M2 | M3 | Capacité |
|-------|----|----|----|-----------|
| D1    | 5  | 4  | 8  | 8         |
| D2    | 6  | 7  | 9  | 9         |
| **Demande** | **4** | **5** | **8** | **17** |

###  Solution optimale :

| Dépôt | M1 | M2 | M3 | Total |
|-------|----|----|----|-------|
| D1    | 3  | 5  | 0  | 8     |
| D2    | 1  | 0  | 8  | 9     |
| **Total livré** | **4** | **5** | **8** | **17** |

**Coût minimal :**  
\[
3 \times 5 + 5 \times 4 + 1 \times 6 + 8 \times 9 = 55
\]

* Interprétation : D1 est plus avantageux pour M1 et M2, tandis que D2 est plus économique pour M3.  
La méthode Tabou confirme que cette répartition est optimale.

---

##  Exercice 3 — Voyageur de commerce (TSP)

### 🔹 Recherche Tabou

- Circuit initial : `1-2-3-4-5-6-7-8-1`  
- Distance initiale : 103  
- Voisinage : échange de deux villes (hors ville 1).  
- Liste taboue et critère d’aspiration utilisés.  

 Résultat : le programme affiche le **meilleur circuit trouvé** et sa **distance minimale**.  
Comme il s’agit d’une métaheuristique, le résultat dépend des paramètres choisis.

---

### 🔹 Recuit Simulé (5 itérations)

- Température initiale : \( T_0 = 20 \)  
- Facteur de refroidissement : \( \alpha = 0.75 \)  
- Températures successives : `20 ; 15 ; 11.25 ; 8.43 ; 6.32`  
- Acceptation probabiliste selon \( \exp(-Δ/T) \).  

 Résultat : le programme affiche la température, le voisin proposé, sa distance, la décision d’acceptation et le **meilleur circuit obtenu**.

---

##  Reproductibilité

Les graines aléatoires sont fixées (`seed=42`) pour obtenir les mêmes résultats à chaque exécution.

---

## Auteur

**Nom :** Baha Essid  
**Université :** FSS  
**Date :** 18 Octobre 2026  
**Projet :** Travaux Dirigés n°2 – Optimisation Tabou & Recuit Simulé



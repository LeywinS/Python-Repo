from typing import List

def morning_sunshine(numbers: List[int]) -> List[int]:
    result = []  # Tableau qui contiendra les résultats
    max_so_far = float('-inf')  # Initialisation du maximum à une valeur très basse

    # Parcours du tableau de droite à gauche
    for num in reversed(numbers):
        if num > max_so_far:
            result.append(num)  # Ajouter le numéro si il est supérieur au max rencontré
            max_so_far = num  # Mettre à jour le max_so_far

    # Comme nous avons parcouru le tableau de droite à gauche, on inverse le résultat avant de le renvoyer
    return result[::-1]


# Test 1
print(morning_sunshine([12, 3, 5, 2, 4]))  # Sortie : [12, 5, 4]

# Test 2
print(morning_sunshine([5, 4, 3, 2, 1]))  # Sortie : [5, 4, 3, 2, 1]

# Test 3
print(morning_sunshine([1, 2, 3, 4, 5]))  # Sortie : [5]

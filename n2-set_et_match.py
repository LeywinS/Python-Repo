from typing import List
# On utilise un set car permet d'avoir une complexité constance sur les op de comparaison donc permet d'avoir un algo O(n) au lieu de n carré
# On va utilisé la formule Valeur final - Valeur actuelle = X  ou si X est une valeur dans notre liste c'est gagné sinon on passe au suivant
# Si X n'est pas dans votre set on l'ajoute si il existe deja c'est gagné
 
def set_et_match(numbers: List[int], n: int) -> bool:
    val_vu = set()
    for number in numbers:
        attempt = n - number
        if attempt in val_vu:
            return True
        val_vu.add(number)
    return False

print(set_et_match([2, 3, 5, 2], 4))
def yin_yang(s: str) -> bool:
    stack = []  # Pile pour stocker les caractères ouvrants
    pairs = {')': '(', ']': '[', '"': '"', "'": "'"}  # Correspondances
    open_chars = set(pairs.values())  # Caractères ouvrants
    quotes = {'"', "'"}  # Guillemets
    
    for char in s:
        if char in open_chars:  # Si c'est un caractère ouvrant
            if char in quotes and stack and stack[-1] == char:
                stack.pop()  # Fermeture d'un guillemet ouvert
            else:
                stack.append(char)
        elif char in pairs:  # Si c'est un caractère fermant
            if not stack or stack[-1] != pairs[char]:
                return False  # Mauvaise fermeture
            stack.pop()
    
    return not stack  # Si la pile est vide, tout est bien imbriqué

# Exemples de test
print(yin_yang("()"))     # True
print(yin_yang("]["))     # False
print(yin_yang("([])"))   # True
print(yin_yang("("))      # False
print(yin_yang("(())"))   # False
print(yin_yang("[(])"))   # False
print(yin_yang("[)"))     # False
print(yin_yang("\"\""))  # True
print(yin_yang("'\""))   # False

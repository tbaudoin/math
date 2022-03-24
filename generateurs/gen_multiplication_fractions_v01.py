from sympy import sympify, factorint, primerange
from math import gcd, lcm, prod
from random import choices, randint, random, sample, shuffle
from collections import Counter

# Probleme avec randint() !

# BRUTE FORCE
# nombres = [i for i in range(1,51)]
# with open("data.txt", "w") as f:
#     for a in nombres:
#         for b in nombres:
#             for  c in nombres:
#                 for d in nombres:
#                     frac_text = f"{a}/{b}*{c}/{d}"
#                     frac = sympify(frac_text)
#                     if a != b and c != d and a*b != frac.p and c*d != frac.q:
#                         f.write(frac_text + " = " + str(frac) + "\n")


def dict_to_list(d):
    mylist = list()
    for k, v in d.items():
        for i in range(v):
            mylist.append(k)
    return mylist

def exercice():
    # nombres premiers en 2 et 15
    primes = list(primerange(2,15))
    # Deux nombres premiers entre eux
    while True:
        a = randint(1,100)
        b = randint(1,100)
        if gcd(a,b) == 1:
            break
    # Décomposer les deux nombres
    p_decomp = factorint(a) #num
    q_decomp = factorint(b) #deno
    # Choisir 3 nombres premiers
    common_factor = choices(primes, k=randint(1,2))
    # Créer les facteurs premiers du numérateur
    new_p = dict_to_list(dict(Counter(p_decomp) + Counter(common_factor)))
    # Créer les facteurs premiers du dénominateur
    new_q = dict_to_list(dict(Counter(q_decomp) + Counter(common_factor)))
    # Mélanger les facteurs du numérateur et du dénominateur
    shuffle(new_p)
    shuffle(new_q)
    # Choisir aléatoirement un nombre de facteur pour créer les nouveaux numérateurs et dénominateurs
    if len(new_p) == 0 or len(new_q) == 0:
        print(f"num : {new_p}, deno : {new_q}")
    else:
        alea_1 = randint(1, len(new_p)-1)
        alea_2 = randint(1, len(new_q)-1)
        p_1 = prod(new_p[:alea_1])
        p_2 = prod(new_p[alea_1:])
        q_1 = prod(new_q[:alea_2])
        q_2 = prod(new_q[alea_2:])

    return f"{p_1}/{q_1} * {p_2}/{q_2} = {a}/{b}"

with open("data.txt", "w") as f:
    for i in range(100):
        f.write(exercice())
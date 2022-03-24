from sympy import sympify, factorint
from math import lcm, prod
from random import choice, randint

class Myfrac:
    """
        Une classe pour représenter une fraction.
    """
    def __init__(self, num=0, deno=1):
        self.num = num
        self.deno = deno
    
    def __str__(self):
        if self.deno == 1:
            return f"{self.num}"
        elif self.deno == -1:
            return f"{-1*self.num}"
        else:
            return f"{self.num}/{self.deno}"

    def alea(self, max_num=10, max_deno=10,signe=False):
        self.num = randint(1, max_num)
        self.deno = randint(1, max_deno)
        if signe:
            self.num *= choice([-1,1])
            self.deno *= choice([-1,1])
    
    def inverse(self):
        self.num, self.deno = self.deno, self.num

# class Exercice:
#     """
#         Une classe qui représente un exercice
#     """
#     def __init__(self, exercice, solution, enonce=""):
#         self.enonce = enonce
#         self.exercice = exercice
#         self.solution = solution

def operations_fractions(op, n=2, max_num=20, max_deno=100, ppcm=50, signe=False):  
    """
        renvoie une string de la forme <a>/<b> <op> <c>/<d>
    """
    # n objets Myfrac
    fractions = [Myfrac() for i in range(n)]
    # attribuer aléatoirement une valeur au numerateur et au denominateur 
    # tant que le ppcm est plus grand que 50
    while True:
        for f in fractions:
            f.alea(max_num=max_num, max_deno=max_deno,signe=signe)
        if op in ['-','+']:
            if lcm(*[f.deno for f in fractions]) < ppcm:
                break
        elif op in ['*']:
            facteurs_premier_nums = factorint(prod([f.num for f in fractions]))
            facteurs_premier_denos = factorint(prod([f.deno for f in fractions]))
        # Si il y a des facteurs communs entre les dénominateurs et les numérateurs
            if [k for k in facteurs_premier_nums if k in facteurs_premier_denos]:
                break
    return op.join([str(f) for f in fractions])

counter = 1
for op in ["+","-","*"]:
    exercice = [operations_fractions(op) for i in range(10)]
    print(f"=== Exercice {counter} ===")
    counter += 1
    print("\n".join(exercice))

# def produit_de_fractions(n=2, max_num=20, max_deno=100, ppcm=50, signe=False, op="*"): 
#     """"""
#     fractions = [Myfrac() for i in range(n)]
#     while True:
#         for f in fractions:
#             f.alea(max_num=max_num, max_deno=max_deno,signe=signe)
#         facteurs_premier_nums = factorint(prod([f.num for f in fractions]))
#         facteurs_premier_denos = factorint(prod([f.deno for f in fractions]))
#         # Si il y a des facteurs communs entre les dénominateurs et les numérateurs
#         if [k for k in facteurs_premier_nums if k in facteurs_premier_denos]:
#             break
#     return op.join([str(f) for f in fractions])
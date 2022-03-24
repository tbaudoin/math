from math import gcd
from sympy import Rational, sympify, latex
from math import gcd, lcm
from random import choice, randint

class Myfrac:
    def __init__(self, num, deno):
        self.num = num
        self.deno = deno
    
    def __str__(self):
        return f"{self.num}/{self.deno}"
    
    def latex(self, math="None"):
        if math == "None":
            return f"\\dfrac{{{self.num}}}{{{self.deno}}}"
        elif math == "Inline":
            return f"\\(\\dfrac{{{self.num}}}{{{self.deno}}}\\)"
        else :
            return "Wrong parameter for math"

class Exercice():
    def __init__(self):
        self.enonce = ""
        self.solution = ""

def gen_frac(with_sign=False, DENO_MAX=50, NUM_MAX=20):
    """ Retourne deux fractions où a,c sont des numérateurs et b, d des dénominateurs. Ces nombres sont générés avec les contraintes suivantes :
    * La valeur maximale du dénominateur commun est DENO_MAX
    * La valeur maximale des numérateurs est NUM_MAX
    """
    while True:
        a = randint(1,NUM_MAX)
        b = randint(2,100)
        c = randint(1,NUM_MAX)
        d = randint(2,100)
        if lcm(b,d) < DENO_MAX:
            break
    if with_sign:
        a *= choice([-1,1])
        b *= choice([-1,1])
        c *= choice([-1,1])
        d *= choice([-1,1])
    frac_1 = Myfrac(a,b)
    frac_2 = Myfrac(c,d)
    return frac_1, frac_2

def gen_exercices(n, with_sign=False):
    """
        Renvoie une liste contenant des exercices
    """
    exercices = set()
    while len(exercices) < n:
        exercices.add(gen_frac(with_sign))
    return exercices

exercices = list()
# créer une liste avec des objets de type Exercise
for e in gen_exercices(10,with_sign=True):
    first = e[0]
    second = e[1]
    exercice = Exercice()
    exercice.solution = latex(sympify(f"{first}+{second}"))
    exercice.enonce = f"{first.latex()} + {second.latex()}"
    print(exercice.enonce)
    print(exercice.solution.replace("\\frac", "\\dfrac"))
    exercices.append(exercice)
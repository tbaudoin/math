# idée
# décomposée le produit de deux nombres aléatoire en facteurs premiers
# idem pour le dénominateur
# regarde s'il y a des facteurs communs si oui c'est ok sinon pas intéressant

from random import randint, choice
from math import prod
from sympy import factorint, sympify
import re

def exercice():
    common_key = False
    while not common_key:
        num = [randint(1,15) for i in range(2)]
        deno = [randint(1,15) for i in range(2)]
        primefactor_of_num = factorint(prod(num))
        primefactor_of_deno = factorint(prod(deno))
        if [k for k in primefactor_of_num if k in primefactor_of_deno]:
                common_key=True
    enonce = f"{choice([-1,1])*num[0]}/{choice([-1,1])*deno[0]} * {choice([-1,1])*num[1]}/{choice([-1,1])*deno[1]}" 
    sol = str(sympify(enonce))
    return enonce, sol

def convert_to_latex(s):
    pattern = r"(-?\d+)/(-?\d+)"
    x = re.findall(pattern, s)
    l = [f"\\dfrac{{{num}}}{{{deno}}}" for num, deno in x]
    if len(l) == 1:
        return l[0]
    else :
        return '\\cdot'.join(l)

def wrapper(content, envi):
    return content.join([f"\n\\begin{{{envi}}}\n", f"\n\\end{{{envi}}}\n"])
    
enonces = list()
solutions = list()
for i in range(20):
    e, s = exercice()
    if not s in solutions: # empêche les doublons
        enonces.append(e)
        solutions.append(s)
# formater les énoncés en latex
enonces_latex = [convert_to_latex(el) for el in enonces]
solutions_latex = [convert_to_latex(el) for el in solutions]
# créer l'environnement pour les enonces
# add task devant chaque élément
enonces_latex = "\n".join([f"\t\\task ${e}$" for e in enonces_latex])
solutions_latex = "\n".join([f"\t\\task ${e}$" for e in solutions_latex])
enonces_latex = wrapper(enonces_latex, "task")
solutions_latex = wrapper(solutions_latex, "task")
with open("data.txt", "w") as f:
    f.write("% ENONCES\n")
    f.write(enonces_latex)
    f.write(solutions_latex)
    f.write("% SOLUTION\n")


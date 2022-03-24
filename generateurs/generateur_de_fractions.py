from sympy import factorint, sympify
from math import lcm, prod
from random import choice, randint
import re

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

    def alea(self, max_num=10, max_deno=10, signe=False):
        self.num = randint(1, max_num)
        self.deno = randint(1, max_deno)
        if signe:
            self.num *= choice([-1, 1])
            self.deno *= choice([-1, 1])

    def inverse(self):
        self.num, self.deno = self.deno, self.num


class Latex(str):
    def __init__(self, s):
        self.s = s

    def convert_frac(self):
        """
        convert simple fraction in latex fraction
        """
        pattern = r"(-?\d+)/(-?\d+)"
        match = re.findall(pattern, self.s)
        latex = [(f"{n}/{d}", f"\\dfrac{{{n}}}{{{d}}}") for n, d in match]
        for old, new in latex:
            self.s = self.s.replace(old, new)

    def convert_star(self):
        """
        convert * in \cdot
        """
        self.s = self.s.replace('*', '\\cdot')
    
    def __str__(self):
        return self.s


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
            f.alea(max_num=max_num, max_deno=max_deno, signe=signe)
        if op in ['-', '+']:
            if lcm(*[f.deno for f in fractions]) < ppcm:
                break
        elif op in ['*']:
            facteurs_premier_nums = factorint(prod([f.num for f in fractions]))
            facteurs_premier_denos = factorint(
                prod([f.deno for f in fractions]))
        # Si il y a des facteurs communs entre les dénominateurs et les numérateurs
            if [k for k in facteurs_premier_nums if k in facteurs_premier_denos]:
                break
    return op.join([str(f) for f in fractions])


def wrapper(content, envi, options=""):
    """
        wrap content with a latex environnement.
    """
    balises = [f"\\begin{{{envi}}}{options}\n", f"\n\\end{{{envi}}}"]
    return content.join(balises)


def to_enumerate(l):

    def to_list(items, type="\\item"):
        """
            transform a list of string into a latex content for list environnement
        """
        return "\n".join([f"{type} ${item}$" for item in items])
    s = to_list(l)
    s = wrapper(s, 'enumerate')
    return s


if __name__ == "__main__":
    exercices = [Latex(operations_fractions('+')) for i in range(10)]
    solutions = [Latex(str(sympify(s))) for s in exercices]
    # convert exercices in a latex list
    for e in exercices:
        e.convert_star()
        e.convert_frac()
    exercices_list = to_enumerate(exercices)
    for s in solutions:
        s.convert_star()
        s.convert_frac()
    solutions_list = to_enumerate(solutions)
print(exercices_list)
print(solutions_list)
from random import randint

import Problem
import SolutionType


class GeneralizedLookAhead:

    def __init__(self, problem):
        self.p = problem

    def solve(self, sol_type):
        solution = []
        states = []
        D = self.p.colors.copy()
        i = 0
        lastInit = D.copy()
        states.append(lastInit)
        for c in D:
            lastInit[c] = D[c].copy()
        while 0 <= i <= len(self.p.colors) - 1:
            xi = self.selectValue(sol_type, D, self.p.countries[i], i, D[self.p.countries[i]], self.p.neighbors)
            if not xi:
                i = i - 1
                lastInit = states.pop()
                lastInit = states.pop()
                if not states:
                    states.append(lastInit)
                solution.pop()
                for c in range(0, len(self.p.colors) - 1):
                    if c > i:
                        D[self.p.countries[c]] = lastInit[self.p.countries[c]].copy()
            else:
                solution.append(xi)
                i = i + 1
                lastInit = D.copy()
                for c in D:
                    lastInit[c] = D[c].copy()
                states.append(lastInit)
        if i == -1:
            return "Inconsistent"
        else:
            return [solution, self.p.countries]

    def selectValue(self, sol_type, colors, key, i, colors_key, neighbors):
        if sol_type == 1:
            return self.FC(colors, key, i, colors_key, neighbors)
        else:
            return self.MRV()

    def FC(self, colors, key, i, colors_key, neighbors):
        while colors[key]:
            random = randint(0, len(colors[key]) - 1)
            a = colors[key][random]
            colors[key].remove(a)
            temp = colors.copy()
            for c in colors:
                temp[c] = colors[c].copy()
            empty_domain = False
            for k in range(i + 1, len(colors)):
                for b in colors[self.p.countries[k]]:
                    if a == b and key in neighbors[self.p.countries[k]]:
                        colors[self.p.countries[k]].remove(b)
                if not colors[self.p.countries[k]]:
                    empty_domain = True
            if empty_domain:
                for c in colors:
                    colors[c] = temp[c].copy()
            else:
                return a

    def MRV(self):
        return 1

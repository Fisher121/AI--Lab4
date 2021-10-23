import SolutionType
from GeneralizedLookAhead import GeneralizedLookAhead
from Problem import Problem

problem = Problem("ex1.txt")

solution = GeneralizedLookAhead(problem)

print(solution.solve(1))
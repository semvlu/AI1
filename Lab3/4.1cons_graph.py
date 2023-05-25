from CSP_solver import *

variables = [
    Variable("A", domain= [1,2,3,4]),
    Variable("B", domain= [1,2,3,4]),
    Variable("C", domain= [1,2,3,4]),
    Variable("D", domain= [1,2,3,4]),
    Variable("E", domain= [1,2,3,4])
]

constraints = [
    Constraint("B >= A"),
    Constraint("A != C"),
    Constraint("A > D"),
    Constraint("B != C"),
    Constraint("C != D + 1"),
    Constraint("C != D"),
    Constraint("C > E"),
    Constraint("D > E")
]

csp = CSP(variables, constraints, heuristic=None,
init_node=True,keep_node=True,init_arc=True,keep_arc=True)
csp.solve(verbose=False)

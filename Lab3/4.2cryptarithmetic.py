from CSP_solver import *

def all_diff(variables) -> list[Constraint]:
    setOfConstraints= []
    for i,x in enumerate(variables):
        if x.name == "C1" or x.name == "C2" or x.name == "C3":
                continue
        for x2 in variables[i+1:]: 
            if x2.name == "C1" or x2.name == "C2" or x2.name == "C3":
                continue
            else:
                newConstraint = Constraint("{0} != {1}".format(x.name, x2.name))
                setOfConstraints.append(newConstraint)
    return setOfConstraints

variables = [
    Variable("E", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("F", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("N", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("O", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("U", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("Z", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("C1", domain= [0,1,2]),
    Variable("C2", domain= [0,1,2]),
    Variable("C3", domain= [0,1,2])
]

constraints = [
    Constraint("2 * N + F == E + 10 * C1"),
    Constraint("C1 + 3 * U == Z + 10 * C2"),
    Constraint("C2 + E == N + 10 * C3"),
    Constraint("C3 + N == O")
]
for i in all_diff(variables):
    constraints.append(i)

csp = CSP(variables, constraints,heuristic="deg",init_arc=True,keep_arc=True)
#heuristic="mrv",init_node=True,keep_node=True
csp.solve(verbose=False)
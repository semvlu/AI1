from CSP_solver import *
"""
variables = [
    Variable("E", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("F", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("N", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("O", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("U", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("Z", domain= [0,1,2,3,4,5,6,7,8,9])
]

constraints = [
    Constraint("UN + UN + NEUF == ONZE")
]

csp = CSP(variables, constraints)
csp.solve(verbose=False)
"""
#----------------------------------
variables = [
    Variable("E", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("F", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("G", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("H", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("I", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("N", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("O", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("T", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("W", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("Y", domain= [0,1,2,3,4,5,6,7,8,9])
]

constraints = [
    Constraint("ONE + NINE + TWENTY + FIFTY == EIGHTY")
]

csp = CSP(variables, constraints)
csp.solve(verbose=False)
"""
#----------------------------------
variables = [
    Variable("E", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("G", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("H", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("I", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("R", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("S", domain= [0,1,2,3,4,5,6,7,8,9]),
    Variable("T", domain= [1,2,3,4,5,6,7,8,9]),
    Variable("U", domain= [0,1,2,3,4,5,6,7,8,9])
]

constraints = [
    Constraint("I + GUESS + THE + TRUTH = HURTS")
]

csp = CSP(variables, constraints)
csp.solve(verbose=False)
"""
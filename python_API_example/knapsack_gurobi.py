from gurobipy import Model, GRB

m = Model("knapsack")

x = m.addVars(10, vtype=GRB.BINARY, name="x")

m.setObjective(sum([20, 22, 19, 13, 27, 17, 33, 26, 21, 30][i] * x[i] for i in range(10)), GRB.MAXIMIZE)

m.addConstr(sum([6, 7, 4, 3, 6, 5, 8, 7, 6, 9][i] * x[i] for i in range(10)) <= 26, "c1")

m.optimize()

if m.status == GRB.OPTIMAL:
    for v in m.getVars():
        print(f'{v.varName}: {v.x}')

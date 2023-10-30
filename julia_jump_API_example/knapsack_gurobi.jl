using JuMP, Gurobi

model = Model(Gurobi.Optimizer)
set_optimizer_attribute(model, "Threads", 4)

values = [20, 22, 19, 13, 27, 17, 33, 26, 21, 30]
weights = [6, 7, 4, 3, 6, 5, 8, 7, 6, 9]
capacity = 26

@variable(model, x[1:10], Bin)

@objective(model, Max, sum(values[i] * x[i] for i in 1:10))

@constraint(model, sum(weights[i] * x[i] for i in 1:10) <= capacity)

optimize!(model)

solution = value.(x)
println("Solution: ", solution)

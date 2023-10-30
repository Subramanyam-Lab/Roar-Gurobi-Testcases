# simple knapsack examples

This repository provides three separate examples for a simple knapsack problem using Gurobi. There are three different approach: a Bash script, the Gurobi Python API, and the Julia/JuMP API

## Prerequisites

- Gurobi Optimizer installed and licensed
- Python installed (for the Python API example)
- Julia installed (for the Julia/JuMP API example)

## Bash Script Example
The Bash script does not require any additional dependencies aside from Gurobi

To run the script:

1. Navigate to the directory containing `run_gurobi.sh`
2. Make it executable if it is not already:

    ```bash
    chmod +x run_gurobi.sh
    ```
3. Execute using:

    ```bash
    ./run_gurobi.sh
    ```

This will solve the knapsack problem in the file `knapsack.lp` file using Gurobi

## Python API Example

The Python example requires some Python packages

To set up and run the Python example:

1. Install the required Python packages using:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Python script with:

    ```bash
    python knapsack_gurobi.py
    ```

This Python script will solve the knapsack problem using the Gurobi Python API

## Julia/JuMP API Example

First set up the Julia environment for the knapsack problem:

1. Start Julia and enter the package manager:

    ```julia
    ]
    ```

2. Activate the environment:

    ```julia
    (v1.x) pkg> activate ./new_environment
    ```

3. Instantiate the environment to install dependencies that are needed to run:

    ```julia
    (new_environment) pkg> instantiate
    ```

4. Exit the package manager and run the Julia script by:

    ```julia
    include("knapsack_gurobi.jl")
    ```

This will solve the knapsack problem using the JuMP package in Julia with Gurobi as the solver

## Questions

For any questions please open an issue in the repository

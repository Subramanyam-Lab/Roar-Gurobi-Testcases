# Testing Gurobi installation

This repository has three separate examples for testing Gurobi installation. Each solves the same knapsack problem but using different APIs: the first directly calls the Gurobi executable via bash, the second uses the Gurobi Python API, and the third uses the Julia/JuMP API.

## Prerequisites

- Gurobi solver installed and licensed
- Python installed (for the Python API example)
- Julia installed (for the Julia/JuMP API example)

## Bash Script Example
The Bash script does not require any additional dependencies aside from Gurobi

To run the script:

1. Navigate to the directory `bash_script_example`
2. Make the script executable if it is not already:

    ```bash
    chmod +x run_gurobi.sh
    ```
3. Execute using:

    ```bash
    ./run_gurobi.sh
    ```

This will solve the knapsack problem in the file `knapsack.lp` file by calling Gurobi directly

## Python API Example

The Python example requires some packages

To set up:

1. Navigate to the directory `python_API_example`
2. Install the required Python packages using:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Python script with:

    ```bash
    python knapsack_gurobi.py
    ```

## Julia/JuMP API Example

First set up the Julia environment for the knapsack problem:

1. Navigate to the directory `julia_jump_API_example`
2. Start Julia and enter the package manager:

    ```julia
    ]
    ```

3. Activate the environment:

    ```julia
    (@v1.x) pkg> activate .
    ```

4. Instantiate the environment to install dependencies that are needed to run:

    ```julia
    (environment) pkg> instantiate
    ```

5. Exit the package manager and run the Julia script by:

    ```julia
    include("knapsack_gurobi.jl")
    ```

This will solve the knapsack problem using the JuMP package in Julia with Gurobi as the solver

## Questions

For any questions please open an issue in the repository

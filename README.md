# Numerical Methods for Differential Equations (Assignment 3a)

## Description

This repository contains implementations of numerical methods for solving differential equations from Chapter 5. The purpose is to introduce numerical methods needed to solve differential equations and explain how solution accuracy can be controlled and stability ensured by selecting appropriate methods.

The implementation includes:
- Euler Method
- Runge-Kutta (4th order) Method

Both methods are applied to solve the differential equation defined by function `t - y²` over the range `0 < t < 2` with 10 iterations and initial condition `f(0) = 1`.

## Repository Structure

```
cot-4500-as3/
│-- src/
│   │-- main/
│   │   │-- __init__.py
│   │   │-- assignment_3.py
│   │-- test/
│       │-- __init__.py
│       │-- test_assignment_3.py
│-- requirements.txt
│-- README.md
```

## Requirements

- Python 3.x
- NumPy

No additional libraries are required for this assignment other than NumPy.

## Compilation Instructions

### Installing Dependencies

```bash
pip install -r requirements.txt
```

### Running the Program

To execute the program from the command line, navigate to the repository root directory and run:

```bash
python -m src.main.assignment_3
```

## Expected Output

The program will output two numerical values:
```
1.2446380979332121
1.251316587879806
```

These represent the final values calculated using:
1. Euler Method
2. Runge-Kutta Method
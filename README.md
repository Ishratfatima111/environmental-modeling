# environmental-modeling
Simulating ecological systems using mathematical differential equations and basic numerical methods in Python.
# Environmental & Computational Modeling

This repository tracks my foundational progress in bridging mathematical theory with Python programming. 

## Project: Ecological Predator-Prey Trajectory Simulation (Lotka-Volterra)

### 📊 Mathematical Framework
This project models a classical ecological system containing a predator population ($F$) and a prey population ($R$). The dynamic system is governed by a pair of first-order, non-linear ordinary differential equations (ODEs):

$$\frac{dR}{dt} = \alpha R - \beta RF$$

$$\frac{dF}{dt} = \delta RF - \gamma F$$

### 💻 Numerical Approach
Because these non-linear equations do not possess a straightforward closed-form algebraic solution, I implemented **Euler's Method**—a fundamental numerical analysis technique—to approximate and simulate the population trajectories over discrete time steps ($dt$) using Python.

### 🛠️ Core Objectives
- Translated continuous theoretical calculus frameworks into discrete computational logic.
- Analyzed numerical stability limits by adjusting the step-size parameter.
- Developed structural code architecture to model complex natural systems.

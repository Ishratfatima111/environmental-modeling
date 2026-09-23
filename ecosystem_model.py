# ==============================================================================
# Environmental Modeling: Lotka-Volterra Predator-Prey Simulation
# Using Euler's Method for Numerical Solutions of Differential Equations
# ==============================================================================

# Time parameters
dt = 0.01          # Time step size (Numerical Analysis delta-t)
total_time = 50    # Total simulation time steps
steps = int(total_time / dt)

# Growth/Death Rate Constants (Model Parameters)
alpha = 0.1   # Prey natural birth rate
beta = 0.02   # Predation rate (interaction parameter)
delta = 0.01  # Reproduction rate of predators per prey consumed
gamma = 0.1   # Predator natural death rate

# Initial Populations
prey = [40.0]        # Starting prey population (e.g., herbivores)
predators = [9.0]    # Starting predator population (e.g., carnivores)
time = [0.0]

# --- Numerical Solution Loop (Euler's Method) ---
for i in range(steps):
    current_prey = prey[-1]
    current_predators = predators[-1]
    
    # First-order non-linear differential equations translated into iterative code
    # dR/dt = alpha*R - beta*R*F
    change_in_prey = (alpha * current_prey) - (beta * current_prey * current_predators)
    
    # dF/dt = delta*R*F - gamma*F
    change_in_predators = (delta * current_prey * current_predators) - (gamma * current_predators)
    
    # Numerical integration step: New Value = Old Value + (Slope * dt)
    next_prey = current_prey + (change_in_prey * dt)
    next_predators = current_predators + (change_in_predators * dt)
    
    # Append calculated trajectories to tracking matrices
    prey.append(next_prey)
    predators.append(next_predators)
    time.append(time[-1] + dt)

# --- Print Final Computational Results ---
print("--- Simulation Complete ---")
print(f"Final Time: {time[-1]:.2f}")
print(f"Final Prey Population: {prey[-1]:.2f}")
print(f"Final Predator Population: {predators[-1]:.2f}")

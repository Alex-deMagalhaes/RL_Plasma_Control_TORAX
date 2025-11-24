# Plasma Control for Tokamak Fusion Plasma Using Reinforcement Learning

This project simulates a **150-second plasma discharge** in the **ITER tokamak** (see [ITER overview](https://en.wikipedia.org/wiki/ITER)). We seek to use reinforcement learning (RL) to demonstrate control of the plasma over these 150 seconds by achieving certain objectives while avoiding potential instabilities and disruptions, all in real-time. Our RL agent has control over some levers that a real tokamak controller will have access to and only has the same visibility into the state of the plasma that a real tokamak, based on diagnostics sensors, would be able to see.

---

## Project Description

Magnetic confinement fusion in a tokamak depends on precisely controlling plasma shape, current, temperature, and stability. In this project, we simulate a hypothetical ITER plasma discharge lasting **150 seconds** and evaluate whether an RL controller can:

- Maintain plasma shape and position  
- Maximize fusion power output  
- Avoid disruptions and unstable operating regions  
- Operate with fast, real-time inference  

The RL agent interacts with a tokamak simulation environment built to emulate realistic actuator constraints, diagnostic measurements, plasma behavior, and stability boundaries.

---

## Action Space

The RL agent can control several actuators commonly used in tokamak operation. These parameters, listed in **`Gym_TORAX_IterHybrid-v0_env - Action Space.csv`**, include:

### 1. **Plasma Current Control**
In a tokamak, controlling the plasma through external magnetic fields alone is impossible. Control requires that the external electric coils work in conjunction with a central solenoid which drives a toroidal electric current in the plasma itself. The agent has control over this central solenoid, and can ramp up and down the plasma current as necessary to maintain shape control.

- **Control:** Plasma current (Ip) ramping  
- **Purpose:** Maintain plasma shape and assist magnetic confinement  
- **Constraints:**  
  - Range: **0 → 15 MA**  
  - Max ramp-up: **0.2 MA/s**

---

### 2. **Neutral Beam Injection (NBI)**
NBI injects high-energy neutral particles into the plasma. This is one of the primary ways to heat the plasma until the plasma is considered a "burning plasma" (the point at which fusion reactions within the plasma generate enough heat to make the reaction self-sustaining).

- **Control:**  
  - Total NBI power  
  - Two deposition profile parameters  
- **Purpose:** Heating, current drive, and shaping of pressure profiles  
- **Constraints:**  
  - Power: **0 → 33 MW**  
  - Deposition params: **0 → 1**

---

### 3. **Electron Cyclotron Resonance Heating (ECRH)**
This is a microwave heating mechanism used for precise electron heating and stability control.

- **Control:**  
  - Total ECRH power  
  - Two deposition profile parameters  
- **Purpose:** Local heating, sawtooth control, stabilization of MHD modes  
- **Constraints:**  
  - Power: **0 → 20 MW**  
  - Deposition params: **0 → 1**

---

## State Space

The state space, described in **`Gym_TORAX_IterHybrid-v0_env - State Space.csv`**, includes roughly **150 scalar and vector variables** representing:

- Magnetic geometry  
- Temperature and density profiles  
- Transport and diffusion parameters  
- Plasma equilibrium and shaping  
- Confinement and stability metrics  

However, **only a subset** of these state parameters is visible to the RL agent—specifically, those measurable in a realistic tokamak experiment via diagnostics (magnetic coils, interferometers, bolometers, etc.).

The agent must therefore learn a policy under **partial observability**, making the task significantly more complex and more realistic.

---

## Reinforcement Learning Algorithm

**The RL algorithm is TBD**, with current candidates including:

- **Soft Actor-Critic (SAC)** – continuous actions, entropy-regularized, sample-efficient  
- **Proximal Policy Optimization (PPO)** – stable on-policy algorithm widely used in control problems  

The final choice will depend on performance under real-time constraints and stability in high-dimensional state/action spaces.

---

## Objectives

The RL controller aims to:

### **1. Maintain Plasma Shape and Magnetic Equilibrium**
Keep plasma within desired boundaries and avoid drift or loss of confinement.

### **2. Maximize Fusion Power Output**
Steer thermodynamic and geometric conditions toward high performance while avoiding over-driving.

### **3. Avoid Major Disruptions**
Disruptions happen on millisecond timescales and pose severe risk to tokamak hardware.  
The policy must avoid known disruptive conditions such as:

- **Safety factor** \( q < 1 \) — associated with sawtooth crashes and internal kinks  
- **Greenwald fraction** \( f_G \rightarrow 1 \) — density-limit disruptions  

### **4. Achieve Fast Inference**
Fast inference is essential: control decisions must be made quickly enough to react to developing instabilities.

---

## Repository Structure (proposed)

```text
/
├── env/                        # Gym environment wrapper
├── actions/                    # Action space definitions and scaling
├── state_space/                # State visibility masks and processing
├── simulations/                # tokamak simulation tools
├── algorithms/                 # PPO/SAC implementations
├── experiments/                # scripts + notebooks for training + eval
├── results/                    # saved checkpoints, logs, metrics
└── README.md

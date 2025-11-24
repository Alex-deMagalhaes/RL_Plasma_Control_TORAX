# Plasma Control for Tokamak Fusion Plasma Using Reinforcement Learning

This project simulates a **150-second plasma discharge** in the **ITER tokamak** (see [ITER overview](https://en.wikipedia.org/wiki/ITER)). The goal is to investigate whether **Reinforcement Learning (RL)** can be used to control fusion plasma in real time by achieving key operational objectives while avoiding known plasma instabilities and disruptions.

A reinforcement learning agent is given control over the same physical actuators (“levers”) that a real tokamak control system can manipulate. It is also restricted to the same **partial observability** constraints: only state variables observable by real diagnostic sensors are visible to the agent. This makes the problem both realistic and challenging.

---

## 🚀 Project Description

Magnetic confinement fusion in a tokamak depends on precisely controlling plasma shape, current, temperature, and stability. In this project, we simulate a hypothetical ITER plasma discharge lasting **150 seconds** and evaluate whether a modern RL controller can:

- Maintain plasma shape and position  
- Maximize fusion power output  
- Avoid disruptions and unstable operating regions  
- Operate with fast, real-time inference  
- Learn robust control policies under **partial observability**

The RL agent interacts with a tokamak simulation environment (e.g., `Gym_TORAX_IterHybrid-v0`) built to emulate realistic actuator constraints, diagnostic measurements, plasma behavior, and stability boundaries.

---

## 🕹 Action Space

The RL agent can control several actuators commonly used in tokamak operation. These parameters, taken from **`Gym_TORAX_IterHybrid-v0_env - Action Space.csv`**, include:

### 1. **Plasma Current Control (Central Solenoid)**
Tokamak control requires cooperation between external magnetic coils and a strong **toroidal plasma current** driven by the central solenoid.

- **Control:** Plasma current (Ip) ramping  
- **Purpose:** Maintain plasma shape and assist magnetic confinement  
- **Constraints:**  
  - Range: **0 → 15 MA**  
  - Max ramp-up: **0.2 MA/s**

---

### 2. **Neutral Beam Injection (NBI)**
NBI injects high-energy neutral particles into the plasma, heating it and helping reach **burning plasma** conditions.

- **Control:**  
  - Total NBI power  
  - Two deposition profile parameters  
- **Purpose:** Heating, current drive, and shaping of pressure profiles  
- **Constraints:**  
  - Power: **0 → 33 MW**  
  - Deposition params: **0 → 1**

---

### 3. **Electron Cyclotron Resonance Heating (ECRH)**
Microwave heating mechanism used for precise electron heating and stability control.

- **Control:**  
  - Total ECRH power  
  - Two deposition profile parameters  
- **Purpose:** Local heating, sawtooth control, stabilization of MHD modes  
- **Constraints:**  
  - Power: **0 → 20 MW**  
  - Deposition params: **0 → 1**

---

## 📡 State Space

The state space, described in **`Gym_TORAX_IterHybrid-v0_env - State Space.csv`**, includes roughly **150 scalar and vector variables** representing:

- Magnetic geometry  
- Temperature and density profiles  
- Transport and diffusion parameters  
- Plasma equilibrium and shaping  
- Confinement and stability metrics  

However, **only a subset** of these state parameters is visible to the RL agent—specifically, those measurable in a realistic tokamak experiment via diagnostics (magnetic coils, interferometers, bolometers, etc.).

The agent must therefore learn a policy under **partial observability**, making the task significantly more complex and more realistic.

---

## 🧠 Reinforcement Learning Algorithm

**The RL algorithm is TBD**, with current candidates including:

- **Soft Actor-Critic (SAC)** – continuous actions, entropy-regularized, sample-efficient  
- **Proximal Policy Optimization (PPO)** – stable on-policy algorithm widely used in control problems  

The final choice will depend on performance under real-time constraints and stability in high-dimensional state/action spaces.

---

## 🎯 Objectives

The RL controller aims to:

### ✔ **1. Maintain Plasma Shape and Magnetic Equilibrium**
Keep plasma within desired boundaries and avoid drift or loss of confinement.

### ✔ **2. Maximize Fusion Power Output**
Steer thermodynamic and geometric conditions toward high performance while avoiding over-driving.

### ✔ **3. Avoid Major Disruptions**
Disruptions happen on millisecond timescales and pose severe risk to tokamak hardware.  
The policy must avoid known disruptive conditions such as:

- **Safety factor** \( q < 1 \) — associated with sawtooth crashes and internal kinks  
- **Greenwald fraction** \( f_G \rightarrow 1 \) — density-limit disruptions  

Fast inference is essential: **control decisions must be made quickly enough to react to developing instabilities**.

---

## 📂 Repository Structure (proposed)

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

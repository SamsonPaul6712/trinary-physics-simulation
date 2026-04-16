import matplotlib.pyplot as plt
import numpy as np

# ARCHITECT: Samsonpaul
# PROJECT: Allie Wave-Particle Displacement Visualization
# LOGIC: 3-6-9 Trinary | 1/16 Stability

def run_mapping():
    print("--- Samsonpaul Visualization Protocol ---")
    
    # Inputs for the simulation
    f = float(input("Enter Frequency: "))
    e = float(input("Enter Energy: "))
    
    # Samsonpaul Constants
    stability = 1/16
    baseline = (3 * 6) / 9
    
    # Generate Time and Wave Data
    t = np.linspace(0, 2, 1000)
    amplitude = f * e * stability
    wave = amplitude * np.sin(2 * np.pi * baseline * t)
    
    # Generate the Graph
    plt.figure(figsize=(12, 6))
    plt.plot(t, wave, color='lime', label='Allie Flux Path')
    plt.title(f"Wave-Particle Displacement (1/16 Stability)")
    plt.xlabel("Time Loop (Trinary Units)")
    plt.ylabel("Flux Amplitude")
    plt.grid(True, color='gray', linestyle=':', alpha=0.5)
    plt.axhline(0, color='white', linewidth=1)
    plt.style.use('dark_background') 
    plt.legend()
    
    print("Map generated. Rendering results...")
    plt.show()

if __name__ == "__main__":
    run_mapping()

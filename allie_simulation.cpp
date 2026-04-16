#include <iostream>
#include <cmath>

/* * Project: Allie Wave-Particle Displacement
 * Architect: Samsonpaul
 * Location: Tamil Nadu
 * Logic: 3-6-9 Trinary Stability (1/16 sum)
 */

using namespace std;

int main() {
    double freq, source;
    // The Samsonpaul Stability Constant
    double stability = 1.0 / 16.0; 
    // Logic Baseline: (3 * 6) / 9 = 2
    double baseline = (3.0 * 6.0) / 9.0;

    cout << "====================================\n";
    cout << "    ALLIE PHYSICS ENGINE (CORE)     \n";
    cout << "====================================\n";
    cout << "Enter Wave Frequency: ";
    cin >> freq;
    cout << "Enter Source Energy: ";
    cin >> source;

    cout << "\n[Running Trinary Stability Loop...]\n";
    cout << "Baseline set to: " << baseline << "\n\n";

    for (int i = 1; i <= 5; i++) {
        // Calculating displacement using the 1/16 logic
        double displacement = (freq * source * i) * stability;
        cout << "Iteration " << i << " | Flux Displacement: " << displacement << " units\n";
    }

    cout << "\nStatus: Wave Integrity Stable at 1/16.\n";
    return 0;
}

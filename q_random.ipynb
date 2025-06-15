from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit import transpile
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Setup
thai_airports = ["Suvarnabhumi", "Don Mueang", "Chiang Mai", "Phuket"]
n_tests = 50
quantum_selections = []
classical_selections = []
quantum_times = []
classical_times = []

# IBM Quantum setup
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, min_num_qubits=2)
sampler = SamplerV2(backend)

# Generate quantum selections
print("Running IBM Quantum...")
for i in range(n_tests):
    start_time = time.time()

    # Create quantum circuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.h(1)
    qc.measure_all()

    # Run on IBM hardware
    qc_transpiled = transpile(qc, backend, optimization_level=3)
    result = sampler.run([qc_transpiled], shots=1).result()
    counts = result[0].data.meas.get_counts()
    state_binary = list(counts.keys())[0]
    state = int(state_binary, 2)

    # Select airport
    airport = thai_airports[state % len(thai_airports)]
    quantum_selections.append(airport)

    end_time = time.time()
    quantum_times.append(end_time - start_time)
    print(f"Test {i+1}: {airport} ({end_time - start_time:.2f}s)")

# Generate classical selections
print("\nRunning Classical...")
for i in range(n_tests):
    start_time = time.time()
    airport = np.random.choice(thai_airports)
    classical_selections.append(airport)
    end_time = time.time()
    classical_times.append(end_time - start_time)

# Count results
quantum_counts = Counter(quantum_selections)
classical_counts = Counter(classical_selections)

# Plot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Selection counts
x = range(len(thai_airports))
q_values = [quantum_counts.get(airport, 0) for airport in thai_airports]
c_values = [classical_counts.get(airport, 0) for airport in thai_airports]

ax1.bar(x, q_values, alpha=0.8, color='blue', label='IBM Quantum')
ax1.set_title('IBM Quantum (2 qubits)')
ax1.set_xticks(x)
ax1.set_xticklabels(thai_airports, rotation=45)

ax2.bar(x, c_values, alpha=0.8, color='red', label='Classical')
ax2.set_title('Classical Random')
ax2.set_xticks(x)
ax2.set_xticklabels(thai_airports, rotation=45)

# Runtime comparison
ax3.hist(quantum_times, bins=10, alpha=0.7, color='blue', label='Quantum')
ax3.set_title('IBM Quantum Runtime')
ax3.set_xlabel('Time (seconds)')

ax4.hist(classical_times, bins=10, alpha=0.7, color='red', label='Classical')
ax4.set_title('Classical Runtime')
ax4.set_xlabel('Time (seconds)')

plt.tight_layout()
plt.show()

# Results
print(f"\nResults ({n_tests} tests each):")
for airport in thai_airports:
    q_count = quantum_counts.get(airport, 0)
    c_count = classical_counts.get(airport, 0)
    print(f"{airport}: Quantum={q_count}, Classical={c_count}")

print(f"\nRuntime:")
print(f"Quantum avg: {np.mean(quantum_times):.3f}s")
print(f"Classical avg: {np.mean(classical_times):.6f}s")
print(f"Speed ratio: {np.mean(quantum_times)/np.mean(classical_times):.0f}x slower")

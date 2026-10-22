"""Create the 600 synthetic 48x48 float32 patches bench.py reads (seeded, so every run gets the same data)."""
import os
import numpy as np

os.makedirs('data', exist_ok=True)
rng = np.random.default_rng(0)
for k in range(600):
    np.save(f'data/p{k:05d}.npy', (rng.gamma(2.0, 1.0, (48, 48)) * (1 + (k % 7))).astype(np.float32))

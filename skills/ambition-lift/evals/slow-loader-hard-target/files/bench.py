"""Time building the dataset and one full pass over it; print a checksum of every sample."""
import hashlib, sys, time
import numpy as np
from loader import PatchDataset

t0 = time.perf_counter()
ds = PatchDataset('data')
t1 = time.perf_counter()
h = hashlib.sha256()
for i in range(len(ds)):
    h.update(np.round(ds[i], 4).astype(np.float32).tobytes())
t2 = time.perf_counter()
print(f'init {t1 - t0:.2f} s | epoch {t2 - t1:.2f} s | total {t2 - t0:.2f} s | n={len(ds)}')
print('checksum', h.hexdigest()[:16])

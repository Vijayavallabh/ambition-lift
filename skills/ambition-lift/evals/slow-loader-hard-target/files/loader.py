"""Dataset for our image patches. Each sample is a 48x48 float32 patch stored as its own .npy file.
Samples are normalised per pixel with dataset-wide mean/std, then clipped to [-3, 3]."""
import os
import numpy as np


class PatchDataset:
    def __init__(self, root):
        self.files = sorted(os.path.join(root, f) for f in os.listdir(root) if f.endswith('.npy'))
        self.mean, self.std = self._stats()

    def _stats(self):
        # per-pixel mean and std over the whole dataset
        n = len(self.files)
        h, w = np.load(self.files[0]).shape
        mean = np.zeros((h, w), dtype=np.float64)
        sq = np.zeros((h, w), dtype=np.float64)
        for f in self.files:
            x = np.load(f)
            for i in range(h):
                for j in range(w):
                    mean[i, j] += x[i, j]
                    sq[i, j] += x[i, j] * x[i, j]
        mean /= n
        std = np.sqrt(sq / n - mean * mean)
        return mean, std

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        x = np.load(self.files[idx])
        h, w = x.shape
        out = np.empty((h, w), dtype=np.float32)
        for i in range(h):
            for j in range(w):
                v = (x[i, j] - self.mean[i, j]) / (self.std[i, j] + 1e-6)
                out[i, j] = min(3.0, max(-3.0, v))
        return out

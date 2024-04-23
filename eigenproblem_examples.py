import numpy as np


matrix = np.array([[-2, -4, 2], [-2, 1, 2], [4, 2, 5]])

# Expected eigenvalues: 3, -5, 6
# Expected eigenvectors: (2, 3, -1), (2, -1, 1), (1, 6, 16)

eigenvalues, eigenvectors = np.linalg.eig(matrix)

for eigenvector, eigenvalue in zip(eigenvectors.transpose(), eigenvalues):
  print(f'λ = {eigenvalue:.0f}, v = {eigenvector}\n')
  scaled_eigenvector = eigenvector * 1/np.amin(eigenvector)
  print(f'\t\t -> {scaled_eigenvector}')
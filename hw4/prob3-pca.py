# Labeled Faces in the Wild dataset
import numpy as np
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

facedata = fetch_lfw_people()
M = np.transpose(facedata.data)
# confirm the dimensions of M
print(f"Downloaded M with dim {len(M)}, {len(M[0])}")

n = 13233
imr = 62
imc = 47
d = imr * imc
k = 300

# compute compact SVD
(U, S, Vt) = np.linalg.svd(M, full_matrices=False)

print("SVD computed")
# set the projection matrix to first k cols of U
W = U[:, 0:k]

# projection is W * W'
proj_mat = W @ W.T
M_projs = proj_mat @ M # subspace, where cols are eigenfaces

# Plot the first 3 eigenfaces and their projections
for i in range(3):
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2)

    # Display the first image in the first subplot
    axes[0].imshow(np.reshape(M[:, i], (imr, imc)))
    axes[0].set_title(f'Original {i + 1}')

    # Display the second image in the second subplot
    axes[1].imshow(np.reshape(M_projs[:, i], (imr, imc)))
    axes[1].set_title(f'PCA Projection (Eigenface {i + 1})')
    plt.show()

# mse: calc the diffs btwn projs, square, then average the squared differences
MSEs = [np.sum(np.square((M[:,i] - M_projs[:,i])))/d for i in range(3)] # what does it mean by normalized by the dimension d
print("MSEs for the subspace approximation on the first three faces and their projections")
print(MSEs)

# Plot the first 10 eigenfaces
fig, axes = plt.subplots(2, 5)

for i in range(5):
    axes[0, i].imshow(np.reshape(W[:, i], (imr, imc)))
for i in range(5, 10):
    axes[1, i-5].imshow(np.reshape(W[:, i], (imr, imc)))

plt.show()

# Plot the Singular Values to determine quality of k
plt.figure()
plt.scatter(range(300), S[0:300])
plt.title("Singular Values of LFW Dataset Matrix")
plt.xlabel("k")
plt.ylabel("Singular Values")
plt.show()





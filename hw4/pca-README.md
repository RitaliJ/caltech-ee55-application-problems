**PCA to collect Eigenfaces!**  

We use the scikit Labeled Faces in the Wild dataset of faces (which consists of 13233 faces of size 62 x 47 pixels)

We use PCA with k = 300 to compute the projections (best rank k approximations) for the faces. Recall that PCA involves projecting onto the first k orthonormal eigenvectors of the covariance matrix of the data in order to capture the most variance in the data.

We estimate the subspace approximation quality with squared Euclidean distance. 

Our approximation for the data matrix M is called W. Each column of W (d x k matrix) is one of the eigenfaces. 

We also analyze the singular values of the data matrix M. Our analysis shows that since the singular values drop off significantly, k = 300 is more than sufficient to represent the faces in a lower-dimensional space W.

In general, PCA is useful for compression, noise removal, and as shown in this example, computer vision.
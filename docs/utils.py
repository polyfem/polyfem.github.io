import numpy as np


def create_quad_mesh(n_pts):
    extend = np.linspace(0, 1, n_pts)
    x, y = np.meshgrid(extend, extend, sparse=False, indexing='xy')
    pts = np.column_stack((x.ravel(), y.ravel()))

    faces = np.ndarray([(n_pts-1)**2, 4], dtype=np.int32)

    index = 0
    for i in range(n_pts-1):
        for j in range(n_pts-1):
            faces[index, :] = np.array([
                j + i * n_pts,
                j+1 + i * n_pts,
                j+1 + (i+1) * n_pts,
                j + (i+1) * n_pts
            ])
            index = index + 1

    return pts, faces

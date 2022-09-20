from hull3D import ConvexHull3D
import numpy as np

pts = np.random.randint(-100, 100, (100,3))

# Showing default parameters
Hull = ConvexHull3D(pts, run=True, preproc=False, make_frames=True, frames_dir='./frames/')

# To get Vertex objects:
vertices = Hull.DCEL.vertexDict.values()

# To get indices:
pts = Hull.getPts()    # to get pts in order used by ConvexHull3d
hull_vertices = pts[Hull.getVertexIndices()]

# To get vertices of each Face:
faces = [[list(v.p()) for v in face.loopOuterVertices()] for face in Hull.faceDict.values()]


#Hull.generateImage(show=True)
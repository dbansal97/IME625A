import numpy as np

def getStates(matrix):
    absorb = []
    trans = []
    for idx in range(matrix.shape[0]):
        if matrix[idx][idx] == 1:
            absorb.append(idx)
        else:
            trans.append(idx)

    return absorb, trans

def getStandard(matrix, absorb, trans):
    n = len(matrix)
    stdMatrix = np.zeros(matrix.shape)
    numAbs = len(absorb)
    numTrans = len(trans)
    idxAbs = list(range(n-numAbs, n))
    idxTrans = list(range(0, n-numAbs))
    stdMatrix[np.ix_(idxAbs, idxAbs)] = np.eye(numAbs)
    stdMatrix[np.ix_(idxTrans, idxTrans)] = matrix[np.ix_(trans, trans)]
    stdMatrix[np.ix_(idxTrans, idxAbs)] = matrix[np.ix_(trans, absorb)]
    return stdMatrix

def getQ(matrix, absorb, trans):
    return (matrix[np.ix_(trans, trans)])

def getCanonical(matrix):
    absorb, trans = getStates(matrix)
    print("Absorbing States : ", absorb)
    print("Transient States : ", trans)
    standard = getStandard(matrix, absorb, trans)
    Q = getQ(matrix, absorb, trans)
    return standard, Q

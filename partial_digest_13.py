L = [2,2,3,3,4,5,6,7,8,10]
X = []

def partialDigestAlgo(L):
    global X,width 
    width = max(L)
    L.remove(width)
    X = [0,width]
    form(L,X)

def subset_of_L(y,X,L):
    for i in X:
        if abs(y-i) not in L:
            return False
    return True

def removeNumbers(y,X,L):
    for i in X:
        if abs(y-i) in L:
            L.remove(abs(y-i))
        #print(L)
def Digest(y,X):
    deltaX = []
    for i in X:
        deltaX.append(abs(y-i))
    return deltaX

def form(L,X):
    if not L:
        X.sort()
        print(X)
        return 
    y = max(L)

    if subset_of_L(y,X,L):
        X.append(y)
        removeNumbers(y, X, L)
        form(L, X)
        if y in X:
           X.remove(y)
        L.extend(Digest(y, X))

    else:
        X.append(abs(width-y))
        removeNumbers(abs(width-y), X, L)
        form(L, X)
        if abs(width-y) in X:
            X.remove(abs(width-y))
        L.extend(Digest(abs(width-y), X))
    return 

if __name__ == "__main__":
    partialDigestAlgo(L)

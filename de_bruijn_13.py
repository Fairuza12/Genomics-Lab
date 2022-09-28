import math
edges = []
nodes = set()
 
def dfs(A,k,vertex):
     
    for i in range(k):
        s = vertex + A[i]
        if (s not in nodes):
            nodes.add(s)
            dfs(A,k,s[1:])
            edges.append(i)
 
def deBruijn(A, k, n):
     
    startNode = A[0] * (n - 1)
    dfs(A,k,startNode)
     
    Sring = ""
     
    # Number of edges
    l = pow(k, n)
    for i in range(l):
        Sring += A[edges[i]]
         
    Sring += startNode
    return Sring

if __name__=="__main__":
    sequel = "GACTTACGTACT"
    euler = deBruijn(sequel,3,2)
    for i in range(0,len(euler)-2):
        if i != len(euler)-3:
            print(euler[i:i+2],"->",end="")
        else:
            print(euler[i:i+2])
    print("\n")

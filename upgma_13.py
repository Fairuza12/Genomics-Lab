import numpy as np
matrix = [
    [], #A
    [9], #B
    [8, 11], #C
    [12, 15, 10], #D
    [15, 18, 19, 5]] #E

def merge_label(label,x,y):
    if y<x:
        x,y = y,x #Swap if indices not ordered
    label[x] = "("+label[x]+","+label[y]+")"
    del label[y] #Remove redundant label

def merge_matrix(matrix,x,y):
    if y<x:
        x,y = y,x
    row = []
    for i in range(0,x):
        row.append((matrix[x][i]+matrix[y][i])/2) #Reconstruct row
    matrix[x] = row
    #Reconstruct entire column(i,x)
    for i in range(x+1,y):
        matrix[i][x] = (matrix[i][x]+matrix[y][i])/2
    for i in range(y+1,len(matrix)):
        matrix[i][x] = (matrix[i][x]+matrix[i][y])/2 #Rest of the values
        del matrix[i][y]
    del matrix[y] 
    #print(matrix)

def mini_cell(matrix):
    mini = float("inf") #Default
    a,b = -1,-1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]<mini:
                mini = matrix[i][j]
                a,b = i,j
    return a,b #Coordinate of minimum cell

def all_labels(start,end):
    label = []
    for i in range(ord(start),ord(end)+1):
        label.append(chr(i))
    return label 

def UPGMA(matrix,label):
    while len(label)>1:
        a,b = mini_cell(matrix)
        merge_matrix(matrix,a,b)
        merge_label(label,a,b)
    return label[0]
label = all_labels("A","E")
print(UPGMA(matrix,label))

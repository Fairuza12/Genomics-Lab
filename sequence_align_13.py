import numpy as np

#Declaring sequence
seq1 = "CTCGCAGC"
seq2 = "CATTCAG"

#Declaring scores for match or mismatch eka gap penalty
match = 10
mismatch = -2
gap = -5

#Create matrices
main_matrix = np.zeros((len(seq1)+1,len(seq2)+1))
checker_matrix = np.zeros((len(seq1),len(seq2)))

#Fill the main matrix and checker matrix according to the scores
for i in range(len(seq1)):
    for j in range(len(seq2)):
        if(seq1[i]==seq2[j]):
            checker_matrix[i][j] = match;
        else:
            checker_matrix[i][j] = mismatch;
print(checker_matrix)

#Step1: INITIALIZE
for i in range(len(seq1)+1):
    main_matrix[i][0] = i*gap;
for j in range(len(seq2)+1):
    main_matrix[0][j] = j*gap;

#Step2: MATRIX FILLING
for i in range(1,len(seq1)+1):
    for j in range(1,len(seq2)+1):
        main_matrix[i][j] = max(main_matrix[i-1][j-1]+checker_matrix[i-1][j-1],main_matrix[i-1][j]+gap,main_matrix[i][j-1]+gap)
print(main_matrix)

#Step3: TRACEBACK
alignment1 = ""
alignment2 = ""
l1 = len(seq1)
l2 = len(seq2)
while(l1>0 and l2>0):
    if (main_matrix[l1][l2] == main_matrix[l1-1][l2-1]+checker_matrix[l1-1][l2-1]):
        alignment1 = seq1[l1-1]+alignment1
        alignment2 = seq2[l2-1]+alignment2
        l1 = l1-1
        l2 = l2-1
    elif(main_matrix[l1][l2] == main_matrix[l1-1][l2]+gap):
        alignment1 = seq1[l1-1]+alignment1
        alignment2 = "-" + alignment2
        l1 = l1-1
    else:
        alignment1 = "-" + alignment1 
        alignment2 = seq2[l2-1] + alignment2 
        l2 = l2-1
print(alignment1)
print(alignment2)  

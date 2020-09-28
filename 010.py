import copy

class A:
    def __init__(self, P, Q, n):        # construction function
        self.P = P
        self.Q = Q
        self.n = n

    def OBST(self):
        n = self.n

        # initialization
        W = [ ([0] * (n+1)) for i in range(n+1)]           # W represent weight(0:n, 0:n): weight
        C = copy.deepcopy(W)                               # C represent cost(0:n, 0:n):   two-dimensional array
        R = copy.deepcopy(W)                               # R represent R(0:n, 0:n):      root of the tree
        # initialization
        for i in range(n):
            W[i][i] = self.  Q[i]; C[i][i] = 0; R[i][i] = 0
            W[i][i+1] = self.Q[i] + self.Q[i+1] +self.P[i+1];  C[i][i+1] = W[i][i+1];  R[i][i+1] = i+1
        W[n][n] = self.Q[n];  C[n][n] = 0;  R[n][n] = 0

        # evaluate other value: W,C,R
        for m in range(2, n+1):                              # find m node binary search tree
            for i in range(0, n-m+1):
                j = i + m
                W[i][j] = W[i][j-1] + self.P[j] + self.Q[j]
                min = 100                                    # big enought number
                for l in range(R[i][j-1], R[i+1][j]+1):      # Knuth thought: R[i][j-1] <= k <= R[i+1][j]
                    cost = C[i][l-1] + C[l][j]
                    if cost < min:
                        min = cost                           # variable min achieve minimum 
                        k = l                                # k represent the value that let cost achieve minimum 
                
                C[i][j] = W[i][j] + C[i][k-1] + C[k][j]      # calculate value: C
                R[i][j] = k                                  # calculate value: R

        return R

    def output(self, R, i, j, n, k):            # R: the matrix of root; i,j: array index; n: array dimension; k:the root
        if i != j:
            m = R[i][j]                             # achieve the number of the root

            if j - i == n:                          # judge whether the root or not
                print(m, -1)
            else:
                print(m, k)

            self.output(R, i, m-1, n, m)            # left tree
            self.output(R, m, j, n, m)              # right tree


if __name__ == '__main__':
    P = [0, 1, 4, 2, 1]       # P(1:n) effective
    Q = [4, 2, 4, 1, 1]       # Q(0:n) effective
    n = 4                     # (a1, a2, a3, a4) = (do if read while)  

    a = A(P, Q, n)            # call class A
    R = a.OBST()              # call function OBST of class
    print('Parent representation:')
    a.output(R, 0, n, n, -1)  # view the tree

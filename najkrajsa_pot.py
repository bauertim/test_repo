def cena(a):
    @caching
    def c(i,j):
        if i == 0 and j == 0:
            return a[0][0]
        elif i == 0:
            return c(0, j-1) + a[0][j]
        elif j == 0:
            return c(i-1, 0) + a[i][0]
        else:
            return min(c(i-1, j), c(i, j-1)) + a[i][j]
    n = len(a[0])
    m = len(a)
    return c(m-1, n-1)

def caching(f):

    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else: 
            r = f(*args)
            cache[args] = r
            return r
    return g 

# Preizkus:
t = [[9,1,0,4,3,5],
     [7,3,2,3,4,8],
     [4,1,6,0,3,2],
     [5,3,8,7,1,3],
     [1,3,2,1,4,0],
     [1,3,2,1,4,0]]
print ("I. Najcenejsa pot na t stane", cena(t))



def pot(a):

    @caching
    def cena(i,j):
        if i == 0 and j == 0:
            return a[0][0]
        elif i == 0:
            return cena(0, j-1) + a[0][j]
        elif j == 0:
            return cena(i-1, 0) + a[i][0]
        else:
            return min(cena(i-1, j), cena(i, j-1)) + a[i][j]

    m = len(a) # st vrstic
    n = len(a[0]) # st stolpcev
    pot = [None for i in range(n+m-1)]
    (i, j) = (n-1, m-1) # polnimo od konca proti začetku, lahko bi tudi obratno
    for k in range(n+m-1):
        pot[k] = (i,j) 
        if i == 0: 
            j = j - 1
        elif j == 0:
            i = i - 1
        elif cena(i-1, j) < cena(i, j-1):
            i = i - 1
        else:
            j = j - 1
    return pot

print('Najcenejsa pot za t je ', pot(t))
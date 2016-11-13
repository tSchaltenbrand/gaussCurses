class Matrix:
    """Simple matrix class supporting matrix addition and multiplication"""
    def __init__(self, m = [[]]):
        self.__matrix = m
        self.__rows = len(m)
        self.__cols = 0
        if self.__rows > 0:
            self.__cols = len(m[0])

    def setRows(self, n):
        if n > self.__rows:
            self.__matrix += [[0 for i in range(self.__cols)] for j in range(n - self.__rows)]
        else:
            self.__matrix = self.__matrix[0:(n - self.__rows)]
        self.__rows = n
    def getRows(self):
        return self.__rows

    def setCols(self, n):
        if n > self.__cols:
            for col in self.__matrix:
                col += [0 for i in range(n - self.__cols)]
        else:
            for i in range(self.__rows):
                self.__matrix[i] = self.__matrix[i][0:(n - self.__cols)]
        self.__cols = n
    def getCols(self):
        return self.__cols

    def setValue(self,i,j,value):
        self.__matrix[j][i] = value
    def getValue(self,i,j):
        return self.__matrix[j][i]

    def getMatrix(self):
        return self.__matrix

    def __add__(self, other):
        sumMat = Matrix()
        if self.__rows == other.getRows() and self.__cols == other.getCols():
            sumMat.setRows(self.__rows)
            sumMat.setCols(self.__cols)
            for j in range(self.__rows):
                for i in range(self.__cols):
                    sumMat.setValue(i,j,self.__matrix[j][i] + other.getValue(i,j))
        return sumMat
    def __mul__(self, other):
        mulMat = Matrix([[0 for i in range(other.getCols())] for j in range(self.__rows)])
        if self.__cols == other.getRows():
            for j in range(mulMat.getRows()):
                for i in range(mulMat.getCols()):
                    val = 0
                    for n in range(self.__cols):
                        val += self.__matrix[j][n] * other.getValue(i,n)
                    print(i,j,mulMat.getMatrix())
                    mulMat.setValue(i,j,val)
        return mulMat
    def __repr__(self):
        maxLotSize = max([max([len(str(i)) for i in row]) for row in self.__matrix])
        outString = '┌' + ' ' * (1 + self.__cols * (1 + maxLotSize)) + '┐' + '\n'
        for row in self.__matrix:
            outString += "│ " + ' '.join([format(str(i), ">" + str(maxLotSize) +"s") for i in row]) + " │" + '\n'
        outString += '└' + ' ' * (1 + self.__cols * (1 + maxLotSize)) + '┘'
        return outString

def identity(n, one = 1, zero = 0):
    """Returns an n * n identity matrix"""
    return Matrix([[one if i == j else zero for i in range(n)] for j in range(n)])

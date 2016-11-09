class Matrix:
    """Simple matrix class supporting matrix addition and multiplication"""
    def __init__(self):
        self.__rows = 0
        self.__cols = 0
        self.__matrix = []

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
            for col in self.__matrix:
                col = col[0:(n - self.__cols)]
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
        mulMat = Matrix()
        if self.__cols == other.getRows():
            mulMat.setRows(self.__rows)
            mulMat.setCols(other.getCols())
            for j in range(mulMat.getRows()):
                for i in range(mulMat.getCols()):
                    val = 0
                    for n in range(self.__cols):
                        val += self.__matrix[j][n] * other.getValue(i,n)
                    mulMat.setValue(i,j,val)
        return mulMat

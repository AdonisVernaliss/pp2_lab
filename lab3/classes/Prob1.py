class myString:    
    def getString(self):
        self.st = input() 

    def printString(self):
        print(self.st.upper())

s = myString()

s.getString()
s.printString()
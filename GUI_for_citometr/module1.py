import serial

s = serial.Serial('COM10')
print(type(s))


class ComPortRW:
    port = srial.Serial('') #port from which data is read
    startSymbol = '>' #symvol of beginning data binary string
    endSymbol = '<' #sumbo; of ending data, binary string
                        


    def __init__(self, comPortName = str, startSymbol = str, endSymbol = str):
        self.port = serial.Serial(comPortName)
        self.startSymbol = startSymbol
        self.endSymbol = endSymbol

    def readFromComPort(self):
        result = ""
        inp = b''
        while(inp != self.startSymbol): #skip data before start symbol
            inp = s.read()

        while(1):                  #read data from port until get endSymbol
            inp = s.read()
            if (inp == self.endSymbol):
                break
            result += inp.decode("utf-8")

        return result

    def writeToComPort(self, data):#, port):
        print(data.encode('utf-8'))


for i in range(10):
    writeDataToPort(str(i))
#    print(readFromComPort(s, b'>', b'<'))


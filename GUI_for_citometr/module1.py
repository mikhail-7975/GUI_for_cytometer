import serial

s = serial.Serial('COM10')
print(type(s))

def readFromComPort(ComPort, #port from which data is read
                    startSymbol, #symvol of beginning data binary string
                    endSymbol #sumbo; of ending data, binary string
                    ):
    result = ""
    inp = b''
    while(inp != startSymbol): #skip data before start symbol
        inp = s.read()

    while(1):                  #read data from port until get endSymbol
        inp = s.read()
        if (inp == endSymbol):
            break
        result += inp.decode("utf-8")

    return result

def writeDataToPort(data):#, port):
    print(data.encode('utf-8'))

for i in range(10):
    writeDataToPort(str(i))
#    print(readFromComPort(s, b'>', b'<'))


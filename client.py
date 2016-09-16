
def next_byte():
    msg = input("input a byte: ")
    return(int(msg, 16).to_bytes(1,'big'))


def getNumOfLines():
    number = b''
    for i in range(0,4):
        msg = next_byte()
        number += msg
    print("Number of lines = %s" % int.from_bytes(number,'big'))
    return int.from_bytes(number,'big')


def readMessage(numOfNewLines, listOfLines):
    i = 0;
    print(len(listOfLines))
    while i < numOfNewLines:
        msg = next_byte()
        if len(listOfLines) - 1 < i :
            print("added a new index to the list")
            listOfLines.append(msg)
        else:
            print("just added: %s , to the message" % msg.decode())
            listOfLines[i] += msg

        if msg == b'\n':
            print("hit a new line")
            i += 1



def writeMessageToFile(listOfLines):
    file = open("finalMessage.txt","w")
    for bytes in listOfLines:
        file.write(bytes.decode())
    file.close()


list = []
readMessage(getNumOfLines(),list)
writeMessageToFile(list)


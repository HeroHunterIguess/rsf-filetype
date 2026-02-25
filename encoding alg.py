# exmaple/test input
binput = "1101100001101100111010000110101010111010000101101010000001100100"
print(binput)
# split up long numbers
def longNumSplitter(count):
    longstr=""
    for char in str(count):
        longstr+=char
        count=str(count)[1:]
        if len(count)>0:
            longstr+="/"
    return longstr
def updateNum(curNum):
    if curNum==1:
        return 0
    elif curNum==0:
        return 1
# encode input
def encode(binaryinput):
    numcounter=0
    final=binaryinput[0]
    for i in range(len(binaryinput)):
        if binaryinput[i]==binaryinput[i-1]:
            numcounter+=1
        else: 
            if numcounter<9:
                final+=str(numcounter)
                numcounter=1
            else: 
                final+=longNumSplitter(numcounter)
                numcounter=1
    final+=longNumSplitter(numcounter)
    numcounter=1
    # clean and return output
    if final[0]=="0":
        final=final[1:]
    return final
encoded=encode(binput) 
print(encoded)
# take in input and decode it 
def decode(binaryinput):
    final=""
    currentNum=int(binaryinput[0])
    for i in range(len(binaryinput)):
        # need to also check if next char is / without overflow
        if not (i+1)==len(binaryinput):
            if binaryinput[i]!="/" and binaryinput[i-1]!="/" and binaryinput[i+1]!="/":
                # add that amount of the currentNum to final
                for i in range(int(binaryinput[i])):
                    final+=str(currentNum)
            elif binaryinput[i]=="/":
                # parse longer numbers
                amount=binaryinput[i-1]+binaryinput[i+1]
                for i in range(int(amount)):
                    final+=str(currentNum)
            else:
                continue
        # update current number
        currentNum=updateNum(currentNum)
    # update and restore final number
    currentNum=updateNum(currentNum)
    for i in range(int(binaryinput[i])):
        final+=str(currentNum)
    # clean and return final
    final=final[1:]
    return final
decoded=decode(encoded)
print(decoded)

class Encoder:
    # split up long numbers
    @staticmethod
    def longNumSplitter(count):
        longstr=""

        for char in str(count):
            longstr+=char
            count=str(count)[1:]

            if len(count)>0:
                longstr+="/"

        return longstr
    
    @staticmethod
    def updateNum(curNum):
        if curNum==1:
            return 0
        elif curNum==0:
            return 1
    
    # encode input
    @staticmethod
    def encode(binaryinput):
        numcounter=1
        final=binaryinput[0]

        for i in range(1,len(binaryinput)):

            if binaryinput[i]==binaryinput[i-1]:
                numcounter+=1
            else: 
                if numcounter<9:
                    final+=str(numcounter)
                    numcounter=1
                else: 
                    final+=Encoder.longNumSplitter(numcounter)
                    numcounter=1
        
        final+=Encoder.longNumSplitter(numcounter)
        numcounter=1

        # clean and return output
        if final[0]=="0":
            final=final[1:]
        return final

    # take in input and decode it 
    @staticmethod
    def decode(binaryinput):
        final=""
        currentNum=int(binaryinput[0])

        for i in range(1,len(binaryinput)):
            # need to also check if next char is / without overflow
            if not (i+1)==len(binaryinput):
                if binaryinput[i]!="/" and binaryinput[i-1]!="/" and binaryinput[i+1]!="/":
                    # add that amount of the currentNum to final
                    for n in range(int(binaryinput[i])):
                        final+=str(currentNum)
                elif binaryinput[i]=="/":
                    # parse longer numbers
                    amount=binaryinput[i-1]+binaryinput[i+1]

                    for j in range(int(amount)):
                        final+=str(currentNum)
                else:
                    continue
            
            # update current number
            currentNum=Encoder.updateNum(currentNum)
        
        # update and restore final number
        currentNum=Encoder.updateNum(currentNum)
        
        for i in range(int(binaryinput[i])):
            final+=str(currentNum)
        
        # clean and return final
        final=final[1:]
        return final

class Compression:
    # split up long numbers
    @staticmethod
    def longNumSplitter(count):
        long_str=""

        for char in str(count):
            long_str+=char
            count=str(count)[1:]

            if len(count)>0:
                long_str+="/"

        return long_str

    # update the current number being looked at
    @staticmethod
    def updateNum(current_number):
        if current_number==1:
            return 0
        elif current_number==0:
            return 1
    
    # encode input
    @staticmethod
    def encode(binary_input):
        counter=1
        # setting what it starts w/
        final=binary_input[0]
        binary_input=binary_input[1:]

        for i in range(1,len(binary_input)):

            if binary_input[i]==binary_input[i-1]:
                counter+=1
            else: 
                if counter<9:
                    final+=str(counter)
                    counter=1
                else: 
                    final+=Compression.longNumSplitter(counter)
                    counter=1
        
        # this may need to be reimplimented, just commented out for testing rng
        #final+=Compression.longNumSplitter(counter)
        #counter=1

        # clean and return output
        if final[0]=="0":
            final=final[1:]
        return final

    # take in input and decode it 
    @staticmethod
    def decode(binary_input):
        final=""
        slashIndices=[]
        current_num=int(binary_input[0])

        for i in range(len(binary_input)):
            # need to also check if next char is / without overflow
            if not (i+1)==len(binary_input):
                if binary_input[i]!="/" and binary_input[i-1]!="/" and binary_input[i+1]!="/":
                    # add that amount of the current_num to final
                    for n in range(int(binary_input[i])):
                        final+=str(current_num)3
                elif binary_input[i]=="/":
                    slashIndices.append(i)
                    
                
                    #for j in range(int(amount)):
                    #    final+=str(current_num)
                else:
                    continue
            
            # update current number
            current_num=Compression.updateNum(current_num)
        
        # update and restore final number
        current_num=Compression.updateNum(current_num)
        
        for i in range(int(binary_input[i])):
            final+=str(current_num)
        
        # clean and return final
        final=final[1:]
        return final

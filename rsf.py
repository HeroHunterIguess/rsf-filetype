import pygame
from encoder import Encoder

# default var setup
width=100
height=100
datalist=[]

# initializing pygame stuff
pygame.init()
running = True
screen = pygame.display.set_mode((width, height))

# reading and parsing image data file 
with open('/home/herohunter/Everything/Coding/python projects/custom image filetype/data.rsf', 'r') as file:
    rb=file.read()

# encode data and write it to encoded.rsf
encodedbinary=Encoder.encode(rb)
with open('/home/herohunter/Everything/Coding/python projects/custom image filetype/encoded.rsf', 'w') as file:
    file.write(encodedbinary)

# decode data and write it to recoded.rsf
rb=Encoder.decode(encodedbinary)

with open('/home/herohunter/Everything/Coding/python projects/custom image filetype/recoded.rsf', 'w') as file:
    file.write(rb)

for i in range(len(rb)):
    if i%8==7:
        binary=int(rb[i-7]+rb[i-6]+rb[i-5]+rb[i-4]+rb[i-3]+rb[i-2]+rb[i-1]+rb[i], 2)
        datalist.append(binary)

# setting height and width based on image data
width=datalist[0]
height=datalist[1]
screen=pygame.display.set_mode((width, height))

iteration=0
# run window and render data
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    if iteration==0:
        layerHeight=-1
        for i in range((len(datalist)-2)//3):
            if i%width==0:
                layerHeight+=1
            if i==0:
                screen.set_at((i%width,layerHeight), (datalist[2],datalist[3],datalist[4]))
            else:
                screen.set_at((i%width,layerHeight), (datalist[(i*3)-1],datalist[(i*3)],datalist[(i*3)+1]))
        
        screen.set_at((i%width,layerHeight), (datalist[-3],datalist[-2],datalist[-1]))

        pygame.display.flip()
        iteration=1


#Sec01# #Importing DIfferent Libraries into the main file
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from PIL import Image






#Sec02# Creating a class of Front lights
class Frontlights():
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        circle1 = plt.Circle(self.pos, 20, color=self.color)    #Light shape, size and color attributes being set
        ax0.add_patch(circle1)




#Sec03# Creating a class of Top lights
class TopLights():
    def __init__(self, ax, pos, color, intensity):
        self.pos = pos
        self.color = color
        self.intensity = intensity

        ax.fill([self.pos, self.pos + 40, self.pos + 40, self.pos], [490, 490, 500, 500], color=self.color)                                 # A small rectangle at the top
        ax.fill([self.pos, self.pos + 40, self.pos + 100, self.pos - 60], [490, 490, 100, 100], color=self.color, alpha=self.intensity)     # the beam of the lights




#Sec04# Creating a class of Smoke particle
class Smoke:
    def __init__(self, position):
        self.position = position

    def stepChange(self, row_range, col_range):
        self.position = (
            self.position[0] + np.random.randint(-(row_range/2), row_range+1),                                       #The position of the particles will change randomly 
            self.position[1] + np.random.randint(-(col_range/2), col_range+1)
        )

    def plotparticle(self, ax, alpha):
        ax.plot(self.position[0], self.position[1], 'o', markersize= 10, color= "grey" , alpha=alpha)               #Setting the shape, size and color of each particle





#Sec05# Creating a class of SmokeMachine
class SmokeMachine:
    def __init__(self, position, num_smoke):
        self.position = position
        self.num_smoke = [Smoke(position) for _ in range(num_smoke)]    

    def stepChange(self, row_range, col_range):
        for smoke in self.num_smoke:
            smoke.stepChange(row_range, col_range)

    def plotparticles(self, ax, alpha):
        for smoke in self.num_smoke:
            smoke.plotparticle(ax, alpha)






#Sec06# Lists created for to store light colors and intensities from data file

filedata = []
clight1 = []
clight2 = []
clight3 = []
clight4 = []
clight5 = []
ilight1 = []
ilight2 = []
ilight3 = []
ilight4 = []
ilight5 = []





#Sec07# Going through a data file to read it and split it into the above defined buckets

with open("lights2.csv", "r") as file:
    data = file.readlines()

for eachline in data:
    spliteachline = eachline.split(",")
    clight1.append(spliteachline[0].strip())
    clight2.append(spliteachline[1].strip())
    clight3.append(spliteachline[2].strip())
    clight4.append(spliteachline[3].strip())
    clight5.append(spliteachline[4].strip())
    ilight1.append(float(spliteachline[5]))
    ilight2.append(float(spliteachline[6]))
    ilight3.append(float(spliteachline[7]))
    ilight4.append(float(spliteachline[8]))
    ilight5.append(float(spliteachline[9]))




#Sec08# Setting up how many iterations so we can show it as animation
iterations = 100





#Sec09# Creating a figure that has two plots. One for front lights the other for top lights
fig, (ax0, ax) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]},
                              figsize = (10,10))






#Sec10# Creation of smoke machines using the Smoke Machine Class.
smoke_machine1 = SmokeMachine((0, 200), num_smoke=30)                                                           # Position of machine and num of smoke particles set
smoke_machine2 = SmokeMachine((0, 100), num_smoke=30)                                                             # Position of machine and num of smoke particles set


#Sec11# Importing a picture of the band
image_path = "/home/20972008/Desktop/Fop Final Assignment/Scenario2/band2.png"                                                           #Setting a path to the png file
image = Image.open(image_path)                                                                                   #using PIL library to load the png into the image variable
desired_width = 350                                                                                              #Setting the desired width for the picture in pixels
desired_height = 230                                                                                             #Setting the desired height for the picture in pixels
resized_image = image.resize((desired_width, desired_height))                                                    # Resizing the image into a resized image variable
x_position = 70                                                                                                  # setting X-coordinate of the image's position
y_position = 70                                                                                                  # setting Y-coordinate of the image's position


#Sec12# Importing a picture of the the background
image_path2 = "/home/20972008/Desktop/Fop Final Assignment/Scenario2/background.jpg"
image2 = Image.open(image_path2)
desired_width2 = 500  
desired_height2 = 500 
resized_image2 = image2.resize((desired_width, desired_height))
x_position2 = 0  
y_position2 = 0  


#Sec13# Importing a picture of the the Logo for SpinalTap
image_path3 = "/home/20972008/Desktop/Fop Final Assignment/Scenario2/tap-logo.png"
image3 = Image.open(image_path3)
desired_width3 = 200  # Desired width in pixels
desired_height3 = 100  # Desired height in pixels
resized_image3 = image3.resize((desired_width3, desired_height3))
x_position3 = 150  
y_position3 = 330  




#Sec14# Creating a function called animate so that under it all things would animate
def animate(i):





    #Sec15# Setting up the first subplot that contains all Front lights
    ax0.set_aspect("equal")
    ax0.fill([0,500,500,0],[0,0,50,50], color="black")                                                  #Setting coordinates and color of fill

    #Sec16#  Setting up the second plot the contains the audience view of the concert
    ax.clear()
    ax.set_xlim(0, 500)                                                                                 #Setting x lim to the graph
    ax.set_ylim(0, 500)                                                                                 #Setting x lim to the graph
    ax.set_aspect("equal")                                                                              #setting the aspect ratio of it to be equal
    ax.set_facecolor("black")                                                                           #setting the face color to black    


    ax.text(250, 30, 'We have 20972008 People in Crowd',                                                #Creating a textbox with different customization
        fontsize=7,
        color='red',
        fontweight='bold',
        horizontalalignment='center',
        verticalalignment='bottom',
        bbox={'facecolor': 'black', 'edgecolor': 'white', 'linewidth': 1, 'pad': 5})






    #Sec17# Setting up the Front Lights for subplot 1
    light1 = Frontlights((30, 25),clight5[i])                                                               
    light2 = Frontlights((140,25),clight2[i])                                                         # giving coordiantes and taking lights from file through variables
    light3 = Frontlights((250,25),clight1[i])                                                           # giving coordiantes and taking lights from file through variables
    light4 = Frontlights((360,25),clight3[i])
    light5 = Frontlights((470,25),clight4[i])


    #Sec18# Setting up the TopLights for subplot 2
    light3 = TopLights(ax, 230, clight1[i], ilight1[i])
    light2 = TopLights(ax, 130, clight2[i], ilight2[i])                                             # giving coordiantes and taking lights and intensities from file through variables
    light4 = TopLights(ax, 330, clight3[i], ilight3[i])
    light5 = TopLights(ax, 430, clight4[i], ilight4[i])
    light1 = TopLights(ax, 30, clight5[i], ilight5[i])




    
    #Sec19# Creation of Stage 

    #Bottom Stage
    ax.fill([500, 0, 0, 500], [0, 0, 70, 70], color="Blue", edgecolor="black")
    ax.fill([0, 500, 0, 500], [0, 0, 70, 70], color="#4F4F4F", edgecolor="black")

    #Add circle to stage
    circle10 = plt.Circle([30,35],20, color="black", alpha=0.5)
    ax.add_patch(circle10)
    circle10 = plt.Circle([470,35],20, color="black", alpha=0.5)
    ax.add_patch(circle10)

    #Upper Stage
    ax.fill([470,30,30,470],[70,70,100,100], edgecolor="white", color="#C8A165")





    #Sec20# Setting up the pictures imported into the plot

    ax.imshow(resized_image2, extent=[x_position2, x_position2 + desired_width2, y_position2, y_position2 + desired_height2])

    ax.imshow(resized_image, extent=[x_position, x_position + desired_width, y_position, y_position + desired_height])
    
    ax.imshow(resized_image3, extent=[x_position3, x_position3 + desired_width3, y_position3, y_position3 + desired_height3])
    





    #Sec21# Setting up Props (Speakers)
    speaker1 = plt.Rectangle([30,100], 50,150, edgecolor="white", facecolor="#4F4F4F")
    ax.add_patch(speaker1)
    speaker2 = plt.Rectangle([420,100], 50,150, edgecolor="white", facecolor="#4F4F4F")
    ax.add_patch(speaker2)

    sp1circle1= plt.Circle([55,210],20, color="black")
    ax.add_patch(sp1circle1)
    sp1circle2= plt.Circle([55,210],10, color="red")
    ax.add_patch(sp1circle2)

    sp1circle1= plt.Circle([55,150],20, color="black")
    ax.add_patch(sp1circle1)
    sp1circle2= plt.Circle([55,150],10, color="red")
    ax.add_patch(sp1circle2)


    sp1circle1= plt.Circle([445,210],20, color="black")
    ax.add_patch(sp1circle1)
    sp1circle2= plt.Circle([445,210],10, color="red")
    ax.add_patch(sp1circle2)

    sp1circle1= plt.Circle([445,150],20, color="black")
    ax.add_patch(sp1circle1)
    sp1circle2= plt.Circle([445,150],10, color="red")
    ax.add_patch(sp1circle2)





    #Sec22# Setting up the Smoke Machines and the Particles

    smoke_machine1.stepChange(20, 20)                                                                # Move smoke randomly within 100 units in row/column directions
    smoke_machine1.plotparticles(ax,0.5)

    smoke_machine2.stepChange(20, 20)                                                                 # Move smoke randomly within 100 units in row/column directions
    smoke_machine2.plotparticles(ax, 0.5)



    #Sec23# Title set in a way to show the title plus the iteration number                          
    plt.suptitle(f"Stageview_{i+1}", fontsize="18")






#Sec24# Animation created and shown on the plot
ani = FuncAnimation(fig, animate, frames=iterations, interval=200)
plt.show()
















#Sec25# #BONUS FEATURE#

class Person():

        def __init__(self,pos,color):
            self.pos = pos
            self.color = color

        def face(self):
            face =  plt.Circle([self.pos[0],self.pos[1]],20, facecolor = self.color, edgecolor = "black")
            ax.add_patch(face)

        def torso(self):
            torso = plt.Rectangle([self.pos[0]-30,self.pos[1]-120], 60,100, facecolor = self.color, edgecolor = "black")
            ax.add_patch(torso)

        def legs(self):
            leg1 = plt.Rectangle([self.pos[0]-30,self.pos[1]-200], 20,100, facecolor = self.color, edgecolor = "black")
            leg2 = plt.Rectangle([self.pos[0]+10,self.pos[1]-200], 20,100, facecolor = self.color, edgecolor = "black")
            ax.add_patch(leg1)
            ax.add_patch(leg2)

        def arms(self):
            arm1= plt.Rectangle([self.pos[0]-40,self.pos[1]-100], 9,80, facecolor = self.color, edgecolor = "black")
            ax.add_patch(arm1)
            arm2= plt.Rectangle([self.pos[0]+31,self.pos[1]-100], 10,80, facecolor = self.color, edgecolor = "black")
            ax.add_patch(arm2)



    #Setting up humans
    #person1= Person((140,300),"red")
    #person1.legs()
    #person1.face()
    #person1.torso()
    #person1.arms()

    #person2= Person((250,300),"yellow")
    #person2.face()
    #person2.legs()
    #person2.torso()
    #person2.arms()

    #person2= Person((360,300),"green")
    #person2.face()
    #person2.legs()
    #person2.torso()
    #person2.arms()


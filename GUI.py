"""
PH2150 Second Year Python Project
Author: Nickolas Theodoulou
"""


import pylab
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkMessageBox as msg
import numpy as np

from scipy import *
from scipy.special import hermite
from math import factorial
import matplotlib.pyplot as plt
from Tkinter import Tk, Frame, BOTH


#I dont use these here but they for getting the user to input things/warning messages
import tkMessageBox #output only in the form of a popup
import tkSimpleDialog #lets the user input a string
import tkFileDialog

  #
   # def fill(image, color):
   #     """Fill image with a color=(r,b,g)."""
   #     r,g,b = color
   #     width = image.width()
   #     height = image.height()
   #     hexcode = "besselpic.gif" % (r,g,b)
   #     horizontal_line = "{" + " ".join([hexcode]*width) + "}"
   #     image.put(" ".join([horizontal_line]*height))
   #
   #     photo = tkinter.PhotoImage(width=32, height=32)
   #
   #     fill(photo, (255,0,0))  # Fill with red...
   #
   #     label = tkinter.Label(root, image=photo)
   #     label.grid()
   #
hbar = 1.056e-34
#set hbar as this will later be used in various functions

def InfinteWave(x, n):
    return sqrt((2/1))*sin(n*pi*x/1)
 #This is the wavefunction of the 1-D infinite square well, it will later be plotted next to the harmonic oscilaltor wavefunction and the probability density of the 1-D infnite Sq Well
def HarmonicWave(x, n):
    return ((hermite(n)(x))*exp(-x**(2.)/(2.)))/(sqrt((2.)**(n)*factorial(n)*sqrt(pi)))
 #This is the wavefunction of the 1-D Quantum Harmonic Oscillator
def InfinteWaveSQ(x, n):
    return sqrt((2/1))*sin(n*pi*x/1)*sqrt((2/1))*sin(n*pi*x/1)
 #This is the probability density of of the 1-D infnite Sq Well
def HarmonicWaveSQ(x, n):
    return ((hermite(n)(x))*exp(-x**(2.)/(2.)))/(sqrt((2.)**(n)*factorial(n)*sqrt(pi)))*((hermite(n)(x))*exp(-x**(2.)/(2.)))/(sqrt((2.)**(n)*factorial(n)*sqrt(pi)))
#This is the probability density of of the 1-D Quantum Harmonic Oscillator
def ClassicHarmonicSq(x, n):
    return (1./(np.pi*np.sqrt((2*n)+(1.)-x**(2.))))
#This is the classical probability density of the 1-D Quantum Harmonic Oscillator which will be plotted on the same graph as the quantum P.D so they can be compared
def InfinitePotEnergy1(x, n, m, L):
    return (hbar**2*n**2*pi**2)/2*m*L**2*x**0

#This function calculates the energy of the 1-D infinite sq well for n , I was going to plot both n and m on one graph however I wasnt able to due to time constraints
#I also have x**0 which equals 1 in this equation as for some reason if the function isn't a function of x it wouldnt plot and I found this to be the easiest way possible to
#get my code to work. I did the same thing for the energy of the harmonic oscillator
def HarmonicOscillatorEnergy1(x, n, omega):#this code calculates the energy of a harmonic oscialltor which depends on n and omega I also put in x**0 as this wouldn't work
#I also ran out of time to create a programme that showed 2 energy levels but ran out of time however I left the code in as it didnt interfere with the rest of the code.
    return ((2*n)+1)*hbar*omega/2*x**0
def HarmonicOscillatorEnergy2(x, m, omega):
    return ((2*m)+1)*hbar*omega/2*x**0
# I was going to plot both n and m on one graph however I wasnt able to due to time constraints
#I also have x**0 which equals 1 in this equation as for some reason if the function isn't a function of x it wouldnt plot and I found this to be the easiest way possible to
#get my code to work.


class homePage:#This is the first class which I am using for the mainpage so that the graphs can be opened by clicking on a button from here, this will also be used as a welcome page
    #and also to go to my pdf file,


    def __init__(self,master):
        self.master = master

        self.frame = Frame(self.master, bg ='blue')#This creates a frame for all the buttons on the main page


        T = Text(height=2, width=120)
        T.pack()
        T.insert(END, "Welcome to my programme which visualy demonstrates the 1-D Infinite Square Well and the 1-D Quantum Harmonic Oscillator")

        text = Text(self.frame)
        text.insert(INSERT,'This program demonstrates various 1-D probabilities of the Infinite Potential Well and Harmonic Oscillator in quantum mechanics.')
        text.pack()

        self.mainb1 = Button(self.frame,text = 'Wavefunction of Infinite Potential Well and Quantum Harmonic Oscillator',width = 100, command = self.InfiniteSqWellandHarmonic)
        self.mainb1.pack()#this is a button that will then be instructed to open a new page that shows the Wavefunction of Infinite Potential Well and Quantum Harmonic Oscillator
        #all the other buttons in this section the same thing but open different windows
        self.mainb2 = Button(self.frame,text = 'Probability Disribution of the Infinite Square Well and Quantum Harmonic Oscillator',width = 100, command = self.SqInfiniteSqWellandHarmonicSq)
        self.mainb2.pack()
        self.mainb3 = Button(self.frame,text = 'Wavefunction of the Infinite Square Well and the Probability Disribution of the Infinite Square Well',width = 100, command = self.InfiniteSqWellandSqInfiniteSqWel)
        self.mainb3.pack()
        self.mainb4 = Button(self.frame,text = 'Wavefunction of the Quantum Harmonic Oscillator and the Probability Disribution of the Quantum Harmonic Oscillator',width = 100, command = self.HarmonicandSqHarmonic)
        self.mainb4.pack()
        self.mainb5 = Button(self.frame,text = 'Classical and Quantum probability distribution of the Quantum Harmonic Oscillator',width = 100, command = self.ClassicandQuantumHarmonic)
        self.mainb5.pack()
        self.mainb6 = Button(self.frame,text = 'Energy levels of a particle in an Infinite Square Well and Quantum Harmonic Oscillator',width = 100, command = self.InfinitePotandHarmEnergy)
        self.mainb6.pack()

        self.frame.pack()



    def close_window(self):
        self.master.destroy()

    def menu(self,frame): #creates a menu tool bar at the top of the frame
        self.menubar = Menu(frame)
        self.filemenu = Menu(self.menubar,tearoff=0) #File Menu
        self.filemenu.add_command(label ="Exit",command=self.close_window)
        self.menubar.add_cascade(label="File",menu=self.filemenu)

        self.helpmenu = Menu(self.menubar,tearoff=0)#Help Menu
        #self.helpmenu.add_command(label="About",command=self.info)
        self.menubar.add_cascade(label="Help",menu=self.helpmenu)

    def InfiniteSqWellandHarmonic(self):
        self.newWindow = Toplevel(self.master)
        self.app = InfiniteSqWell(self.newWindow), Harmonic(self.newWindow)

    def SqInfiniteSqWellandHarmonicSq(self):
        self.newWindow = Toplevel(self.master)
        self.app = InfiniteSqWellSQ(self.newWindow), HarmonicSQ(self.newWindow)

    def InfiniteSqWellandSqInfiniteSqWel(self):
        self.newWindow = Toplevel(self.master)
        self.app = InfiniteSqWell(self.newWindow), InfiniteSqWellSQ(self.newWindow)

    def HarmonicandSqHarmonic(self):
        self.newWindow = Toplevel(self.master)
        self.app = Harmonic(self.newWindow), HarmonicSQ(self.newWindow)

    def ClassicandQuantumHarmonic(self):
        self.newWindow = Toplevel(self.master)
        self.app = CLassicalProb(self.newWindow)

    def InfinitePotandHarmEnergy(self):
        self.newWindow = Toplevel(self.master)
        self.app = InfinitePotentialEnergy(self.newWindow), HarmonicOscillatorEn(self.newWindow)




class InfiniteSqWell:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)
        self.makeInputs(frame)

    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(6,3.5), dpi=100)
        self.figPlot = self.fig.add_subplot(111)
        #The next line is the important bit, you can not just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,1) of the master frame
        self.canvas.get_tk_widget().grid(row = 0, column = 3)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 3)

    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        self.InputFrame = Frame(frame)
        self.InputFrameDesc = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        self.InputFrame.grid(column = 0, row = 0)
        self.InputFrameDesc.grid(column = 4, row = 0)
        #the lables
        self.lbln = Label(self.InputFrame, text = "n=0,1,2,..", justify=LEFT)
        self.lbln.grid(column= 0,row= 0)

        self.textleftgraph = StringVar()
        self.textlefth = Label(self.InputFrameDesc, textvariable = self.textleftgraph, wraplength=300)
        self.textleftgraph.set("The infinite square well describes a particle free to move in a space surrounded by impenetrable barriers. The model is used as a hypothetical "
"example to illustrate the differences between classical and quantum systems. In classical systems for example, if a ball is trapped inside a large box, the particle can move at "
"any speed within the box and it is no more likely to be found at one position than another. However, when the well becomes very narrow (on the scale of a few nanometers), quantum"
" effects become important and so the particle may only occupy certain energy levels given. The normalized wavefunction is given by:")
        self.textlefth.grid(column= 0, columnspan=3, row=0)


        #add gif in the right hand side column which is an equarion.
        self.photo = PhotoImage(file="wavefuncinfinite.gif")
        #InputFrame2 tells the program to place the gif in the right hand column of the program.
        self.photoloc = Label(self.InputFrameDesc, image=self.photo)
        #This tells the program which row to place the picture in.
        self.photoloc.grid(column=0, columnspan=5, row=1)



        #Entry Boxes
        self.entn = Scale(self.InputFrame, from_=1, to=10, orient=HORIZONTAL)
        self.entn.grid(column = 1, row = 0)



        self.button = Button(frame,text="?",command=self.writeB1)#creates the first button changing the colour. the command is put in which will later be defined
        self.button.grid(column = 2, row = 0)

        self.butPlot = Button(self.InputFrame, text ='PLOT', command = self.calcPattern)# pressing the button runs the method calcPattern
        self.butPlot.grid(column = 0, row = 1)

    def writeB1(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of n. This is so the wavefunction can be compared to either the probability"
" distribution of the 1-D infinite square well or the wavefunction of the 1-D harmonic oscillator. Each time you press plot, the graph will be re-set to the corresponding wavefunction for a given n.")

    def calcPattern(self):
        self.n = int(self.entn.get())#.get returns a string from that object

        self.x = linspace(0, 1, 500)
        self.figPlot.clear()


        self.figPlot.plot(self.x, InfinteWave( self.x,self.n), label='Wavefunction for 1-D Infinite Square Well' .format(self.n), color='yellow')

        #Add a legend to display the label.
        self.figPlot.legend(loc="middle right",prop={'size':7})
        #Set the title for the plot
        self.figPlot.set_title('Wavefunction for 1-D Infinite Square Well', size=11)
        #Set the x and y labels
        self.figPlot.set_ylabel(r'$\psi_n(x)$', size=11)
        self.figPlot.set_xlabel('x', size=11)


        # Setting the x-axis major tick's location
        self.figPlot.set_xticks([0,1])
        # Setting the x-axis major tick's label
        self.figPlot.set_xticklabels(['0','L'])
        self.figPlot.set_yticks([0,3])
        # Setting the x-axis major tick's label
        self.figPlot.tick_params(labelright=True)
        self.figPlot.set_yticklabels(['',r'$\infty$'])

        #Show the plot on the canvas
        self.canvas.show()       #updates the canvas,


class Harmonic:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)
        self.makeInputs(frame)

    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(6,3.5), dpi=100)
        self.figPlot = self.fig.add_subplot(111)
        #The next line is the important bit, you can not just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,3) of the master frame
        self.canvas.get_tk_widget().grid(row = 0, column = 3)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 3)

    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        self.InputFrame = Frame(frame)
        self.InputFrameDesc = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        self.InputFrame.grid(column = 0, row = 0)
        self.InputFrameDesc.grid(column = 4, row = 0)
        #the lables
        self.lbln = Label(self.InputFrame, text = "n=0,1,2,..", justify=LEFT)
        self.lbln.grid(column= 0,row= 0)

        self.textleftgraph = StringVar()
        self.textlefth = Label(self.InputFrameDesc, textvariable = self.textleftgraph, wraplength=300)
        self.textleftgraph.set("The quantum harmonic oscillator is one of the foundation problems of quantum mechanics. It can be applied rather directly to the explanation"
"of the vibration spectra of diatomic molecules, but has implications far beyond such simple systems. It is the foundation for the understanding of complex modes of vibration"
" in larger molecules, the motion of atoms in a solid lattice, the theory of heat capacity, etc. The wavefunctions for the quantum harmonic oscillator contain the Gaussian"
            " form which allows them to satisfy the necessary boundary conditions at infinity. The wave function of it is:")
        self.textlefth.grid(column= 0, columnspan=3, row=0)


        #add gif in the right hand side column which is an equarion.
        self.photo = PhotoImage(file="harmwav.gif")
        #InputFrame2 tells the program to place the gif in the right hand column of the program.
        self.photoloc = Label(self.InputFrameDesc, image=self.photo)
        #This tells the program which row to place the picture in.
        self.photoloc.grid(column=0, columnspan=3, row=1)



        #Entry Boxes
        self.entn = Scale(self.InputFrame, from_=0, to=10, orient=HORIZONTAL)
        self.entn.grid(column = 1, row = 0)

        self.button = Button(frame,text="?", fg="red",command=self.writeB1)#creates the first button changing the colour. the command is put in which will later be defined
        self.button.grid(column = 2, row = 0)
        #A button!
        #I have used the co-ord (0,9) just to show that it will auto remove blank rows/columns
        self.butPlot = Button(self.InputFrame, text ='PLOT', command = self.calcPattern)# pressing the button runs the method calcPattern
        self.butPlot.grid(column = 0, row = 1)



    def writeB1(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of n. This is so the wavefunction can be compared to either the probability"
" distribution of the 1-D harmonic oscillator or the wavefunction of the infinte square well. Each time you press plot, the graph will be re-set to the corresponding wavefunction for a given n.")

    def calcPattern(self):
        self.n = int(self.entn.get())#.get returns a string from that object

        self.x = linspace(-10, 10, 500)
        self.figPlot.clear()


        self.figPlot.plot(self.x, HarmonicWave(self.x, self.n), label='Wavefunction for 1-D Harmonic Oscillator' .format(self.n), color='blue')

        #Add a legend to display the label.
        self.figPlot.legend(loc="middle right",prop={'size':7})
        #Set the title for the plot
        self.figPlot.set_title('Wavefunction for 1-D Harmonic Oscillator',size=11)
        #Set the x and y labels
        self.figPlot.set_ylabel(r'$\psi_n(x)$', size=11)
        self.figPlot.set_xlabel('x', size=11)


        self.figPlot.spines['right'].set_color('none')
        self.figPlot.spines['top'].set_color('none')
        self.figPlot.xaxis.set_ticks_position('bottom')
        self.figPlot.spines['bottom'].set_position(('data', 0))
        self.figPlot.yaxis.set_ticks_position('left')
        self.figPlot.spines['left'].set_position(('data', 0))


        self.figPlot.set_xticks([-10,10])
        # Setting the x-axis major tick's label
        self.figPlot.set_xticklabels(['','x'])

        self.figPlot.set_yticks([0,2])
        # Setting the x-axis major tick's label

        self.figPlot.set_yticklabels(['',r'$\psi_n(x)$'])

        #Show the plot on the canvas
        self.canvas.show()       #updates the canvas,


class InfiniteSqWellSQ:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)
        self.makeInputs(frame)

    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(6,3.5), dpi=100)
        self.figPlot = self.fig.add_subplot(111)
        #The next line is the important bit, you can not just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,1) of the master frame
        self.canvas.get_tk_widget().grid(row = 0, column = 3)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 3)

    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        self.InputFrame = Frame(frame)
        self.InputFrameDesc = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        self.InputFrame.grid(column = 0, row = 0)
        self.InputFrameDesc.grid(column = 4, row = 0)
        #the lables
        self.lbln = Label(self.InputFrame, text = "n=0,1,2,..", justify=LEFT)
        self.lbln.grid(column= 0,row= 0)

        self.textleftgraph = StringVar()
        self.textlefth = Label(self.InputFrameDesc, textvariable = self.textleftgraph, wraplength=300)
        self.textleftgraph.set("For the particle in a box with infinite walls, the probability must be equal to one for finding it within the box. The condition for normalization is then")
        self.textlefth.grid(column= 0, columnspan=4, row=0)

        #add gif in the right hand side column which is an equarion.
        self.photo = PhotoImage(file="wavefunsq.gif")
        #InputFrame2 tells the program to place the gif in the right hand column of the program.
        self.photoloc = Label(self.InputFrameDesc, image=self.photo)
        #This tells the program which row to place the picture in.
        self.photoloc.grid(column=0, columnspan=5, row=1)

        #Entry Boxes
        self.entn = Scale(self.InputFrame, from_=1, to=10, orient=HORIZONTAL)
        self.entn.grid(column = 1, row = 0)

        self.button = Button(frame,text="?", fg="red",command=self.writeB1)#creates the first button changing the colour. the command is put in which will later be defined
        self.button.grid(column = 2, row = 0)

        #A button!
        #I have used the co-ord (0,9) just to show that it will auto remove blank rows/columns
        self.butPlot = Button(self.InputFrame, text ='PLOT', command = self.calcPattern)# pressing the button runs the method calcPattern
        self.butPlot.grid(column = 0, row = 9)

    def writeB1(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of n. This is so the probability distribution can be compared to either the wavefunction"
" of the infinite square well or the probability distribution of the 1-D harmonic Oscillator. Each time you press plot, the graph will be re-set to the corresponding wavefunction for a given n.")


    def calcPattern(self):
        self.n = int(self.entn.get())#.get returns a string from that object

        self.x = linspace(0, 1, 500)
        self.figPlot.clear()


        self.figPlot.plot(self.x, InfinteWaveSQ( self.x,self.n), label='Probability density for 1-D Infinite Square Well' .format(self.n), color='green')

        #Add a legend to display the label.
        self.figPlot.legend(loc="middle right",prop={'size':7})
        #Set the title for the plot
        self.figPlot.set_title('Probability density for 1-D Infinite Square Well', size=11)
        #Set the x and y labels
        self.figPlot.set_ylabel(r'$\psi_n(x)$', size=11)
        self.figPlot.set_xlabel('x', size=11)


        # Setting the x-axis major tick's location
        self.figPlot.set_xticks([0,1])
        # Setting the x-axis major tick's label
        self.figPlot.set_xticklabels(['0','L'])
        self.figPlot.set_yticks([0,3])
        # Setting the x-axis major tick's label
        self.figPlot.tick_params(labelright=True)
        self.figPlot.set_yticklabels(['',r'$\infty$'])

        #Show the plot on the canvas
        self.canvas.show()       #updates the canvas,


class HarmonicSQ:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)
        self.makeInputs(frame)

    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(6,3.5), dpi=100)
        self.figPlot = self.fig.add_subplot(111)
        #The next line is the important bit, you can not just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,1) of the master frame
        self.canvas.get_tk_widget().grid(row = 0, column = 3)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 3)

    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        self.InputFrame = Frame(frame)
        self.InputFrameDesc = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        self.InputFrame.grid(column = 0, row = 0)
        self.InputFrameDesc.grid(column = 4, row = 0)
        #the lables
        self.lbln = Label(self.InputFrame, text = "n=0,1,2,..", justify=LEFT)
        self.lbln.grid(column= 0,row= 0)

        self.textleftgraph = StringVar()
        self.textlefth = Label(self.InputFrameDesc, textvariable = self.textleftgraph, wraplength=300)
        self.textleftgraph.set("For the quantum harmonic oscillator, the square of the wavefunction gives the probability of finding the oscillator at a particular value of "
"x. Note that there is a finite probability that the oscillator will be found outside the potential well indicated by the smooth curve. This is forbidden in classical physi"
    "cs and can be seen by:")
        self.textlefth.grid(column= 0, columnspan=5, row=0)


        #add gif in the right hand side column which is an equarion.
        self.photo = PhotoImage(file="harmopic.gif")
        #InputFrame2 tells the program to place the gif in the right hand column of the program.
        self.photoloc = Label(self.InputFrameDesc, image=self.photo)
        #This tells the program which row to place the picture in.
        self.photoloc.grid(column=0, columnspan=5, row=1)

        #Entry Boxes
        self.entn = Scale(self.InputFrame, from_=0, to=10, orient=HORIZONTAL)
        self.entn.grid(column = 1, row = 0)

        self.button = Button(frame,text="?", fg="red",command=self.writeB1)#creates the first button changing the colour. the command is put in which will later be defined
        self.button.grid(column = 2, row = 0)

        #A button!
        #I have used the co-ord (0,9) just to show that it will auto remove blank rows/columns
        self.butPlot = Button(self.InputFrame, text ='PLOT', command = self.calcPattern)# pressing the button runs the method calcPattern
        self.butPlot.grid(column = 0, row = 9)

    def writeB1(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of n. This is so the probability distribution can be compared to either the wavefunction"
" of the harmonic oscillator or the probability distribution of the infinite  square well. Each time you press plot, the graph will be re-set to the corresponding wavefunction for a given n.")


    def calcPattern(self):
        self.n = int(self.entn.get())#.get returns a string from that object

        self.x = linspace(-10, 10, 500)
        self.figPlot.clear()


        self.figPlot.plot(self.x, HarmonicWaveSQ(self.x, self.n), label='Probability density for a 1-D Harmonic Oscillator' .format(self.n), color='red')

        #Add a legend to display the label.
        self.figPlot.legend(loc="middle right",prop={'size':7})
        #Set the title for the plot
        self.figPlot.set_title('Probability density for a 1-D Harmonic Oscillator',size=11)
        #Set the x and y labels
        self.figPlot.set_ylabel(r'$\psi_n(x)$', size=11)
        self.figPlot.set_xlabel('x', size=11)


        self.figPlot.spines['right'].set_color('none')
        self.figPlot.spines['top'].set_color('none')
        self.figPlot.xaxis.set_ticks_position('bottom')
        self.figPlot.spines['bottom'].set_position(('data', 0))
        self.figPlot.yaxis.set_ticks_position('left')
        self.figPlot.spines['left'].set_position(('data', 0))


        self.figPlot.set_xticks([-10,10])
        # Setting the x-axis major tick's label
        self.figPlot.set_xticklabels(['','x'])

        self.figPlot.set_yticks([0,2])
        # Setting the x-axis major tick's label

        self.figPlot.set_yticklabels(['',r'$\psi_n(x)$'])

        #Show the plot on the canvas
        self.canvas.show()       #updates the canvas,


class CLassicalProb:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)
        self.makeInputs(frame)

    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(7,5), dpi=100)
        self.figPlot = self.fig.add_subplot(111)
        #The next line is the important bit, you can not just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,1) of the master frame
        self.canvas.get_tk_widget().grid(row = 0, column = 3)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 3)

    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        self.InputFrame = Frame(frame)
        self.InputFrameDesc = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        self.InputFrameDesc.grid(column = 4, row = 0)
        self.InputFrame.grid(column = 0, row = 0)
        #the lables
        self.lbln = Label(self.InputFrame, text = "n=0,1,2,..", justify=LEFT)
        self.lbln.grid(column= 0,row= 0)

        self.textleftgraph = StringVar()
        self.textlefth = Label(self.InputFrameDesc, textvariable = self.textleftgraph, wraplength=300)
        self.textleftgraph.set("For the quantum harmonic oscillator, the square of the wavefunction gives the probability of finding the oscillator at a particular value of "
"x. Note that there is a finite probability that the oscillator will be found outside the potential well indicated by the smooth curve. This is forbidden in classical physi"
    "cs and can be seen by:")
        self.textlefth.grid(column= 0, columnspan=5, row=0)


        #add gif in the right hand side column which is an equarion.
        self.photo = PhotoImage(file="harmopic.gif")
        #InputFrame2 tells the program to place the gif in the right hand column of the program.
        self.photoloc = Label(self.InputFrameDesc, image=self.photo)
        #This tells the program which row to place the picture in.
        self.photoloc.grid(column=0, columnspan=5, row=1)

        #Entry Boxes
        self.entn = Scale(self.InputFrame, from_=0, to=25, orient=HORIZONTAL)
        self.entn.grid(column = 1, row = 0)

        self.button = Button(frame,text="?", fg="red",command=self.writeB1)#creates the first button changing the colour. the command is put in which will later be defined
        self.button.grid(column = 2, row = 0)

        #A button!
        #I have used the co-ord (0,9) just to show that it will auto remove blank rows/columns
        self.butPlot = Button(self.InputFrame, text ='PLOT', command = self.calcPattern)# pressing the button runs the method calcPattern
        self.butPlot.grid(column = 0, row = 1)

    def writeB1(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of n to compare the classical and quantum probability distribution of the 1-D harmonic"
"Oscillator can be compared Each time you press plot, the graph will be re-set to the corresponding wavefunction for a given n.")


    def calcPattern(self):
        self.n = int(self.entn.get())#.get returns a string from that object

        self.x = linspace(-10, 10, 500)
        self.figPlot.clear()



        self.figPlot.plot(self.x, ClassicHarmonicSq(self.x, self.n), label='Quantum Probability distribution for 1-D Harmonic Oscillator' .format(self.n), color='yellow')
        self.figPlot.plot(self.x, HarmonicWaveSQ(self.x, self.n), label='Classical Probability distribution for 1-D Harmonic Oscillator' .format(self.n), color='green')

        #Add a legend to display the label.
        self.figPlot.legend(loc="middle right",prop={'size':7})
        #Set the title for the plot
        self.figPlot.set_title('Comparison of classical and quantum distribution for 1-D Harmonic Oscillator',size=11)
        #Set the x and y labels
        self.figPlot.set_ylabel(r'$\psi_n(x)$', size=11)
        self.figPlot.set_xlabel('x', size=11)




        self.figPlot.set_xticks([-10,10])
        # Setting the x-axis major tick's label
        self.figPlot.set_xticklabels(['-'r'$\infty$',r'$\infty$'])
        self.figPlot.set_yticks([0,3])
        # Setting the x-axis major tick's label

        self.figPlot.set_yticklabels(['',r'E$\_n$'])



        self.canvas.show()       #updates the canvas,


class InfinitePotentialEnergy:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)
        self.makeInputs(frame)

    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(6,3.5), dpi=100)
        self.figPlot = self.fig.add_subplot(111)
        #The next line is the important bit, you can not just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,1) of the master frame
        self.canvas.get_tk_widget().grid(row = 0, column = 3)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 3)

    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        self.InputFrame = Frame(frame)
        self.InputFrameDesc = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        self.InputFrame.grid(column = 0, row = 0)
        self.InputFrameDesc.grid(column = 4, row = 0)
        #the lables
        self.lbln = Label(self.InputFrame, text = "n=1,2,..", justify=LEFT)
        self.lbln.grid(column= 0,row= 0)
        self.lblm = Label(self.InputFrame, text = "m=1,2,..", justify=LEFT)
        self.lblm.grid(column= 0,row= 1)
        self.lblL = Label(self.InputFrame, text = "L=0,1,2,..", justify=LEFT)
        self.lblL.grid(column= 0,row= 2)

        self.textleftgraph = StringVar()
        self.textlefth = Label(self.InputFrameDesc, textvariable = self.textleftgraph, wraplength=300)
        self.textleftgraph.set("This page was made to demonstrate the difference between the magnitued of the energy levels of both quantum systems. "
                               "The quantised energy levels for the 1-D Infinite Square Well is given by:")
        self.textlefth.grid(column= 0, columnspan=3, row=0)


        #add gif in the right hand side column which is an equarion.
        self.photo = PhotoImage(file="wellen.gif")
        #InputFrame2 tells the program to place the gif in the right hand column of the program.
        self.photoloc = Label(self.InputFrameDesc, image=self.photo)
        #This tells the program which row to place the picture in.
        self.photoloc.grid(column=0, columnspan=5, row=1)

        #Entry Boxes
        self.entn = Scale(self.InputFrame, from_=1, to=10, orient=HORIZONTAL)
        self.entn.grid(column = 1, row = 0)
        self.entm = Scale(self.InputFrame, from_=1, to=10, orient=HORIZONTAL)
        self.entm.grid(column = 1, row = 1)
        self.entL = Scale(self.InputFrame, from_=1, to=10, orient=HORIZONTAL)
        self.entL.grid(column = 1, row = 2)


        self.button1 = Button(frame,text="?", fg="red",command=self.writeB1)#creates the first button changing the colour. the command is put in which will later be defined
        self.button1.grid(column = 2, row = 0)
        self.button2= Button(frame,text="?", fg="red",command=self.writeB2)#creates the first button changing the colour. the command is put in which will later be defined
        self.button2.grid(column = 2, row = 1)
        self.button3 = Button(frame,text="?", fg="red",command=self.writeB3)#creates the first button changing the colour. the command is put in which will later be defined
        self.button3.grid(column = 2, row = 2)




        #A button!
        #I have used the co-ord (0,9) just to show that it will auto remove blank rows/columns
        self.butPlot = Button(self.InputFrame, text ='PLOT', command = self.calcPattern)# pressing the button runs the method calcPattern
        self.butPlot.grid(column = 0, row = 3)

    def writeB1(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of n corresponding to the energy levels")
    def writeB2(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of m which is the mass of the particle")


    def writeB3(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of L so that the user has more variables to change for a corresponding energy.")


    def calcPattern(self):
        self.n = int(self.entn.get())#.get returns a string from that object
        self.m = int(self.entm.get())
        self.L = int(self.entL.get())

        self.x = linspace(-10, 10, 500)
        self.figPlot.clear()


        self.figPlot.plot(self.x, InfinitePotEnergy1(self.x, self.n,self.m,self.L), label='Energy for Infinite Square Well for n' .format(self.n), color='blue')

        #Add a legend to display the label.
        self.figPlot.legend(loc="middle right",prop={'size':7})
        #Set the title for the plot
        self.figPlot.set_title('Energy for Infinite Square Well',size=11)
        #Set the x and y labels
        self.figPlot.set_ylabel('E'r'$\_n(x)$', size=11)
        self.figPlot.set_xlabel('', size=11)

        self.figPlot.set_xticks([-10,10])
        # Setting the x-axis major tick's label
        self.figPlot.set_xticklabels(['',''])



        self.canvas.show()       #updates the canvas,


class HarmonicOscillatorEn:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)
        self.makeInputs(frame)

    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(6,3.5), dpi=100)
        self.figPlot = self.fig.add_subplot(111)
        #The next line is the important bit, you can not just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,1) of the master frame
        self.canvas.get_tk_widget().grid(row = 0, column = 3)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 3)

    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        self.InputFrame = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        self.InputFrameDesc = Frame(frame)
        self.InputFrame.grid(column = 0, row = 0)
        self.InputFrameDesc.grid(column = 4, row = 0)
        #the lables
        self.lbln = Label(self.InputFrame, text = "n=0,1,2,..", justify=LEFT)
        self.lbln.grid(column= 0,row= 0)
        self.lblomega = Label(self.InputFrame, text = "Omega=0,1,..", justify=LEFT)
        self.lblomega.grid(column= 0,row= 1)

        self.textleftgraph = StringVar()
        self.textlefth = Label(self.InputFrameDesc, textvariable = self.textleftgraph, wraplength=300)
        self.textleftgraph.set("The quantised energy levels for the 1-D harmonic oscillator is given by:")
        self.textlefth.grid(column= 0, columnspan=3, row=0)


        #add gif in the right hand side column which is an equarion.
        self.photo = PhotoImage(file="harmen.gif")
        #InputFrame2 tells the program to place the gif in the right hand column of the program.
        self.photoloc = Label(self.InputFrameDesc, image=self.photo)
        #This tells the program which row to place the picture in.
        self.photoloc.grid(column=0, columnspan=5, row=1)

        #Entry Boxes
        self.entn = Scale(self.InputFrame, from_=0, to=30, orient=HORIZONTAL)
        self.entn.grid(column = 1, row = 0)
        self.entomega = Scale(self.InputFrame, from_=1, to=100, orient=HORIZONTAL)
        self.entomega.grid(column = 1, row = 1)

        self.button1 = Button(frame,text="?", fg="red",command=self.writeB1)#creates the first button changing the colour. the command is put in which will later be defined
        self.button1.grid(column = 2, row = 0)
        self.button2= Button(frame,text="?", fg="red",command=self.writeB2)#creates the first button changing the colour. the command is put in which will later be defined
        self.button2.grid(column = 2, row = 1)


        #A button!
        #I have used the co-ord (0,9) just to show that it will auto remove blank rows/columns
        self.butPlot = Button(self.InputFrame, text ='PLOT', command = self.calcPattern)# pressing the button runs the method calcPattern
        self.butPlot.grid(column = 0, row = 9)


    def writeB1(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of n corresponding to the energy levels"
"I initially wanted to add a function for m so that the two energy values could be compared however I didnt have enough time to implement this feature.")
    def writeB2(self):#I then used the same type of code but changed the name of it so that it would correspond to the second button and so on
        return msg.showinfo("info","This slider lets the user chose different values of omega so that the user has more variables to change for a corresponding energy."
"omega corresponds to angular frequency")


    def calcPattern(self):
        self.n = int(self.entn.get())

        self.omega = int(self.entomega.get())

        self.x = linspace(-10, 10, 500)
        self.figPlot.clear()


        self.figPlot.plot(self.x, HarmonicOscillatorEnergy1(self.x, self.n,self.omega), label='Energy for Infinite Square Well' .format(self.n), color='blue')


        #Add a legend to display the label.
        self.figPlot.legend(loc="center right",prop={'size':7})
        #Set the title for the plot
        self.figPlot.set_title('Energy levels for Quantum Harmonic Oscillator',size=11)
        #Set the x and y labels
        self.figPlot.set_ylabel('E'r'$\_n(x)$', size=11)
        self.figPlot.set_xlabel('', size=11)

        self.figPlot.set_xticks([-10,10])
        # Setting the x-axis major tick's label
        self.figPlot.set_xticklabels(['',''])



        self.canvas.show()       #updates the canvas,


def main():
    plt.show()
    root = Tk()
    app = homePage(root)
    text = Text(root)
#run the main loop
    root.mainloop() #this is closed by the user closing the tk window.
    root.destroy()

if __name__ == '__main__':
    main()
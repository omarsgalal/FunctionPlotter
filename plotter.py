import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class Plotter:
    """
    This class is for plotting user defined functions
    """

    def __init__(self,  window):
        """
        the class constructor puts all necessary widgits in a tkinter window

        Parameters:
        -----------
        window: tkinter object
        """
        self.window = window

        # create a the user defined function box and label
        self.functionBox = Entry(window)
        self.functionLabel = Label(window, text='Enter your function here')


        # create a box and label for minimum x value
        self.minXBox = Entry(window)
        self.minXLabel = Label(window, text='Enter min of x')

        # create a box and label for maximum x value
        self.maxXBox = Entry(window)
        self.maxXLabel = Label(window, text='Enter max of x')

        # create a button for plotting
        self.button = Button (window, text="plot", command=self.plot)


        # packing widgets
        self.functionLabel.pack()
        self.functionBox.pack()

        self.minXLabel.pack()
        self.minXBox.pack()

        self.maxXLabel.pack()
        self.maxXBox.pack()

        self.button.pack()
        self.canvas = None
       

    def plot (self):
        """
        This function gets called when the plot button gets triggered
        """
        func = self.functionBox.get().replace('^', '**')
        minX, maxX = self.validateMinMax(self.minXBox.get(), self.maxXBox.get())

        X, y = self.evaluateFunction(func, minX, maxX)

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(X, y,color='blue')

        a.set_title ("Function Plot", fontsize=16)
        a.set_ylabel("y", fontsize=14)
        a.set_xlabel("x", fontsize=14)

        try: 
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError: 
            pass                
        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()


    def evaluateFunction (self, funciton, minX, maxX):
        """
        This function validates user input function and evaluate it for plotting

        Parameters
        ----------
        function: string with the user defined function
        minX: float with minimum value of x
        maxX: float with maximum value of x

        Returns
        -------
        tuple of two numpy arrays X, y where X contains values on x-axis
        and y contains values on y-axis
        """
        try:
            step = (maxX - minX) / 500
            X = np.array([i for i in np.arange(minX, maxX, step)])
            y = np.array([eval(funciton, {"x": i}) for i in np.arange(minX, maxX, step)])
            return X, y
        except SyntaxError:
            messagebox.showinfo("Function Syntax Error", "Please type a valid function")
        except ZeroDivisionError:
            messagebox.showinfo("Divide By Zero Error", "Can't divide by zero")
        except NameError:
            messagebox.showinfo("Check variable x", "The only variable that can exist is x")
        except:
            messagebox.showinfo("Error", "Check that you wrote a valid function and valid inputs")


    def validateMinMax (self, minX, maxX):
        """
        This function validates user input on min and max values of x

        Parameters
        ----------
        minX: string with min value of x
        maxX: string with max value of x

        Returns
        -------
        tuple with minX and maxX as floats
        """
        try:
            minX = float(minX)
            maxX = float(maxX)
            if maxX <= minX:
                messagebox.showinfo("Min Max Error", "Max must be greater than Min")
            else:
                return minX, maxX
        except:
            messagebox.showinfo("Min Max Error", "Min and Max values of x must be valid float numbers")


window= Tk()
window.title("Plotter")
window.geometry('700x750')
start= Plotter (window)
window.mainloop()
import tkinter as tk
import tkinter.ttk as ttk
import tkinter

  
# class Frame
class Frame:
    # main method
    def main():  

        # reset method for reset button
        def reset():
            weightvar.set("")
            heightvar.set("")
            BMI.config(text = "")
            result.config(text = "", background="SystemButtonFace")


        # calculate method to display message box on calculate button click
        def calculate():
            # getting values from entry and converting them to float
            w = float(weightvar.get())
            h = float(heightvar.get())

            # applying BMI formula
            bmi = round((w/h/h)*10000, 2)

            # displaying bmi in label
            BMI.config(text = bmi)

            # condition statements for bmi 
            # and displaying result in label with different colors
            if bmi > 0 and bmi <= 18.5:
                result.config(text= "You are UNDERWEIGHT!",background = "blue")
            elif bmi >18.5 and bmi < 25:
                result.config(text= "You are HEALTHY!",background = "green")
            elif bmi >= 25 and bmi < 30:
                result.config(text= "You are OVERWEIGHT!", background= "yellow")
            elif bmi >= 30 and bmi < 40:
                result.config(text= "You are OBESE!",background = "orange")
            elif bmi >= 40:
                result.config(text= "You are EXTREME OBESE!", background = "red")


            

        # initialising frame
        frame = tkinter.Tk()   
        frame.title('BMI Calculator')
        frame.geometry("350x300") 

        # initializing control variables
        weightvar = tk.StringVar()
        heightvar = tk.StringVar()
        

        # initializing controls with alignment
        title = ttk.Label(frame,text = "Welcome to the BMI Calculator!", font = "Helvetica 16 bold").place(x = 15,  y = 15)

        # the label for height 
        height = ttk.Label(frame,text = "Height(cm)").place(x = 40,  y = 60)  
            
        # the label for weight  
        weight = ttk.Label(frame,text = "Weight(kg)").place(x = 40, y = 90)  

        # a normal label to display text
        display = ttk.Label(frame,text = "Your BMI is").place(x = 145, y = 180)  

        # result labels where results will be displayed. They have no text initially
        # placing them in center using anchor='center'
        BMI = ttk.Label(frame,text = "",font = "Helvetica 18 bold")
        BMI.place(relx=0.5, rely=0.725, anchor='center')
        result = ttk.Label(frame,text = "",font = "Helvetica 16 bold")
        result.place(relx=0.5, rely=0.85, anchor='center')  
            
        weightEntry = tk.Entry(frame,width = 20, textvariable = weightvar)
        weightEntry.place(x = 150,y = 90) 
        heightEntry = tk.Entry(frame,width = 20, textvariable = heightvar)
        heightEntry.place(x = 150,y = 60)


        # reset/ clear button
        reset = tk.Button(frame,text = "Clear", width=20, command=reset,fg = "blue").place(x = 100,y = 150)

        # calculate button
        calculate = tk.Button(frame,text = "Calculate", width=20,fg = "blue", command=calculate).place(x = 100,y = 120) 
        


        # running the mainloop for tkinter
        frame.mainloop() 

    # calling the main method
    if __name__ == "__main__":
        main()
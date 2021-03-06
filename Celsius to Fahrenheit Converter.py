from tkinter import *
import tkinter.font as font


# Function to Convert Celsius to Fahrenheit
def convert():
    temp_celsius = celsius_value.get()

    if temp_celsius.replace('.', '', 1).isdigit():
        error_msg.grid_forget()
        temp_fahrenheit = (float(temp_celsius) * 9/5) + 32
        output_fahrenheit.config(text='Temperature in Fahrenheit : ' + str(temp_fahrenheit))

    else:
        error_msg.grid(row=1, column=1)


#def onReturn(event):
    #print("Return Pressed")


my_window = Tk()
my_window.title("Celsius to Fahrenheit Converter")

# Displaying the heading inside window
description = Label(text='Celsius ---> Fahrenheit', font=font.Font(size=20), fg='black')
description.pack()

frame = Frame(my_window)
frame.pack(pady=20)

# Entry box to enter temperature in celsius
message_one = Label(frame, text='Enter Temperature in Celsius: ', font=font.Font(size=12))
message_one.grid(row=0, column=0)

celsius_value = Entry(frame)
celsius_value.grid(row=0, column=1)

# To display error message
error_msg = Label(frame, text='Please enter valid input...', font=font.Font(size=8), fg='red')

# To display the output
output_fahrenheit = Label(frame, font=font.Font(size=12))
output_fahrenheit.grid(row=2, column=0, columnspan=2, pady=10)

# Submit button

submit_btn = Button(frame, text='Convert', font=font.Font(size=15), width=20, fg='black', bg='tomato', bd=0, padx=10, pady=15,
                    command=convert)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)
#submit_btn.bind("<Return>", onReturn)


my_window.geometry('500x250')
my_window.mainloop()


### CREATED BY : MuhammadRahim
### Telegram : @OnlyAero
### Github : github.com/AeroOnLy

### Tools : Calculator Bitwise Operation using Python 

import tkinter as tk

mainWindow = tk.Tk()
mainWindow.geometry('500x700')
mainWindow.resizable(0,0)
mainWindow.config(bg = 'gray5')
mainWindow.title("Calculator - Bitwise Operator")


# dev
dev = tk.Label(mainWindow,text='Muhammad Rahim 21.83.0643\nPemrograman Python' , font='candara 12 bold', fg= 'spring green', bg='grey5')
dev.pack(padx=10, pady=10)

# Label 1
label_1 = tk.Label(mainWindow,text='╔════════════════╗\n- CALCULATOR - BITWISE OPERATOR -\n╚════════════════╝' , font='candara 18 bold', bg="grey5" ,fg='spring green')
label_1.pack(padx=10, pady=2)
# Label 2
label_2 = tk.Label(mainWindow,text = '&  Bitwise AND  &\n|  Bitwise OR  |\n^  Bitwise XOR  ^\n~  Bitwise NOT  ~', font='candara 18 bold', bg="grey5" ,fg='spring green')
label_2.pack(padx=10, pady=8,)
# Label 3 First Input
label_3 = tk.Label(mainWindow,text = 'Please, Enter the First Number:', font='candara 15 bold', fg= 'spring green', bg='grey5')
label_3.pack(padx=10, pady=5,)
first_input = tk.Entry(mainWindow , font='arial 15', width=40, bg='dark sea green')
first_input.pack(padx=10, pady=2,)
# Label 4 Second Input
label_4 = tk.Label(mainWindow,text = 'Please, Enter the Second Number:', font='candara 15 bold', fg= 'spring green', bg='grey5')
label_4.pack(padx=10, pady=5,)
second_input = tk.Entry(mainWindow , font='arial 15', width=40, bg='dark sea green')
second_input.pack(padx=10, pady=2,)
# Label Operator
label_operation = tk.Label(mainWindow,text="BITWISE OPERATION", font='candara 15 bold', fg= 'spring green', bg='grey5')
label_operation.pack(padx=10, pady=15,)

label_operation = tk.Label(mainWindow,text="= _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ =", font='candara 15 bold', bg="grey5" ,fg='spring green')
label_operation.pack(side=tk.BOTTOM, expand=True)

def bit_and():
    number_1 = int(first_input.get())
    number_2 = int(second_input.get())
    result = number_1 & number_2
    result_label.config(text="--- RESULT ---\n" +str(result))

def bit_or():
    number_1 = int(first_input.get())
    number_2 = int(second_input.get())
    result = number_1 | number_2
    result_label.config(text="--- RESULT ---\n" +str(result))

def bit_xor():
    number_1 = int(first_input.get())
    number_2 = int(second_input.get())
    result = number_1 ^ number_2
    result_label.config(text="--- RESULT ---\n" +str(result))

def bit_not():
    number_1 = int(first_input.get())
    number_2 = int(second_input.get())
    result = ~ number_1
    result_label.config(text="--- RESULT ---\n" +str(result))


ipadding = {'ipadx': 10, 'ipady': 10}
# Addition Button
addition_button = tk.Button(mainWindow, text="AND", font='arial 10 bold', width=10, height=1, padx='3', bg='dark sea green', command=lambda:bit_and()).place(x=52 , y=490)

# Subtract Button
subtract_button = tk.Button(mainWindow, text="OR", font='arial 10 bold', width=10, height=1, padx='3', bg='dark sea green', command=lambda:bit_or()).place(x=152 , y=490)

# Multiply Button
multiply_button = tk.Button(mainWindow, text="XOR", font='arial 10 bold', width=10, height=1, padx='3', bg='dark sea green', command=lambda:bit_xor()).place(x=252 , y=490)

# Divide Button
divide_button = tk.Button(mainWindow, text="NOT", font='arial 10 bold', width=10, height=1, padx='3', bg='dark sea green', command=lambda:bit_not()).place(x=352 , y=490)

# Result or Output
result_label = tk.Label(mainWindow, text="--- RESULT ---\n", font='arial 15 bold', fg='spring green', bg='grey5')
result_label.pack(anchor=tk.CENTER, expand=True)

mainWindow.mainloop()

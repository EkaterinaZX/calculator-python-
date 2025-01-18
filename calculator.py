from tkinter import*
import math

window = Tk()

window.title('Calculator')
window.geometry('300x300+900+50')
window.config(bg='black')

entry = Entry(window, width=10, font=('Arial', 25), bd=10, relief=SOLID, bg='#222222', fg='white', justify='right')
entry.place(x = 60, y = 0)

def input_into_entry(symbol):
    entry.insert(END, symbol)
    


def factorial():
    number = int(entry.get())
    result = math.factorial(number)
    entry.delete(0, END)  
    entry.insert(0, str(result))


def procent():
    number = float(entry.get())  
    result = number / 100  
    entry.delete(0, END)  
    entry.insert(0, str(result))
    



def clear():
    entry.delete(0, END)


def clear_last():
    current_text = entry.get()  
    new_text = current_text[:-1]
    entry.delete(0, END)  
    entry.insert(0, new_text)


def count_result():
    text = entry.get()
    result = None

    

    if '+' in text:
        splitted_text = text.split('+')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first+second
        

    if '-' in text:
        splitted_text = text.split('-')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first-second
        

    if '/' in text:
        splitted_text = text.split('/')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first+second
        if second == 0:
            result = "Ошибка: нельзя "
        else:
            result = first / second

        

    if '*' in text:
        splitted_text = text.split('*')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first*second
    

    clear()
    entry.insert(0, result)


button_style = {'bg': 'black', 'fg': 'white', 'font': ('Arial', 18), 'width': 4, 'height': 2}



btn_umn = Button(window, text = '*', command =lambda : input_into_entry('*'), **button_style)
btn_umn.place(x = 60, y = 50, width = 50, height = 50)

btn_prc = Button(window, text = '%', command = procent, **button_style)
btn_prc.place(x = 110, y = 50, width = 50, height = 50)

btn_fac = Button(window, text = '!', command = factorial, **button_style)
btn_fac.place(x = 160, y = 50, width = 50, height = 50)

btn_del = Button(window, text = 'C', command = clear_last, **button_style)
btn_del.place(x = 210, y = 50, width = 50, height = 50)

btn1 = Button(window, text = '1', command = lambda : input_into_entry('1'), **button_style)
btn1.place(x = 60, y = 100, width = 50, height = 50)

btn2 = Button(window, text = '2', command = lambda : input_into_entry('2'), **button_style)
btn2.place(x = 110, y = 100, width = 50, height = 50)

btn3 = Button(window, text = '3', command = lambda : input_into_entry('3'), **button_style)
btn3.place(x = 160, y = 100, width = 50, height = 50)

btn_plus = Button(window, text = '+', command = lambda : input_into_entry('+'), **button_style)
btn_plus.place(x = 210, y = 100, width = 50, height = 50)

btn4 = Button(window, text = '4', command = lambda : input_into_entry('4'), **button_style)
btn4.place(x = 160, y = 150, width = 50, height = 50)

btn5 = Button(window, text = '5', command = lambda : input_into_entry('5'), **button_style)
btn5.place(x = 60, y = 150, width = 50, height = 50)

btn6 = Button(window, text = '6', command = lambda : input_into_entry('6'), **button_style)
btn6.place(x = 110, y = 150, width = 50, height = 50)

btn_minus = Button(window, text = '-', command = lambda : input_into_entry('-'), **button_style)
btn_minus.place(x = 210, y = 150, width = 50, height = 50)

btn7 = Button(window, text = '7', command = lambda : input_into_entry('7'), **button_style)
btn7.place(x = 60, y = 200, width = 50, height = 50)

btn8 = Button(window, text = '8', command = lambda : input_into_entry('8'), **button_style)
btn8.place(x = 110, y = 200, width = 50, height = 50)

btn9 = Button(window, text = '9', command = lambda : input_into_entry('9'), **button_style)
btn9.place(x = 160, y = 200, width = 50, height = 50)

btn_div = Button(window, text = '/', command = lambda : input_into_entry('/'), **button_style)
btn_div.place(x = 210, y = 200, width = 50, height = 50)

btn_dr = Button(window, text = '.', command = lambda : input_into_entry('.'), **button_style)
btn_dr.place(x = 60, y = 250, width = 50, height = 50)

btn0 = Button(window, text = '0', command = lambda : input_into_entry('0'), **button_style)
btn0.place(x = 110, y = 250, width = 50, height = 50)

btn_result = Button(window, text = '=', command = count_result, **button_style)
btn_result.place(x = 160, y = 250, width = 50, height = 50)

btn_clean = Button(window, text = 'CE', command = clear, **button_style)
btn_clean.place(x = 210, y = 250, width = 50, height = 50)


window.mainloop()
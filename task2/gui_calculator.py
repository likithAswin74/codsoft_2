import tkinter as calc

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    pass


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        
    except:
       clear_field()
       text_result.insert(1.0,"error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass



root=calc.Tk()
root.geometry("300x275")
text_result = calc.Text(root, height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)


button1=calc.Button(root,text="1", background="yellow", command=lambda: add_to_calculation(1), width=5, font=("Arial",14))
button1.grid(row=3, column=1)
button2=calc.Button(root,text="2",background="yellow",command=lambda: add_to_calculation(2),width=5,font=("Arial",14))
button2.grid(row=3,column=2)

button3=calc.Button(root,text="3",background="yellow",command=lambda: add_to_calculation(3),width=5,font=("Arial",14))
button3.grid(row=3,column=3)

button4=calc.Button(root,text="4",background="yellow",command=lambda: add_to_calculation(4),width=5,font=("Arial",14))
button4.grid(row=4,column=1)

button5=calc.Button(root,text="5",background="yellow",command=lambda: add_to_calculation(5),width=5,font=("Arial",14))
button5.grid(row=4,column=2)

button6=calc.Button(root,text="6",background="yellow",command=lambda: add_to_calculation(6),width=5,font=("Arial",14))
button6.grid(row=4,column=3)

button7=calc.Button(root,text="7",background="yellow",command=lambda: add_to_calculation(7),width=5,font=("Arial",14))
button7.grid(row=5,column=1)

button8=calc.Button(root,text="8",background="yellow",command=lambda: add_to_calculation(8),width=5,font=("Arial",14))
button8.grid(row=5,column=2)

button9=calc.Button(root,text="9",background="yellow",command=lambda: add_to_calculation(9),width=5,font=("Arial",14))
button9.grid(row=5,column=3)

button0=calc.Button(root,text="0",background="yellow",command=lambda: add_to_calculation(0),width=5,font=("Arial",14))
button0.grid(row=6,column=2)

buttonplus=calc.Button(root,text="+",background="yellow",command=lambda: add_to_calculation("+"),width=5,font=("Arial",14))
buttonplus.grid(row=3,column=4)

buttonminus=calc.Button(root,text="-",background="yellow",command=lambda: add_to_calculation("-"),width=5,font=("Arial",14))
buttonminus.grid(row=4,column=4)

buttonmul=calc.Button(root, text="*",background="yellow",command=lambda: add_to_calculation("*"),width=5,font=("Arial",14))
buttonmul.grid(row=5,column=4)

buttondiv=calc.Button(root, text="/",background="yellow",command=lambda: add_to_calculation("/"),width=5,font=("Arial",14))
buttondiv.grid(row=6,column=4)

buttonopen=calc.Button(root,text="(",background="yellow",command=lambda: add_to_calculation("("),width=5,font=("Arial",14))
buttonopen.grid(row=6,column=1)

buttonclose=calc.Button(root,text=")",background="yellow",command=lambda: add_to_calculation(")"),width=5,font=("Arial",14))
buttonclose.grid(row=6,column=3)



buttonequal=calc.Button(root,text="=",command=evaluate_calculation,width=5,font=("Arial",14))
buttonequal.grid(row=2,column=3)

buttondot=calc.Button(root,text=".",command=lambda: add_to_calculation("."),width=5,font=("Arial",14))
buttondot.grid(row=2,column=1)

buttonclear=calc.Button(root,text="C",command=clear_field,width=5,font=("Arial",14))
buttonclear.grid(row=2,column=4)

buttont=calc.Button(root,text="%",command=lambda: add_to_calculation("%"),width=5,font=("Arial",14))
buttont.grid(row=2,column=2)

root.mainloop()









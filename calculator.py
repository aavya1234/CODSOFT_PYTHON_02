from tkinter import *
first_num=second_num=operation=None
root=Tk()
root.title("Calculator")
root.geometry('260x400')
root.resizable(False,False)
root.configure(background="black")

result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=40,padx=25)
result_label.config(font=("Arial",30,'bold'))

btn9=Button(root,text='9',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=0)
btn9.config(font=('Arial',14))

btn8=Button(root,text='8',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('Arial',14))

btn7=Button(root,text='7',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=2)
btn7.config(font=('Arial',14))

btn_add=Button(root,text='+',bg='white',fg='black',width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('Arial',14))

btn6=Button(root,text='6',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=0)
btn6.config(font=('Arial',14))

btn5=Button(root,text='5',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('Arial',14))

btn4=Button(root,text='4',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=2)
btn4.config(font=('Arial',14))

btn_subtract=Button(root,text='-',bg='white',fg='black',width=5,height=2,command=lambda:get_operator('-'))
btn_subtract.grid(row=2,column=3)
btn_subtract.config(font=('Arial',14))

btn3=Button(root,text='3',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=0)
btn3.config(font=('Arial',14))

btn2=Button(root,text='2',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('Arial',14))

btn1=Button(root,text='1',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=2)
btn1.config(font=('Arial',14))

btn_multiply=Button(root,text='*',bg='white',fg='black',width=5,height=2,command=lambda:get_operator('*'))
btn_multiply.grid(row=3,column=3)
btn_multiply.config(font=('Arial',14))

btn_clear=Button(root,text='AC',bg='white',fg='black',width=5,height=2,command=lambda:clear())
btn_clear.grid(row=4,column=0)
btn_clear.config(font=('Arial',14))

btn0=Button(root,text='0',bg='white',fg='black',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('Arial',14))

btn_result=Button(root,text='=',bg='white',fg='black',width=5,height=2,command=lambda:get_result())
btn_result.grid(row=4,column=2)
btn_result.config(font=('Arial',14))

btn_divide=Button(root,text='/',bg='white',fg='black',width=5,height=2,command=lambda:get_operator('/'))
btn_divide.grid(row=4,column=3)
btn_divide.config(font=('Arial',14))

def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(operator):
    global first_num,second_num,operation
    current=(result_label['text'])
    if current:
        first_num=int(current)
        operation=operator
        result_label.config(text=f"{first_num}{operation}")
    

def get_result():
    global first_num,second_num,operation
    current=(result_label['text'])
    if operation and current and current!=operation:
        second_num=int(current.split(operation)[1])

        if operation=='+':
            result=first_num+second_num
        elif operation=='-':
            result=first_num-second_num
        elif operation=='*':
            result=first_num*second_num
        elif operation=='/':
            if second_num==0:
                result=0
            else:
                result=round(first_num/second_num,2)
    else:
        result='Error'
    result_label.config(text=str(result))

root.mainloop()

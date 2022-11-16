from tkinter import *
exprsn = ""
class Calculator:
    def click(str1):
        global exprsn
        exprsn = exprsn + str(str1)
        eqn.set(exprsn)


    def delete():
        global exprsn
        exprsn = ""
        eqn.set(exprsn)


    def equal():
        if(True):
            global exprsn
            total = str(eval(exprsn))
            eqn.set(total)
            exprsn = ""
        else:
            eqn.set('error')
            exprsn = ""

if __name__ == '__main__':
            obj1=Calculator
            r = Tk()
            r.title("Calculator")
            eqn = StringVar()
            expression_field = Entry(r, textvariable=eqn)
            expression_field.grid(columnspan=4, ipadx=70)

            button1 = Button(r, text=' 1 ', fg='white', bg='black',command=lambda: obj1.click(1), height=2, width=7)
            button1.grid(row=2, column=0)

            button2 = Button(r, text=' 2 ', fg='white', bg='black',command=lambda: obj1.click(2), height=2, width=7)
            button2.grid(row=2, column=1)

            button3 = Button(r, text=' 3 ', fg='white', bg='black',command=lambda: obj1.click(3), height=2, width=7)
            button3.grid(row=2, column=2)

            button4 = Button(r, text=' 4 ', fg='white', bg='black',command= lambda: obj1.click(4), height=2, width=7)
            button4.grid(row=3, column=0)

            button5 = Button(r, text=' 5 ', fg='white', bg='black',command=lambda: obj1.click(5), height=2 ,width=7)
            button5.grid(row=3, column=1)

            button6 = Button(r, text=' 6 ', fg='white', bg='black',command=lambda: obj1.click(6), height=2, width=7)
            button6.grid(row=3, column=2)

            button7 = Button(r, text=' 7 ', fg='white', bg='black',command=lambda: obj1.click(7), height=2, width=7)
            button7.grid(row=4, column=0)

            button8 = Button(r, text=' 8 ', fg='white', bg='black',command=lambda: obj1.click(8), height=2, width=7)
            button8.grid(row=4, column=1)

            button9 = Button(r, text=' 9 ', fg='white', bg='black',command=lambda: obj1.click(9), height=2, width=7)
            button9.grid(row=4, column=2)

            button0 = Button(r, text=' 0 ', fg='white', bg='black',command=lambda: obj1.click(0), height=2, width=7)
            button0.grid(row=5, column=0)

            addition = Button(r, text=' + ', fg='white', bg='black',command=lambda: obj1.click("+"), height=2, width=7)
            addition.grid(row=2, column=3)

            subtraction = Button(r, text=' - ', fg='white', bg='black',
                           command=lambda: obj1.click("-"), height=2, width=7)
            subtraction.grid(row=3, column=3)

            multiplication = Button(r, text=' x ', fg='white', bg='black',
                              command=lambda: obj1.click("*"), height=2, width=7)
            multiplication.grid(row=4, column=3)

            division = Button(r, text=' / ', fg='white', bg='black',
                            command=lambda: obj1.click("/"), height=2, width=7)
            division.grid(row=5, column=3)

            equal_pre = Button(r, text=' = ', fg='white', bg='black',command=lambda: obj1.equal(), height=2, width=7)
            equal_pre.grid(row=5, column=2)

            clearall = Button(r, text='Clear', fg='white', bg='black',command=lambda: obj1.delete(), height=2, width=7)
            clearall.grid(row=5, column='1')

            Decimal = Button(r, text='.', fg='white', bg='black',command=lambda: obj1.click('.'), height=2, width=7)
            Decimal.grid(row=6, column=0)
            r.mainloop()



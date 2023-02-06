from datetime import datetime
from tkinter import *

counter = 10800
running = False


def counter_label(label):
    def count():
        if running:
            global counter
            tt = datetime.fromtimestamp(counter)
            string = tt.strftime('%H:%M:%S')
            display = f'{string: ^24}'
            label.config(text=display)
            label.after(1000, count)
            counter += 1

    count()


def start(label):
    global running
    running = True
    counter_label(label)


def stop():
    global running
    running = False


def reset():
    global counter
    counter = 10800


if __name__ == '__main__':
    root = Tk()
    root.title('Stopwatch')

    root.minsize(width=250, height=70)
    label = Label(root, text='Welcome!', fg='black', font='Verdana 30 bold')
    label.pack()
    f = Frame(root)
    start = Button(f, text='Start', width=6, command=lambda: start(label))
    stop = Button(f, text='Stop', width=6, command=stop)
    reset = Button(f, text='Reset', width=6, command=reset)
    printer = Button(
        f, text='printer', width=6, command=lambda: print('TESTE')
    )
    f.pack(anchor='center', pady=5)
    start.pack(side='left')
    stop.pack(side='left')
    reset.pack(side='left')
    printer.pack(side='left')
    root.mainloop()

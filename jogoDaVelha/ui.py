from functools import partial
from tkinter import *

import stopwatch as timer
import engine
from config import PATH, colors, images, window


def open_window():
    win = Tk()
    win.title(window['title'])
    win.geometry(window['geometry'])
    win.configure(bg=colors['bg-dark'], padx=10, pady=10)
    win.resizable(width=0, height=0)
    return win


def main_menu(win, arcade, local):
    weight = int(window['width']) // 2
    frame = Frame(win, bg=colors['bg-dark'], name='main_menu')
    frame.columnconfigure(index=0, weight=weight)
    set_image(frame, 'jogo', 0, 0)
    set_menu_buttons(
        frame=frame,
        texts=['Arcade', 'Local'],
        commands=[partial(show_arcade, arcade), partial(show_local, local)],
    )
    set_menu_labels(frame, ['🤖', '😏'], 'blue', W)
    set_menu_labels(frame, ['😏', '😏'], 'red', E)
    set_button_return(arcade, frame, exit_arcade)
    set_button_return(local, frame, exit_local)
    frame.place(x=0, y=0, width=window['width'], height=window['height'])
    return frame


def arcade(win):
    frame = Frame(win, bg=colors['bg-dark'], name='arcade')
    set_score(frame)
    set_grid(frame)
    frame.place(x=0, y=0, width=window['width'], height=window['height'])
    return frame


def local(win):
    frame = Frame(win, bg=colors['bg-dark'], name='local')
    set_score(frame)
    add_player(frame, '❌', 'red', 1, 0)
    add_player(frame, '⭕', 'blue', 2, 2)
    set_grid(frame)
    frame.place(x=0, y=0, width=window['width'], height=window['height'])
    return frame


def show_arcade(frame):
    timer.start(set_label_message(frame))
    frame.tkraise()


def show_local(frame):
    frame.tkraise()


def exit_arcade(frame):
    timer.stop()
    timer.reset()
    frame.tkraise()


def exit_local(frame):
    frame.tkraise()


def on_click(grid_iten, event):
    set_symbol(grid_iten, '❌', 'red')
    desative_enter_leave(grid_iten, None)
    grid_iten.bind(f'<Leave>', partial(desative_enter_leave, grid_iten))
    grid_iten.bind(f'<Enter>', partial(desative_enter_leave, grid_iten))


def on_enter(grid_iten, event):
    grid_iten.config(bg=colors['siaan'], fg=colors['siaan'], cursor='hand2')


def on_leave(grid_iten, event):
    grid_iten.config(bg=colors['bg-dark'], fg=colors['bg-dark'])


def desative_enter_leave(grid_iten, event):
    grid_iten.config(bg=colors['bg-dark'], cursor='arrow')


def update_score(frame, play1_points, play2_points):
    score_points = Label(
        frame,
        text=f'{str(play1_points)[-2:]}:{str(play2_points)[-2:]}',
        font='Ivy 30 bold',
        bg=colors['black'],
        fg=colors['white'],
    )
    score_points.grid(column=1, row=0)


def add_player(frame, symbol, color, number, column):
    Label(
        frame,
        text='\n' * 5 + f'Player{number}',
        bg=colors['black'],
        fg=colors['white'],
    ).grid(column=column, row=0)
    player = {}
    player[symbol] = Label(
        frame,
        text=symbol,
        font='Ivy 30 bold',
        bg=colors['black'],
        fg=colors[color],
    )
    player[symbol].grid(column=column, row=0)


def add_stage(frame, stage):
    Label(
        frame,
        text=f'Estágio: {stage:>4}',
        font='Ivy 25 bold',
        bg=colors['black'],
        fg=colors['white'],
    ).grid(column=0, row=0, columnspan=3, sticky=EW)


def set_button_return(frame, main_menu, exit):
    btn_return = Button(
        frame,
        text='❌SAIR',
        command=partial(exit, main_menu),
        font='Ivy 10 bold',
        bg=colors['black'],
        fg=colors['red'],
        activebackground=colors['bg-dark'],
        activeforeground=colors['yellow'],
        highlightthickness=0,
        borderwidth=0,
    )
    btn_return.grid(row=0, column=1, sticky=N)
    return btn_return


def set_label_message(frame, text=''):
    lb_message = Label(
        frame,
        text=f'{text: ^23}',
        justify='center',
        bg=colors['bg-dark'],
        fg=colors['white'],
        font='Courier 12 bold',
        pady=10,
    )
    lb_message.place(x=0, y=320)
    return lb_message


def set_score(frame):
    score = Label(
        frame, font='Ivy 40 bold', bg=colors['black'], padx=118, pady=15
    )
    score.grid(column=0, row=0, columnspan=3)
    score = Label(frame, bg=colors['bg-dark'], padx=5, pady=5)
    score.grid(column=0, row=1, columnspan=3)


def set_grid(frame):
    grid = {}
    lines = Label(frame)
    lines.place(x=2, y=127, height=188, width=236)
    for row in range(2, 5):
        for col in range(3):
            position = frame._name + str(row) + str(col)
            grid[position] = Label(
                frame,
                text='⬛',
                font='Ivy 30 bold',
                bg=colors['bg-dark'],
                fg=colors['bg-dark'],
                pady=5,
            )
            grid[position].grid(row=row, column=col, sticky=EW, pady=2, padx=2)
            grid[position].bind(
                f'<Button-1>', partial(on_click, grid[position])
            )
            grid[position].bind(f'<Enter>', partial(on_enter, grid[position]))
            grid[position].bind(f'<Leave>', partial(on_leave, grid[position]))


def set_menu_buttons(frame, texts, commands):
    element = {}
    for index, (text, command) in enumerate(zip(texts, commands), start=1):
        element[index] = Button(
            frame,
            text=text,
            command=command,
            font='Ivy 25 bold',
            bg=colors['bg-dark'],
            fg=colors['white'],
            activebackground=colors['bg-dark'],
            activeforeground=colors['yellow'],
            highlightthickness=0,
            borderwidth=0,
        )
        element[index].grid(row=index, column=0, sticky=EW)


def set_menu_labels(frame, texts, fg_color, sticky):
    element = {}
    for index, text in enumerate(texts, start=1):
        element[index] = Label(
            frame,
            text=text,
            font='Ivy 31',
            bg=colors['bg-dark'],
            fg=colors[fg_color],
        )
        element[index].grid(row=index, column=0, sticky=sticky)


def set_image(frame, image, col, row):
    global img
    img = PhotoImage(file=f'{PATH}\\images\\{images[image]}')
    label = Label(frame, image=img, bg=colors['bg-dark'])
    label.grid(row=row, column=col)


def set_symbol(grid_iten, symbol, color):
    if grid_iten['text'] != '⬛':
        return
    grid_iten.config(text=symbol, fg=colors[color])

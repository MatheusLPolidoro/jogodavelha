import ui


def run_game():
    win = ui.open_window()
    frame_arcade = ui.arcade(win)
    frame_local = ui.local(win)
    frame_menu = ui.main_menu(win, frame_arcade, frame_local)
    win.mainloop()


if __name__ == '__main__':
    run_game()

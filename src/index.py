from tkinter import Tk

from initialize_database import initialize_database
from ui.ui import UI


def main():
    window = Tk()

    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    initialize_database()
    main()

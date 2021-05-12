from tkinter import Tk


from ui.ui import UI



def main():
    """Alustellaan tarvittavat kirjastot ja lähdetään ajamaan ohjelmaa
    """
    window = Tk()

    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    
    main()

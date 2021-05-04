from tkinter import ttk, constants, StringVar, Text, messagebox, Listbox
import tkinter
from services.budget_service import BudgetService

class ListView:
    def __init__(self,root, handle_show_list_view, handle_show_login, budget_list):
        self._show_login_view = handle_show_login
        self._handle_show_list_view = handle_show_list_view
        self._root = root
        self._budget_list = budget_list
        self._frame = None
        self._cost_list = None
        
        self._initialize()
    

    def _initialize(self):
        """Käynnistetään listaus näkymä, näkymän alustus ja liitännäis luokkien alustus sekä tiedon haku
        """
        
        self._frame = ttk.Frame(master= self._root)
        self._text = Text(master=self._root, height = 50, width = 100)
        bs = BudgetService()
        self._cost_list = bs._return_cost_list()
        
        
        self._return_button = ttk.Button(master = self._frame, text = "Return", command = self._show_login_view)
        self._return_button.grid(padx = 10, pady = 5)
        self._text.pack()
        

        self._text.insert(tkinter.END,  self._cost_list)
        self._frame.pack()

    def destroy(self):
        """Tuhotaan vanha näkymä
        """
        self._frame.destroy()

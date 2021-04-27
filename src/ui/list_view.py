from tkinter import ttk, constants, StringVar
from services.budget_service import BudgetService

class ListView:
    def __init__(self, handle_show_list_view, handle_show_login):
        self._show_login_view = handle_show_login
        self._handle_show_list_view = handle_show_list_view

        self._pa

    def show_expenses(self):
        select = self._list.curselection()
        print([self._list.get(i) for i in select])

    def pack(self):
        self._frame.pack(fill=ttk.BOTH, side=ttk.left, expand=True)

    def destroy(self):
        self._frame.destroy()

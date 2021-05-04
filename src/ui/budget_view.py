from tkinter import ttk, constants, StringVar
from services.budget_service import BudgetService, UsernameExistsError


class BudgetView:
    def __init__(self, root, handle_show_budget, handle_show_login):
        self._root = root
        self._cost = None
        self._amount = None
        self._handle_show_budget = handle_show_budget
        self._frame = None
        self._error = None
        self._cost = None
        self._amount = StringVar()
        self._budget_service = BudgetService()
        self._show_login_view = handle_show_login
        self._initialize()

    def pack(self):
        self._frame.pack(fill=ttk.BOTH, side=ttk.left, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error)
        cost_label = ttk.Label(master=self._frame, text='Insert cost')
        self._cost_entry = ttk.Entry(master=self._frame, textvariable=self._cost)
        cost_label.grid(padx=5, pady=5)
        self._cost_entry.grid(padx=5, pady=5)

        amount_label = ttk.Label(master=self._frame, text='Insert amount')
        self._amount_entry = ttk.Entry(master=self._frame, textvariable=self._amount)
        amount_label.grid(padx=5, pady=5)
        self._amount_entry.grid(padx=5, pady=5)
        
        
        add_new_cost_button = ttk.Button(master=self._frame, text='Add this cost', 
        command=lambda:[ self._budget_service._add_cost(self._cost, self._amount), self._show_login_view()])

        add_new_cost_button.grid(row=9)

        self._frame.pack()
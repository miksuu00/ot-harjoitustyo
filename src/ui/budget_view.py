from tkinter import ttk, constants, StringVar
from services.budget_service import BudgetService, UsernameExistsError


class BudgetView:
    """Budjetti näkymä jossa muodostetaan ja alustetaan muuttujat sekä otetaan vastaan parametrit
    """
    def __init__(self, root, handle_show_budget, handle_show_login):
        self._root = root
        self._cost = StringVar
        self._amount = StringVar
        self._handle_show_budget = handle_show_budget
        self._frame = None
        self._error = None
        self._budget = []
        self._item_cost = {'item': str, 'amount': float}
        
        self._budget_service = BudgetService()
        self._show_login_view = handle_show_login
        self._initialize()

    def pack(self):
        """Main framen paketointi, käytetään laajalti ympäri ohjelmiston
        """
        self._frame.pack(fill=ttk.BOTH, side=ttk.left, expand=True)

    def destroy(self):
        """Tuhontaan vanha näkymä, käytetään laajalti ympäri ohjelmiston
        """
        self._frame.destroy()

    def _pass_arguments(self, cost, amount):
        self._budget_service._add_cost(cost, amount)

        
    def _add_cost(self, cost, amount):
        self._item_cost['item'] = cost
        self._item_cost['amount'] = amount
        self._budget.append(self._item_cost)

    def _return_shopping(self):
        total_shopping = 0
        for item in self._item_cost:
            total_shopping += float(item['amount'])
        return total_shopping

    def _initialize(self):
        """Luodaan pääframelle labelit, syöttökentät sekä kutsutaan muiden luokkien funktioita saaduilla tiedoilla
        
        """
        self._frame = ttk.Frame(master=self._root)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error)
        self._cost_label = ttk.Label(master=self._frame, text='Insert cost')

        self._cost_entry_var = StringVar()

        self._amount_entry_var = StringVar()

        self._cost_entry = ttk.Entry(master=self._frame)
        self._cost_label.grid(padx=5, pady=5)
        self._cost_entry.grid(padx=5, pady=5)



        self._amount_label = ttk.Label(master=self._frame, text='Insert amount')
        self._amount_entry = ttk.Entry(master=self._frame)
        self._amount_label.grid(padx=5, pady=5)
        self._amount_entry.grid(padx=5, pady=5)
        
        self._cost_entry_var = self._cost_entry.get()
        self._amount_entry_var = self._amount_entry.get()

        
        self._add_new_cost_button = ttk.Button(master=self._frame, text='Add this cost', 
        command=lambda:[ self._add_cost(self._cost_entry_var, self._amount_entry_var), self._show_login_view()])

        self._add_new_cost_button.grid(row=9)

        self._frame.pack()
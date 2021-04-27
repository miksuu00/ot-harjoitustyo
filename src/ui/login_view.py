from tkinter import ttk, StringVar, constants
from services.budget_service import BudgetService, InvalidCredentialsError


class LoginMain:
    def __init__(self, root, _login_attempt, handle_create_new_user, budget_view_screen, handle_show_list_view):
        self._root = root
        self._handle_create_new_user_view = handle_create_new_user
        self._login_attempt = _login_attempt
        self._frame = None
        self._username = None
        self._password = None
        self._error = None
        self._budget_view_screen = budget_view_screen
        self._show_list_view = handle_show_list_view
        self._initialize_login_screen()

    def pack(self):
       # self._initialize_login_screen()
        self._frame.pack(fill=ttk.BOTH, side=ttk.left, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _error_remove(self):
        self._error_label.grid_remove()

    def _login_attempt(self):
        username = self._username.get()
        password = self._password.get()

        try:
            budget_service.login(username, password)
            # tähän joku toiminto mitä tekee jos SUCCESS!
        except InvalidCredentialsError:
            self._error_label_output('Check you credentials! Invalid input!')

    def _error_label_output(self, message):
        self._error.set(message)
        self._error_label.grid()

    def _initialize_login_screen(self):
        self._root.title('Please be prepared to budget')
        self._frame = ttk.Frame(master=self._root)
        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error)

        self._error_label.grid(padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text='Username')
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=3, padx=5, pady=5)
        password_label = ttk.Label(master=self._frame, text=('Password'))
        self._password_entry = ttk.Entry(
            master=self._frame, textvariable=self._password, show='x')
        self._password_entry.grid(row=4, padx=5, pady=5)

        button_login = ttk.Button(
            master=self._frame, text='Press to login', command=self._login_attempt)
        button_login.grid(row=5, padx=5, pady=5)
        button_new_user = ttk.Button(
            master=self._frame, text='Press to create new account', command=self._handle_create_new_user_view)
        # lisää button_new_user, command linkitys "create user view luokkaan(tee myös se luokka ja muista lisätä konstruktorin attribuutti)"
        button_add_cost = ttk.Button(
            master=self._frame, text='Press to add cost', command=self._budget_view_screen)
        button_show_expenses = ttk.Button(master=self._frame, text='Show expenses', command= self._show_list_view)
        button_show_expenses.grid(row=10)
        button_add_cost.grid(row=7)
        button_new_user.grid(row=6)
        self._frame.pack()
        # create_new_user_button=ttk.Button(master=self._frame, 'Create account',command=self._change_new_account_view)

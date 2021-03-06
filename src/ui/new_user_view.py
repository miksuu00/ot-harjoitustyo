from tkinter import ttk, constants, StringVar
from services.budget_service import budget_service, UsernameExistsError


class NewUserView:
    def __init__(self, root, handle_show_login):
        """Konstruktori jossa luodaan päänäkymän jälkeinen visuaalinen ote

        Args:
            root ([pääfreimi jolle rakennetaan]): [frame]
            handle_show_login ([lisäoptio sisäänkirjautumiseen]): [show login liitännäinen]
        """
        self._root = root

        self._handle_show_login = handle_show_login
        self._frame = None
        self._error = StringVar()
        self._new_username = None
        self._new_password = None

        self._initialize()

    def pack(self):
        """pakkaus funktio jota käytetään laajalti ohjelman toiminnallisuudessa,
        paketoi ohjelman metodit yhteen nipppuun
        """
        self._frame.pack(fill=ttk.BOTH, side=ttk.left, expand=True)

    def destroy(self):
        """Tuhoaa vanhan näkymän, jotta uusi pääsee pinnalle, käytetään laajaltin ohjelman toiminnallisuudesssa
        """
        self._frame.destroy()

    def _create_new_user(self):
        """Luodaan uusi käyttäjä (kun tietokannat implementoitu
        )
        """
        username = self._username_entry.get()
        password = self._username_entry.get()
        if len(username) == 0 or len(password) < 8:

            self._show_error(
                'Type username and password (password minimun length is 8 characters)')
            return
        try:
            budget_service.create_user(username, password)
            self._create_new_user()
        except UsernameExistsError:
            self._show_error('Username already exists, choose another one!')

    def _show_error(self, message):
        """Funkito virhe viestin esittämiseen

        Args:
            message (Tiedoksianto): Virheen mukainen tiedoksianto
        """
        self._error.set(message)
        self._error_label.grid()

    def _initialize(self):

        """Käynnistetään näkymän luonti,
        luodaan frame, labelit sekä entry-kentät
        """
        self._frame = ttk.Frame(master=self._root)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error)
        username_label = ttk.Label(master=self._frame, text='Choose username')
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text='Choose password')
        self._password_entry = ttk.Entry(
            master=self._frame, textvariable=self._new_password, show='x')
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(padx=5, pady=5)

        create_new_user_button = ttk.Button(
            master=self._frame, text='Create new account', command=self._create_new_user)
        button_login = ttk.Button(
            master=self._frame, text='Login now', command=self._handle_show_login)
        create_new_user_button.grid(padx=5, pady=5)
        button_login.grid(padx=5, pady=5)
        self._frame.pack()

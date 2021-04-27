from ui.login_view import LoginMain
from ui.new_user_view import NewUserView
from tkinter import ttk, constants
from ui.budget_view import BudgetView
from ui.list_view import ListView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
       # self.pack()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginMain(
            self._root, self._show_main_screen, self._show_new_user_view, self._show_budget_view, self._show_list_view)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_main_screen(self):
        self._hide_current_view()
        self._current_view = LoginMain(
        self._root, self._show_login_view, self._show_new_user_view)

    def _show_new_user_view(self):
        self._hide_current_view()
        self._current_view = NewUserView(self._root, self._show_login_view)

    def _show_budget_view(self):
        self._hide_current_view()
        self._current_view = BudgetView(self._root, self._show_budget_view, self._show_login_view)

    def _show_list_view(self):
        self._hide_current_view()
        self._current_view = ListView(self._root, self._show_list_view, self._show_login_view)

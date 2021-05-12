

class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass




class BudgetService:

    def __init__(self):
        """Konstrukotri alustaa listat kirjanpidolle
        """

        self._budget = []
        self._income = []
        self._item_income = {'income': str , 'amount':float}
        self._item_cost = {'item': str, 'amount': float}
    def _add_cost(self, cost, amount):
        """lisätään kulu kirjanpidolle jotta pysytään kirjoilla kuluista

        Args:
            cost ([type]): [description]
            amount ([type]): [description]
        """
        self._item_cost ['item'] = cost
        self._item_cost['amount'] = amount
        self._budget.append(self._item_cost)

    def _add_income(self, income, amount):
        """lisätään tulo ja sen luokka tuloikirjanpidolle
        jotta pysytään tuloissa mukanaa
 
        Args:
            income (Sisääntulo): Mikä on sisääntulon luokka, palkka, bonus vai lottovoitto
            amount (Summa): Numeerinen määritelmä tulosta
        """
        self._dict_income={'income' :income, 'income_amount':amount}

    def _get_all_costs_total(self):
        """Palauttaa kokonais kulujen numeerisen arvon

        Returns:
            Kulut: Kulujen summa
        """
        total_cost = 0
        for line in self._budget:
            total_cost += line[1]

        return total_cost
    def _get_all_income_total(self):
        """Palautetaan tulojen kokonaissumma

        Returns:
            Tulotyypin laji: Paljonko tuloja on numeerisena rahayksikkönä
        """
        total_income = 0
        for inc in self._income:
            total_income += inc[1]
        return total_income
    def _return_cost_list(self):
        """Koko tämän hetkisen kululistan palautus

        Returns:
            Lista: pitää sisällään kulun ja summan
        """
     
        grand_total=0
        for items in self._budget:
            grand_total += items['amount']
        
        return f'This is what you spent {grand_total}'

    
    
        



budget_service = BudgetService()




class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass




class BudgetService:

    def __init__(self):
        self._budget = []
        self._income = []
    def _add_cost(self, cost, amount):
        insert = (cost, amount)
        self._budget.append(insert)

    def _add_income(self, income, amount):
        income_insert = (income, amount)
        self._income.append(income_insert)

    def _get_all_costs_total(self):
        total_cost = 0
        for line in self._budget:
            total_cost += line[1]

        return total_cost
    def _get_all_income_total(self):
        total_income = 0
        for inc in self._income:
            total_income += inc[1]
        return total_income
    def _return_cost_list(self):
        total_cost = 0
        for line in self._budget:
            
            total_cost += int(line[1])
        return f"Total cost is: {total_cost}"
    def _return_income_list(self):
        return self._income
    
    
    
        



budget_service = BudgetService()

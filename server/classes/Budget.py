class Budget:
    def __init__(self, username):
        self.categories = []
        self.name = username
        self.budget_log = []

        @property
        def money_left(self):
            return self._money_left

        @money_left.setter
        def money_left(self):  # Computationally inefficient, probably not relevant for a local machine.
            self._money_left = 0
            for cat in self.categories:
                self._money_left += cat.money_left

        @property
        def money_total(self):
            return self._money_total

        @money_total.setter
        def money_total(self):  # Computationally inefficient, but that is probably not relevant for a local machine.
            self._money_total = 0
            for cat in self.categories:
                self._money_total += cat.money_total

    def addCategory(name, amountMoney):
        pass
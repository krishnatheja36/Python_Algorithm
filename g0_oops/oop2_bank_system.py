# OOP: Two-class pattern — single object + manager
# Pattern: Account handles one account, BankSystem manages many
# Concepts: encapsulation, private helpers, error handling, separation of concerns

class Account:
    def __init__(self, account_id: str, owner: str, initial_balance: float = 0.0):
        self.account_id = account_id
        self.owner = owner
        self._balance = initial_balance     # private

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: {self._balance}")
        self._balance -= amount
        return self._balance

    def get_balance(self) -> float:
        return self._balance

    @property
    def balance(self) -> float:             # @property: access like an attribute
        return self._balance

    def __repr__(self):
        return f"Account(id={self.account_id}, owner={self.owner}, balance={self._balance})"


class BankSystem:
    def __init__(self):
        self._accounts = {}                 # account_id -> Account

    def add_account(self, account_id: str, owner: str, initial_balance: float = 0.0) -> Account:
        if account_id in self._accounts:
            raise ValueError(f"Account {account_id} already exists")
        account = Account(account_id, owner, initial_balance)
        self._accounts[account_id] = account
        return account

    def delete_account(self, account_id: str) -> bool:
        self._get_account(account_id)       # raises if not found
        del self._accounts[account_id]
        return True

    def check_balance(self, account_id: str) -> float:
        return self._get_account(account_id).get_balance()

    def deposit(self, account_id: str, amount: float) -> float:
        return self._get_account(account_id).deposit(amount)

    def withdraw(self, account_id: str, amount: float) -> float:
        return self._get_account(account_id).withdraw(amount)

    def list_accounts(self) -> list:
        return list(self._accounts.values())

    def _get_account(self, account_id: str) -> Account:    # private helper
        if account_id not in self._accounts:
            raise ValueError(f"Account {account_id} not found")
        return self._accounts[account_id]


if __name__ == "__main__":
    bank = BankSystem()

    bank.add_account("ACC001", "Krishna", 1000.0)
    bank.add_account("ACC002", "Shreekala", 500.0)

    print(bank.check_balance("ACC001"))     # 1000.0
    print(bank.deposit("ACC001", 500.0))    # 1500.0
    print(bank.withdraw("ACC001", 200.0))   # 1300.0

    bank.delete_account("ACC002")

    try:
        bank.check_balance("ACC002")        # ValueError
    except ValueError as e:
        print(f"Error: {e}")

    try:
        bank.withdraw("ACC001", 99999)      # ValueError
    except ValueError as e:
        print(f"Error: {e}")

    print(bank.list_accounts())

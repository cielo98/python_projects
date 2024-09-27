class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}님의 잔액: {self.balance}원")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.owner}님의 잔액이 부족합니다.")
        else:
            self.balance -= amount
            print(f"{self.owner}님의 잔액: {self.balance}원")

    def show_balance(self):
        print(f"{self.owner}님의 현재 잔액: {self.balance}원")


class AccountsList:
    def __init__(self):
        self.accounts = [
            BankAccount("Dina", 39500),
            BankAccount("Rocky", 57000),
            BankAccount("Lizzy", 23700),
        ]

    def find_account(self, owner_name):
        for account in self.accounts:
            if account.owner == owner_name:
                return account
        return None


# 계좌 목록 생성
accounts_list = AccountsList()

# Dina의 계좌 찾기
dina_account = accounts_list.find_account("Dina")

if dina_account:
    dina_account.deposit(50000)
    dina_account.withdraw(9500)
else:
    print("계좌를 찾을 수 없습니다.")

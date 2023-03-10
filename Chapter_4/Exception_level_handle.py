class Invalidwithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance

try:
    raise Invalidwithdrawal(26,40)
except Invalidwithdrawal as e:
    print("I'm sorry, but your withdrawal is "
          "more than your balance by "
          "${}".format(e.overage()))
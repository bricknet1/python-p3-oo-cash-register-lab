#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total

    def add_item(self, item, price, quantity=1):
        self.quantity = quantity
        self.total += price*quantity


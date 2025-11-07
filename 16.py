class Basket:
    def __init__(self):
        self.items = {} 

    def add_item(self, name, price, quantity=1):
  
        if name in self.items:
            self.items[name][1] += quantity
            print(f"Daemata {quantity} - {name}. kalatashia - {self.items[name][1]}.")
        else:
            self.items[name] = [price, quantity]
            print(f"daemata {quantity} x {name}")

    def remove_item(self, name, quantity=1):
        
        if name in self.items:
            self.items[name][1] -= quantity
            if self.items[name][1] <= 0:
                del self.items[name]
                print(f"{name} waishala kalatidan")
            else:
                print(f"kalatidan waishala {quantity} {name}. darcha -  {self.items[name][1]}")
        else:
            print(f"{name} arari kalatashi")

    def total_price(self):
        
        if not self.items:
            print("kalati carielia")
            return
        print("\n nivtebi kalatashi:")
        total = 0
        for name, (price, quantity) in self.items.items():
            subtotal = price * quantity
            total += subtotal
            print(f"- {name}: {price} x {quantity} = {subtotal}")
        print(f"\njamuri fasi: {total}")
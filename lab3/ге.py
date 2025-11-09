food = {
    "milk": 30,
    "eggs": 40,
    "bread": 20,
}
order=[]
class Order:
    def show_food(self):
        for name, price in food.items():
            print(f"{name}: {price}")
    def add_food(self, name):
        if name in food:
            order.append(name)
            print(f"{name} has been added to your order")
        else:
            print(f"{name} not found")
    def remove_food(self, name):
        if name in order:
            order.remove(name)
            print(f"{name} has been removed from your order")
        else:
            print(f"{name} not found")
    def show_order(self):
        for name in order:
            print(f"{name}: {food[name]}")
        if not order:
            print("empty order")
            return
        print("корзина:")
        itemcnt={}
        for item in order:
            itemcnt[item]=itemcnt.get(item, 0)+1
        total = 0
        for item, count in itemcnt.items():
            price = food[item]
            foodttl = price * count
            print(f"{item} x {count}: {foodttl}")
            total += foodttl
        print(f"всего {total}")
if __name__ == "__main__":
    while True:
        print("menu")
        print("1. show food")
        print("2. add food")
        print("3. remove food")
        print("4. show order")
        print("5. exit")
        choice = input("choose action from 1 to 5:")
        if choice == "1":
            Order().show_food()
        elif choice == "2":
            a = input("add food name:")
            Order().add_food(a)
        elif choice == "3":
            b = input("remove food name:")
            Order().remove_food(b)
        elif choice == "4":
            Order().show_order()
        elif choice == "5":
            print("exit")
            break
        else:
            print("invalid choice")
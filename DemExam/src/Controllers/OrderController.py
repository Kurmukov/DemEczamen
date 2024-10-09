from src.Models.Orders import *

class Order_Controller():
    def get(self):
        return Orders.select().execute()

    @classmethod
    def update_order_ready(cls, order_id):
        Orders.update({Orders.status_id: 1}).where(Orders.id == order_id).execute()
    @classmethod
    def add_order(self, count, table, drink, food, shift, status):
        Orders.create(count_cliens = count, table_id = table, drink_id = drink, food_id = food, shift_id = shift, status_id = status)
    @classmethod
    def show_povar(self,orders_id):
        Orders.select(Orders.drink_id and Orders.food_id).where(Orders.id == orders_id).execute()





if __name__ == "__main__":
    ord = Order_Controller()
    for row in ord.get():
        print(row.id, row.count_cliens,row.table_id.number,row.drink_id.name,row.food_id.name,row.shift_id,row.status_id.name)
    ord.update_order_ready(2)

    ord.add_order(2,2,2,2,2, 1)
    ord.show_povar(2)



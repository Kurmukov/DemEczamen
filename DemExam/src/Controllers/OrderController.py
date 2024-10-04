from src.Models.Orders import *

class OrderController():
    def get(self):
        return Orders.select().execute()

if __name__ == "__main__":
    ord = OrderController()
    for row in ord.get():
        print(row.id, row.count_cliens,row.table_id.number,row.drink_id.name,row.food_id.name,row.shift_id,row.status_id.name)
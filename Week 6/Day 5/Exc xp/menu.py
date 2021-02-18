# Exc xp

class MenuItem:
    def __init__(self,item_name,item_price):
        self.item_price=item_price
        self.item_name=item_name

    def run_query(self,query):
        connection=sl.connect("restuarant_menu.db")
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def save_to_db(self):
        query = f"INSERT INTO Restuarant_items (Item, Price) VALUES ('{self.item_name}', {self.item_price})"
        return self.run_query(query)
        
    def delete_from_db(self):
        query=f'DELETE FROM Restuarant_items where Item ="{self.item_name}" '
        return self.run_query(query)
        
    def update_db(self,old_item ):
        query=f"UPDATE Restuarant_items SET Item = '{self.item_name}' WHERE Item = '{old_item}'"
        self.run_query(query)
        query =f"UPDATE Restuarant_items SET Price = {self.item_price} WHERE Item = '{self.item_name}'" 
        self.run_query(query)

    def all_(self):
        query=f'select Item,Price from Restuarant_items'
        connection=sl.connect("restuarant_menu.db")
        cursor = connection.cursor()
        cursor.execute(query)
        results=cursor.fetchall()
        connection.close()
        print(list(results))
        return results

    def get_by_name(self,name):
        query=f'select Item from Restuarant_items where Item ="{name}" '
        connection=sl.connect("restuarant_menu.db")
        cursor = connection.cursor()
        cursor.execute(query)
        results=cursor.fetchall()
        connection.close()
        if len(results) < 1:
            print('Doesnt exist')
        else:    
            print(list(results))
        
	
import sqlite3

class Database:

    def __init__(self, db):    #Constructor that constructs the object
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Book(id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn): 
        self.cur.execute("INSERT INTO Book VALUES(NULL, ?, ? ,?, ?)", (title, author, year, isbn))
        self.conn.commit()
        

    def view(self): 
        self.cur.execute("SELECT * FROM Book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""): 
        self.cur.execute("SELECT * FROM Book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM Book WHERE id=?",(id,))
        self.conn.commit()
        
    def update(self, id,title,author,year,isbn): 
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))  
        self.conn.commit()
        
    def __del__(self):   #For destructing the window
        self.conn.close()

#insert("The Invisible man", "Chetan Bhagat", 2012, 1524834)  
#delete(2)
#update(11,"The","John",2002, 2371912)
#print(view())
#print(search(author="Chetan Bhagat"))
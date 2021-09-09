import sqlite3
DB_PATH = "Budget.db"

def Subtraction(Budget,Spent, slot_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        # Once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()
        # Keep the initial status as Not Started
        Left = int(Budget) - int(Spent)
        c.execute("insert into Budgee(Budget, Spent, Left, slot_id) values(?,?,?,?)", (Budget,Spent,Left,slot_id))
        # We commit to save the change
        conn.commit()
        return {"Left": Left}
    except Exception as e:
        print("Error: ", e)
        return None

def Delete(slot_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from Budgee where slot_id=? ', (slot_id,))
        conn.commit()
    except:
        pass


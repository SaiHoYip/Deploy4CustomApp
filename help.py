import sqlite3

DB_PATH = "Budget.db"  # Update this path accordingly


def Subtraction(Budget,Spent):
    try:
        conn = sqlite3.connect(DB_PATH)
        # Once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()
        # Keep the initial status as Not Started
        Left = int(Budget) - int(Spent)
        c.execute("insert into Budgee(Budget, Spent, Left) values(?,?,?)", (Budget,Spent,str(Left),))
        # We commit to save the change
        conn.commit()
        return {"Spent": Spent}
    except Exception as e:
        print("Error: ", e)
        return None


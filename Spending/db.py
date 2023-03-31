import sqlite3


db = sqlite3.connect("spending.db")

db.execute("""--sql
CREATE TABLE spending (
    Date date,
    money_spent float,
    method_of_purchase VARCHAR(50),
)
""")


db.execute("""--sql
CREATE TABLE money (
    Date date,
    money_got float,     
)
""")
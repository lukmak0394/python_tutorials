import pandas as pd
import classes.database as db

def main():
    db_instance = db.Database()
    tables = db_instance.get_db_tables()
    # print(tables)


main()
    



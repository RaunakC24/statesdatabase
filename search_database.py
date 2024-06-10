import pymysql
import pandas as pd

database = pymysql.connect(
    host= 'sql5.freemysqlhosting.net',
    user = 'sql5710968',
    password= 'HguWrLDflk',
    db = 'sql5710968',
    port = 3306
)

dbcursor = database.cursor()

def search(item_search):
    
    try: 
        dbcursor.execute(item_search)
        result = dbcursor.fetchall()
        columns = [desc[0] for desc in dbcursor.description]
        df = pd.DataFrame(result, columns=columns)
    finally:
        dbcursor.close()
        database.close()
    
    return df

if __name__ == "__main__":

    name = input("Enter the name (or leave blank to skip): ").strip().title()
    state = input("Enter the state abbreviation (ex: 'CA' for California, other leave blank to skip): ").strip().upper()
    party = input("Enter the party name (ex: Democratic, Republican, or Independent) or leave blank to skip: ").strip().capitalize()
    chamber = input("Enter the chamber level (ex: upper or lower) or leave blank to skip: ").strip().lower()
    district = input("Enter the district number or letter (ex: 'F' or 29) or leave blank to skip: ").strip()
    stateorfed = input("Enter if the person is a State or Federal legislator or leave blank to skip: ").strip().capitalize()

    search_find = []

    if name: 
        search_find.append(f"Name = '{name}'")
    if state:
        search_find.append(f"State = '{state}'")
    if party:
        search_find.append(f"Party = '{party}'")
    if chamber:
        search_find.append(f"Chamber = '{chamber}'")
    if district:
        search_find.append(f"District = '{district}'")
    if stateorfed:
        search_find.append(f"StateorFed = '{stateorfed}'")

    combine = " AND ".join(search_find) if search_find else "1=1"

    query_search = f"SELECT Name, Party, District, Chamber, State, StateorFed FROM Legislators WHERE {combine}"

    results = search(query_search)

    outputfile = 'results.txt'
    
    with open(outputfile, 'w') as f:
        f.write(results.to_string(index=False))
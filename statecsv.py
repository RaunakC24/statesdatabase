import pymysql
import pandas as pd
import os
import requests

hostInput = input("Enter the server name: ").strip()
dbInput = input("Enter the database name: ").strip()
userInput = input("Enter the username: ").strip()
passwordInput = input("Enter the password: ").strip()
portInput = input("Enter the port number: ").strip()

port = int(portInput)

database = pymysql.connect(
    host= hostInput,
    user = userInput,
    password= passwordInput,
    db = dbInput,
    port = port
)

dbcursor = database.cursor()

statesAbb = [
    'ak', 'al', 'ar', 'az', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'ia', 'id',
    'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'me', 'mi', 'mn', 'ms', 'mo', 'mt',
    'nc', 'ne', 'nh', 'nj', 'nm', 'nv', 'ny', 'nd', 'oh', 'ok', 'or', 'pa', 
    'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'va', 'vt', 'wa', 'wi', 'wv', 'wy', 'dc', 'us'
]

url = "https://data.openstates.org/people/current/{}.csv"

folder = 'csvfiles'

if not os.path.exists(folder):
    os.makedirs(folder)

dbcursor.execute('DELETE FROM Legislators')

for state in statesAbb:
    new_url = url.format(state)
    response = requests.get(new_url)
    if response.status_code == 200:
        pathoffile = os.path.join(folder, f'{state}.csv')
        with open(pathoffile, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {state}.csv")
    else:
        print(f"Failed to download {state}.csv")

    read = pd.read_csv(pathoffile)

    for _, row in read.iterrows():
        name = row['name']
        party = row['current_party']
        district = row['current_district']
        chamber = row['current_chamber']
        nameofstate = state.upper() if state != 'us' else 'US'
        stateorfed = 'State' if state != 'us' else 'Federal'

        dbcursor.execute(
            "INSERT INTO Legislators (Name, Party, District, Chamber, State, StateorFed) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, party, district, chamber, nameofstate, stateorfed)
            )
        database.commit()

dbcursor.close()
database.close()
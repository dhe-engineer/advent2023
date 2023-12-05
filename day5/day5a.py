import sqlite3
from almanac import seed_almanac as Almanac

# Create a database table if it does not exist
try:
    connection = sqlite3.connect("day5/day5.sqlite3")
    print("Opened table successfully")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS almanac
                        (SEED INT PRIMARY KEY NOT NULL,
                        SOIL INT,
                        FERTILIZER INT,
                        WATER INT,
                        LIGHT INT,
                        TEMPERATURE INT,
                        HUMIDITY INT,
                        LOCATION int);
                        ''')
    print("Table created successfully")
    data_file = open("day5/example.txt", "r", encoding="utf-8").read().split("\n\n")
    almanac_list = []
    for line in data_file:
        if line.find("seeds:") > -1:
            seed_list = line.split(": ")[1]
            seed_list = seed_list.split(" ")
            for item_number, seed in enumerate(seed_list):
                seed_object = Almanac(int(seed))
                almanac_list.append(seed_object)
                cursor.execute('''INSERT OR IGNORE INTO almanac VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', seed_object.get_params())
            connection.commit()
            print(seed_list)
            continue

        if line.find("seed-to-soil map:\n") > -1:
            soil_list = line.split(":\n")[1]
            soil_lists = soil_list.split("\n")
            for seed_index, almanac_object in enumerate(almanac_list):
                for soil_index, soil in enumerate(soil_lists):
                    soil_range = soil.split(" ")
                    if almanac_object.SEED >= int(soil_range[0]) and almanac_object.SEED <= (int(soil_range[0]) + int(soil_range[2])):
                        almanac_object.SOIL = int(soil_range[1]) + (almanac_object.SEED - int(soil_range[0]))
                        cursor.execute('''UPDATE almanac SET SOIL = ? WHERE SEED = ?''', (almanac_object.SOIL, almanac_object.SEED))
                if almanac_object.SOIL == 0:
                    almanac_object.SOIL = almanac_object.SEED
                    cursor.execute('''UPDATE almanac SET SOIL = ? WHERE SEED = ?''', (almanac_object.SOIL, almanac_object.SEED))
            connection.commit()
            print(soil_list)
        print("next line")

    print("done")

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")

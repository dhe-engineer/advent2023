import sqlite3
from almanac import seed_almanac as Almanac


def convert_table(databas_file, almanac_list, target_list, target_string, destination_string):
    try:
        connection = sqlite3.connect(databas_file)
        cursor = connection.cursor()
        for seed_index, almanac_object in enumerate(almanac_list):
            for destination_string_index, target in enumerate(target_list):
                target_range = target.split(" ")
                if almanac_object.get_property(target_string) >= int(target_range[1]) and almanac_object.get_property(target_string) < (int(target_range[1]) + int(target_range[2])):
                    almanac_object.set_property(
                        (int(target_range[0]) + almanac_object.get_property(target_string) - int(target_range[1])), destination_string)
                    cursor.execute('''UPDATE almanac SET %s = ? WHERE %s = ?''' % (destination_string, target_string),
                                   (almanac_object.get_property(destination_string), almanac_object.get_property(target_string)))
            if almanac_object.get_property(destination_string) == 0:
                almanac_object.set_property(almanac_object.get_property(target_string), destination_string)
                cursor.execute('''UPDATE almanac SET %s = ? WHERE %s = ?''' % (destination_string, target_string),
                               (almanac_object.get_property(destination_string), almanac_object.get_property(target_string)))
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        connection.commit()
        if connection:
            connection.close()


def parser(input_file, database_file):
    # Create a database table if it does not exist
    try:
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        cursor.execute('''DROP TABLE IF EXISTS almanac''')
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
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if connection:
            connection.close()

    data_file = open(input_file, "r", encoding="utf-8").read().split("\n\n")
    almanac_list = []
    for line in data_file:
        if line.find("seeds:") > -1:
            try:
                connection = sqlite3.connect(database_file)
                cursor = connection.cursor()
                seed_list = line.split(": ")[1]
                seed_list = seed_list.split(" ")
                for item_number, seed in enumerate(seed_list):
                    seed_object = Almanac(int(seed))
                    almanac_list.append(seed_object)
                    cursor.execute('''INSERT OR IGNORE INTO almanac VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', seed_object.get_all_properties())
                connection.commit()
            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)
            finally:
                if connection:
                    connection.close()
                continue

        if line.find("seed-to-soil map:\n") > -1:
            soil_list = line.split(":\n")[1]
            soil_lists = soil_list.split("\n")
            convert_table(database_file, almanac_list, soil_lists, "SEED", "SOIL")
            continue

        if line.find("soil-to-fertilizer map:\n") > -1:
            fertilizer_list = line.split(":\n")[1]
            fertilizer_lists = fertilizer_list.split("\n")
            convert_table(database_file, almanac_list, fertilizer_lists, "SOIL", "FERTILIZER")
            continue

        if line.find("fertilizer-to-water map:\n") > -1:
            water_list = line.split(":\n")[1]
            water_lists = water_list.split("\n")
            convert_table(database_file, almanac_list, water_lists, "FERTILIZER", "WATER")
            continue

        if line.find("water-to-light map:\n") > -1:
            light_list = line.split(":\n")[1]
            light_lists = light_list.split("\n")
            convert_table(database_file, almanac_list, light_lists, "WATER", "LIGHT")
            continue

        if line.find("light-to-temperature map:\n") > -1:
            temperature_list = line.split(":\n")[1]
            temperature_lists = temperature_list.split("\n")
            convert_table(database_file, almanac_list, temperature_lists, "LIGHT", "TEMPERATURE")
            continue

        if line.find("temperature-to-humidity map:\n") > -1:
            humidity_list = line.split(":\n")[1]
            humidity_lists = humidity_list.split("\n")
            convert_table(database_file, almanac_list, humidity_lists, "TEMPERATURE", "HUMIDITY")
            continue

        if line.find("humidity-to-location map:\n") > -1:
            location_list = line.split(":\n")[1]
            location_lists = location_list.split("\n")
            convert_table(database_file, almanac_list, location_lists, "HUMIDITY", "LOCATION")
            continue

    # Find the entry with the smallest location value
    try:
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()
        cursor.execute('''SELECT LOCATION FROM almanac WHERE LOCATION = (SELECT MIN(LOCATION) FROM almanac)''')
        result = cursor.fetchall()
        print(result)
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if connection:
            connection.close()

    print("done")


if __name__ == "__main__":
    parser("day5/puzzle.txt", "day5/day5puzzle.sqlite3")

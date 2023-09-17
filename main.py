
distance_meters = float(input("Введіть кількість метрів: "))

unit = input("Введіть  'miles' , 'dumes', 'yards': ")
if unit == 'miles':

    distance_miles = distance_meters / 1609.34
    print(distance_meters, "meters is equal to", distance_miles, "miles.")
elif unit == 'dumes':

    distance_dumes = distance_meters * 39.37
    print(distance_meters, "meters is equal to", distance_dumes, "dumes.")
elif unit == 'yards':

    distance_yards = distance_meters * 1.094
    print(distance_meters, "meters is equal to", distance_yards, "yards.")


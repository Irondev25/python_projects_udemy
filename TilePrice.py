y = 'y'

while y == 'y':
    width_of_floor = float(input("Enter your floor's width(in feet): "))
    length_of_floor = float(input("Enter your floor's length(in feet): "))
    cost_of_tile = float(input("Enter tile's cost(in Rupees): "))
    width_of_tile = float(input("Enter your tile's width(in feet): "))
    length_of_tile = float(input("Enter your tile's length(in feet): "))

    area_of_floor = width_of_floor * length_of_floor
    area_of_tile = width_of_tile * length_of_tile

    print("%0.3f Rupees" % ((area_of_floor/area_of_tile)*cost_of_tile))
    y = input("Calculate for another floor(y/n):")

#NAME: Angel Rivera
#Program: CALCULATOR
import math

# Constants
BORDER_COUNT = 25
STAR_BORDER = "*" * BORDER_COUNT

# Print project header
print("\n" + STAR_BORDER + "\nPROJECT I\n" + STAR_BORDER)

while True:
    # Main menu options
    Option = int(input(
        "\nSelect option:\n"
        "(1) Area of figures\n"
        "(2) Units conversion\n"
        "(3) Base conversion\n"
        "(0) Exit\n"))
    
    if Option == 1:
        # Area calculation options
        Area_calculation = int(input(
            "\nSelect option:\n"
            "(1) Area of a SQUARE\n"
            "(2) Area of a RECTANGLE\n"
            "(3) Area of a CIRCLE\n"
            "(4) Area of a TRIANGLE\n"))

        if 1 <= Area_calculation <= 4:
            if Area_calculation == 1: # SQUARE
                side_length = float(input("Enter the length of the side: "))
                area = side_length ** 2
            elif Area_calculation == 2: # RECTANGLE
                base = float(input("Enter the size of the base: "))
                height = float(input("Enter the size of the height: "))
                area = base * height
            elif Area_calculation == 3: # CIRCLE
                radius = float(input("Enter the radius size: "))
                area = math.pi * radius ** 2
            elif Area_calculation == 4: # TRIANGLE
                base = float(input("Enter the size of the base: "))
                height = float(input("Enter the size of the height: "))
                area = 0.5 * base * height

            print("Area of the figure:", area)

            # Check fitting of small figures
            check_fitting = input("Do you want to check how many small figures fit in the initial figure? (y/n) ")

            if check_fitting.lower() == "y":
                small_figure_area = float(input("Enter the area of the small figure: "))
                if small_figure_area <= 0:
                    print("Invalid input: the area of the small figure must be positive.")
                else:
                    fitting_count = area / small_figure_area
                    print("Number of times the small figure fits into the first figure:", fitting_count)
            elif check_fitting.lower() != "n":
                print("Invalid input")

        else:
            print("Invalid input")

    elif Option == 2:
        # Units conversion options
        print("Units Conversion:")
        print("1. Pressure units")
        print("2. Wind speed units")
        unit_option = input("Choose the unit to convert: ")

        if unit_option == "1":
            print("Pressure units:")
            print("1. Pascal (Pa)")
            print("2. Atmosphere (atm)")
            print("3. Bar (bar)")
            original_unit = input("Select the original pressure unit: ")
            value = float(input("Enter the value to be converted: "))

            if original_unit == "1":  # Pascal
                converted_value_atm = value * 9.8692e-6
                converted_value_bar = value * 0.00001
                print(f"{value} Pascal (Pa) is equivalent to {converted_value_atm} Atmosphere (atm) and {converted_value_bar} Bar (bar).")
            elif original_unit == "2":  # Atmosphere
                converted_value_pa = value * 101325
                converted_value_bar = value * 1.01325
                print(f"{value} Atmosphere (atm) is equivalent to {converted_value_pa} Pascal (Pa) and {converted_value_bar} Bar (bar).")
            elif original_unit == "3":  # Bar
                converted_value_pa = value * 100000
                converted_value_atm = value * 0.98692
                print(f"{value} Bar (bar) is equivalent to {converted_value_pa} Pascal (Pa) and {converted_value_atm} Atmosphere (atm).")
            else:
                print("Invalid option")

        elif unit_option == "2":
            print("Wind speed units:")
            print("1. Meters per second (m/s)")
            print("2. Kilometers per hour (km/h)")
            print("3. Miles per hour (mph)")
            original_unit = input("Select the original wind speed unit: ")
            value = float(input("Enter the value to be converted: "))

            if original_unit == "1":  # Meters per second
                converted_value_kmh = value * 3.6
                converted_value_mph = value * 2.23694
                print(f"{value} m/s is equivalent to {converted_value_kmh} km/h and {converted_value_mph} mph.")
            elif original_unit == "2":  # Kilometers per hour
                converted_value_ms = value * 0.277778
                converted_value_mph = value * 0.621371
                print(f"{value} km/h is equivalent to {converted_value_ms} m/s and {converted_value_mph} mph.")
            elif original_unit == "3":  # Miles per hour
                converted_value_ms = value * 0.44704
                converted_value_kmh = value * 1.60934
                print(f"{value} mph is equivalent to {converted_value_ms} m/s and {converted_value_kmh} km/h.")
            else:
                print("Invalid option")

    elif Option == 3:
        # Base conversion
        hex_number = input("Enter a hexadecimal number: ")
        decimal_number = int(hex_number, 16)
        print("Decimal equivalent:", decimal_number)

    elif Option == 0:
        # Exit program
        print("Exiting the program...")
        break

    else:
        print("Invalid option")

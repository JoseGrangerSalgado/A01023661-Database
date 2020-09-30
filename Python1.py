import csv,pandas

def Pop():
    population_2010 = []
    value_errors = ["--","NA"]
    country_exceptions = ["World","Country", "Asia & Oceania", "Africa", "Europe", "Central & South America", "North America",
    "Eurasia", "Middle East"]

    with open("A01023661-Database\populationbycountry19802010millions.csv") as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            if row[-1] not in value_errors and row[0] not in country_exceptions:
                population_2010.append([float(row[-1]), row[0]])

    population_2010.sort(reverse=True)
    print(population_2010[:5])

def Gas():
    gas = []
    value_errors = ["value","NA"]
    country_exceptions = ["World","Country", "Asia & Oceania", "Africa", "Europe", "Central & South America", "North America",
    "Eurasia", "Middle East"]

    with open("A01023661-Database\greenhouse_gas_inventory_data_data.csv") as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            if row[2] not in value_errors and row[0] not in country_exceptions:
                gas.append([str(row[2]), row[0], row[1]])

    gasf = [i for n, i in enumerate(gas) if i not in gas[:n]]
    gasf.sort(reverse=True)
    print(gasf[:5])


if __name__ == "__main__":

    print("The countries with most population are :\n")
    Pop()
    print("\nThe countries with most pollution and their respective years are : \n")
    Gas()

    print("\nTherefore, we can only attribute a correlation to the US")
    
    
   

    

def main():
    file = input("Name of textfile containing names (Separted by Commas): ")
    with open(f"{file}.txt") as f:
        splitNames = f.read().split(",")
        stripedNames = [name.strip().split(" ") for name in splitNames]
        lastNames = [[name[-1], stripedNames.index(name)] for name in stripedNames]
        lastNames.sort()
        sortedNames = [splitNames[lastName[-1]].strip("\n") for lastName in lastNames]
        for name in sortedNames:
            print(name)

if __name__ == "__main__":
    main()
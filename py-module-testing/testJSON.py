import json


def main():

    testDict = {
        "seth": 1,
        "tal": 2
    }

    print(type(testDict))
    print(testDict)

    with open("testjson.json", 'w') as jsonFile:
        json.dump(testDict, jsonFile, indent=2)

    with open("testjson.json", 'r') as jsonFile:
        newDict = json.load(jsonFile)
        print(type(newDict))
        print(newDict)


main()

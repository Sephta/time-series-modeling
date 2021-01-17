import pickle as pkl
# import sys


def main():

    testDict = {
        "seth": 1,
        "tal": 2
    }

    print(type(testDict))

    # binary-write to pickle file
    with open("testPickle.pickle", 'wb') as pickleFile:
        pkl.dump(testDict, pickleFile)

    with open("testPickle.pickle", 'r') as pickleFile:
        newDict = pkl.load(pickleFile)
        print(type(newDict))


# runs anything from main
main()

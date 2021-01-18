import pandas as pd
import sys


def main():
    # Read the file contents and print to console
    if (len(sys.argv) > 1):
        readCSV = pd.read_csv(f'./{sys.argv[1]}/{sys.argv[2]}')
        print(readCSV)
    else:
        readCSV = pd.read_csv('./py-module-testing/test.csv')
        print(readCSV)
        # with open("filetest.txt", 'wr') as file:
        #     pd.DataFrame.to_csv(file)


main()

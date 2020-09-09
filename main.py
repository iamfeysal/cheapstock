import numpy as np
import pandas as pd


def currency_iso_check():
    """CLI application that takes in currency (using ISO 4217 code)
    as an
    argument and displays whether or not the currency is
    supported in
    the application """

    csvdata = pd.read_csv('Stocks/Cheap.Stocks.Internationalization'
                          '.Currencies.csv')  # read the csv file

    data = csvdata[['Country', 'Currency', 'ISO 4217 Code']]  # display all
    # data for the specified items
    # print(data)

    all_data = data.values  # getting only the values of the date on the item
    # specified
    # print(all_data)

    for _ in all_data:  # the _ variable indicates that the loop variable isn't
        # actually used
        print('')
        user = input('Enter currency:')
        print('')
        currency_iso = (user in user in np.array(all_data)[:, 2])
        return currency_iso


def main():
    print('')
    print('Hi, welcome to our small stock command line interface')
    print('')

    while True:
        print(
            "Use these short codes:"
            "ccs - check currency support,"
            " help - help menu,"
            " exit - exit application")
        print('')
        short_code = input().lower()  # change input to lowercase
        print('')
        if short_code == 'ccs':
            if currency_iso_check():
                print('YES THIS CURRENCY IS SUPPORTED', )
                print('')
                break
            else:
                print('THIS CURRENCY IS NOT SUPPORTED\Kindly check your input '
                      'as the iso digits are case sensitive(they must be in '
                      'Capital Case ')
                print('')
                break

        elif short_code == 'help':
            print(
                "Welcome to the help menu. / we are still learning your likes")
            print('')
            break
        elif short_code == 'exit':
            print(
                "We hate you going!, but we love you taking break")
            print('')
            break
        else:
            print(
                "404 error, (Inputs not found) Kindly try using the short "
                "code "
                "provided for consistency")
            print('')


if __name__ == "__main__":
    main()

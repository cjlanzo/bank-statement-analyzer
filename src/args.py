import argparse

def parseArgs():
    parser = argparse.ArgumentParser(
        prog='StatementAnalyzer',
        description='Analyzes credit card and bank statements and formats them in excel'
    )

    parser.add_argument('-p', '--plugin', required=True, choices=['citi', 'cap_one', 'chase'])
    parser.add_argument('-f', '--filename', required=True)

    return parser.parse_args()
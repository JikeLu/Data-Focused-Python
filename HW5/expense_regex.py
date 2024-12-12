# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    records = []

    with open('expenses.txt') as f:
        for i in f:
            records.append(i.replace('\n', ''))

    # 1a
    # pat = r'D'

    # 1b
    # pat = r'\''

    # 1c
    # pat = r'\"'

    # 1d
    # pat = r'^7'

    # 1e
    # pat = r'[rt]$'

    # 1f
    # pat = r'\.'

    # 1g
    # pat = r'r.*g'

    # 1h
    # pat = r'([A-Z][A-Z])'

    # 1i
    # pat = r'\,'

    # 1j
    # pat = r'\,.*\,.*\,'

    # 1k
    # pat = r'^[^vwxyz]*$'

    # 1l
    # pat = r'^[1-9][0-9]\.[0-9][0-9]'

    # 1n
    # pat = r'\('

    # 1o
    # pat = r'^[1-9]\d{2,}\.\d+:meal'

    # 1p
    # pat = r'^\d+\.+\d+:\D{4}:.*$'

    # 1q
    # pat = r'^\d+\.+\d+:\D+:\d{4}03\d{2}:'

    # 1r
    # pat = r'a.*b.*c.*'

    # 1s
    # pat = r'r'(..).*\1.*\1.*''

    # 1t
    # pat = r'\d+\.+\d+:\D+:\d{8}:.*([0-9].*a|a.*[0-9])'

    # 1u
    # pat = r'^[^A-Z]*$'

    # 1v
    # pat = 'di|d.i'


    for line in records:
        if re.search(pat, line) != None:
            print(line)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

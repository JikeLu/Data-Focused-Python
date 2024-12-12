# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fl = open('expenses.txt', 'rt', encoding='utf-8')
    records = []
    for line in fl:
        records.append(line.strip())

    for line in records:
        print(line)
    fl.close

    fl2 = open('expenses.txt', 'rt', encoding='utf-8')
    records2 = [line.strip() for line in fl2]
    print("\nrecords == records2:",
                    records == records2, '\n')
    fl2.close

    fl3 = open('expenses.txt', 'rt', encoding='utf-8')
    records3 = tuple(tuple(line.strip().split(sep=":") for line in fl3))
    for tup in records3:
        print(tup)
    fl3.close

    cat_set = {tup[1] for tup in records3[1:]}
    date_set = {tup[2] for tup in records3[1:]}
    print('Categories:', cat_set, '\n')
    print('Dates:     ', date_set, '\n')

    rec_num_to_record = {k: v for (k, v) in zip(range(len(records3)), records3)}

    for rn in range(len(rec_num_to_record)):
        print('{:3d}: {}'.format(rn,
                                    rec_num_to_record[rn]))

    for i in rec_num_to_record.items():
        print('{:3d}: {}'.format(i[0], i[1]))


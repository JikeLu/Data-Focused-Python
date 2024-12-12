# Code completed by Jike Lu alone. Until 2 hours before due teammate didn't provide any support.

from datetime import datetime


def time_check(str):
    start = datetime(2021, 9, 1, 0, 0, 0)
    end = datetime(2023, 12, 31, 0, 0, 0)
    time = datetime.strptime(str, '%Y%m')
    if time >= start and time <= end:
        return True
    else:
        return False

def time(str):
    if len(str) == 6:
        time = datetime.strptime(str, '%Y%m')
        return time.strftime('%Y-%m')

    if len(str) == 8:
        time = datetime.strptime(str, '%Y%m%d')
        return time.strftime('%Y-%m-%d')

    return 0

def TypeB(type):
    B = []
    for i in type:
        if i[5:15] == 'CL        ' and i[15:18] == "FUT" and time_check(i[18:24]):
            B.append({'Futures Code': "CL",
                       'Contract Month': time(i[18:24]),
                       'Contract Type': "Fut",
                       'Futures Exp Date': time(i[91:99]),
                       'Options Exp Date': '',
                       'Options Code': ''})
        if i[5:15] == 'LO        ' and i[15:18] == "OOF" and time_check(i[18:24]):
            B.append({'Futures Code': 'CL',
                        'Contract Month': time(i[18:24]),
                        'Contract Type': 'Opt',
                        'Futures Exp Date': '',
                        'Options Exp Date': time(i[91:99]),
                        'Options Code': 'LO'})
            #print(B)
    return B

def Type81(type):
    CL = []
    LO = []
    for i in type:
        if i[5:15] == 'CL        ' and i[28:29] == ' ' and time_check(i[29:35]):
            CL.append({'Futures Code': 'CL',
                         'Contract Month': time(i[29:35]),
                         'Contract Type': 'Fut',
                         'Strike Price': '',
                         'Settlement Price': float(i[108:122])/100})
        if i[5:15] == 'LO        ' and i[28:29] != ' ' and time_check(i[29:35]):
            LO.append({'Futures Code': 'CL',
                         'Contract Month': time(i[29:35]),
                         'Contract Type': 'Call' if i[28:29] == 'C' else 'Put',
                         'Strike Price': float(i[47:54]) / 100,
                         'Settlement Price': float(i[108:122]) / 100})
    return CL + LO

def writedown(B, _81, f):
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format('Futures', 'Contract', 'Contract',
                                                                          'Futures', 'Options', 'Options') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format('Code', 'Month', 'Type', 'Exp Date',
                                                                          'Code', 'Exp Date') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format('-------', '--------', '--------',
                                                                          '----------', '-------', '--------') + '\n')
    for i in B:
        f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format(i['Futures Code'], i['Contract Month'],
                                                                              i['Contract Type'], i['Futures Exp Date'],
                                                                              i['Options Code'],
                                                                              i['Options Exp Date']) + '\n')

    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<6}   {4:<10}'.format('Futures', 'Contract', 'Contract', 'Strike',
                                                                 'Settlement') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<6}   {4:<10}'.format('Code', 'Month', 'Type', 'Price', 'Price') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<6}   {4:<10}'.format('-------', '--------', '--------', '------',
                                                                 '----------') + '\n')
    for i in _81:
        f.write('{0:<7}   {1:<8}   {2:<8}   {3:>6}   {4:>10.2f}'.format(str(i['Futures Code']), str(i['Contract Month']),
                                                                    str(i['Contract Type']),
                                                                    '' if i['Strike Price'] == '' else '%.2f' % float(i['Strike Price']),
                                                                    float(i['Settlement Price'])) + '\n')


if __name__ == '__main__':
    with open('cme.20210709.c.pa2', 'r') as fin:
        type_B = []
        type_81 = []
        for i in fin.readlines():
            t = i.replace('\n', '')
            if t.startswith('B '):
                type_B.append(t)
            if t.startswith('81'):
                type_81.append(t)
        #print(len(type_B), len(type_81))
        fin.close()
    TypeB = TypeB(type_B)
    Type81 = Type81(type_81)
    with open('CL_expirations_and_settlements.txt', 'w') as fout:
        writedown(TypeB, Type81, fout)
        fout.close()
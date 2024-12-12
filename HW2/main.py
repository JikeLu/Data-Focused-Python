# Author: Xiang Tan, Alexander Chen

# CL: Future code: [5:15] == "CL        "
#     Contract Month: [18:24]
#     Contract Type: [15:18]
#     Expire Date: [91:99]
#     Option Code: Null
#     Options Exp: Null

# LO: Future Code: null
#     Contract Month: [18:24]
#     Contract Type: [15；18] == "OOF"
#     Expire Date: null
#     Option Code：[5:15] == "LO        "
#     Option ExpireDate: [91:99]

# 81f:Future Code: [5:15] == 'CL        '
#     Contract Month: [29:35]
#     Contract Type: [25:28] == 'FUT' IF NO p and c
#     Strike Price:
#     Settlement Price: [108:122]

# 81O: Future Code: [5:15] == 'CL        '
#      Contract Month: [29:35]
#      Contract Type: [28:29] == call put if p c exists ' '
#      Strike Price: [47:55] if p c exits
#      Settlement Price: [108:122]


# filter the time domain
def time_filter(timestr):
    from datetime import datetime
    starttime = datetime(2021, 8, 31, 0, 0, 0)
    endtime = datetime(2023, 12, 31, 0, 0, 0)

    if len(timestr) == 6:
        timeo = datetime.strptime(timestr, '%Y%m')
        if timeo > starttime and timeo < endtime:
            return True, timeo.strftime('%Y-%m')

    if len(timestr) == 8:
        timeo = datetime.strptime(timestr, '%Y%m%d')
        return True, timeo.strftime('%Y-%m-%d')

    return False, 0


# deal with float
def dealWithFloat(i):
    if i == '':
        return ''
    else:
        return '%.2f' % float(i)


# correct type
def correctType(ct):
    if 'C' in ct and 'O' in ct:
        return 'Call'
    if 'P' in ct and 'O' in ct:
        return 'Put'
    if 'F' in ct:
        return 'Fut'


# 8 for strike 2 for settlement
def correctPrice(s, a):
    return str(int(s) / 10 ** a)


# output TypeB
def writeTypeB(tableB, f):
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format('Futures', 'Contract', 'Contract',
                                                                          'Futures', 'Options', 'Options') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format('Code', 'Month', 'Type', 'Exp Date',
                                                                          'Code', 'Exp Date') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format('-------', '--------', '--------',
                                                                          '----------', '-------', '--------') + '\n')
    for i in tableB:
        f.write('{0:<7}   {1:<8}   {2:<8}   {3:<10}   {4:<7}   {5:<8}'.format(i['Futures Code'], i['Contract Month'],
                                                                              i['Contract Type'], i['Futures Exp Date'],
                                                                              i['Options Code'],
                                                                              i['Options Exp Date']) + '\n')


# output Type81
def writeType81(table81, f):
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<6}   {4:<10}'.format('Futures', 'Contract', 'Contract', 'Strike',
                                                                 'Settlement') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<6}   {4:<10}'.format('Code', 'Month', 'Type', 'Price', 'Price') + '\n')
    f.write('{0:<7}   {1:<8}   {2:<8}   {3:<6}   {4:<10}'.format('-------', '--------', '--------', '------',
                                                                 '----------') + '\n')
    for i in table81:
        f.write(
            '{0:<7}   {1:<8}   {2:<8}   {3:>6}   {4:>10.2f}'.format(str(i['Futures Code']), str(i['Contract Month']),
                                                                    str(i['Contract Type']),
                                                                    dealWithFloat(i['Strike Price']),
                                                                    float(i['Settlement Price'])) + '\n')


# extract typeB and type81 into two lists
def load_source():
    with open('cme.20210709.c.pa2', 'r') as f:
        type_B = []
        type_81 = []
        type = []
        for i in f.readlines():
            t = i.replace('\n', '')
            if t.startswith('B '):
                type_B.append(t)
            if t.startswith('81'):
                type_81.append(t)
        print(len(type_B), len(type_81))
        return type_B, type_81


# process typeB
def processTypeB(typeB):
    tableB = [{'Futures Code': "CL",
               'Contract Month': time_filter(i[18:24])[1],
               'Contract Type': correctType(i[15:18]),
               'Futures Exp Date': time_filter(i[91:99])[1],
               'Options Exp Date': '',
               'Options Code': ''} for i in typeB if i[5:15] == 'CL        ' and time_filter(i[18:24])[0]] + [
                 {'Futures Code': 'CL',
                  'Contract Month': time_filter(i[18:24])[1],
                  'Contract Type': 'Opt',
                  'Futures Exp Date': '',
                  'Options Exp Date': time_filter(i[91:99])[1],
                  'Options Code': 'LO'} for i in typeB if
                 i[5:15] == 'LO        ' and i[15:18] == "OOF" and time_filter(i[18:24])[0]]
    print(tableB)
    return tableB


def processType81(type81):
    table811 = [{'Futures Code': 'CL',
                 'Contract Month': time_filter(i[29:35])[1],
                 'Contract Type': 'Fut',
                 'Strike Price': '',
                 'Settlement Price': correctPrice(i[108:122], 2)} for i in type81 if
                i[5:15] == 'CL        ' and i[28:29] == ' ' and time_filter(i[29:35])[0]]

    table812 = [{'Futures Code': 'CL',
                 'Contract Month': time_filter(i[29:35])[1],
                 'Contract Type': 'Call' if i[28:29] == 'C' else 'Put',
                 'Strike Price': correctPrice(i[47:54], 2),
                 'Settlement Price': correctPrice(i[108:122], 2)} for i in type81 if
                i[5:15] == 'LO        ' and i[28:29] != ' ' and time_filter(i[29:35])[0]]
    return table811 + table812


def output(processedTypeB, processedType81):
    with open('correct.txt', 'w') as f:
        writeTypeB(processedTypeB, f)
        writeType81(processedType81, f)


def runPipeline():
    typeB, type81 = load_source()
    output(processTypeB(typeB), processType81(type81))


# Here we go!
if __name__ == '__main__':
    runPipeline()



import re

def getApp(filename):
    
    lgName = ''
    llName = ''
    pgName = ''
    email = ''
    address = ''
    gender = ''
    isUgrad = ''
    inst = ''
    prog = ''
    gradDate = ''
    year = ''
    referal = ''
    prev = ''
    where = ''
    cost = ''
    support = ''
    depSupport = ''
    why = ''
    
    
    f = open(filename, 'r')
    for line in f:
        pattern = re.compile("[0-9][0-9]")
        if pattern.match(line[0:2]):
            if line[0:2] == "00":
                lgName = line[3:len(line)-2]
            elif line[0:2] == "01":
                llName = line[3:len(line)-2]
            elif line[0:2] == "02":
                pgName = line[3:len(line)-2]
            elif line[0:2] == "03":
                email = line[3:len(line)-2]
            elif line[0:2] == "04":
                address = line[3:len(line)-2]
            elif line[0:2] == "05":
                gender = line[3:len(line)-2]
            elif line[0:2] == "06":
                isUgrad = line[3:len(line)-2]
            elif line[0:2] == "07":
                inst = line[3:len(line)-2]
            elif line[0:2] == "08":
                prog = line[3:len(line)-2]
            elif line[0:2] == "09":
                gradDate = line[3:len(line)-2]
            elif line[0:2] == "10":
                year = line[3:len(line)-2]
            elif line[0:2] == "11":
                referal = line[3:len(line)-2]
            elif line[0:2] == "12":
                prev = line[3:len(line)-2]
            elif line[0:2] == "13":
                where = line[3:len(line)-2]
            elif line[0:2] == "14":
                cost = line[3:len(line)-2]
            elif line[0:2] == "15":
                support = line[3:len(line)-2]
            elif line[0:2] == "16":
                depSupport = line[3:len(line)-2]
            elif line[0:2] == "17":
                why = line[3:len(line)-2]
    
    return {
        'name' : llName + ", " + pgName,
        'legName' : llName + ", " + lgName,
        'lgName' : lgName,
        'llName' : llName,
        'pgName' : pgName,
        'email' : email,
        'address' : address,
        'gender' : gender,
        'isUgrad' : isUgrad,
        'inst' : inst,
        'prog' : prog,
        'gradDate' : gradDate,
        'year' : year,
        'referal' : referal,
        'prev'  : prev,
        'where' : where,
        'cost' : cost,
        'support' : support,
        'depSupport' : depSupport,
        'why' : why}

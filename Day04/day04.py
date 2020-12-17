import sys
import re 


# input in lines
wholeInput = sys.stdin.read()
lst = wholeInput.split("\n\n")
length = len(lst)

nValid = 0

# go through all passports

for i in range(0, length):
    # split by either space or new line
    lst[i] = re.split(' |\n', lst[i])

    # check that it has all the required fields (ignoring country)
    if (len(lst[i]) < 7):
        continue
    
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    for line in range(0, len(lst[i])):
        data = lst[i][line].split(':')
        field = data[0]
        val = data[1] 

        if (field == "byr"):
            # 4 digits between 1920 and 2002
            if (val.isdigit() and int(val) >= 1920 and int(val) <= 2002):
                byr = True
        if (field == "iyr"):
            if (val.isdigit() and int(val) >= 2010 and int(val) <= 2020):
                iyr = True
        if (field == "eyr"):
            if (val.isdigit() and int(val) >= 2020 and int(val) <= 2030):
                eyr = True
        if (field == "hgt"):
            if (re.search("^[0-9]{3}cm$", val) != None):
                if (int(val[0:3]) >= 150 and int(val[0:3]) <= 193):
                    hgt = True
            if (re.search("^[0-9]{2}in$", val) != None):
                if (int(val[0:2]) >= 59 and int(val[0:2]) <= 76):
                    hgt = True
        if (field == "hcl"):
            if (re.search("^#[0-9a-f]{6}$", val) != None):
                hcl = True
        if (field == "ecl"):
            if (re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", val) != None):
                ecl = True
        if (field == "pid"):
            if (re.search("^[0-9]{9}$", val) != None):
                pid = True
        
    # add to nValid if its valid
    if (byr and iyr and eyr and hgt and hcl and ecl and pid):
        nValid += 1
        print(lst[i])

print(nValid)
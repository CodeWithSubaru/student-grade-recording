import re
from os import system
from func.Sanitize import sanitize


class Database:

    recordCopy = dict()

    # gets the data by its match regex
    def get(self, record):
        with open('./db/students_record.txt', 'r') as db:
            x = db.read()

            dataRecords = {
                "s_no": sanitize(re.findall(r"Id: \b\d+", x), 4),
                "firstName": sanitize(re.findall(r"First Name: \b\w+.+", x), 12),
                "middleName": sanitize(re.findall(r"Middle Name: \b\w+.+", x), 13),
                "lastName": sanitize(re.findall(r"Last Name: \b\w+.+", x), 11),
                "firstSem": re.findall(r"1st Semester", x),
                "firstSemPrelims": sanitize(re.findall(r"1st Sem Prelims: \D|1st Sem Prelims: \b\d\.\d", x), 17),
                "firstSemMidTerm": sanitize(re.findall(r"1st Sem Mid Term: \D|1st Sem Mid Term: \b\d\.\d", x), 18),
                "firstSemFinals": sanitize(re.findall(r"1st Sem Finals: \D|1st Sem Finals: \b\d\.\d", x), 16),
                "secondSem": re.findall(r"2nd Semester", x),
                "secondSemPrelims": sanitize(re.findall(r"2nd Sem Prelims: \D|2nd Sem Prelims: \b\d\.\d", x), 17),
                "secondSemMidTerm": sanitize(re.findall(r"2nd Sem Mid Term: \D|2nd Sem Mid Term: \b\d\.\d", x), 18),
                "secondSemFinals": sanitize(re.findall(r"2nd Sem Finals: \D|2nd Sem Finals: \b\d\.\d", x), 16)
            }

            # to make a copy to our record
            self.recordCopy = dataRecords.copy()

            return dataRecords.get(record)

    # write record in txt file using append mode
    def writeRecord(self, s_no='', firstName='', middleName='', lastName='',
                    firstSemPrelims="", firstSemMidTerm="", firstSemFinals="",
                    secondSemPrelims="", secondSemMidTerm="", secondSemFinals=""):

        with open('./db/students_record.txt', "a") as db:
            db.write(f'Id: {s_no}\n')
            db.write(f'First Name: {firstName}\n')
            db.write(f'Middle Name: {middleName}\n')
            db.write(f'Last Name: {lastName}\n')
            db.write(f'1st Semester\n')
            db.write(f'1st Sem Prelims: {firstSemPrelims}\n')
            db.write(f'1st Sem Mid Term: {firstSemMidTerm}\n')
            db.write(f'1st Sem Finals: {firstSemFinals}\n')
            db.write(f'2nd Semester\n')
            db.write(f'2nd Sem Prelims: {secondSemPrelims}\n')
            db.write(f'2nd Sem Mid Term: {secondSemMidTerm}\n')
            db.write(f'2nd Sem Finals: {secondSemFinals}\n\n')

    # for updating record in txt file using write mode
    def updateRecord(self):

        with open('./db/students_record.txt', 'w') as db:
            for i in range(len(self.recordCopy.get('s_no'))):

                db.write(f'Id: {self.recordCopy.get("s_no")[i]}\n')
                db.write(
                    f'First Name: {self.recordCopy.get("firstName")[i]}\n')
                db.write(
                    f'Middle Name: {self.recordCopy.get("middleName")[i]}\n')
                db.write(f'Last Name: {self.recordCopy.get("lastName")[i]}\n')
                db.write(f'1st Semester\n')
                db.write(
                    f'1st Sem Prelims: {self.recordCopy.get("firstSemPrelims")[i]}\n')
                db.write(
                    f'1st Sem Mid Term: {self.recordCopy.get("firstSemMidTerm")[i]}\n')
                db.write(
                    f'1st Sem Finals: {self.recordCopy.get("firstSemFinals")[i]}\n')
                db.write(f'2nd Semester\n')
                db.write(
                    f'2nd Sem Prelims: {self.recordCopy.get("secondSemPrelims")[i]}\n')
                db.write(
                    f'2nd Sem Mid Term: {self.recordCopy.get("secondSemMidTerm")[i]}\n')
                db.write(
                    f'2nd Sem Finals: {self.recordCopy.get("secondSemFinals")[i]}\n\n')
    
    # automatically generate new id
    def generateId(self, studentId):

        if not studentId:
            studentId = 1
        else:
            studentId = int(studentId[-1])
            studentId += 1
        return studentId

class Student(Database):

    def updateRecord(self):
        return super().updateRecord()

    def writeRecord(self, s_no='', firstName='', middleName='', lastName='', firstSemPrelims="", firstSemMidTerm="", firstSemFinals="", secondSemPrelims="", secondSemMidTerm="", secondSemFinals=""):
        return super().writeRecord(s_no, firstName, middleName, lastName, firstSemPrelims, firstSemMidTerm, firstSemFinals, secondSemPrelims, secondSemMidTerm, secondSemFinals)

    # gets the length of student id
    def s_noLength(self):
        return len(self.get('s_no'))


class Interface:

    cycle = True
    tryAgain = True

    def clear():
        return system('cls')

    def patternLineLong():
        print('\n**----------=========*^*=========----------**\n')

    def patternLineShort():
        print('\n**------=====*^*=====------**\n')

    def space(numberOfSpace):
        for i in range(numberOfSpace + 1):
            print()
    
    def box(self, inputs, num=0):
        print(f"  ╔════════════════════════════╗")
        print(f" ║".ljust(30) + "  ║")
        print(f" ║".ljust(30) + "  ║")
        if type(inputs) == list:
            for i in inputs:
                print(f"║".center(3) + f" {i}".center(18) + "║".center(num))
        else:
            print(f" ║".ljust(4) +
                  f" *{inputs}* ".center(18) + "    ║".center(num))
        print(f" ║".ljust(30) + "  ║")
        print(f" ║".ljust(30) + "  ║")
        print(f"  ╚════════════════════════════╝")

    def boxB(self, inputs, num=0):
        print(f"  ╔═══════════════════════════════════════════╗")
        print(f" ║".ljust(44) + "   ║")
        print(f" ║".ljust(44) + "   ║")
        if type(inputs) == list:
            for i in inputs:
                print(f"║".center(3) + f" {i}".center(42) + "║".center(num))
        else:
            print(f"║".center(3) + f" *{inputs}*".center(42) + "║".center(num))
        print(f" ║".ljust(44) + "   ║")
        print(f" ║".ljust(44) + "   ║")
        print(f"  ╚═══════════════════════════════════════════╝")

    def tryagain(self):
        again = input(f'Try Again [Y/N] : ')

        if(again.title() == "Y"):
            return True

        elif(again.title() == "N"):
            return False

        else:
            return False

    def inp(self, txt):
        return input(f"Press <enter> to {txt}... \n → ")

    # confirmation if record is ok
    def yesOrNo(self, option):
        option = option.title()

        if(option == 'Y'):
            return True
        elif option or not option:
            return False


    def raiseError(self, checkInp, errorMes):
        try:
            if not checkInp:
                raise ValueError(errorMes)
            else:
                return True
        except ValueError as e:
            print(f' * Please enter your {e} *')

# End of class


def homepage():

    interf = Interface()

    while interf.cycle:
        Interface.clear()
        Interface.patternLineLong()
        print('Welcome To Student Grade Recording!'.center(50))
        Interface.patternLineLong()
        Interface.space(1)
        
        interf.boxB([
            '   * Enter your Operations *',
            '→ [ V ] View record',
            '     → [ A ] Add Name / Grade',
            '  → [ U ] Update Grade',
            '  → [ D ] Delete record',
            '  → [ E ] Exit Program'
        ], 6)
        std = Student()
        option = interf.inp('confirm')

        option = option.title()
        if option == 'V':
            viewStudentRecords()
        elif option == 'A':
            Interface.clear()
            Interface.space(2)
            interf.boxB([' * Choose Your Operation *', ' ', '[ 1 ] Add Name of Student'.ljust(
                35), ' [ 2 ] Add / Update Grade of Student'], 6)
            option = interf.inp('confirm')

            if option == "1":
                addStudentsName()
            elif option == "2":
                addStudentsGrade()

        elif option == 'U':
            updateSpecificGrade()

        elif option == 'D':
            deleteRecord()

        elif option == 'E' or not option or option:
            Interface.clear()
            Interface.space(3)
            print('         > Program Terminated... Come Again! <    ')
            Interface.space(3)
            interf.cycle = False


def viewStudentRecords():

    std = Student()
    interf = Interface()

    Interface.clear()

    Interface.space(2)

    if std.s_noLength() < 1:
        interf.boxB(' Sorry, There\'s Nothing in Here ', 5)
    else:

        interf.boxB('Here are your List of Students!', 6)
        print(" ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print('|'.center(4) + f"".center(5), "|".center(4),
              f"".ljust(50) + "|".ljust(2), f"".center(15),
              f"{std.get('firstSem')[0]}".center(15), f"".center(19) + "|".ljust(2),
              f"".center(15), f"{std.get('secondSem')[0]}".center(15),
              f"".center(19) + "|".ljust(2))

        print("|".center(4) + f"".center(5), "|".center(4),
              f"".ljust(50) + "|",
              f"--------------------------------------------------------------------------------------------------------- |")

        print('|'.center(4) + f"No.".center(5), "|".center(4),
              f"Name".ljust(50) +
              "|".ljust(2), f"Prelims".center(15) + "|".ljust(2),
              f"Mid Term".center(15) + "|".ljust(2), f"Finals".center(15) + "|".ljust(2),
              f"Prelims".center(15) + "|".ljust(2), f"Mid Term".center(15) + "|".ljust(2),
            f"Finals".center(15) + "|".ljust(2))

        print(" -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        for u in range(std.s_noLength()):
            print(
                '|'.center(4) +
                f"{std.get('s_no')[u]}".center(5), "|".center(4),
                f"{std.get('lastName')[u]} , {std.get('firstName')[u]} {std.get('middleName')[u]}".ljust(
                    50)
                + "|".ljust(2),
                f"{std.get('firstSemPrelims')[u]}".center(
                    15) + "|".ljust(2),
                f"{std.get('firstSemMidTerm')[u]}".center(
                        15) + "|".ljust(2),
                f"{std.get('firstSemFinals')[u]}".center(15) + "|".ljust(2),
                f"{std.get('secondSemPrelims')[u]}".center(
                        15) + "|".ljust(2),
                f"{std.get('secondSemMidTerm')[u]}".center(
                        15) + "|".ljust(2),
                f"{std.get('secondSemFinals')[u]}".center(15) + "|"
            )
            print(" -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    interf.inp('exit')


def addStudentsName():

    std = Student()
    interf = Interface()

    Interface.clear()
    Interface.space(1)
    interf.boxB('Enter your Student\'s Last Name', 6)
    lastName = interf.inp('confirm').title()
    Interface.space(2)

    Interface.space(1)
    interf.boxB('Enter your Student\'s First Name', 6)
    firstName = interf.inp('confirm').title()
    Interface.space(2)

    Interface.space(1)
    interf.boxB('Enter your Student\'s Middle Name', 6)
    middleName = interf.inp('confirm').title()

    last = interf.raiseError(lastName, 'Last Name')
    first = interf.raiseError(firstName, 'First Name')
    middle = interf.raiseError(middleName, 'Middle Name')

    if lastName in std.get('lastName') and firstName in std.get('firstName') and middleName in std.get('middleName'):
        Interface.space(3)
        interf.boxB(
            ['Sorry but', f'{lastName}, {firstName} {middleName}', 'already exists!'], 5)
        interf.inp('exit')
    elif last and first and middle:
        Interface.space(3)
        interf.boxB([f'Are you sure you want to add as',
                    f'{lastName}, {firstName} {middleName}', ' ', '[ Y ] Yes', '[ N ] No'], 6)
        option = interf.inp('confirm')
        Interface.space(3)

        yesOrNo = interf.yesOrNo(option)

        if yesOrNo:
            userId = std.generateId(std.get('s_no'))
            std.writeRecord(userId, firstName, middleName, lastName)
            interf.box(' Added succesfully! ', 5)
        else:
            interf.box('Operation Cancelled!')

        interf.cycle = interf.inp('exit')
    else:
        interf.tryAgain = interf.tryagain()
        if interf.tryAgain:
            addStudentsName()


def addStudentsGrade():
    std = Student()
    interf = Interface()

    Interface.clear()

    if std.s_noLength() >= 1:

        # Table
        Interface.space(2)
        print(" -----------------------------------------------------------------")
        print('|'.center(4) + f"Id".center(5),
              "|".center(4), f"Name".ljust(50) + "|")
        print(" -----------------------------------------------------------------")
        for u in range(std.s_noLength()):
            print('|'.center(4) + f"{std.get('s_no')[u]}".center(5), "|".center(4),
                  f"{std.get('lastName')[u]} , {std.get('firstName')[u]} {std.get('middleName')[u]}".ljust(50) +
                  "|".ljust(2))
            print(" -----------------------------------------------------------------")

        Interface.space(2)
        interf.boxB('Enter your Student\'s Id', 5)
        studentId = interf.inp('confirm')
        Interface.space(2)

        if studentId in std.get('s_no'):

            # Get Student Id
            s_no = std.get('s_no').index(studentId)

            interf.boxB(['* Enter your semester *',
                        '[ 1 ] First Semester', '[ 2 ] Second Semester'], 5)
            sem = interf.inp('confirm')
            Interface.space(2)

            if sem == "1":

                Interface.space(2)
                print(f" Id: {std.get('s_no')[s_no]}")
                print(f" Student Name: {std.get('lastName')[s_no]}, " +
                      f"{std.get('firstName')[s_no]} {std.get('middleName')[s_no][:1]}.")

                if std.get('firstSemPrelims')[s_no]:
                    print(
                        f" Current First Sem Prelims: {std.get('firstSemPrelims')[s_no]}")
                    Interface.space(1)

                interf.boxB('Enter your Student\'s Prelims', 5)
                firstSemPrelims = interf.inp('confirm')
                Interface.space(2)

                if std.get('firstSemMidTerm')[s_no]:
                    print(
                        f" Current First Sem Mid Term: {std.get('firstSemMidTerm')[s_no]}")
                    Interface.space(1)

                interf.boxB('Enter your Student\'s Mid Term', 5)
                firstSemMidTerm = interf.inp('confirm')
                Interface.space(2)

                if std.get('firstSemFinals')[s_no]:
                    print(
                        f" Current First Sem Finals: {std.get('firstSemFinals')[s_no]}")
                    Interface.space(1)

                interf.boxB('Enter your Student\'s Finals', 5)
                firstSemFinals = interf.inp('confirm')
                Interface.space(2)

                Interface.space(3)

                interf.boxB([
                    f'Are you sure you want to add as follow:',
                    f'Prelims: {firstSemPrelims}',
                    f'Mid Term: {firstSemMidTerm}',
                    f'Finals: {firstSemFinals}',
                    ' ',
                    '[ Y ] Yes',
                    '[ N ] No'
                ], 6)

                option = interf.inp('confirm')
                yesOrNo = interf.yesOrNo(option)

                if yesOrNo:
                    std.recordCopy.get('firstSemPrelims')[
                        s_no] = firstSemPrelims
                    std.recordCopy.get('firstSemMidTerm')[
                        s_no] = firstSemMidTerm
                    std.recordCopy.get('firstSemFinals')[s_no] = firstSemFinals
                    std.updateRecord()
                    Interface.space(2)
                    interf.box('Added succesfully!', 10)
                    interf.inp('exit')

                else:
                    Interface.clear()
                    interf.box('Operation Cancelled!')
                    interf.tryAgain = interf.tryagain()
                    if interf.tryAgain:
                        addStudentsGrade()

            elif sem == '2':

                if std.get('secondSemPrelims')[s_no]:
                    print(
                        f" Current Second Sem Prelims: {std.get('secondSemPrelims')[s_no]}")
                    Interface.space(1)

                interf.boxB('Enter your Student\'s Prelims', 5)
                secondSemPrelims = interf.inp('confirm')
                Interface.space(2)

                if std.get('secondSemMidTerm')[s_no]:
                    print(
                        f" Current Second Sem Mid Term: {std.get('secondSemMidTerm')[s_no]}")
                    Interface.space(1)

                interf.boxB('Enter your Student\'s Mid Term', 5)
                secondSemMidTerm = interf.inp('confirm')
                Interface.space(2)

                if std.get('secondSemFinals')[s_no]:
                    print(
                        f" Current Second Sem Finals: {std.get('secondSemFinals')[s_no]}")
                    Interface.space(1)

                interf.boxB('Enter your Student\'s Finals', 5)
                secondSemFinals = interf.inp('confirm')
                Interface.space(2)

                Interface.space(3)
                interf.boxB([
                    f'Are you sure you want to add as follow:',
                    f'Prelims: {secondSemPrelims}',
                    f'Mid Term: {secondSemMidTerm}',
                    f'Finals: {secondSemFinals}',
                    ' ',
                    '[ Y ] Yes',
                    '[ N ] No'
                ], 6)
                option = interf.inp('confirm')
                yesOrNo = interf.yesOrNo(option)

                if yesOrNo:
                    std.recordCopy.get('secondSemPrelims')[
                        s_no] = secondSemPrelims
                    std.recordCopy.get('secondSemMidTerm')[
                        s_no] = secondSemMidTerm
                    std.recordCopy.get('secondSemFinals')[
                        s_no] = secondSemFinals
                    std.updateRecord()
                    Interface.space(2)
                    interf.box('Added succesfully!', 10)
                    interf.inp('exit')

                else:
                    Interface.clear()
                    interf.box('Operation Cancelled!')
                    interf.tryAgain = interf.tryagain()
                    if interf.tryAgain:
                        addStudentsGrade()
            else:

                print(f' * Invalid Option! *')
                interf.tryAgain = interf.tryagain()
                if interf.tryAgain:
                    addStudentsGrade()

        else:
            if studentId:
                print(f' * Student Id: {studentId} not found! *')
            else:
                interf.raiseError(studentId, 'Student Id')

            
            interf.tryAgain = interf.tryagain()
            if interf.tryAgain:
                addStudentsGrade()
    else:
        Interface.space(2)
        print(f' * Add Name of Student First! *')
        interf.inp('exit')


def updateSpecificGrade():
    std = Student()
    interf = Interface()

    # Table
    Interface.clear()
    Interface.space(2)
    if std.s_noLength() >= 1:
        print(" -----------------------------------------------------------------")
        print('|'.center(4) + f"Id".center(5),
            "|".center(4), f"Name".ljust(50) + "|")
        print(" -----------------------------------------------------------------")
        for u in range(std.s_noLength()):
            print('|'.center(4) + f"{std.get('s_no')[u]}".center(5), "|".center(4),
                f"{std.get('lastName')[u]} , {std.get('firstName')[u]} {std.get('middleName')[u][:1]}.".ljust(50) +
                "|".ljust(2))
            print(" -----------------------------------------------------------------")

        Interface.space(2)
        interf.boxB('Enter your Student\'s Id', 5)
        studentId = interf.inp('confirm')
        Interface.space(2)

        if studentId in std.get('s_no'):

            # Get Student Id
            s_no = std.get('s_no').index(studentId)

            interf.boxB(['* Enter your semester *',
                        '[ 1 ] First Semester', '[ 2 ] Second Semester'], 5)
            sem = interf.inp('confirm')
            Interface.space(2)

            interf.boxB(['* Enter your Grading Period *',
                        '[ 1 ] Prelims', '  [ 2 ] Mid Term', '[ 3 ] Finals'], 5)
            gradingPeriod = interf.inp('confirm')
            Interface.space(2)

            if sem == "1":

                if gradingPeriod == '1':
                    if std.get('firstSemFinals')[s_no]:
                        print(
                            f" Current First Sem Prelims: {std.get('firstSemPrelims')[s_no]}")

                    interf.boxB('Enter your Student\'s Prelims', 5)
                    firstSemPrelims = interf.inp('confirm')
                    Interface.space(2)
                    std.recordCopy.get('firstSemPrelims')[s_no] = firstSemPrelims

                elif gradingPeriod == '2':
                    if std.get('firstSemFinals')[s_no]:
                        print(
                            f" Current First Sem Mid Term: {std.get('firstSemMidTerm')[s_no]}")

                    interf.boxB('Enter your Student\'s Mid Term', 5)
                    firstSemMidTerm = interf.inp('confirm')
                    Interface.space(2)
                    std.recordCopy.get('firstSemMidTerm')[s_no] = firstSemMidTerm

                elif gradingPeriod == '3':

                    if std.get('firstSemFinals')[s_no]:
                        print(
                            f" Current First Sem Finals: {std.get('firstSemFinals')[s_no]}")

                    interf.boxB('Enter your Student\'s Finals', 5)
                    firstSemFinals = interf.inp('confirm')
                    Interface.space(2)
                    std.recordCopy.get('firstSemFinals')[s_no] = firstSemFinals

            elif sem == '2':
                if gradingPeriod == '1':
                    if std.get('secondSemPrelims')[s_no]:
                        print(
                            f" Current Second Sem Prelims: {std.get('secondSemPrelims')[s_no]}")

                    interf.boxB('Enter your Student\'s Prelims', 5)
                    secondSemPrelims = interf.inp('confirm')
                    Interface.space(2)
                    std.recordCopy.get('secondSemPrelims')[s_no] = secondSemPrelims

                elif gradingPeriod == '2':
                    if std.get('secondSemMidTerm')[s_no]:
                        print(
                            f" Current Second Sem Mid Term: {std.get('secondSemMidTerm')[s_no]}")

                    interf.boxB('Enter your Student\'s Mid Term', 5)
                    secondSemMidTerm = interf.inp('confirm')
                    Interface.space(2)
                    std.recordCopy.get('secondSemMidTerm')[s_no] = secondSemMidTerm

                elif gradingPeriod == '3':
                    if std.get('secondSemFinals')[s_no]:
                        print(
                            f" Current Second Sem Finals: {std.get('secondSemFinals')[s_no]}")

                    interf.boxB('Enter your Student\'s Finals', 5)
                    secondSemFinals = interf.inp('confirm')
                    Interface.space(2)
                    std.get('secondSemFinals')[s_no] = secondSemFinals


            else:
                print(f' * Invalid Option! *')
                interf.tryAgain = interf.tryagain()
                if interf.tryAgain:
                    addStudentsGrade()
            
            std.updateRecord()
            print(' Record Updated succesfully! ')
            interf.inp('exit')

        else:
            if studentId:
                print(f' * Student Id: {studentId} not found! *')
                interf.inp('exit')
            else:
                interf.raiseError(studentId, 'Student Id')
                interf.inp('exit')

    else:
        print(f' * Add Name of Student First! *')
        interf.inp('exit')
        

def deleteRecord():
    std = Student()
    interf = Interface()

    # Table
    Interface.clear()
    Interface.space(2)
    if std.s_noLength() >= 1:
        print(" -----------------------------------------------------------------")
        print('|'.center(4) + f"Id".center(5),
            "|".center(4), f"Name".ljust(50) + "|")
        print(" -----------------------------------------------------------------")
        for u in range(std.s_noLength()):
            print('|'.center(4) + f"{std.get('s_no')[u]}".center(5), "|".center(4),
                f"{std.get('lastName')[u]} , {std.get('firstName')[u]} {std.get('middleName')[u][:1]}.".ljust(50) +
                "|".ljust(2))
            print(" -----------------------------------------------------------------")

        delete = input('What do you want to delete: ')

        if delete in std.recordCopy.get('s_no'):

            delete = std.recordCopy.get('s_no').index(delete)

            firstName = std.recordCopy.get('firstName').pop(delete)
            middleName = std.recordCopy.get('middleName').pop(delete)
            lastName = std.recordCopy.get('lastName').pop(delete)

            Interface.space(3)
            interf.boxB([f"Are you sure you want to delete",
                        f"{lastName}, {firstName} {middleName}"], 6)
            option = interf.inp('confirm')
            yesOrNo = interf.yesOrNo(option)
            Interface.space(3)

            if yesOrNo:
                std.recordCopy.get('firstSem').pop(delete)
                std.recordCopy.get('firstSemPrelims').pop(delete)
                std.recordCopy.get('firstSemMidTerm').pop(delete)
                std.recordCopy.get('firstSemFinals').pop(delete)
                std.recordCopy.get('secondSem').pop(delete)
                std.recordCopy.get('secondSemPrelims').pop(delete)
                std.recordCopy.get('secondSemMidTerm').pop(delete)
                std.recordCopy.get('secondSemFinals').pop(delete)
                std.recordCopy.get('s_no').pop(delete)
                std.updateRecord()
                print(' * Record deleted succesfully! *')
                interf.inp('exit')
                

            else:
                interf.box('Operation Cancelled!')
                interf.inp('exit')
                

        elif not delete:
            interf.raiseError(delete, 'Id')

            interf.tryAgain = interf.tryagain()
            if interf.tryAgain:
                deleteRecord()

        else:
            print(f' * Student\'s Id {delete} not found! *')
            interf.inp('exit')
            

    else:
        print(f' * Add Name of Student First! *')
        interf.inp('exit')


if __name__ == '__main__':
    homepage()
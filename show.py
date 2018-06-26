from abc import ABC, abstractmethod, ABCMeta

class showType(metaclass=ABCMeta):

    @abstractmethod
    def show(self, Logfunc):
        pass

class showStandard(showType):

    def show(self, Logfunc):
    # formate the printed Output
        Name = Logfunc.Name
        Input = Logfunc.getInput()
        Output = Logfunc.getOutput()
        Type = type(Logfunc).__name__


        Length = [len(Output)*3 + 23, len(Input)*3 + 23, len(Name) + 23, len(Type) + 23, len('Standard') + 6]
        Length.sort(key=int, reverse=True)

        cwidth = int(Length[0])
        
        InputShow = ''
        for x in range(len(Input)):
            if x != len(Input)-1:
                InputShow += str(Input[x]) + ', '
            else:
                InputShow += str(Input[x])

        OutputShow = ''
        for x in range(len(Output)):
            if x != len(Output)-1:
                OutputShow += str(Output[x]) + ', '
            else:
                OutputShow += str(Output[x])

        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:^{0}}} --".format(cwidth-6)

        print(first_last)
        print(format_string.format("Standard"))
        print(first_last)

        format_string = "-- {{0:15}}: {{1:{0}}} --".format(cwidth-23)
        print(format_string.format("Name", Name))
        print(format_string.format("Type", Type))
        print(format_string.format("Input", str(InputShow)))
        print(format_string.format("True Inputs", str(Input.count(1))))
        print(format_string.format("False Inputs", str(Input.count(0))))
        print(format_string.format("Output", str(OutputShow)))
        print(first_last)
        print("\n")

class showAddition(showType):


    def show(self, Logfunc):
        
        Name = Logfunc.Name
        Input = Logfunc.getInput()
        Output = Logfunc.getOutput()
        Type = type(Logfunc).__name__

        if len(Output)>1:
            Number = int(len(Input)/(len(Output)-1))
        else:
            Number = 1

    # formate the printed Output

        Length = [len(Output)*2 + 18, len(Input)/Number*2 + 18, len(Name) + 18, len(Type) + 18, len('Binary Addition') + 6]
        Length.sort(key=int, reverse=True)

        cwidth = int(Length[0])

        first_last = ''.ljust(cwidth, '-')
        line = "-- " + ''.ljust(cwidth -6, '_') + " --"
        format_string = "-- {{0:^{0}}} --".format(cwidth-6)
        Numbers = []
        for x in range(Number):
            Numbers.append('')
            a = int((x)*len(Input)/Number)
            b = int((x+1)*len(Input)/Number)
            for y in range(a, b):
                Numbers[x] += str(Input[y])
                Numbers[x] += ' '
        
        Total = ''
        for x in range(len(Output)):
            Total += str(Output[x])
            Total += ' '

        print(first_last)
        print(format_string.format("Binary Addition"))
        print(first_last)

        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth-18)
        print(format_string.format("Name", Name))
        print(format_string.format("Type", Type))

        format_string = "-- {{0:10}}: {{1:>{0}}} --".format(cwidth-18)
        print((format_string.format("Number1", str(Numbers[0]))))

        for x in range(1, Number):
            print((format_string.format("Number{}".format(x+1), '+ ' + str(Numbers[x]))))

        print(line)
        print(format_string.format("Total", str(Total)))
        print(first_last)
        print("\n")

class showDecimal(showType):


    def show(self, Logfunc):

        Name = Logfunc.Name
        Input = Logfunc.getInput()
        Output = Logfunc.getOutput()
        Type = type(Logfunc).__name__

        if len(Output)>1:
            Number = int(len(Input)/(len(Output)-1))
        else:
            Number = 1
        Length = [len(Name) + 18, len(Type) + 18, len('Decimal Addition') + 6]
        Length.sort(key=int, reverse=True)
        cwidth = int(Length[0])

        first_last = ''.ljust(cwidth, '-')
        line = "-- " + ''.ljust(cwidth -6, '_') + " --"
        format_string = "-- {{0:^{0}}} --".format(cwidth-6)

        Numbers = []
        for x in range(Number):
            Numbers.append('')
            a = int((x)*len(Input)/Number)
            b = int((x+1)*len(Input)/Number)
            for y in range(a, b):
                Numbers[x] += str(Input[y])
            Numbers[x] = int(Numbers[x], 2)

        
        Total = ''
        for x in range(len(Output)):
            Total += str(Output[x])
        Total = int(Total, 2)

        print(first_last)
        print(format_string.format("Decimal Addition"))
        print(first_last)

        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth-18)
        print(format_string.format("Name", Name))
        print(format_string.format("Type", Type))

        format_string = "-- {{0:10}}: {{1:>{0}}} --".format(cwidth-18)
        print((format_string.format("Number1", str(Numbers[0]))))

        for x in range(1, Number):
            print((format_string.format("Number{}".format(x+1), '+ ' + str(Numbers[x]))))

        print(line)
        print(format_string.format("Total", str(Total)))
        print(first_last)
        print("\n")

class showGate(showType):


    def show(self, Logfunc):

        Name = Logfunc.Name
        Input = Logfunc.getInput()
        Output = Logfunc.getOutput()
        Type = type(Logfunc).__name__

        if len(Output)>1:
            Number = int(len(Input)/(len(Output)-1))
        else:
            Number = len(Input)

        Numbers = []
        for x in range(Number):
            Numbers.append('')
            a = int((x)*len(Input)/Number)
            b = int((x+1)*len(Input)/Number)
            for y in range(a, b):
                Numbers[x] += str(Input[y])
        
        Total = ''
        for x in range(len(Output)):
            Total += str(Output[x])

        Length = 3 + len(Numbers[0]) + 3 + len(Type) + 4 + 3 + len(Output) + 3
        cwidth = int(Length)

        line = ''.ljust(cwidth, '-')
        first= '-- ' + ''.ljust(len(Numbers[0]) + 3, ' ') + chr(1) + ''.ljust(len(Type) + 2, chr(9552)) + chr(9559) + ''.ljust(len(Output) + 3, ' ') + ' --'
        last = '-- ' + ''.ljust(len(Numbers[0]) + 3, ' ') + chr(9562) + ''.ljust(len(Type) + 2, chr(9552)) + chr(4) + ''.ljust(len(Output) + 3, ' ') + ' --'
        InputGate = chr(9552) + chr(9552) + chr(9571) + ''.ljust(len(Type) + 2, ' ') + chr(5) + ''.ljust(len(Output) + 3, ' ')
        TypeGate = chr(9552) + chr(9552) + chr(9571) + ' ' + str(Type) + ' ' + chr(9568) + chr(9552) + chr(9552) + ' ' + str(Total)
        format_string = "-- {{0:^{0}}} --".format(cwidth-6)

        print(line)
        print(format_string.format("Gate"))
        print(line)
        print(format_string.format("Name:"+str(Name)))
        print(first)

        for x in range(Number):
            import math
            if x+1 == math.ceil(Number/2):
                print('-- ' + Numbers[x] + ' ' + TypeGate + ' --')
            else:
                print('-- ' + Numbers[x] + ' ' + InputGate + ' --')

        print(last)
        print(line)
        print("\n")

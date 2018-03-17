__version__ = "1.0"                 # Verwaltungsinfos
__author__ = "Sarah Schüller"


class AndGate:                      # Klassendeklaration
    def __init__ (self):            # Attribute definieren    
    #sets all values to false for initilization
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "YaAndGate"

    def execute(self):
    # checks if both iputs are true
        self.__Output = False
        if self.__Input0 == True:
            if self.__Input1 == True:
                self.__Output = True

    def show(self):
    # formate the printed Output
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth-18)

        print(first_last)
        print(format_string.format("Name", self.__Name))
        print(format_string.format("Type", type(self).__name__))
        print(format_string.format("Input0", str(self.__Input0)))
        print(format_string.format("Input1", str(self.__Input1)))
        print(format_string.format("Output", str(self.__Output)))
        print(first_last)

    def __str__ (self):
    # turns boolean into string
        if self.__Output == True:
            return "True"
        else:
            return "False"
        
        if self.__Input0 == True:
            return "True"
        else:
            return "False"
        
        if self.__Input1 == True:
            return "True"
        else:
            return "False"

    #set Getter and Setter with property
    
    @property
    def Input0(self):
        return self.__Input0

    @Input0.setter
    def Input0(self, Input0):
        if isinstance(Input0, bool):
            self.__Input0 = Input0
    
    @property
    def Input1(self):
        return self.__Input1

    @Input1.setter
    def Input1(self, Input1):
        if isinstance(Input1, bool):
            self.__Input1 = Input1
    
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        if isinstance(Name, bool):
            self.__Name = Name

    @property
    def Output(self):
        return self.__Output

class OrGate:                      # Klassendeklaration
    def __init__ (self):            # Attribute definieren    
    # sets all values to false for initilization            
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "YaOrGate"

    def execute(self):
    # checks if one of the Iputs is true
        self.__Output = False
        if self.__Input0 == True:
            self.__Output = True
        elif self.__Input1 == True:
            self.__Output = True

    def show(self):
    # formate the printed Output
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth-18)

        print(first_last)
        print(format_string.format("Name", self.__Name))
        print(format_string.format("Type", type(self).__name__))
        print(format_string.format("Input0", str(self.__Input0)))
        print(format_string.format("Input1", str(self.__Input1)))
        print(format_string.format("Output", str(self.__Output)))
        print(first_last)

    def __str__ (self):
    # turns boolean into string
        if self.__Output == True:
            return "True"
        else:
            return "False"
        
        if self.__Input0 == True:
            return "True"
        else:
            return "False"
        
        if self.__Input1 == True:
            return "True"
        else:
            return "False"

    #set Getter and Setter with property

    @property
    def Input0(self):
        return self.__Input0

    @Input0.setter
    def Input0(self, Input0):
        if isinstance(Input0, bool):
            self.__Input0 = Input0
    
    @property
    def Input1(self):
        return self.__Input1

    @Input1.setter
    def Input1(self, Input1):
        if isinstance(Input1, bool):
            self.__Input1 = Input1
    
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        if isinstance(Name, bool):
            self.__Name = Name

    @property
    def Output(self):
        return self.__Output


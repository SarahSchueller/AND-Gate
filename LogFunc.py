from abc import ABC, abstractmethod

__version__ = "1.0"                 
__author__ = "Sarah Schüller"

# abstract class
class LogFunc(ABC):                      
    def __init__ (self, InputNr, OutputNr):                
    #sets all values to false for initilization
        self.__Input = []
        self._Output = []
        self.__Name = ""
        for x in range(InputNr):
            self.__Input.append(0)
        for x in range(OutputNr):
            self._Output.append(0)
        self.execute()

    def show(self):
    # formate the printed Output
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth-18)

        print(first_last)
        print(format_string.format("Name", self.__Name))
        print(format_string.format("Type", type(self).__name__))
        print(format_string.format("Input", str(self.__Input)))
        print(format_string.format("Output", str(self._Output)))
        print(first_last)

    def __str__ (self):
    # turns boolean into string
        if self._Output == True:
            return "True"
        else:
            return "False"
        
        if isinstance(self.__Input, list):
            Input = '['
            for x in range(len.self__Input):
                Input += self.__Input[x]
                Input += ' '
            Input += ']'

    @abstractmethod
    def execute(self):
    # implement logic in childclass
        raise NotImplementedError

    #set Getter and Setter with property
    
    @property
    def Input(self):
        return self.__Input
    
    def setInput(self, Index, Input):
        if [0,1].count(Input) == 1 and Index < len(self.__Input):
            self.__Input[Index] = Input
    
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        if isinstance(Name, str):
            self.__Name = Name

    @property
    def Output(self):
        return self._Output

class AndGate(LogFunc):  

    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)   
        self.Name = "AndGate"

    def execute(self):
    # checks if both iputs are true
        self._Output = 0
        if self.Input.count(0) == 0:
            self._Output = 1

 
class OrGate(LogFunc):                     
        
    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "OrGate"

    def execute(self):
    # checks if one of the Iputs is true
        self._Output = 0
        if self.Input.count(1) >= 1:
            self._Output = 1

class NAndGate(LogFunc): 

    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "NAndGate"                    
   
    def execute(self):
    # checks if both iputs are not true
        self._Output = 1
        if self.Input.count(0) == 0:
            self._Output = 0

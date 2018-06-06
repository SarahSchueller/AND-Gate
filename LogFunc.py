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
        self.setInputNr(InputNr)
        self._setOutputNr(OutputNr)

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

    @abstractmethod
    def execute(self):
    # implement logic in childclass
        raise NotImplementedError

    #set Getter and Setter with property
    

    def getInput(self):
        return self.__Input

    def getInputElement(self, idx):
        return self.__Input[idx]
    
    def setInput(self, Index, Input):
        if [0,1].count(Input) == 1 and Index < len(self.__Input) and Index > -1:
            self.__Input[Index] = Input
        elif Index > len(self.__Input) or  Index < 0:
            print('The given idex is not correct please choose an index between 0 and',len(self.__Input))
        elif [0,1].count(Input) != 1:
            print('Please choose 0 or 1 for false or true as value')
    
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

    def setInputNr(self, number):
        if number > -1:
            self.__Input = []
            for x in range(number):
                self.__Input.append(0)
            self.execute()
        else:
            print('The Number of Inputs has to greater than 0.')

    def _setOutputNr(self, number):
        if number > 0:
            self._Output = []
            for x in range(number):
                self._Output.append(0)
            self.execute()
        else:
            print('The Number of Outputs has to greater than 0.')

class AndGate(LogFunc):  

    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)   
        self.Name = "AndGate"

    def execute(self):
    # checks if both iputs are true
        self._Output = 0
        if self.getInput().count(0) == 0:
            self._Output = 1

 
class OrGate(LogFunc):                     
        
    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "OrGate"

    def execute(self):
    # checks if one of the Iputs is true
        self._Output = 0
        if self.getInput().count(1) >= 1:
            self._Output = 1    

class NAndGate(LogFunc): 

    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "NAndGate"                    
   
    def execute(self):
    # checks if both iputs are not true
        self._Output = 1
        if self.getInput().count(0) == 0:
            self._Output = 0

class NOrGate(LogFunc):                     
        
    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "NOrGate"

    def execute(self):
    # checks if all Iputs are false 
        self._Output = 0
        if self.getInput().count(1) == 0:
            self._Output = 1

class XOrGate(LogFunc):                     
        
    def __init__ (self, InputNr):             
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "XOrGate"

    def execute(self):
    # checks if number of true Iputs is odd 
        self._Output = 0
        if  self.getInput().count(1) % 2 == 1:
            self._Output = 1

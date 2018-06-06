from abc import ABC, abstractmethod

__version__ = "1.0"                 
__author__ = "Sarah Schüller"

# abstract class
class LogFunc(ABC):                      
    def __init__ (self):                
    #sets all values to false for initilization
        self.__Input0 = False
        self.__Input1 = False
        self._Output = False
        self.__Name = ""
        self.execute()

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
        print(format_string.format("Output", str(self._Output)))
        print(first_last)

    @abstractmethod
    def execute(self):
    # implement logic in childclass
        raise NotImplementedError

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
        if isinstance(Name, str):
            self.__Name = Name

    @property
    def Output(self):
        return self._Output

class AndGate(LogFunc):  

    def __init__ (self):             
        LogFunc.__init__(self)   
        self.__Name = "AndGate"

    def execute(self):
    # checks if both iputs are true
        self._Output = False
        if self.Input0 == self.Input1 ==  True:
            self._Output = True 

class NAndGate(LogFunc): 

    def __init__ (self):            
        LogFunc.__init__(self)   
        self.__Name = "NAndGate"                    
   
    def execute(self):
    # checks if both iputs are not true
        self._Output = True
        if self.Input0 == self.Input1 == True:
            self._Output = False

class OrGate(LogFunc):                     
        
    def __init__ (self):            
        LogFunc.__init__(self)  
        self.__Name = "OrGate"

    def execute(self):
    # checks if one of the Iputs is true
        self._Output = True
        if self.Input0 == self.Input1 == False:
            self._Output = False

class NOrGate(LogFunc):                     
        
    def __init__ (self):            
        LogFunc.__init__(self)  
        self.__Name = "NOrGate"

    def execute(self):
    # checks if one of the Iputs is true
        self._Output = False
        if self.Input0 == self.Input1 == False:
            self._Output = True

class XOrGate(LogFunc):                     
        
    def __init__ (self):            
        LogFunc.__init__(self)  
        self.__Name = "XOrGate"

    def execute(self):
    # checks if one of the Iputs is true
        self._Output = False
        if self.Input0 != self.Input1:
            self._Output = True

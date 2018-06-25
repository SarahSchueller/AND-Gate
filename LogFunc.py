from abc import ABC, abstractmethod
from show import *
__version__ = "1.0"                 
__author__ = "Sarah Schüller"

# abstract class
class LogFunc(ABC):                      
    def __init__ (self, InputNr, OutputNr):                
    #sets all values to false for initilization
        self._Input = []
        self._Output = [] 
        self.__Name = ""
        self._showType = showStandard()
        self._setInputNr(InputNr)
        self._setOutputNr(OutputNr)
        self.execute()

    def show(self):
        self.getShowType().show(self.Name, type(self).__name__, self.getInput(), self.getOutput())

    @abstractmethod
    def execute(self):
    # implement logic in childclass
        raise NotImplementedError

    #set Getter and Setter 

    def getInput(self):
        return self._Input

    def getInputElement(self, idx):
        return self._Input[idx]
    
    def setInput(self, Index, Input):
        if [0,1].count(Input) == 1 and Index < len(self._Input) and Index > -1:
            self._Input[Index] = Input
        elif Index > len(self._Input)-1 or  Index < 0:
            raise ValueError('The given index is not correct please choose an index between 0 and '+str(len(self._Input)-1))
        elif [0,1].count(Input) != 1:
            raise ValueError('Please choose 0 or 1 for false or true as value')
    
    def getOutput(self):
        return self._Output

    def getOutputElement(self, idx):
        return self._Output[idx]

    def _setOutput(self, Index, Output):
        if [0,1].count(Output) == 1 and Index < len(self._Output) and Index > -1:
            self._Output[Index] = Output
        elif Index > len(self._Output)-1 or  Index < 0:
            raise ValueError('The given index is not correct please choose an index between 0 and '+str(len(self._Output)-1))
        elif [0,1].count(Output) != 1:
            raise ValueError('Please choose 0 or 1 for false or true as value')

    def _setInputNr(self, number):
        if number > -1:
            self._Input = []
            for x in range(number):
                self._Input.append(0)
        else:
            raise ValueError('The Number of Inputs has to be greater than -1.')

    def _setOutputNr(self, number):
        if number > 0:
            self._Output = []
            for x in range(number):
                self._Output.append(0)
        else:
            raise ValueError('The Number of Outputs has to greater be than 0.')

    def getShowType(self):
        return self._showType
    
    def setShowType(self, showType):
        self._showType = showType

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        if isinstance(Name, str):
            self.__Name = Name


class AndGate(LogFunc):  

    def __init__ (self, InputNr): 
        if InputNr < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
  
        LogFunc.__init__(self, InputNr, 1)   
        self.Name = "AndGate"

    def execute(self):
    # checks if both iputs are true
        self._setOutput(0,0)
        if self.getInput().count(0) == 0:
            self._setOutput(0,1)

    def setInputNr(self, number):
        if number < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
        else:
            self._setInputNr(number)
            self.execute()

 
class OrGate(LogFunc):                     
        
    def __init__ (self, InputNr):
        if InputNr < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
       
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "OrGate"

    def execute(self):
    # checks if one of the Iputs is true
        self._setOutput(0,0)
        if self.getInput().count(1) >= 1:
            self._setOutput(0,1) 

    def setInputNr(self, number):
        if number < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
        else:
            self._setInputNr(number)
            self.execute()   


class NAndGate(LogFunc): 

    def __init__ (self, InputNr):  
        if InputNr < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
      
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "NAndGate"                    
   
    def execute(self):
    # checks if both iputs are not true
        self._setOutput(0,1)
        if self.getInput().count(0) == 0:
            self._setOutput(0,0)

    def setInputNr(self, number):
        if number < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
        else:
            self._setInputNr(number)
            self.execute() 


class NOrGate(LogFunc):                     
        
    def __init__ (self, InputNr):
        if InputNr < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
        
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "NOrGate"

    def execute(self):
    # checks if all Iputs are false 
        self._setOutput(0,0)
        if self.getInput().count(1) == 0:
            self._setOutput(0,1)

    def setInputNr(self, number):
        if number < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
        else:
            self._setInputNr(number) 
            self.execute()


class XOrGate(LogFunc):                     
        
    def __init__ (self, InputNr):
        if InputNr < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
        
        LogFunc.__init__(self, InputNr, 1)    
        self.Name = "XOrGate"

    def execute(self):
    # checks if number of true Iputs is odd 
        self._setOutput(0,0)
        if  self.getInput().count(1) % 2 == 1:
            self._setOutput(0,1)

    def setInputNr(self, number):
        if number < 2:
            raise ValueError('There must be minimum 2 Inputs.') 
        else:
            self._setInputNr(number) 
            self.execute()


class HalfAdder(LogFunc):

    def __init__(self):
        self.__sum = XOrGate(2)
        self.__sum.Name = "sum"
        self.__carry = AndGate(2)
        self.__carry.Name = "carry"
        LogFunc.__init__(self, 2, 2)
        self.Name = "HalfAdder"

    def execute(self):

        self.__sum.setInput(0, self.getInputElement(0))
        self.__sum.setInput(1, self.getInputElement(1))

        self.__carry.setInput(0, self.getInputElement(0))
        self.__carry.setInput(1, self.getInputElement(1))

        self.__sum.execute()
        self.__carry.execute()

        self._setOutput(0, self.__carry.getOutputElement(0))
        self._setOutput(1, self.__sum.getOutputElement(0))


class FullAdder(LogFunc):

    def __init__(self):
        self.__sum = [HalfAdder(), HalfAdder()]
        self.__sum[0].Name = "sum1"
        self.__sum[1].Name = "sum2"
        self.__carry = OrGate(2)
        self.__carry.Name = "carry"
        LogFunc.__init__(self, 3, 2)
        self.Name = "FullAdder"

    def execute(self):

        self.__sum[0].setInput(0, self.getInputElement(0))
        self.__sum[0].setInput(1, self.getInputElement(1))
        self.__sum[0].execute()

        self.__sum[1].setInput(0, self.getInputElement(2))
        self.__sum[1].setInput(1, self.__sum[0].getOutputElement(1))
        self.__sum[1].execute()

        self.__carry.setInput(0, self.__sum[0].getOutputElement(0))
        self.__carry.setInput(1, self.__sum[1].getOutputElement(0))
        self.__carry.execute()

        self._setOutput(0, self.__carry.getOutputElement(0))
        self._setOutput(1, self.__sum[1].getOutputElement(1))

class EightBitAdder(LogFunc):

    def __init__(self):
        self.__sum = HalfAdder()
        self.__sum.Name = "sum"
        self.__carry = [FullAdder(), FullAdder(), FullAdder(), FullAdder(), FullAdder(), FullAdder(), FullAdder()]
        for x in range(7):
            self.__carry[x].Name = "carry{}".format(x)
        LogFunc.__init__(self, 16, 9)
        self.Name = "EightBitAdder"

    def execute(self):    
        self.__sum.setInput(0, self.getInputElement(7))
        self.__sum.setInput(1, self.getInputElement(15))
        self.__sum.execute()
        self._setOutput(8, self.__sum.getOutputElement(1))

        self.__carry[0].setInput(0, self.getInputElement(6))
        self.__carry[0].setInput(1, self.getInputElement(14))
        self.__carry[0].setInput(2, self.__sum.getOutputElement(0))
        self.__carry[0].execute()
        self._setOutput(7, self.__carry[0].getOutputElement(1))

        for x in range(1, 7):
            self.__carry[x].setInput(0, self.getInputElement(6-x))
            self.__carry[x].setInput(1, self.getInputElement(14-x))
            self.__carry[x].setInput(2, self.__carry[x-1].getOutputElement(0))
            self.__carry[x].execute()
            self._setOutput(7-x, self.__carry[x].getOutputElement(1))
        
        self._setOutput(0, self.__carry[6].getOutputElement(0))

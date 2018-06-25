import unittest
import random
from LogFunc import AndGate
from LogFunc import OrGate
from LogFunc import XOrGate
from LogFunc import NOrGate
from LogFunc import NAndGate
from LogFunc import HalfAdder
from LogFunc import FullAdder
from LogFunc import EightBitAdder

class AndGateTest(unittest.TestCase):

    def testcase_00(self):
        a = AndGate(4)
        for x in range(4):
            self.assertFalse(a.getInputElement(x), 'Class AndGate: Testcase 0 failed.')
        self.assertFalse(a.getOutputElement(0), 'Class AndGate: Testcase 0 failed.')
        self.assertEqual(len(a.getInput()), 4, 'Class AndGate: Testcase 4_{} failed.'.format(x))

    def testcase_01(self):
        for y in range(4):
            a = AndGate(4)
            a.setInput(y, 1)
            a.execute()
            self.assertFalse(a.getOutputElement(0), 'Class AndGate: Testcase 1_{} failed.'.format(y))

    def testcase_02(self):
        for y in range(3):
            a = AndGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.getOutputElement(0), 'Class AndGate: Testcase 2_{} failed.'.format(y))

    def testcase_02_3(self):
        a = AndGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class AndGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = AndGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertFalse(a.getOutputElement(0), 'Class AndGate: Testcase 3_{} failed.'.format(y))
    
    def testcase_04(self):
        a = AndGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertTrue(a.getOutputElement(0), 'Class AndGate: Testcase 4 failed.')

    def testcase_05(self):
        a = AndGate(4)
        for x in range(2,5):
            a.setInputNr(x)
            self.assertEqual(len(a.getInput()),x, 'Class AndGate: Testcase 4_{} failed.'.format(x))

class OrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = OrGate(4)
        for x in range(4):
            self.assertFalse(a.getInputElement(x), 'Class OrGate: Testcase 0 failed.')
        self.assertFalse(a.getOutputElement(0), 'Class OrGate: Testcase 0 failed.')
        self.assertEqual(len(a.getInput()), 4, 'Class OrGate: Testcase 4_{} failed.'.format(x))

    def testcase_01(self):
        for y in range(4):
            a = OrGate(4)
            a.setInput(y, 1)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class OrGate: Testcase 1_{} failed.'.format(y))

    def testcase_02(self):
        for y in range(3):
            a = OrGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class OrGate: Testcase 2_{} failed.'.format(y))

    def testcase_02_3(self):
        a = OrGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertTrue(a.getOutputElement(0), 'Class OrGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = OrGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class OrGate: Testcase 3_{} failed.'.format(y))
    
    def testcase_04(self):
        a = OrGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertTrue(a.getOutputElement(0), 'Class OrGate: Testcase 4 failed.')

    def testcase_05(self):
        a = OrGate(4)
        for x in range(2,5):
            a.setInputNr(x)
            self.assertEqual(len(a.getInput()),x, 'Class OrGate: Testcase 4_{} failed.'.format(x))

class NAndGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NAndGate(4)
        for x in range(4):
            self.assertFalse(a.getInputElement(x), 'Class NAndGate: Testcase 0 failed.')
        self.assertTrue(a.getOutputElement(0), 'Class NAndGate: Testcase 0 failed.')
        self.assertEqual(len(a.getInput()), 4, 'Class NAndGate: Testcase 4_{} failed.'.format(x))

    def testcase_01(self):
        for y in range(4):
            a = NAndGate(4)
            a.setInput(y, 1)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class NAndGate: Testcase 1_{} failed.'.format(y))

    def testcase_02(self):
        for y in range(3):
            a = NAndGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class NAndGate: Testcase 2_{} failed.'.format(y))

    def testcase_02_3(self):
        a = NAndGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertTrue(a.getOutputElement(0), 'Class NAndGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = NAndGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class NAndGate: Testcase 3_{} failed.'.format(y))
    
    def testcase_04(self):
        a = NAndGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class NAndGate: Testcase 4 failed.')

    def testcase_05(self):
        a = NAndGate(4)
        for x in range(2,5):
            a.setInputNr(x)
            self.assertEqual(len(a.getInput()),x, 'Class NAndGate: Testcase 4_{} failed.'.format(x))

class NOrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NOrGate(4)
        for x in range(4):
            self.assertFalse(a.getInputElement(x), 'Class NOrGate: Testcase 0 failed.')
        self.assertTrue(a.getOutputElement(0), 'Class NOrGate: Testcase 0 failed.')
        self.assertEqual(len(a.getInput()), 4, 'Class NOrGate: Testcase 4_{} failed.'.format(x))

    def testcase_01(self):
        for y in range(4):
            a = NOrGate(4)
            a.setInput(y, 1)
            a.execute()
            self.assertFalse(a.getOutputElement(0), 'Class NOrGate: Testcase 1_{} failed.'.format(y))

    def testcase_02(self):
        for y in range(3):
            a = NOrGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.getOutputElement(0), 'Class NOrGate: Testcase 2_{} failed.'.format(y))

    def testcase_02_3(self):
        a = NOrGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class NOrGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = NOrGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertFalse(a.getOutputElement(0), "Class NOrGate: Testcase 3_{} failed.".format(y))
    
    def testcase_04(self):
        a = NOrGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class NOrGate: Testcase 4 failed.')

    def testcase_05(self):
        a = NOrGate(4)
        for x in range(2,5):
            a.setInputNr(x)
            self.assertEqual(len(a.getInput()),x, 'Class NOrGate: Testcase 4_{} failed.'.format(x))

class XOrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = XOrGate(4)
        for x in range(4):
            self.assertFalse(a.getInputElement(x), 'Class XOrGate: Testcase 0 failed.')
        self.assertFalse(a.getOutputElement(0), 'Class XOrGate: Testcase 0 failed.')
        self.assertEqual(len(a.getInput()), 4, 'Class XOrGate: Testcase 4_{} failed.'.format(x))

    def testcase_01(self):
        for y in range(4):
            a = XOrGate(4)
            a.setInput(y, 1)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class XOrGate: Testcase 1_{} failed.'.format(y))

    def testcase_02(self):
        for y in range(3):
            a = XOrGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.getOutputElement(0), 'Class XOrGate: Testcase 2_{} failed.'.format(y))

    def testcase_02_3(self):
        a = XOrGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class XOrGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = XOrGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class XOrGate: Testcase 3_{} failed.'.format(y))
    
    def testcase_04(self):
        a = XOrGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class XOrGate: Testcase 4 failed.')

    def testcase_05(self):
        a = XOrGate(4)
        for x in range(2,5):
            a.setInputNr(x)
            self.assertEqual(len(a.getInput()),x, 'Class XOrGate: Testcase 4_{} failed.'.format(x))

class HalfAdderTest(unittest.TestCase):

    def testcase_00(self):
        a = HalfAdder()
        self.assertFalse(a.getInputElement(0), 'Class HalfAdder: Testcase 0 failed.')
        self.assertFalse(a.getInputElement(1), 'Class HalfAdder: Testcase 0 failed.')
        self.assertFalse(a.getOutputElement(0), 'Class HalfAdder: Testcase 0 failed.')
        self.assertFalse(a.getOutputElement(1), 'Class HalfAdder: Testcase 0 failed.')

    def testcase_01(self):
        a = HalfAdder()
        a.setInput(0, 0)
        a.setInput(1, 0)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class HalfAdder: Testcase 1 failed.')
        self.assertFalse(a.getOutputElement(1), 'Class HalfAdder: Testcase 1 failed.')

    def testcase_02(self):
        a = HalfAdder()
        a.setInput(0, 1)
        a.setInput(1, 0)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class HalfAdder: Testcase 2 failed.')
        self.assertTrue(a.getOutputElement(1), 'Class HalfAdder: Testcase 2 failed.')
    
    def testcase_03(self):
        a = HalfAdder()
        a.setInput(0, 0)
        a.setInput(1, 1)
        a.execute()
        self.assertFalse(a.getOutputElement(0), 'Class HalfAdder: Testcase 3 failed.')
        self.assertTrue(a.getOutputElement(1), 'Class HalfAdder: Testcase 3 failed.')
    
    def testcase_04(self):
        a = HalfAdder()
        a.setInput(0, 1)
        a.setInput(1, 1)
        a.execute()
        self.assertTrue(a.getOutputElement(0), 'Class HalfAdder: Testcase 4 failed.')
        self.assertFalse(a.getOutputElement(1), 'Class HalfAdder: Testcase 4 failed.')

class FullAdderTest(unittest.TestCase):

    def testcase_00(self):
        a = FullAdder()
        for x in range(3):
            self.assertFalse(a.getInputElement(x), 'Class FullAdder: Testcase 0 failed.')
        self.assertFalse(a.getOutputElement(0), 'Class FullAdder: Testcase 0 failed.')
        self.assertFalse(a.getOutputElement(1), 'Class FullAdder: Testcase 0 failed.')


    def testcase_01(self):
        for y in range(3):
            a = FullAdder()
            a.setInput(y, 1)
            a.execute()
            self.assertFalse(a.getOutputElement(0), 'Class FullAdder: Testcase 1_{} failed.'.format(y))
            self.assertTrue(a.getOutputElement(1), 'Class FullAdder: Testcase 1_{} failed.'.format(y))

    def testcase_02(self):
        for y in range(2):
            a = FullAdder()
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.getOutputElement(0), 'Class FullAdder: Testcase 2_{} failed.'.format(y))
            self.assertFalse(a.getOutputElement(1), 'Class FullAdder: Testcase 2_{} failed.'.format(y))

    def testcase_02_2(self):
        a = FullAdder()
        a.setInput(2, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertTrue(a.getOutputElement(0), 'Class FullAdder: Testcase 2_3 failed.') 
        self.assertFalse(a.getOutputElement(1), 'Class FullAdder: Testcase 2_3 failed.') 

    def testcase_03(self):
        a = FullAdder()
        for x in range(3):
            a.setInput(x, 1)
        a.execute()
        self.assertTrue(a.getOutputElement(0), 'Class FullAdder: Testcase 3 failed.')
        self.assertTrue(a.getOutputElement(1), 'Class FullAdder: Testcase 3 failed.')

class EightBitAdderTest(unittest.TestCase):

    def testcase_00(self):   
        a = EightBitAdder()
        for x in range(16):
            self.assertFalse(a.getInputElement(x), 'Class EightBitAdder: Testcase 0 failed.')
        for x in range(9):
            self.assertFalse(a.getOutputElement(x), 'Class EightBitAdder: Testcase 0 failed.')

    def testcase_01(self):

        for x in range(1000):
            a = EightBitAdder()

            for y in range(16):
                a.setInput(y, random.randint(0, 1))

            Number1 = ""
            for z in range(8):    
                Number1 += str(a.getInputElement(z))

            Number2 = ""
            for w in range(8, 16):    
                Number2 += str(a.getInputElement(w))

            a.execute()

            Total = ""
            for i in range(9):    
                Total += str(a.getOutputElement(i))

            Sum = int(Number1, 2) + int(Number2, 2)
            Result = int(Total, 2)
            
            self.assertEqual(Result, Sum, 'Class EightBitAdder: Testcase 01_{} failed.'.format(x))


if __name__ == '__main__':
    unittest.main()             # führt automatisch alle Methoden aus, die mit testcase_ beginnen

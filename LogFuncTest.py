import unittest
from LogFunc import AndGate
from LogFunc import OrGate
from LogFunc import XOrGate
from LogFunc import NOrGate
from LogFunc import NAndGate

class AndGateTest(unittest.TestCase):

    def testcase_00(self):
        a = AndGate(4)
        for x in range(4):
            self.assertFalse(a.Input[x], 'Class AndGate: Testcase 0 failed.')
        self.assertFalse(a.Output, 'Class AndGate: Testcase 0 failed.')

    def testcase_01(self):
        for y in range(4):
            a = AndGate(4)
            for x in range(1):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.Output, 'Class AndGate: Testcase 1_%s failed.'%(y))

    def testcase_02(self):
        for y in range(3):
            a = AndGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.Output, 'Class AndGate: Testcase 2_%s failed.'%(y))

    def testcase_02_3(self):
        a = AndGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertFalse(a.Output, 'Class AndGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = AndGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertFalse(a.Output, 'Class AndGate: Testcase 3_%s failed.'%(y))
    
    def testcase_04(self):
        a = AndGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertTrue(a.Output, 'Class AndGate: Testcase 4 failed.')
    
    def testcase_05(self):
        a = AndGate(4)
        for x in range(5):
            a.setInputNr(x)
            self.assertEqual(len(a.Input), x, 'Class AndGate: Testcase 5_%s failed.'%(x))

class OrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = OrGate(4)
        for x in range(4):
            self.assertFalse(a.Input[x], 'Class OrGate: Testcase 0 failed.')
        self.assertFalse(a.Output, 'Class OrGate: Testcase 0 failed.')

    def testcase_01(self):
        for y in range(4):
            a = OrGate(4)
            for x in range(1):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.Output, 'Class Orate: Testcase 1_%s failed.'%(y))

    def testcase_02(self):
        for y in range(3):
            a = OrGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.Output, 'Class OrGate: Testcase 2_%s failed.'%(y))

    def testcase_02_3(self):
        a = OrGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertTrue(a.Output, 'Class OrGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = OrGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertTrue(a.Output, 'Class OrGate: Testcase 3_%s failed.'%(y))
    
    def testcase_04(self):
        a = OrGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertTrue(a.Output, 'Class OrGate: Testcase 4 failed.')

    def testcase_05(self):
        a = OrGate(4)
        for x in range(5):
            a.setInputNr(x)
            self.assertEqual(len(a.Input), x, 'Class AndGate: Testcase 5_%s failed.'%(x))

class NAndGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NAndGate(4)
        for x in range(4):
            self.assertFalse(a.Input[x], 'Class NAndGate: Testcase 0 failed.')
        self.assertTrue(a.Output, 'Class NAndGate: Testcase 0 failed.')

    def testcase_01(self):
        for y in range(4):
            a = NAndGate(4)
            for x in range(1):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.Output, 'Class NAndGate: Testcase 1_%s failed.'%(y))

    def testcase_02(self):
        for y in range(3):
            a = NAndGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.Output, 'Class NAndGate: Testcase 2_%s failed.'%(y))

    def testcase_02_3(self):
        a = NAndGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertTrue(a.Output, 'Class NAndGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = NAndGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertTrue(a.Output, 'Class NAndGate: Testcase 3_%s failed.'%(y))
    
    def testcase_04(self):
        a = NAndGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertFalse(a.Output, 'Class NAndGate: Testcase 4 failed.')

    def testcase_05(self):
        a = NAndGate(4)
        for x in range(5):
            a.setInputNr(x)
            self.assertEqual(len(a.Input), x, 'Class AndGate: Testcase 5_%s failed.'%(x))

class NOrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NOrGate(4)
        for x in range(4):
            self.assertFalse(a.Input[x], 'Class NOrGate: Testcase 0 failed.')
        self.assertTrue(a.Output, 'Class NOrGate: Testcase 0 failed.')

    def testcase_01(self):
        for y in range(4):
            a = NOrGate(4)
            for x in range(1):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.Output, 'Class NOrate: Testcase 1_%s failed.'%(y))

    def testcase_02(self):
        for y in range(3):
            a = NOrGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.Output, 'Class NOrGate: Testcase 2_%s failed.'%(y))

    def testcase_02_3(self):
        a = NOrGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertFalse(a.Output, 'Class NOrGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = NOrGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertFalse(a.Output, 'Class NOrGate: Testcase 3_%s failed.'%(y))
    
    def testcase_04(self):
        a = NOrGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertFalse(a.Output, 'Class NOrGate: Testcase 4 failed.')

    def testcase_05(self):
        a = NOrGate(4)
        for x in range(5):
            a.setInputNr(x)
            self.assertEqual(len(a.Input), x, 'Class AndGate: Testcase 5_%s failed.'%(x))

class XOrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = XOrGate(4)
        for x in range(4):
            self.assertFalse(a.Input[x], 'Class XOrGate: Testcase 0 failed.')
        self.assertFalse(a.Output, 'Class XOrGate: Testcase 0 failed.')

    def testcase_01(self):
        for y in range(4):
            a = XOrGate(4)
            for x in range(1):
                a.setInput(x + y, 1)
            a.execute()
            self.assertTrue(a.Output, 'Class XOrate: Testcase 1_%s failed.'%(y))

    def testcase_02(self):
        for y in range(3):
            a = XOrGate(4)
            for x in range(2):
                a.setInput(x + y, 1)
            a.execute()
            self.assertFalse(a.Output, 'Class XOrGate: Testcase 2_%s failed.'%(y))

    def testcase_02_3(self):
        a = XOrGate(4)
        a.setInput(3, 1)
        a.setInput(0, 1)
        a.execute()
        self.assertFalse(a.Output, 'Class XOrGate: Testcase 2_3 failed.')
    
    def testcase_03(self):
        for y in range(4):
            a = XOrGate(4)
            for z in range(4):
                a.setInput(z , 1)
            for x in range(1):
                a.setInput(x + y, 0)
            a.execute()
            self.assertTrue(a.Output, 'Class XOrGate: Testcase 3_%s failed.'%(y))
    
    def testcase_04(self):
        a = XOrGate(4)
        for x in range(4):
            a.setInput(x, 1)
        a.execute()
        self.assertFalse(a.Output, 'Class XOrGate: Testcase 4 failed.')

    def testcase_05(self):
        a = XOrGate(4)
        for x in range(5):
            a.setInputNr(x)
            self.assertEqual(len(a.Input), x, 'Class AndGate: Testcase 5_%s failed.'%(x))



if __name__ == '__main__':
    unittest.main()             # führt automatisch alle Methoden aus, die mit testcase_ beginnen

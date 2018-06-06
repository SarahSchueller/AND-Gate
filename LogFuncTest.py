import unittest
from LogFunc import AndGate
from LogFunc import OrGate
from LogFunc import NOrGate
from LogFunc import XOrGate
from LogFunc import NAndGate

class AndGateTest(unittest.TestCase):

    def testcase_00(self):
        a = AndGate()
        self.assertFalse(a.Input0, 'Class NAndGate: Testcase 0 failed.')
        self.assertFalse(a.Input1, 'Class NAndGate: Testcase 0 failed.')
        self.assertFalse(a.Output, 'Class NAndGate: Testcase 0 failed.')

    def testcase_01(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, 'Class AndGate: Testcase 1 failed.')

    def testcase_02(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, 'Class AndGate: Testcase 2 failed.')
    
    def testcase_03(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, 'Class AndGate: Testcase 3 failed.')
    
    def testcase_04(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, 'Class AndGate: Testcase 4 failed.')

class OrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = OrGate()
        self.assertFalse(a.Input0, 'Class OrGate: Testcase 0 failed.')
        self.assertFalse(a.Input1, 'Class OrGate: Testcase 0 failed.')
        self.assertFalse(a.Output, 'Class OrGate: Testcase 0 failed.')

    def testcase_01(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, 'Class OrGate: Testcase 1 failed.')

    def testcase_02(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, 'Class OrGate: Testcase 2 failed.')
    
    def testcase_03(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, 'Class OrGate: Testcase 3 failed.')
    
    def testcase_04(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, 'Class OrGate: Testcase 4 failed.')

class NAndGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NAndGate()
        self.assertFalse(a.Input0, 'Class NAndGate: Testcase 0 failed.')
        self.assertFalse(a.Input1, 'Class NAndGate: Testcase 0 failed.')
        self.assertTrue(a.Output, 'Class NAndGate: Testcase 0 failed.')

    def testcase_01(self):
        a = NAndGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, 'Class NAndGate: Testcase 1 failed.')

    def testcase_02(self):
        a = NAndGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, 'Class NAndGate: Testcase 2 failed.')
    
    def testcase_03(self):
        a = NAndGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, 'Class NAndGate: Testcase 3 failed.')
    
    def testcase_04(self):
        a = NAndGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, 'Class NAndGate: Testcase 4 failed.')

class NOrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NOrGate()
        self.assertFalse(a.Input0, 'Class NOrGate: Testcase 0 failed.')
        self.assertFalse(a.Input1, 'Class NOrGate: Testcase 0 failed.')
        self.assertTrue(a.Output, 'Class NOrGate: Testcase 0 failed.')

    def testcase_01(self):
        a = NOrGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, 'Class NOrGate: Testcase 1 failed.')

    def testcase_02(self):
        a = NOrGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, 'Class NOrGate: Testcase 2 failed.')
    
    def testcase_03(self):
        a = NOrGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, 'Class NOrGate: Testcase 3 failed.')
    
    def testcase_04(self):
        a = NOrGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, 'Class NOrGate: Testcase 4 failed.')

class XOrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = XOrGate()
        self.assertFalse(a.Input0, 'Class XOrGate: Testcase 0 failed.')
        self.assertFalse(a.Input1, 'Class XOrGate: Testcase 0 failed.')
        self.assertFalse(a.Output, 'Class XOrGate: Testcase 0 failed.')

    def testcase_01(self):
        a = XOrGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, 'Class XOrGate: Testcase 1 failed.')

    def testcase_02(self):
        a = XOrGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, 'Class XOrGate: Testcase 2 failed.')
    
    def testcase_03(self):
        a = XOrGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, 'Class XOrGate: Testcase 3 failed.')
    
    def testcase_04(self):
        a = XOrGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, 'Class XOrGate: Testcase 4 failed.')

if __name__ == '__main__':
    unittest.main()             # führt automatisch alle Methoden aus, die mit testcase_ beginnen

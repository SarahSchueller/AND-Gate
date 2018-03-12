__version__ = "1.0"                 # Verwaltungsinfos
__author__ = "Sarah Schüller"


class AndGate:                      # Klassendeklaration
    def __init__ (self):            # Attribute definieren
        self.Input0 = False
        self.Input1 = False
        self.Output = False
        self.Name = "YaAndGate"

    def execute(self):
        self.Output = False
        if self.Input0 == True:
            if self.Input1 == True:
                self.Output = True

    def show(self):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth-18)

        print(first_last)
        print(format_string.format("Name", self.Name))
        print(format_string.format("Type", type(self).__name__))
        print(format_string.format("Input0", str(self.Input0)))
        print(format_string.format("Input1", str(self.Input1)))
        print(format_string.format("Output", str(self.Output)))
        print(first_last)

    def __str__ (self):
        if self.Output == True:
            return "True"
        else:
            return "False"
        
        if self.Input0 == True:
            return "True"
        else:
            return "False"
        
        if self.Input1 == True:
            return "True"
        else:
            return "False"




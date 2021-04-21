class Selection_variable():
    def __init__(self, data, variable):
        self.data = data
        self.variable = variable

    def select_var(self):
        return [row[self.data[0].index(self.variable)] for row in self.data]

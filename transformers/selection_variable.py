class Selection_variable():
    def __init__(self, data, variable):
        self.data = data
        self.variable = variable

    def select_une_var(self):
        return [[row[self.data[0].index(self.variable)]] for row in self.data]

    # def select_multiple_var(self):
    #     new_data = [[row[self.data[0].index(self.liste_variable[0])]] for row in self.data]
    #     for variable in self.liste_variable[1:]:
    #         for i in range(len(new_data)):
    #             new_data[i].append(self.select_une_var(variable)[i])
    #     return new_data



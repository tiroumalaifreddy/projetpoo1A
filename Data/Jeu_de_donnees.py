class Jeu_de_donnees():
    def __init__(self, data):
        self.column_names = data[0]
        self.rows = data[1:]

    def add_row(self, row, position = -1):
        if len(self.column_names) == len(row):
            if position >= 0:
                self.rows.insert(position, row)
            else:
                self.rows.insert((len(self.rows) + 1) + position, row)

    def remove_row(self, position):
        self.rows.pop(position)

    def add_column(self, name, column, position = -1):
        if len(self.rows) == len(column):
            if position >= 0:
                self.column_names.insert(position, name)
                for i in range(len(self.rows)):
                    self.rows[i].insert(position, column[i])
            else:
                self.column_names.insert((len(self.column_names) + 1 + position), name)
                for i in range(len(self.rows)):
                    self.rows[i].insert((len(self.rows[i]) + 1 + position), column[i])

    def remove_column(self, position = -1):
        self.column_names.pop(position)
        for liste in self.rows:
            liste.pop(position)

    def __str__(self):
        return "{}".format([self.column_names] + self.rows)
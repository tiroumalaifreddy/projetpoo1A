from Data.Jeu_de_donnees import Jeu_de_donnees
import csv

class Export_csv:
    def export(self, Table, filename):
        column_names = Table.column_names
        rows = Table.rows
        with open(filename, "w") as f:
            write = csv.writer(f)
            write.writerow(column_names)
            write.writerows(rows)

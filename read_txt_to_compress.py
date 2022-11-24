import pandas as pd

class BinaryTable:
    
    def __init__(self):
        self.table = pd.read_excel("./HuffmanAdaptativo.xlsx", dtype=str)
        self.alphabet = list(self.table["caracter"].unique())
        self.binary_map = list(self.table["binario"].unique())

    def text2binary(self, character):
        if character in self.alphabet:
            return self.table["binario"][self.table["caracter"] == character].values[0]

    def binary2text(self, binary):
        if binary in self.binary_map:
            return self.table["caracter"][self.table["binario"] == binary].values[0]


if __name__ == "__main__":
    table = BinaryTable()
    binary = table.text2binary("s")
    print(table.binary2text(binary))
from huffman import HuffmanCoding
import sys

print("Cual es el archivo que desea comprimir?")
path = input()

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)
# Adaptive Huffman Tree 🎄
📚 Practice #3 of Computer organization subject. Adaptative Huffman tree algorithm

## Team members 🤜🏽🤛🏽
* [Miguel Cabrera](https://github.com/Miguelco23 "GitHub")
* [Benjamin De la Torre](https://github.com/bened18 "GitHub")
* [Sebastian Marin](https://github.com/smaring2 "GitHub")

## Compilator used ✅
Python 3.10.6

### [Video link](https://www.youtube.com/watch?v=uV_MeIxBY-8&feature=youtu.be)📽

___

## Description 📝

We have a huffmanCoding class with the atributes and functions necesary for the compression. 
We also have a main script where we select the file to compress and import huffmanCoding to create de .bin file

```py
from huffman import HuffmanCoding
import sys

print("Cual es el archivo que desea comprimir?")
path = input()

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)
```

### Initial class diagram

![class diagram](class-diagram-1.jpeg)
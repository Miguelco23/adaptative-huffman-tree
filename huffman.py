import heapq
import os

class HuffmanCoding:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

    # Clase para los nodos del arbol (letra, peso e hijos)
	class HeapNode:
		def __init__(self, char, freq):
			self.char = char
			self.freq = freq
			self.left = None
			self.right = None

		# Comparaciones, less than, equals
		def __lt__(self, other):
			return self.freq < other.freq

		def __eq__(self, other):
			if(other == None):
				return False
			if(not isinstance(other, HeapNode)):
				return False
			return self.freq == other.freq

    # Crea el diccinario con el peso de los caracteres
	def make_frequency_dict(self, text):
		frequency = {}
		for character in text:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1
		return frequency

    # Crea la cola de prioridad ordenando las letras por peso
	def make_heap(self, frequency):
		for key in frequency:
			node = self.HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

    # Une los primeros nodos de la cola y crea el arbol
	def merge_nodes(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = self.HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)

    #Lee el arbol recursivamente y crea el codigo para cada letra
	def make_codes_helper(self, root, current_code):
		if(root == None):
			return

		if(root.char != None):
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")


	def make_codes(self):
		root = heapq.heappop(self.heap)
		current_code = ""
		self.make_codes_helper(root, current_code)

    # Dados los codigos, traduce el texto a los codigos de sus letras
	def get_encoded_text(self, text):
		encoded_text = ""
		for character in text:
			encoded_text += self.codes[character]
		return encoded_text

    # Añade 0s para que el total sea multiplo de 8 bits el restultado
	def pad_encoded_text(self, encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text

    # Convierte el texto codificado en un arreglo de bytes 
	def get_byte_array(self, padded_encoded_text):
		if(len(padded_encoded_text) % 8 != 0):
			print("El texto codificado no fue rellenado correctamente")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b

    # Metodo para comprimir el texto del archivo
	def compress(self):
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + ".bin"

		with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
			text = file.read()
			text = text.rstrip()

			frequency = self.make_frequency_dict(text)
			self.make_heap(frequency)
			self.merge_nodes()
			self.make_codes()

			encoded_text = self.get_encoded_text(text)
			padded_encoded_text = self.pad_encoded_text(encoded_text)

			b = self.get_byte_array(padded_encoded_text)
			output.write(bytes(b))

		print("Compressed")
		return output_path





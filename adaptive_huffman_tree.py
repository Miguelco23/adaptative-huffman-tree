import click
import os
from multiprocessing import Process
from read_txt_to_compress import BinaryTable

class InvalidCharacterError(Exception):
    pass

def huffmantree(txt, identificador):
    file = open(f"./files_compressed/compress{identificador}.txt", "w")
    file.write(txt)
    file.close()
    return txt



def split(a: list, n: int):
    procs = []
    identificador = 1
    if n < 5 and n > 0:
        k, m = divmod(len(a), n)
        separate = list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)))
        
        # instantiating process with arguments
        for hilo in separate:
            #print(name)
            proc = Process(target=huffmantree, args=(hilo,identificador,))
            #file = open(f"./compress{identificador}.txt", "w")
            #file.write(proc)
            #file.close()
            identificador = identificador + 1
            procs.append(proc)
            proc.start()
        # complete the processes
        for proc in procs:
            proc.join()
        #print(list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)))) 
        return separate
    elif n <= 0:
        return "Por lo menos debe haber 1 hilo"
    elif n > 4:
        return "No se soportan mas de 4 hilos"
        


@click.command("huffman")
@click.option("-f", "--file", required=True, help="Archivo a comprimir")
@click.option("-t", "--threads", default=4, help="Numero de hilos")
def huffman(file, threads):
    try:
        print(f"El archivo pesa: {os.stat(file).st_size} bytes")
        with open(file, "r") as f:
            txt = f.read()

        b_table = BinaryTable()

        # Caso base: string vacía
        if len(txt) == 0:
            return "esta vacio el archivo"

        # Obtener los caracteres unicos
        characters = set(txt)

        # Validar que todos los caracteres pertencen al alfabeto
        if not all(c in b_table.alphabet for c in characters):
            raise InvalidCharacterError("Símbolo encontrado genera error de compresión")
        
        split(txt, threads)
    except InvalidCharacterError as e:
        print(e)
        raise click.Abort()


# Recibir la cadena de string por teclado
if __name__ == '__main__':
    huffman()

# Metodo con el diccionario en ASCII para chechear errores y para contar frecuencia de cada caracter
def checkFrecuency(obj, text):

    ascii = [' ','!','"','#','$','%','&','á','é','í','ó','ú','Á','É','Í','Ó','Ú','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','W','V','X','Y','Z','[',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~',]

    for i in text:
        if i not in ascii:
            print("Símbolo encontrado genera error de compresión")
            return
        
        obj[i] = text.count(i)

    
# Metodo para ordenar la cola de prioridad
def orderFrecuency(freq):
    sortedF = sorted(freq.items(), key=lambda x: x[1],)
    return sortedF

  
    
#Escribir archivo
def writeFile(text, filename):

    def listToString(s):
 
        str1 = ""
 
        for ele in s:
            str1 += "01"
 
        return str1

    file = open(filename, 'w')
    print(text)
    print(listToString(text))
    file.write(listToString(text))




# Main
if __name__ == "__main__":
    print("Cual es el nombre del arcivo que desea comprimir?")
    nombre = input()
    archivo = open(nombre).read()

    freq = {}
    checkFrecuency(freq, archivo)
    newFreq = orderFrecuency(freq)

    print("Cual es el nombre del archivo comprimido?")
    nombre = input()
    writeFile(newFreq, nombre)





# Metodo con el diccionario en ASCII para chechear errores y para contar frecuencia de cada caracter
def checkFrecuency(obj, text):

    ascii = [' ','!','"','#','$','%','&','á','é','í','ó','ú','Á','É','Í','Ó','Ú','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','W','V','X','Y','Z','[',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~',]

    for i in text:
        if i not in ascii:
            print("Símbolo encontrado genera error de compresión")
            return
        
        obj[i] = text.count(i)

    
# Metodo para ordenar la cola de prioridad e imprimirla
def printOrdenedFrequency(freq):

    sortedFreq = sorted(freq.items(), key=lambda x: x[1],)
 
    cont = 106 
    for i in sortedFreq:  
        print(i)
        cont = cont - 1
        if cont == 0: 
            return
    





# Main
if __name__ == "__main__":
    print("Cual es el nombre del arcivo que desea comprimir?")
    nombre = input()
    archivo = open(nombre).read()

    freq = {}
    checkFrecuency(freq, archivo)
    printOrdenedFrequency(freq)




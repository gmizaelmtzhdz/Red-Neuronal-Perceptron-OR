'''

    Autor: Mizael Martinez
    Red Neuronal: OR

'''
class PerceptronOR:
    def __init__(self):
        self.__conjuntoDeEntrenamiento=None
        self.__pesos=None
        self.__umbral=0
        self.__tasaDeAprendizaje=0
    def establecerConjuntoEntrenamiento(self,conjuntoDeEntrenamiento):
        self.__conjuntoDeEntrenamiento=conjuntoDeEntrenamiento

    def establecerPesos(self,pesos):
        self.__pesos=pesos

    def establecerUmbral(self,umbral):
        self.__umbral=umbral

    def establecerTasaDeAprendizaje(self,tasaDeAprendizaje):
        self.__tasaDeAprendizaje=tasaDeAprendizaje

    def entrenarRed(self):
        contador_de_errores=0
        while True:
            contador_de_errores=0
            for entrada,salida in self.__conjuntoDeEntrenamiento:
                print pesos
                resultado=self.sumarEntradasYPesos(entrada) > umbral
                error=salida-resultado
                if error != 0:
                    contador_de_errores+=1
                    self.actualizarPesos(entrada,error)
            if contador_de_errores==0:
                break

    def sumarEntradasYPesos(self,entradas):
        contador=0
        n=len(entradas)
        suma=0
        while contador < n:
            suma=suma+entradas[contador]*self.__pesos[contador]
            contador+=1
        return suma
    def actualizarPesos(self,entradas,error):
        for indice, valor in enumerate(entradas):
            self.__pesos[indice]=self.__pesos[indice]+self.__tasaDeAprendizaje*error*valor
    def imprimirPesos(self):
        print self.__pesos


umbral = 0.5
tasa_de_aprendizaje = 0.1
pesos=[0,0]
conjunto_de_entrenamiento = [((0,0),0), ((0,1),1), ((1,0),1), ((1,1), 1)]

perceptronOR=PerceptronAND()
perceptronOR.establecerConjuntoEntrenamiento(conjunto_de_entrenamiento)
perceptronOR.establecerPesos(pesos)
perceptronOR.establecerUmbral(umbral)
perceptronOR.establecerTasaDeAprendizaje(tasa_de_aprendizaje)
perceptronOR.entrenarRed()
perceptronOR.imprimirPesos()

#probando la red neuronal
print perceptronOR.sumarEntradasYPesos((1,0))>umbral

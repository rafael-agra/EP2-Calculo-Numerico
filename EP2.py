# Nome: Rafael Agra de Castro Motta Nº USP 11807192
# Nome: Thaís dos Santos Ferreira N° USP: 11820513

#Importação da biblioteca numpy
import numpy as np

#Calculo da Quadrantura de Gauss para casos sem funcao
def QuadraturaGauss1(funcao, n,  a, b, c, d): 
    # Funcao do numpy que retorna os nos e pesos dados no enunciado
    x_, wx =  np.polynomial.legendre.leggauss(n)
    y_, wy = map(np.array, (x_, wx))
    

    I = 0
    #Loop que calcula a primeira integral
    for i in range (n):
        I_ = 0
        m1 = (b - a) / 2
        m2 =  (b + a) / 2
        x = (m1* x_[i]) + m2 
        #Calculo da segunda integral
        for j in range(n):
            dd = d
            cc = c
            g1 = (dd - cc) / 2
            g2 = (dd + cc) / 2
            
            I_ += funcao(x, g1 * y_[j] +  g2) * wy[j]
        I += wx[i] * g1 * I_ 
  
    I *= m1

    return I



#Calculo da Quadrantura de Gauss para casos com funcao em ambos
def QuadraturaGauss2(funcao, n,  a, b, c, d): 
    # Funcao do numpy que retorna os nos e pesos dados no enunciado
    x_, wx =  np.polynomial.legendre.leggauss(n)
    y_, wy = map(np.array, (x_, wx))
    

    I = 0
    #Loop que calcula a primeira integral
    for i in range (n):
        I_ = 0
        m1 = (b - a) / 2
        m2 =  (b + a) / 2
        x = (m1* x_[i]) + m2 
        #Calculo da segunda integral
        for j in range(n):
            dd = d(x)
            cc = c(x)
            g1 = (dd - cc) / 2
            g2 = (dd + cc) / 2
            
            I_ += funcao(x, g1 * y_[j] +  g2) * wy[j]
        I += wx[i] * g1 * I_ 
  
    I *= m1

    return I

#Calculo da Quadrantura de Gauss para casos com funcao em 1 apenas
def QuadraturaGauss3(funcao, n,  a, b, c, d): 
    # Funcao do numpy que retorna os nos e pesos dados no enunciado 
    x_, wx =  np.polynomial.legendre.leggauss(n)
    y_, wy = map(np.array, (x_, wx))
    
    I = 0
    #Loop que calcula a primeira integral
    for i in range (n):
        I_ = 0
        m1 = (b - a) / 2
        m2 =  (b + a) / 2
        x = (m1* x_[i]) + m2 
        #Calculo da segunda integral
        for j in range(n):
            dd = d(x)
            cc = c
            g1 = (dd - cc) / 2
            g2 = (dd + cc) / 2
            
            I_ += funcao(x, g1 * y_[j] +  g2) * wy[j]

        I += wx[i] * g1 * I_ 
  
    I *= m1

    return I


#---------
# Cubo
# --------

#Funcao do Cubo
f1 = lambda x, y : 1 #dydx
#Adicao dos limites de integracao
d = 1
c = 0
b = 1
a = 0
I1_1 = QuadraturaGauss1(f1, 6, a, b, c, d)  
I1_2 = QuadraturaGauss1(f1, 8, a, b, c, d)  
I1_3 = QuadraturaGauss1(f1, 10, a, b, c, d)  
print("----EXEMPLO 1----")
print("Cubo para (para n = 6): ", I1_1)
print("Cubo para (para n = 8): ", I1_1)
print("Cubo para (para n = 10): ", I1_1)

#---------
#Tetraedro
#---------
#Funcao do Cubo
f1_ = lambda x, y : 1 - x - y
#Adicao dos limites de integracao
a = 0
b = 1
c = 0
d = lambda x : 1-x
I2_1 = QuadraturaGauss3(f1_, 6, a, b, c, d)
I2_2 = QuadraturaGauss3(f1_, 8, a, b, c, d)
I2_3 = QuadraturaGauss3(f1_, 10, a, b, c, d)

print("Tetraedro (para n = 6): ", I2_1)
print("Tetraedro (para n = 8): ", I2_2)
print("Tetraedro (para n = 10): ", I2_3)


#--------
# Exemplo 2
#--------
#DyDx

a = 0
b = 1
c = 0
d = lambda x : 1-x**2
f3 = lambda x, y : 1 
I3_1 = QuadraturaGauss3(f3, 6, a, b, c, d)
I3_2 = QuadraturaGauss3(f3, 8, a, b, c, d)
I3_3 = QuadraturaGauss3(f3, 10, a, b, c, d)

print("----EXEMPLO 2----")
print("DyDx (para n = 6): ", I3_1)
print("DyDx (para n = 8): ", I3_2)
print("DyDx (para n = 10): ", I3_3)

# ---------
#DxDy 

a = 0
b = 1 
c = 0
d = lambda x: np.sqrt(1-x)
f2 = lambda x, y : 1
I4_1 = QuadraturaGauss3(f2, 6, a, b, c, d)
I4_2 = QuadraturaGauss3(f2, 8, a, b, c, d)
I4_3 = QuadraturaGauss3(f2, 10, a, b, c, d)

print("DxDy (para n = 6): ", I4_1)
print("DxDy (para n = 8): ", I4_2)
print("DxDy (para n = 10): ", I4_3)

#--------
# Exemplo 3 
#--------
# Area
b = 0.5
a = 0.1
f3 = lambda x, y : np.sqrt((np.e ** ((2 * y) / x ) / x ** 2 + (np.e ** ((2 * y) / x) * y ** 2)/ x ** 4 + 1)) #dxdy
d = lambda x :  x ** 2
c = lambda x : x ** 3
I5_1 = QuadraturaGauss2(f3, 6, a, b, c, d)
I5_2 = QuadraturaGauss2(f3, 8, a, b, c, d)
I5_3 = QuadraturaGauss2(f3, 10, a, b, c, d)

print("----EXEMPLO 3----")
print("Area (para n = 6): ", I5_1)
print("Area (para n = 8): ", I5_2)
print("Area (para n = 10): ", I5_3)

#--------
# Volume 

f3_ = lambda x, y: np.e ** (y/x) #dydx

I6_1 = QuadraturaGauss2(f3_, 6, a, b, c, d)
I6_2 = QuadraturaGauss2(f3_, 8, a, b, c, d)
I6_3 = QuadraturaGauss2(f3_, 10, a, b, c, d)

print("Volume (para n = 6): ", I6_1)
print("Volume (para n = 8): ", I6_2)
print("Volume (para n = 10): ",I6_3)


#--------
# Exemplo 4
#--------
a = 0
b = 0.25
c = 0
d = lambda y : np.sqrt(1-(y+0.75)**2)
f5 = lambda x, y : y
I7_1 = QuadraturaGauss3(f5, 6, a, b, c, d)
I7_1F = I7_1*2*np.pi

I7_2 = QuadraturaGauss3(f5, 8, a, b, c, d)
I7_2F = I7_2*2*np.pi

I7_3 = QuadraturaGauss3(f5, 10, a, b, c, d)
I7_3F = I7_3*2*np.pi

print("----EXEMPLO 4----")
print("Calota (para n = 6): ", I7_1F)
print("Calota (para n = 8): ", I7_2F)
print("Calota (para n = 10): ",I7_3F)

#--------
#Solido de revolucao 

a = -1
b = 1   
c = 0
d = lambda y : np.e**(-y**2)
f6 = lambda x, y : y

I8_1 = QuadraturaGauss3(f6, 6, a, b, c, d)
I8_1F = 2*np.pi*I8_1


I8_2 = QuadraturaGauss3(f6, 8, a, b, c, d)
I8_2F = 2*np.pi*I8_2


I8_3 = QuadraturaGauss3(f6, 10, a, b, c, d)
I8_3F = 2*np.pi*I8_3

print("Solido de revolucao (para n = 6): ", I8_1F)
print("Solido de revolucao (para n = 8): ", I8_2F)
print("Solido de revolucao (para n = 10): ",I8_3F)





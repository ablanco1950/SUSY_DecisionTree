# Test dataset
ContaMax=5000000
Start=4500000


NodoRaiz=7
Nodo1=1
Nodo2=7
Nodo3=1
ValorDecision=1208 
ValorDecision1=604
ValorDecision2=764
ValorDecision3=919



# Case training
#ContaMax=4500000
#Start=1

TopeMemoria = 20004 

import time

Inicio=time.time()
       
Max=[float(20.553449630737305)]
Max.append(float(2.10160493850708))
Max.append(float(1.7348390817642212))
Max.append(float(33.035621643066406))
Max.append(float(2.059720754623413))
Max.append(float(1.734686255455017))
Max.append(float(21.068876266479492))
Max.append(float(1.7406890392303467))
Min=[float(0.25488153100013733)]
Min.append(float(-2.1029269695281982))
Min.append(float(-1.7347885370254517))
Min.append(float(0.4285859763622284))
Min.append(float(-2.0593061447143555))
Min.append(float(-1.7342021465301514))
Min.append(float(2.598710998427123E-4))
Min.append(float(-1.7271170616149902))

def CalcIndex(Max, Min, Nodo, ValorNodo):
    ValorNodo =ValorNodo - Min[Nodo-1]
    Maximo = Max[Nodo-1]
    Maximo = Maximo - Min[Nodo-1]
    indice =(int) (((TopeMemoria - 2.0) * ValorNodo)/ Maximo)
    if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
            print("index overflowed=" + str( indice) + " in  the field ="+ str(Nodo) )
            indice=TopeMemoria
    return indice

f=open("C:\SUSY.csv","r")

Conta=0;
TotAciertos=0.0
TotFallos=0.0


for linea in f:
    Conta=Conta+1
    if Conta < Start :continue
    if Conta > ContaMax :break
    lineadelTrain =linea.split(",")
    ValorTrain =float(lineadelTrain[NodoRaiz])
    indice=CalcIndex(Max, Min, NodoRaiz, ValorTrain)
    if indice <= ValorDecision:
         
         ValorTrain =float(lineadelTrain[Nodo1])
         indice=CalcIndex(Max, Min, Nodo1, ValorTrain)
         if indice > ValorDecision1: 
             ValorTrain =float(lineadelTrain[Nodo2])
             indice=CalcIndex(Max, Min, Nodo2, ValorTrain)
             if indice > ValorDecision2:   
                 ClasePredecida=1
             else:
                 ValorTrain =float(lineadelTrain[Nodo3])
                 indice=CalcIndex(Max, Min, Nodo3, ValorTrain)
                 if indice > ValorDecision3:   
                     ClasePredecida=1
                 else:
                     ClasePredecida=0
         else:
             
                 ClasePredecida=0
            
    else:
            # campo7 > 1208 es clase 1 con p=88%
            ClasePredecida= 1
    ClaseLeida=float(lineadelTrain[0])
    Clase=int(ClaseLeida)
    if Clase==ClasePredecida:
        TotAciertos=TotAciertos+1
    else:
        TotFallos=TotFallos+1
    
print("")  
print("RESULTS DECISION TREE")     
print("Total hits TEST = " + str(TotAciertos))
print("Total failures TEST = " + str(TotFallos))

Fin =time.time()  
print ( "")
print( " Time = " + str(Fin - Inicio) )

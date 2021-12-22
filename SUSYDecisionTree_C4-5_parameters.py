Campo=8

NodoRaiz=7
Nodo1=1
Nodo2=7

ValorDecision=1208
ValorDecision1=518
ValorDecision2=1633

import numpy as np
import math


""" CLASIFIER FUNCTION ==========================================================="""

def Susy_C4_5(Y_train, X_Train, Y_test, X_test, W):
    
                
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
        NumClases=2
        NumCampos =9
        #TopeMemoria = 154
        TopeMemoria = 20004
        
        # Got frm https://stackoverflow.com/questions/15448594/how-to-add-elements-to-3-dimensional-array-in-python
        TabVotos = np.zeros((NumCampos,TopeMemoria+1,NumClases))
        
        Maximo=0.0
        Conta=0.0
        Cont=-1
        
        ContClase=[float(0.0)]
        for j in range(NumClases):
             ContClase.append(float(0.0))
       
        Start=0
        End = 4500000
       
    
       
        f=open("C:\\SUSY.csv ","r")
        
        
        for linea in f:
            
            lineadelTrain =linea.split(",")
            Conta = Conta + 1
            if Conta < Start:
                continue
            if Conta > End:
                break
            ValorTrain =float(lineadelTrain[NodoRaiz])
            ValorTrain =ValorTrain - Min[NodoRaiz-1]
            Maximo = Max[NodoRaiz-1]
            Maximo = Maximo - Min[NodoRaiz-1]
            indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
            if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                    print("index overflowed=" + str( indice) + " in  the field ="+ str(ValorDecision) )
                    indice=TopeMemoria
            # Rama < Nodo Raiz
            #if indice > ValorDecision: continue
            # Rama =< nodo raiz
            if indice <= ValorDecision: continue
            ValorTrain =float(lineadelTrain[Nodo1])
            ValorTrain =ValorTrain - Min[Nodo1-1]
            Maximo = Max[Nodo1-1]
            Maximo = Maximo - Min[Nodo1-1]
            indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
            if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                    print("index overflowed=" + str( indice) + " in  the field ="+ str(ValorDecision) )
                    indice=TopeMemoria
            #if (indice <= ValorDecision1):continue
            if (indice > ValorDecision1):continue
            ValorTrain =float(lineadelTrain[Nodo2])
            ValorTrain =ValorTrain - Min[Nodo2-1]
            Maximo = Max[Nodo2-1]
            Maximo = Maximo - Min[Nodo2-1]
            indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
            if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                    print("index overflowed=" + str( indice) + " in  the field ="+ str(ValorDecision) )
                    indice=TopeMemoria
            if (indice > ValorDecision2):continue
            #if (indice <= ValorDecision2):continue
            Cont = Cont +1
            if len(W) == 1:
              FactorPri=1.0
            else:
                FactorPri=W[Cont]
                
            ClaseLeida=float(lineadelTrain[0])
            Clase=int(ClaseLeida)
                               
            ContClase[Clase]=ContClase[Clase] + 1
                       
            
           
            z=-1
            for x  in lineadelTrain:
                
                z=z+1
                if z==NumCampos:
                    break
              
                if z==0: continue
                   
                ValorTrain =float(lineadelTrain[z])
                ValorTrain =ValorTrain - Min[z-1]
                Maximo = Max[z-1]
                Maximo = Maximo - Min[z-1]
                indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
                if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                    print("index overflowed=" + str( indice) + " in  the field ="+ str(z-1) )
                    indice=TopeMemoria
                Wvalor=0.0
             
                Wvalor= TabVotos[z,TopeMemoria-1,Clase]
                Wvalor= Wvalor + 1
                TabVotos[z,TopeMemoria-1,Clase]=Wvalor 
               
                Wvalor= TabVotos[z,indice,Clase]
                Wvalor=Wvalor+FactorPri
                TabVotos[z,indice,Clase]=Wvalor 
                # print("Acumula en el indice = " + str(indice) + " Clase =" + str(Clase) + " Wvalor =" + str(Wvalor))
       
        f.close()
        
       # for Campo in range(NumCampos):
       
        ContaPanta=0
        HClase_PreguntaMin=999999999.0
        indiceMin=999999
        for i in range (TopeMemoria-2):
            # ClaseMenos y ClaseMas computan computan las clases
            # que existen con valores del campo menos o mas del 
            # campo considerado
            ClasesMenos = np.zeros(NumClases)
            ClasesMas = np.zeros(NumClases)
            TotClaseMenos=0
            TotClaseMas=0
            EntroCampoMenos=0
            EntroCampoMas=0
            for y in range(i):
               
                for w in range (NumClases):
                    # print("Recupera indice = "+str(i) + "Clase= " + str(w) + "Valor = " +str(TabVotos[Campo,i,w]))
                    TotClaseMenos= TotClaseMenos + TabVotos[Campo,y,w]
                    ClasesMenos[w]=ClasesMenos[w]+ TabVotos[Campo,y,w]
            
            for j in range (NumClases):
                    if (ClasesMenos[j] != 0.0) :
                        P=ClasesMenos[j]/TotClaseMenos
                        # print("Indice =" + str(i) + " Clase= " + str(j) +  " Probabilidad Campo  "+  str(P) + "Total Clases = "+ str(TotClases))
                        EntroCampoMenos= EntroCampoMenos +  P*math.log(1.0/P,2)
            #print("Entropy < indiex =" +str(i) + " field "+  str(Campo)+ " = " + str(EntroCampoMenos) )
            for y in range(i,TopeMemoria-2):
               
                for w in range (NumClases):
                    # print("Recupera indice = "+str(i) + "Clase= " + str(w) + "Valor = " +str(TabVotos[Campo,i,w]))
                    TotClaseMas= TotClaseMas + TabVotos[Campo,y,w]
                    ClasesMas[w]=ClasesMas[w]+ TabVotos[Campo,y,w]
            
            for j in range (NumClases):
                    if (ClasesMas[j] != 0.0) :
                        P=ClasesMas[j]/TotClaseMas
                        # print("Indice =" + str(i) + " Clase= " + str(j) +  " Probabilidad Campo  "+  str(P) + "Total Clases = "+ str(TotClases))
                        EntroCampoMas= EntroCampoMas +  P*math.log(1.0/P,2)
            #print("Entropy > index=" +str(i) + " field "+  str(Campo)+ " = " + str(EntroCampoMas) )
            HClase_Pregunta =(TotClaseMenos/(TotClaseMenos+TotClaseMas) )*EntroCampoMenos +  (TotClaseMas/(TotClaseMenos+TotClaseMas) )*EntroCampoMas
            #print("HClass_Question index =" +str(i) + " field "+  str(Campo)+ " = " + str(HClase_Pregunta) )
            if (HClase_Pregunta < HClase_PreguntaMin):
                indiceMin=i
                HClase_PreguntaMin=HClase_Pregunta
            ContaPanta=ContaPanta + 1
            if ContaPanta > 1000:
                print("Procesa 1000")
                ContaPanta=0
        print("Index minimum =" +str(indiceMin) + " field "+  str(Campo)+ " Class Question " + str(HClase_PreguntaMin) )
        ClasesMenos = np.zeros(NumClases)
        ClasesMas = np.zeros(NumClases)
        TotClaseMenos=0
        TotClaseMas=0
        for y in range(indiceMin+1,TopeMemoria-2):
               
                for w in range (NumClases):
                   
                    TotClaseMas= TotClaseMas + TabVotos[Campo,y,w]
                    ClasesMas[w]=ClasesMas[w]+ TabVotos[Campo,y,w]
        for y in range(indiceMin):
                
                for w in range (NumClases):
                   
                    TotClaseMenos = TotClaseMenos + TabVotos[Campo,y,w]
                    ClasesMenos[w]=ClasesMenos[w]+ TabVotos[Campo,y,w] 
        print(" " )
        print("Index Classes Values = " + str(indiceMin))
        for w in range (NumClases):
                    print("Class = " + str(w) + " in branch > "+ str( ClasesMas[w]) + " in branch < "+ str( ClasesMenos[w]))
                                                                                            
############################################################################33
# MAIN
###########################################################################333

Y_train=[float(1.0)]
X_train=[float(1.0)]
Y_test=[float(1.0)]
X_test=[float(1.0)]
W=[float(1.0)]
Susy_C4_5(Y_train, X_train, Y_test, X_test, W)

    
###SIMULACIÓN ESTADíSTICA DEL RISK

import numpy as np
import random
import matplotlib.pyplot as plt


j1_array=np.array([]);j2_array=np.array([]);

unidades=np.arange(2,100)
n=1000


for und1 in unidades:
    und2=und1
    orund1=und1
    orund2=und2
    
    k1=0;k2=0;cont=0;kt1=0;kt2=0;v1=0;v2=0;
    for partidas in range(0,n):
    
        und1=orund1
        und2=orund2
        
        while (und1>=1) and (und2!=0):
    
            class jugador:
                    atacar3=np.array(sorted([random.randrange(1,7),random.randrange(1,7),random.randrange(1,7)]))[1:3]
                    atacar2=np.array(sorted([random.randrange(1,7),random.randrange(1,7)]))[0:2]
                    atacar1=np.array([random.randrange(1,7)])
                    defender2=np.array(sorted([random.randrange(1,7),random.randrange(1,7)]))[0:2]
                    defender1=np.array([random.randrange(1,7)])
                    
        
             # new instances
            j1=jugador()
            j2=jugador()
            
             # 3-2
            if (und1>=3) and (und2>=2):  
                cont=cont+2
                if j1.atacar3[1] > j2.defender2[1]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1
                        
                if j1.atacar3[0] > j2.defender2[0]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1
    
             # 3-1  
            if (und1>=3) and (und2==1):   
                cont=cont+1
                if j1.atacar3[1] > j2.defender1[0]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1
             # 2-2
            if (und1==2) and (und2>=2): 
                cont=cont+2
                if j1.atacar2[1] > j2.defender2[1]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1
                    
                if j1.atacar2[0] > j2.defender2[0]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1
             # 2-1
            if (und1==2) and (und2==1):  
                cont=cont+1
                if j1.atacar1[0] > j2.defender1[0]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1 
             # 1-2
            if (und1==1) and (und2>=2):  
                cont=cont+1
                if j1.atacar1[0] > j2.defender2[1]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1 
             # 1-1
            if (und1==1) and (und2==1):   
                cont=cont+1
                if j1.atacar1[0] > j2.defender1[0]:
                    k1=k1+1
                    und2=und2-1
                else:
                    k2=k2+1
                    und1=und1-1
        
                    
         # contador de victorias
        if (und1>und2):
            v1=v1+1
        else:
            v2=v2+1
        
    
    j1_array = np.append(j1_array, v1/(partidas+1)*100)
    j2_array = np.append(j2_array, v2/(partidas+1)*100)
    
    
plt.plot(unidades,j1_array,label="J1",color='red')
plt.plot(unidades,j2_array,label="J2",color='blue')
plt.plot(unidades,np.ones(len(unidades))*50,color='black',linestyle='dashed',linewidth = 0.7)
plt.xlabel('number of units of both players')
plt.ylabel('winning probability')
plt.title('Risk probabilities') 
plt.legend() 
  
#Plotting graph
#https://www.youtube.com/watch?v=ufO_BScIHDQ
#https://www.youtube.com/watch?v=B-oExeraNHc
#https://matplotlib.org/stable/tutorials/text/mathtext.html
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

#do 19:20
#https://www.youtube.com/watch?v=2qH_HvoBG0M

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


kGain = 100.0
m_lambda = 0.1386

def funct(x,b, Vun):
    return kGain * Vun * np.exp(-m_lambda * x * b)
    #return kGain * x * b *np.exp(-m_lambda * x)
    #od prije
    #return kGain * b * np.exp(-m_lambda * x)

data = np.loadtxt(fname = 'gainFile.csv', delimiter = ',')
print data

flag = 0
X = []
Y = []
Vun = []
funcdata = []
plt.figure(num=0,dpi=120)

for i in range(len(data)):
    if data[i][0] == 0 and data[i][1] == 0:
        flag +=1
        print (X)
        print (Y)
        print("----------")
        if flag == 1:
            print ("test")
            plt.plot(X, Y, 'ro', label = "first candidate trajectory")
            print ("test1")
            popt, pcov = curve_fit(funct,X,Y,bounds = (0,20))
            print ("test2")
            perr = np.sqrt(np.diag(pcov))

            print ("test3")
            for j in range (len(X)):
                funcdata.append(funct(X[j], popt, Vun[j]))
            print ("test4")
            plt.plot(X,funcdata, 'r', label = "Model")

        elif flag == 2:
            plt.plot(X, Y, 'go', label = "second candidate trajectory")

            popt, pcov = curve_fit(funct,X,Y,bounds = (0,20))
            perr = np.sqrt(np.diag(pcov))

            for j in range (len(X)):
                funcdata.append(funct(X[j], popt, Vun[j]))
            plt.plot(X,funcdata, 'g', label = "Model")
        elif flag == 3:
            plt.plot(X, Y, 'bo', label = "third candidate trajectory")

            popt, pcov = curve_fit(funct,X,Y,bounds = (0,20))
            perr = np.sqrt(np.diag(pcov))

            for j in range (len(X)):
                funcdata.append(funct(X[j], popt, Vun[j]))
            plt.plot(X,funcdata, 'b', label = "Model")
        elif flag == 4:
            plt.plot(X, Y, 'co', label = "fourth candidate trajectory") 

            popt, pcov = curve_fit(funct,X,Y,bounds = (0,20))
            perr = np.sqrt(np.diag(pcov))

            for j in range (len(X)):
                funcdata.append(funct(X[j], popt, Vun[j]))
            plt.plot(X,funcdata, 'c', label = "Model")
        elif flag == 5:
            plt.plot(X, Y, 'mo', label = "fifth candidate trajectory")

            popt, pcov = curve_fit(funct,X,Y,bounds = (0,20))
            perr = np.sqrt(np.diag(pcov))

            for j in range (len(X)):
                funcdata.append(funct(X[j], popt, Vun[j]))
            plt.plot(X,funcdata, 'm', label = "Model") 
        else:
            print ("Error on plotting")
        del X[:]
        del Y[:]
        del Vun[:]
        del funcdata[:]      
    else:
        Y.append(data[i][0])
        X.append(data[i][1])
        Vun.append(data[i][2])
    if flag >= 5:
        break

plt.title("InformationGain-Distance Graph")
plt.xlabel("$L(p_{i},p_{v_{c}})$ / m")
plt.ylabel("$G(v_{c})$")


plt.legend()
plt.savefig('image_plot')
plt.show()
#Plotting graph
#https://www.youtube.com/watch?v=ufO_BScIHDQ
#https://www.youtube.com/watch?v=B-oExeraNHc
#https://matplotlib.org/stable/tutorials/text/mathtext.html
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname = 'gainFile.csv', delimiter = ',')
print data

flag = 0
X = []
Y = []

plt.figure(num=0,dpi=120)

for i in range(len(data)):
    if data[i][0] == 0 and data[i][1] == 0:
        flag +=1
        print (X)
        print (Y)
        print("----------")
        if flag == 1:
            plt.plot(X, Y, 'ro', label = "first candidate trajectory")
        #elif flag == 2:
            #plt.plot(X, Y, 'go', label = "second candidate trajectory")
        #elif flag == 3:
            #plt.plot(X, Y, 'bo', label = "third candidate trajectory")
        elif flag == 4:
            plt.plot(X, Y, 'co', label = "second candidate trajectory") 
        #elif flag == 5:
            #plt.plot(X, Y, 'mo', label = "fifth candidate trajectory") 
        elif flag == 6:
            plt.plot(X, Y, 'yo', label = "third candidate trajectory")
        #elif flag == 7:
            #plt.plot(X, Y, 'ko', label = "seventh candidate trajectory")
        elif flag == 8:
            plt.plot(X, Y, marker='o', color='magenta', linewidth=0, label = "fourth candidate trajectory")
        elif flag == 9:
            plt.plot(X, Y, marker='o', color='orange', linewidth=0, label = "fifth candidate trajectory")
        #elif flag == 10:
            #plt.plot(X, Y, marker='o', color='lightblue', linewidth=0, label = "tenth candidate trajectory")
        #else:
            #print ("Error on plotting")
        del X[:]
        del Y[:]      
    else:
        Y.append(data[i][0])
        X.append(data[i][1])
    if flag >= 12:
        break

plt.title("InformationGain-Distance Graph")
plt.xlabel("$L(p_{i},p_{v_{c}})$ / m")
plt.ylabel("$G(v_{c})$")
plt.legend()
plt.savefig('image_plot')
plt.show()

#X = np.linspace(-10,10, 1000)
#xlist = np.arange(-10,10.1,.1)
#Y = 3*X

#plt.figure(redni broj slike, dots per inch)

#plotting another graph on the same plot
#plt.plot(x,y**(1/2), '--g', label=r"f(x)$^(1/2)$")

#legend writes what is marked with "label"

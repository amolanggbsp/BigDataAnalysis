from matplotlib import pyplot as plt
import numpy as np

data=[[3, 1.5, 1],
      [2, 1,   0],
      [4, 1.5, 1],
      [3, 1,   0],
      [3.5,0.5,1],
      [2, 0.5, 0],
      [5.5, 1, 1],
      [1, 1,   0]]

mystery_flower=[4.5,1]

#length, width, type

#network

#   0   flower type 
#         w1,w2,b
# length, width

w1=np.random.randn()
w2=np.random.randn()
b=np.random.randn()


def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))

T=np.linspace(-10,5,10)
plt.plot(T,sigmoid(T),c='r')
plt.plot(T,sigmoid_p(T),c='b')




#scatter data

plt.axis([0,6,0,6])  #xmin, xmax 
plt.grid()

for i in range(len(data)):
    point = data[i]
    color= "r"
    if point[2]==0:
        color="b" 
    plt.scatter(point[0],point[1],c=color)



#training loop 

learning_rate =0.5
costs=[]

for i in range (1,50000):
    ri=np.random.randint(len(data))
    point=data[ri]
    
    z= point[0] * w1 + point[1] * w2 + b
    pred=sigmoid(z)
    
    target = point[2] 
    cost= np.square(pred-target)
    
    costs.append(cost)

    
    dcost_pred = 2 * (pred-target)
    dpred_dz =sigmoid_p(z)
    
    dz_dw1=point[0]
    dz_dw2 =point[1] 
    dz_db = 1 
    
    dcost_dz = dcost_pred *dpred_dz
    
    dcost_dw1 =dcost_dz *dz_dw1
    dcost_dw2= dcost_dz * dz_dw2
    dcost_db = dcost_dz * dz_db
    
    w1 = w1 - learning_rate *dcost_dw1 
    w2 = w2 - learning_rate *dcost_dw2 
    b= b - learning_rate *dcost_db
    
plt.plot(costs)

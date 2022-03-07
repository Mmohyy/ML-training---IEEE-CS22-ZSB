import matplotlib.pyplot as plt
import numpy as np
import csv

  x = []
  y = []
  with open("dataset.csv", 'r') as file:
      csv_reader = csv.reader(file)
      header = next(csv_reader)
      for row in csv_reader:
          x.append(float(row[0]))
          y.append(float(row[1]))
  n = len(x)

def cost(theta0, theta1,x,y):
    sum = 0
    for i in range(n):
        sum += (hypothesis(theta0, theta1, x[i]) - y[i])**2
    return sum/ (n*2)
  
def hypothesis(theta0, theta1, x):
    return theta0+theta1*x
  
 def gradient_descent(theta0, theta1, alpha):
    sum_0 = 0
    sum_1 = 0
    
    for i in range(n):
        sum_0 += hypothesis(theta0, theta1, x[i]) - y[i]
        sum_1 += (hypothesis(theta0, theta1, x[i]) - y[i]) * x[i]
        
    theta0 -= alpha * sum_0 / n
    theta1 -= alpha * sum_1 / n
    
    return theta0, theta1
  
  def main():
    theta0 = random.random()
    theta1 = random.random()
    alpha = 0.0003
    
    for i in range(100):   
        theta0, theta1 = gradientDescent(theta0, theta1, alpha)
    print("theta0 \t\t theta1")
    print(theta0,theta1)
    
    plt.plot(x, y, 'bo')
    result = []
    for i in x:
        result.append(theta_0 + theta_1 * i)
    plt.plot(x, result, color="red")
    plt.show()

    
if __name__ == '__main__':
    main()  

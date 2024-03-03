from cProfile import label
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.xlabel('day')
plt.ylabel('temp')

plt.plot( x , y , color='green' , linewidth=5 , linestyle='dotted')
plt.show()

plt.plot( x , y , 'gD') # g+ , g+- , g+-. -> can use anything in any order
plt.show() 

plt.plot( x , y , color='blue', marker='+' , linestyle='' , markersize=20 )
plt.show()

plt.plot( x , y , color='#888888', marker='D' , linestyle='' , markersize=5 )
plt.show()

plt.plot( x , y , color='#008840', marker='D' , alpha = 0.5)
plt.show()



import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]

# set axes labels and chart title
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')

plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")

# Show legend
#plt.legend(loc='best')  # -> best means it will set legend at best blank location automatically
plt.legend(loc='upper right',shadow=True,fontsize='large')

plt.grid()  # -> easy to locate any point

plt.show()



#_______Bar Chart_______

import matplotlib.pyplot as plt
import numpy as np

company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
revenue = [90, 136, 89, 27]
profit = [40, 2, 34, 12]

# Generating positions for the bars
x = np.arange(len(company))

# Width of the bars
width = 0.4

plt.ylabel("Revenue & Profit (in Billions)")
plt.title('US Technology Stocks')
plt.xticks(x, company)  # Setting x-axis labels

# Plotting the first bar chart
plt.bar(x - width/2, revenue, width, label='Revenue')

# Plotting the second bar chart slightly shifted to the right
plt.bar(x + width/2, profit, width, label='Profit')

plt.legend()
plt.show()

# to generate horizontal bar chart:

plt.barh(x - width/2, revenue, width, label='Revenue')
plt.barh(x + width/2, profit, width, label='Profit')

plt.legend()
plt.show()



#_______Histogram_______

import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist(blood_sugar_men, rwidth=0.8, bins=3 )    # by default number of bins is set to 10
# histogram needs only single dimension array y axis will contain fre of array
plt.show()

plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

# Histogram showing normal, pre-diabetic and diabetic patients distribution
#  80-100: Normal
#  100-125: Pre-diabetic
#  80-100: Diabetic

plt.hist(blood_sugar_men, bins=[80,100,125,150], rwidth=0.95, color='g') # can provide type of histogram by using histtype='step'
plt.show()

plt.hist([blood_sugar_men,blood_sugar_women], bins=[80,100,125,150], rwidth=0.95, color=['green','orange'],label=['men','women'])
plt.legend()
plt.show()

plt.hist(blood_sugar_men, bins=[80,100,125,150], rwidth=0.95, orientation='horizontal')
plt.show()



#_______Pie chart_______

import matplotlib.pyplot as plt

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]

plt.axis("equal")  # -> to make perfect circle of pie chart
plt.pie( exp_vals , labels=exp_labels , radius=1.5 , autopct = '%0.2f%%' , explode = [0,0.1,0,0,0.1] , startangle = 45)  #-> radius for size of circle
plt.show()
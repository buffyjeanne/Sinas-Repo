#Python Packages (Numpy, Pandas, etc)
#test

############################
#NumPy --> numerical Data, uncludes functions, data Structures
#############################
import numpy as np

#arrays instead of lists to perform operations with data --> faster and compact
#homogeneous : can only contain 1 single datatype ()
x=np.array([1,2,3,4]) #use list and define it as array

#ndarrays: "N-dimensional array"
#BUT: Sub-Arrays have to have same size!! --> represents a matrix
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
x_fail=np.array([[1,2,3],[4,5,6],[7,8]]) #the last entry has only 2 entries
print(x[1][1])
print(x.ndim)
print(x.size) #total number of elements
print(x.shape) #(gives back a tuple!)
x_shape_test=np.array([[[11],[12],[13]],[[21],[22],[23]]])
print(x_shape_test)
print(x_shape_test.shape)


#functions for arrays --> Different as for lists as of syntax
x=np.array([2,1,3]) # not x.append(2) as for lists!
x=np.append(x,2)
x=np.delete(x,0) #delete at index=0
x=np.sort(x)
print(x.sum())
print(x.min())
print(np.mean(x)) #builtin functions for statistics (also median, var and std)
#create range
x2=np.arange(2,10,3)

y=x*2
print(type(y))

x_com=np.array([[11,21],[12,22]])
test=np.append(x_com,[[13,23]]) #does not work when the array has more dims!

#reshape
x=np.arange(1,7)
# do more structure
z=x.reshape(3,2) #3 lines, 2 columns
print(z)
#less structure
x=np.array([[1,2],[3,4], [5,6]])
z=x.reshape(x.size)  
#also: flatten
z2=x.flatten()

#INDEXING
x=np.arange(1,10)
print(x[0:2])
print(x[3:])
print(x[-3:]) #backwards

#Conditions
x=np.arange(1,10)

print(x[  (x<4) & (x%2==0)  ]) #dont forget  the () brackets around each condition
y=(x<4) & (x%2==0) #builds an boolean array


data=np.array([12,20,30])
stab=np.std(data)
avg=np.mean(data)
out=data[abs(data-avg)<abs(stab)]

######################
#PANDAS
####################

import pandas as pd
#SERIES (essentially a column [like 1 dim array]) and DATAFRAMES (mult-dimensional table made up of a collection of series [like multi-dim array])

#easiest way to create Dataframe: create dict
data={'ages':[14,18,30],'heights':[143,180,160]}
df=pd.DataFrame(data) #watch out for capital letters
total_rows=df.count
#Number of rows /#length /#size
len(df)
df.shape
#we can also specify a custom index  --> name the rows
df=pd.DataFrame(data, index=['Daeny', 'Jaime', 'Sina'])
print(df.loc['Sina'])  ##watch out:loc uses square brackets!
print(df["ages"]) #--> result is a series object
print(df.ages)  # alternative
print(df[["ages", "heights"]]) #useful when you want to select only some parts of an object


#Slicing 
print(df.iloc[2]) #select data based on its numeric index --> 3rd row
print(df.iloc[:2])

###########################
#filtering rows
df[df['ages']>18]
df[df.ages>18] #alternative
df.ages>18 #gives back boolean per row

#########################
#column wise operations
data={'num1':[14,181,30],'num2':[143,180,160]}
df=pd.DataFrame(data)
#min between different columns
df['mini']=df[['num1', 'num2']].min(axis=1)

#create column with length of any field in column 
df['len_col']=df['num1'].apply(len)

#sort dataframe
df.sort_values(by=['len_col'], ascending=False)


#change type to int/string
df['num1']=df.num1.astype('str')  #or int/...


df[pd.isnull(df['ages'])]  #filteruing for rows where the column "ages" is NULL / NaN

#READING CSVs -> can directly read into a DataFrame
import os
os.getcwd()
#os.chdir(r"C:\Users\sina_\Documents")
#os.chdir(r"C:\Users\sina_\Documents\-Kopie auf Festplatte\python")
os.chdir(r"C:\Users\sina_\Documents\git_repo\Sinas-Repo")
os.chdir(r"C:\Users\sina.herbst\Documents\git_repos\Sinas-Repo")
df=pd.read_csv("csv_test.csv", sep=';')
print(df.head())
df.info()
df.describe()
df['number'].describe()


df.set_index("year", inplace=True) ##set the year as index now so the first row is deleted

#Adjustments Changes
#Dropping  /deleting 
df.drop('number2', axis=1, inplace=True)  #axis=1--> drop column, inplace=true serves that it is realy deletd, otherwise it is printed a new list without number2
df.drop(2021, axis=0, inplace=True)  #-_> axis=0--> drop row

#Adding / Creating
df['number_new']=df['number']+2

#grouping #group by #sum 
df['number'].value_counts()   #does not make much sense but serves as example
df['year'].value_counts()   #does not work as this is the key!
df.groupby('number')['number2'].sum() #select number, sum(number2) group by number  #also for min, max, mean



#####################################################
#3) applying functions on dataframes
##################################################
data={'strings':['abc-def','34nfa-21','a'],'numbers':[143,180,160]}
df=pd.DataFrame(data) 
#find "-" symbol in strings
df['indices']=df.strings.str.find('-')
#now we want to cut until the "-" if there is one!

# Use Apply with lambda function to make definition with multiple columns
df['extract']=df.apply(lambda x: x['strings'][:x['indices']], axis=1)  ##does work but for the last row the result is different!

#as this is not the total result, we define
def extr(part, end):
    if end==-1:
        out=part
    else :
        out=part[:end]
    return out

#using both lambda and a defined function on a dataset
df['extract_correct']=df.apply(lambda x: extr(x['strings'], x['indices']), axis=1)

    
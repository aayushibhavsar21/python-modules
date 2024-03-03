import pandas as pd

#_________ read csv file _________

df = pd.read_csv("A:\python\panda module.py\stock_data.csv" , skiprows=1)  # to skip one row 
print(df)

df = pd.read_csv("A:\python\panda module.py\stock_data.csv" , header=1)  # 1st line is your header (start count of line from 0) 
print(df)

# if you do not have any header , give your header name using this syntax :
# df = pd.read_csv("A:\python\panda module.py\stock_data.csv", header=None, names = ["ticker","eps","revenue","people"])

df = pd.read_csv("A:\python\panda module.py\stock_data.csv" , nrows=2)  # 1st line is your header (start count of line from 0) 
print(df)

df = pd.read_csv("A:\python\panda module.py\stock_data.csv", na_values=["n.a.", "not available"])
print(df)

# if we want to change any perticular value of column to NaN:
df = pd.read_csv("A:\python\panda module.py\stock_data.csv",  na_values={
        'eps': ['not available'],
        'revenue': [-1],
        'people': ['not available','n.a.']
    })
print(df)

print(df.sample(frac=0.5))  # to print random 50% of our dataset   # output of 50% of our dataframe will be different every time
print(df.sample(frac=0.5,random_state=100))  # output of 50% of our dataframe will be same every time

def convert_people_cell(cell):
    if cell=="n.a.":
        return 'Sam Walton'
    return cell

def convert_price_cell(cell):
    if cell=="n.a.":
        return 50
    return cell
    
df = pd.read_csv("A:\python\panda module.py\stock_data.csv", converters= {
        'people': convert_people_cell,
        'price': convert_price_cell
    })
print(df)



#_________ write in csv file_________

df = pd.read_csv("A:\python\panda module.py\stock_data.csv")

df.to_csv("new.csv") # to make copy of any file 
df.to_csv("new.csv", index=False) # to copy without index (0 1 2 3..)
df.to_csv("new.csv", columns=["tickers","price"], index=False) # to copy any perticular columns
# check changes that made by above syntax in excel  

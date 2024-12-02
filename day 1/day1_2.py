import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('input1', sep=r'\s+', header=None, names=['Col1', 'Col2'])

# Create the lists from the DataFrame columns
list1 = df['Col1'].tolist()
list2 = df['Col2'].tolist()

print("DataFrame:")
print(df)
print("\nlist1 =", list1)
print("list2 =", list2)

referenceColumn = df[['Col2']].value_counts()
# print(referenceColumn)
# print(referenceColumn[3])


similarity = 0
for number in list1:
    try:
        referenceNum = referenceColumn[number]
        # print(referenceNum)
    except KeyError:
        referenceNum = 0

    similarity += number * referenceNum

print(similarity)

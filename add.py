import data

filename = input("Please enter the file name: ")

if filename:
    data.insert_data(filename)
    print("file name added successfully!")
else:
    print("You didn't enter anything!") 

import os

# Opening a file
#f = open("demo.txt","r")
    # Pass rb if reading binary file
    # Pass rt to specifically mention that you are using this open a textfile
    # Pass a to append the data to file

# Reading a file 
#f.read()

# Reading the file one at a time
#f.readline()

# Writing a file 
#f.write("Hello")

# Closing a file 
#f.close()


# Using with clause
with open("demo.text","r") as f:
    f.read()
    
    
    
# Removing a file 
os.remove("demo.text")
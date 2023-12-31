import pandas as pd
import os
file_name = "mailcrawl\spiders\output.csv"
file_name_output = "mailcrawl\spiders\output1.csv"

df = pd.read_csv(file_name, sep="\t or ,")

# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  
df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
df.to_csv(file_name_output, index=False)

os.remove("mailcrawl\spiders\output.csv")
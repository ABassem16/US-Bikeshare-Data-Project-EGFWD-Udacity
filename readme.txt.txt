https://www.geeksforgeeks.org/
https://pandas.pydata.org/docs/reference/
Udacity Course Videos

Side Notes:
I noticed that in washington.csv there was neither birth date nor gender in columns
so i added an if condition to check whether this column is available to prevent an error
from occurring.
Also the data i downloaded had dates only till 30/6 so i added a condition to check
whether the dataframe is empty or not to prevent erros such as KeyErrors
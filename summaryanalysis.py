#-------------------------------------------------------------------------------------------

# Higher Diploma in Science in Computing - Data Analytics

#-------------------------------------------------------------------------------------------

# Project Fisher's Iris Data Set

# This project was created as part of the Data Analysis module for the Higher Diploma in Data Science 
# at ATU University. 
# The project utilizes the Iris dataset to showcase various data analysis and visualization techniques 
# learned throughout the course.

#-------------------------------------------------------------------------------------------
# Author: Carlos Rigueti
#-------------------------------------------------------------------------------------------

# LIBRARIES

#-------------------------------------------------------------------------------------------
 
# Data frames.
import pandas as pd

#-------------------------------------------------------------------------------------------

# LOAD DATA

#-------------------------------------------------------------------------------------------

#---------------------------
# Load the Iris data set.
#---------------------------
  
df = pd.read_csv("iris.csv")
print (df)

#-------------------------------------------------------------------------------------------

# SUMMARY ANALYSIS

#-------------------------------------------------------------------------------------------


# Creating and opening a new text file for summary.
with open("iris_summary.txt", "wt") as file:  

    # Writing the introduction.
    file.write("Higher Diploma in Science in Computing - Data Analytics\n\n")
    file.write("Project Fisher's Iris Data Set\n")
    file.write("The project revolves around accessing and analyzing the Iris dataset, a classic dataset frequently used in the field of\n")
    file.write("data science and machinelearning. By working with this dataset, we aim to demonstrate a range of skills, including data.\n")
    file.write("manipulation, statistical analysis, visualization, and programming techniques using Python within the Jupyter Notebook\n")
    file.write("environment.The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald.\n")
    file.write("Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems'. It is sometimes called Anderson's Iris data\n")
    file.write("set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.\n\n")
    
    # Author.
    file.write("Author: Carlos Rigueti\n\n\n")

    # Writing the Load Data.

    file.write("DATA LOAD:\n\n\n")

    file.write("Load the Iris dataset into a DataFrame.\n\n")
    file.write("df = pd.read_csv('iris.csv')\n")
    file.write("print (df)\n\n")
    file.write(str(df) + "\n\n\n")

    # Writing the Inspect Data.

    file.write("INSPECT DATA:\n\n\n")

    file.write("The first 5 rows of the dataset.\n\n")
    file.write("5rows = df.head()\n")
    file.write("print (5rows)\n\n")
    file.write(str(df.head ()) + "\n\n")

    file.write("The last 5 rows of the dataset.\n\n")
    file.write("last5rows = df.tail()\n")
    file.write("print (lastrows)\n\n")
    file.write(str(df.tail ()) + "\n\n")

    file.write("Informations of the dataset.\n\n")
    file.write("info = df.info ()\n")
    file.write("print (info)\n\n")
    file.write(str(df.info(buf=file)) + "\n\n") #[2]

    file.write("Count the number of null.\n\n")
    file.write("isnull = df.isnull().sum()\n")
    file.write("print (isnull)\n\n")
    file.write(str(df.isnull().sum()) + "\n\n")

    file.write("Describe the data set.\n\n")
    file.write("describe = df.describe()\n")
    file.write("print (describe)\n\n")
    file.write(str(df.describe()) + "\n\n")  
    
    file.write("Compute the Pearson correlation.\n\n")
    file.write("correlation = df.corr(method='pearson', numeric_only=True)\n")
    file.write("print (correlation)\n\n")
    file.write(str(df.corr(method='pearson', numeric_only=True)) + "\n\n")   
    
    file.write("Extract the data from the \"species\" column.\n\n")
    file.write("df.value_counts(['species'])\n")
    file.write("print (species)\n\n")
    file.write(str(df.value_counts('species')) + "\n\n")
    
    file.write("Check the size of your DataFrame.\n\n")
    file.write("df.shape\n")
    file.write(str(df.shape) + "\n\n")

    
    file.write("Describe the data set by Species.\n\n")
    file.write("describe_species = df.groupby('species').describe().transpose()\n")
    file.write("print (describe_species)\n\n")
    file.write(str(df.groupby('species').describe().transpose()) + "\n\n")
    
    # Writing Visualization Data.

    file.write("VISUALIZATION DATA\n\n\n")

    file.write("Bar Chart.\n\n")
    file.write("Fig. 1 - Bar Chart\n\n")

    file.write("Histogram of Iris Flowers.\n\n")
    file.write("Fig. 2 - Histogram\n\n")

    file.write("Histogram of Iris Flowers by Species.\n\n")
    file.write("Fig. 3 - Histogram by Species\n\n")

    file.write("Boxplot of Iris Flowers by Species.\n\n")
    file.write("Fig. 4 - Boxplot\n\n")

    file.write("Correlation Heatmap of the data set.\n\n")
    file.write("Fig. 5 - Heatmap\n\n")

    file.write("Correlation Heatmap of the data set by Species.\n\n")
    file.write("Fig. 6 - Heatmap by Species\n\n")

    file.write("Scatter plot of Iris Flowers by Species.\n\n")
    file.write("Fig. 7 - Scatter plot by Species\n\n")

    file.write("Pair plot of Iris Flowers by Species.\n\n")
    file.write("Fig. 8 - Pair plot by Species \n\n\n")

    # Writing End.

    file.write("End\n")
    file.write("last commit on 20/05/2024.\n\n")
    
   
#-------------------------------------------------------------------------------------------

# REFERENCES

#-------------------------------------------------------------------------------------------

# Reading and Writing to text files in Python. https://www.geeksforgeeks.org/reading-writing-text-files-python/ . [Accessed 14 May 2024].

#-------------------------------------------------------------------------------------------

# Last commit on 20/05/2024.

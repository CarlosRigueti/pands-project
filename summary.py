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


# Create and open a new text file for summary
with open("summary_iris.txt", "w") as file:
    # Write the introduction
    file.write("Higher Diploma in Science in Computing - Data Analytics\n")
    file.write("Author: Carlos Rigueti\n")
    file.write("Programming and Scripting - Iris\n")
    file.write("The project revolves around accessing and analyzing the Iris dataset, a classic dataset frequently used in the field of data science and machine learning. By working with this dataset, we aim to demonstrate a range of skills, including data manipulation, statistical analysis, visualization, and programming techniques using Python within the Jupyter Notebook environment.\n")
    file.write("The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems'. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.\n\n")
    file.write("About this project:\n")
    file.write("It is Iris dataset.\n\n")
    file.write("About Iris.\n\n")
    file.write("Fig. 1 - Iris\n\n")
    file.write("Iris\n")
    file.write("Fischer's Iris Data UCI Machine Learning Repository: Iris Data Set.\n")
    file.write("[2]\n\n")
    file.write("Imports:\n")
    file.write("This project required some libraries to be imported to load, analyze and visualize the data, such as:\n")
    file.write("- Pandas: is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool;\n")
    file.write("- Numpy: is a library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices;\n")
    file.write("- Matplotlib: is a comprehensive library for creating static, animated, and interactive visualizations;\n")
    file.write("- Seaborn: is a data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.\n\n")
    
    # Write the data load section
    file.write("# Data Load:\n")
    file.write("The dataset imported from Palmer Penguins and saved into a file .csv, named as penguins.csv in the repository. The .csv file is using the library pandas as df = pd.read_csv [3]\n\n")
    file.write("# Load the dataset into a DataFrame\n")
    file.write("df = pd.read_csv('iris.csv')\n")
    file.write("print (df)\n")
    file.write(str(df.info (buf=file)) + "\n\n")
    
    # Write the inspect data section
    file.write("# Inspect Data:\n")
    file.write("The inspect data process involves examining and understanding the structure, content, and characteristics of a dataset. It provides users with valuable insights to comprehend the dataset and make informed decisions about data preprocessing, analysis, and modeling. Here's what inspect data typically provides for users to understand the dataset:\n\n")
    file.write("# The first 5 rows of the dataset.\n")
    file.write("df.head ()\n")
    file.write(str(df.head()) + "\n\n")
    file.write("# The last 5 rows of the dataset.\n")
    file.write("df.tail ()\n")
    file.write(str(df.tail()) + "\n\n")
    file.write("# Informations of the dataset.\n")
    file.write("df.info ()\n")
    file.write(str(df.info()) + "\n\n")
    file.write("# Count the number of null.\n")
    file.write("df.isnull ().sum ()\n")
    file.write(str(df.isnull().sum()) + "\n\n")
    file.write("# Descibe the data set.\n")
    file.write("df.describe ()\n")
    file.write(str(df.describe()) + "\n\n")
    file.write("# Compute the Pearson correlation.\n")
    file.write("df.corr(method='pearson', numeric_only=True)\n")
    file.write(str(df.corr(method='pearson', numeric_only=True)) + "\n\n")
    file.write("# Extract the data from the \"species\" column.\n")
    file.write("df.value_counts(['species'])\n")
    file.write(str(df.value_counts(['species'])) + "\n\n")
    file.write("# Check the size of your DataFrame.\n")
    file.write("df.shape\n")
    file.write(str(df.shape) + "\n\n")
    
    # Write the summary statistics section
    file.write("# Summary statistics for numerical variables\n")
    file.write("summary_stats = df.describe()\n")
    file.write(str(df.describe()) + "\n\n")
    file.write("summary_stats = df.head ()\n")
    file.write(str(df.head()) + "\n\n")
    file.write("summary_stats = df.isnull ().sum ()\n")
    file.write(str(df.isnull().sum()) + "\n\n")
    file.write("summary_stats = df.tail ()\n")
    file.write(str(df.tail()) + "\n\n")
    file.write("summary_stats = df.corr(method='pearson', numeric_only=True)\n")
    file.write(str(df.corr(method='pearson', numeric_only=True)) + "\n\n")
    file.write("summary_stats = df.value_counts(['species'])\n")
    file.write(str(df.value_counts(['species'])) + "\n\n")
    file.write("summary_stats = df.shape\n")
    file.write(str(df.shape) + "\n\n")
    
    
    # Writing Data Visualization.

    file.write("DATA VISUALIZATION\n\n\n")

    file.write("plt.bar.\n\n")
    file.write("Fig. 2 - Number of Iris Flowers by Species\n\n")

    file.write("plt.figure.\n\n")
    file.write("Fig. 3 - Relationship between Sepal Length and Width\n\n")

    file.write("sns.load_dataset.\n\n")
    file.write("Fig. 4 - Scatterplot of Sepal Length vs Sepal Width by Species\n\n")

    file.write("Figure of each Histogram.\n\n")
    file.write("Fig. 5, 6, 7, 8 - Histogram\n\n")

    file.write("plt.plot.\n\n")
    file.write("Fig. 9 - Iris Dataset\n\n")

    file.write("plt.subplots.\n\n")
    file.write("Fig. 10 - Iris Dataset\n\n")

    file.write("Boxplot of Iris Dataset Features by Species.\n\n")
    file.write("Fig. 11 - Boxplot of Iris Datase\n\n")

    file.write("Correlation Heatmap by Species.\n\n")
    file.write("Fig. 12 - Heatmap by Species \n\n\n")
    
    file.write("sns.pairplot.\n\n")
    file.write("Fig. 13 - pairplot \n\n\n")

    # Writing End.

    file.write("End\n")
    file.write("last commit on 20/05/2024.\n\n")
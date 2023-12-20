# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_main.py'.

# Import Streamlit and other required modules
import numpy as np
import pandas as pd
import streamlit as st
import census_home as ch
import census_plots as cp


@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above.

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

# Function to display selected page based on user choice
def display_page(page):
    if page == "Home":
        ch.show_home_page(census_df)
    elif page == "Visualise Data":
        cp.show_visualize_page(census_df)

# Adding a navigation in the sidebar using radio buttons
def main():

	st.sidebar.title("Navigation")
	page_selection = st.sidebar.radio("Go to", ("Home", "Visualise Data"))

    # Call the respective pages based on user selection
	display_page(page_selection)

if __name__ == "__main__":
    main()
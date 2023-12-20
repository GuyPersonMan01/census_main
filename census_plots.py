import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_visualize_page(census_df):
    st.title('Visualize Data')

    # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
    plot_list = st.sidebar.multiselect("Select the Charts/Plots:", ['Count Plot', 'Pie Plot', 'Box Plot'])

    # Display plots based on user selection
    if 'Count Plot' in plot_list:
        st.subheader('Count Plot')
        sns.set_theme()
        count_plot = sns.countplot(x='gender', data=census_df)
        st.pyplot(count_plot.figure)

    if 'Pie Plot' in plot_list:
        st.subheader('Pie Plot')
        gender_count = census_df['gender'].value_counts()
        plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
        st.pyplot()

    if 'Box Plot' in plot_list:
        st.subheader('Box Plot')
        box_plot = sns.boxplot(x='education', y='age', data=census_df)
        st.pyplot(box_plot.figure)
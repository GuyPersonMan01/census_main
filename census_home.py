import streamlit as st

def show_home_page(df):
    st.title('Census Data Analysis')
    # Display dataset within beta_expander
    with st.expander("View Dataset"):
        st.write(df)  # Show complete dataset

    # Show dataset summary on click of a checkbox
    show_summary = st.checkbox("Show Dataset Summary")

    if show_summary:
        st.write("Dataset Summary:")
        st.write(df.describe())  # Show dataset summary
import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st

def first_page():
    # Set the title of the app
    st.title("Task Mini Project:")

    # Display a button to navigate to the second page
    if st.button("Go to Second Page"):
        st.session_state.page = "Second Page"

    # Display content for the first page
    st.text("Welcome to the first page!")

def second_page():
    # Set the title of the second page
    st.title("Second Page")

    # Display a button to navigate back to the first page
    if st.button("Go to First Page"):
        st.session_state.page = "Home"

    # Display content for the second page
    st.text("This is the second page!")

def main():
    # Set the title of the app
    st.title("Mini Project Kalla")

    # Define the pages using a dictionary
    pages = {"Home": first_page, "Second Page": second_page}

    # Add a sidebar to select the page
    selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))

    # Run the selected page function
    pages[selected_page]()

if __name__ == "__main__":
    main()

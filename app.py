from forms.downloadReport import downloadReport
from pages.home import home_page
import streamlit as st
from server.navigation import display_page
from forms.createJob import createJob
from forms.ingestResumes import ingestResumes

# This function will handle page navigation
def main():
    page = st.sidebar.radio("Select Page", ["Home", "Create Job", "Ingest Resumes", "Download Report", "Settings"])
    
    if page == "Home":
        home_page()
    elif page == "Create Job":
        createJob()
    elif page == "Ingest Resumes":
        ingestResumes()
    elif page == "Download Report":
        downloadReport()
    elif page == "Settings":
        st.title("Settings Page")

if __name__ == "__main__":
    main()

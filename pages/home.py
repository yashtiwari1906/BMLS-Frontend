import streamlit as st

def home_page():
    # Title
    st.title("Donna's Resume Scanning")

    # First Paragraph - related to resume scanning
    st.subheader("Welcome to Donna's Resume Scanning")
    st.markdown("""
    Resume scanning has never been easier! Donna’s Resume Scanning tool is designed to help you assess resumes efficiently and effectively.
    By using cutting-edge AI and machine learning algorithms, Donna ensures that each resume is analyzed with the highest level of accuracy.
    Whether you are a recruiter or a job seeker, this tool streamlines the process, making it faster and more reliable than ever before.
    """)
    # Random Image
    st.image("https://via.placeholder.com/500x300?text=Resume+Scanning+Image+1", caption="AI-Powered Resume Analysis")

    # Second Paragraph - About the Create Jobnd navigation
    st.markdown("""
    To get started, simply use the Ingest Resumeselow to fill out details about the job you're hiring for. 
    Once you’ve provided the job details, you can upload resumes through other forms. 
    After processing, you can navigate to another page where you'll be able to download your personalized report.
    This process is streamlined to help you find the right candidate without any hassle.
    """)
    # Random Image
    st.image("https://via.placeholder.com/500x300?text=Job+Form+Image", caption="Form for Job Details")

    # Third Paragraph - About the creators and why it was built
    st.markdown("""
    This tool was built with the goal of making the recruitment process more efficient, saving time and effort for HR professionals, recruiters, and hiring managers. 
    The idea was born from the need to process and analyze resumes quickly and accurately, without compromising on quality. We believe that technology can 
    bridge the gap between employers and job seekers, making it easier to match the right people to the right opportunities.

    **Built by:** Yash Tiwari and Arnab Samanta
    """)
    # Random Image
    st.image("https://via.placeholder.com/500x300?text=Team+Image", caption="The Team Behind Donna's Resume Scanning")


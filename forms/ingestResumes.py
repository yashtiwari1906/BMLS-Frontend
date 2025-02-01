import logging
import streamlit as st
import requests


# def ingestResumes():
#     st.header("Create Job")

#     # Example form inputs
#     name = st.text_input("Name")
#     email = st.text_input("Email")
    
#     if st.button("Submit"):
#         st.write(f"Name: {name}, Email: {email}")


import streamlit as st
import io

from constants import CLOUD_RUN_URL

def ingestResumesWithBMLS(hr_email, resumes):

    url = f"{CLOUD_RUN_URL}/api/external-communications/ingest-resumes/?email={hr_email}"

    payload = {}
    files = []
    for idx, pdf_file in enumerate(resumes):
        # Add each file to the "files" dictionary, using a unique name for each file
        files.append(("file[]", (pdf_file.name, pdf_file, "application/pdf")))

    headers = {
    "Content-Type": "application/pdf"
    }
    
    # Perform the POST request
    with requests.Session() as session:
        try:
            response = session.post(url, data=payload, files=files)
            return response

        except Exception as e:
            print(f"Error occurred: {e}")

        # Ensure files are closed after the request is sent
        finally:
            # Close the opened files to avoid resource leakage
            for _, file_tuple in files:
                file_tuple[1].close()

    return None 
    
    

def ingestResumes():
    """Creates the form to upload PDF files and enter parameters."""
    st.header("Upload Your Resume and Fill Job Parameters")

    # Job Parameters
    hr_email = st.text_input("HR Email", "email used to register the job")

    # PDF Upload
    uploaded_pdf = st.file_uploader("Upload Resume PDF", type=["pdf"], accept_multiple_files=True)
    # logging.error(f"type uploaded_pdf {type(uploaded_pdf)}")
    # logging.error(f"uploaded_pdf : {uploaded_pdf}")

    if uploaded_pdf is not None:
       

        # Button to submit the form (you could add further logic here, e.g., saving the data or processing it)
        if st.button("Submit"):
            response = ingestResumesWithBMLS(hr_email, uploaded_pdf)

            if response == None:
                logging.info(f"some error occured while uploading the resumes to BMLS for hr_email: {hr_email}") 
                st.write("resume ingestion failed sorry we will reach shortly or if you can you can write us at yashtiwari1906@gmail.com")
                return

            if response.status_code == 400:
                logging.info(f"some error happened but problem was at the user side for hr_email: {hr_email}")
                response_dict = response.json()
                st.write(f"we faced some problem in processing your request read this message if you can do something: {response_dict["error"]}") 
                return

            if response.status_code == 500:
                logging.info(f"some internal error occured for the hr_email: {hr_email}")
                st.write(f"Sorry for the incovenience but some error had occured we will shortly look into it if possible mail us at yashtiwari1906@gmail.com") 
                return 
            
            response_dict = response.json()
            data = response_dict["data"]
            non_readable_pdf_files = data["nonReadablePDFFileNames"]
            if len(non_readable_pdf_files) == 0:
                st.success("resumes ingested successfully!")
            else:
                st.write(f"some resumes were not machine readable they are {non_readable_pdf_files}")
                st.success("other resumes are ingested successfully!")
            # Here, you can add logic to handle the form submission, like saving the data to a database or further processing


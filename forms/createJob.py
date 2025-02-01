import logging
import streamlit as st
import requests
import json

from constants import CLOUD_RUN_URL, LOCAL_URL


def createJobWithBMLS(hr_name, hr_email, job_title, department, job_desc):
    

    url = f"{CLOUD_RUN_URL}/api/external-communications/create-job-posting/?replace=False"

    payload = json.dumps({
    "personalInfo": {
        "name": hr_name,
        "email": hr_email
    },
    "jobDetailsInfo": {
        "jobTitle": job_title,
        "Department": department,
        "jobDescription": job_desc
    }

  
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def createJob():
    st.header("Create Job")

    # Example form inputs
    hr_name = st.text_input("HR Name")
    hr_email = st.text_input("HR email")
    job_title = st.text_input("Job Title")
    department = st.text_input("Department")
    job_desc = st.text_input("Job Description")

    
    
    
    if st.button("Submit"):
        response = createJobWithBMLS(hr_name, hr_email, job_title, department, job_desc)
        if response.status_code == 200:
            logging.info(f"response from the createJob API hit for the hr_email: {hr_email}")
            st.write(f"Thanks for submitting we are creating your job right now, Name: {hr_name}, Email: {hr_email}")
        elif response.status_code == 400:
            logging.info(f"some error happened but problem was at the user side for hr_email: {hr_email}")
            response_dict = response.json()
            st.write(f"we faced some problem in processing your request read this message if you can do something: {response_dict["error"]}")
        else:
            logging.info(f"some internal error occured for the hr_email: {hr_email}")

import logging
import streamlit as st
import requests
import json

from constants import CLOUD_RUN_URL


def createJobWithBMLS(hr_name, hr_email, job_title, department, company_info, department_info, job_desc):
    

    url = f"{CLOUD_RUN_URL}/api/external-communications/create-job-posting/?replace=False"

    payload = json.dumps({
    "personalInfo": {
        "name": hr_name,
        "email": hr_email
    },
    "jobDetailsInfo": {
        "jobTitle": job_title,
        "Department": department,
        "companyInfo": company_info,
        "DepartmentInfo": department_info,
        "jobDescription": job_desc
    },

    # TODO: will remove after removing it from backend 
    "bucketInformation": {
        "buckets": [
        {
            "bucket_name": "bucket1",
            "bucket_description": [
            "should've worked on ASR with the SOTA apporaches and fine tuned that model with PEFT or simple finetuning",
            "should have experience in deploying these heavy speech models in to the production in to the distributed manner",
            "should have experience in distributed training of the model like FSDT",
            "should be working as a Research Engineer or Research Scientist in a AI focused organization"
            ]
        },
        {
            "bucket_name": "bucket2",
            "bucket_description": [
            "should be working on at least some form of deep learning related field like NLP, Computer Vision, etc",
            "should have worked on deployment of heavy machine learning models",
            "should have worked on data science projects involving in post analysis of models ",
            "should have experience in the hypothesis testing "
            ]
        }
        ]
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
    company_info = st.text_input("Company Information")
    department_info = st.text_input("Department Information")
    job_desc = st.text_input("Job Description")

    
    
    
    if st.button("Submit"):
        response = createJobWithBMLS(hr_name, hr_email, job_title, department, company_info, department_info, job_desc)
        if response.status_code == 200:
            logging.info(f"response from the createJob API hit for the hr_email: {hr_email}")
            st.write(f"Thanks for submitting we are creating your job right now, Name: {hr_name}, Email: {hr_email}")
        elif response.status_code == 400:
            logging.info(f"some error happened but problem was at the user side for hr_email: {hr_email}")
            response_dict = response.json()
            st.write(f"we faced some problem in processing your request read this message if you can do something: {response_dict["error"]}")
        else:
            logging.info(f"some internal error occured for the hr_email: {hr_email}")

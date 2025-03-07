import logging
import streamlit as st
import requests
import json

from constants import CLOUD_RUN_URL


def downloadReportFromBMLS(hr_email):
    

    url = f"{CLOUD_RUN_URL}/api/external-communications/fetch-report/?email={hr_email}"

    payload = {}
    headers = {
    'Content-Type': 'text/csv'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def downloadReport():
    st.header("Create Job")

    # Example form inputs
    hr_email = st.text_input("HR email")
    
    if st.button("Submit"):
        response = downloadReportFromBMLS(hr_email=hr_email)
        
        if response.status_code == 400:
            logging.info(f"some error happened but problem was at the user side for hr_email: {hr_email}")
            response_dict = response.json()
            st.write(f"we faced some problem in processing your request read this message if you can do something: {response_dict["error"]}")

        elif response.status_code == 500:
            logging.info(f"some internal error occured for the hr_email: {hr_email}")
            st.write(f"Sorry for the incovenience but some error had occured we will shortly look into it if possible mail us at yashtiwari1906@gmail.com")

        else:
            logging.info(f"response from the downloadReportFromBMLS API hit for the hr_email: {hr_email} was success")
            report = response.content 

            if report:
                st.success("Report fetched successfully!")

                # Provide the download button
                st.download_button(
                    label="Download Report",
                    data=report,
                    file_name=f"report_{hr_email}.csv",  # Adjust file type based on your report format
                    mime="text/csv"  # Adjust MIME type based on your report format (e.g., 'text/csv' for CSV)
                )

            logging.info(f"response from the createJob API hit for the hr_email: {hr_email}")
            st.write(f"Thanks for using the service!!!")

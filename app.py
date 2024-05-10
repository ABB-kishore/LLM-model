# Import the necessary libraries
import os
from docx import Document as DocxDocument
import arch
from prompts import dictionary
import table
import rag
import streamlit as st
import PyPDF2

# Function to fill the invitation document with data
def fill_invitation(template_path, output_path, data):
    doc = DocxDocument(template_path)
    for paragraph in doc.paragraphs:
        custom_font_name = "ABBvoice"
        paragraph.style.font.name = custom_font_name
        for key,value in data.items():
            if key in paragraph.text:
                for run in paragraph.runs:
                    run.text =  run.text.replace(key, value)
    doc.save(output_path)
 
# Set the title of the Streamlit app
st.title("Budgetary Bid Assistant")

# Allow the user to upload a RFQ file
uploaded_files = st.file_uploader("Upload a RFQ file", type="pdf", accept_multiple_files=True, )

pdf_path = "uploaded.pdf"

file2 = st.file_uploader("upload the architecture file", type="pdf",key="arch")
if file2:
    with open("arch.pdf", "wb") as output_file:
        output_file.write(file2.getvalue())

# If a file is uploaded, process it
if uploaded_files and file2:
    if st.button("Process the document"):
        try:
            # Save the uploaded file
            pdf_merger = PyPDF2.PdfMerger()

            for pdf_file in uploaded_files:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                pdf_merger.append(pdf_reader)
            
            with open(pdf_path, "wb") as output_file:
                pdf_merger.write(output_file)
            
            # Process the uploaded file using rag
            with st.spinner("Extracting the text..."):
                try:
                    rag.file_processing(pdf_path)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    print(e)
            # Extract the architecture using arch
            with st.spinner("Extracting the architecture..."):
                try:
                    arch.architec()
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    print(e)
            # Fill the table using table
            with st.spinner("Adding tables..."):
                try:
                    table.io_fill_table(dictionary["Table1"])
                    table.bom_fill_table(dictionary["bom"])

                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    print(e)

            # Process the document using rag and fill it with responses
            with st.spinner("Processing the document..."):
                responses = {
                    '[servers]': rag.results(dictionary["serve"]),
                    '[non-redundant]': rag.results(dictionary["nonred"]),
                    '[spare]': rag.results(dictionary["Spare"]),
                    '[space]': rag.results(dictionary["space"]),
                    '[safe]': rag.results(dictionary["safe"]),
                    '[Non]': rag.results(dictionary["Non"]),
                    '[HART]': rag.results(dictionary["HART"]),
                    '[SIL]': rag.results(dictionary["SIL"]),
                    '[re]': rag.results(dictionary["Redun"]),
                    '[redundant]': rag.results(dictionary["Red"]),
                    '[Third]': rag.results(dictionary["Third"]),
                    '[controllers]': rag.results(dictionary["controllers"]),
                    '[system]': rag.results(dictionary["System"]),
                    '[Scope]': rag.results(dictionary["scope"]),
                    '[graphics]': rag.results(dictionary["Graphics"]),
                    '[hist]': rag.results(dictionary["histo"]),
                    '[simp]': rag.results(dictionary["Repo1"]),
                    '[comp]': rag.results(dictionary["Repo2"]),
                    '[location]': rag.results(dictionary["location"])
                    
                }
    
            # If a template file is uploaded, fill it with the data
            template_file = "tabinput.docx"
            if template_file is not None:
                with st.spinner("Filling the document..."):
                    # Create a temporary file to store the output document
                    temp_file = "output.docx"
                    fill_invitation(template_file, temp_file, responses)
                st.download_button("Download the filled document", file_name="output.docx", data=open(temp_file, "rb").read())
                st.write("The document has been filled successfully.")
            os.remove(temp_file)
            os.remove(pdf_path)
            os.remove("iminput.docx")
            os.remove("tabinput.docx")
            os.remove("iooutput.docx")
            os.remove("arch.pdf")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            print(e)


import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")
from PIL import Image

# Set the title of the app
st.title("Displaying an Image in Streamlit")

# Add a section for picture
st.header("Image")
upload_file = st.file_uploader("Upload an image", type=["jpeg", "jpg", "png"])

if upload_file:
   image = Image.open(upload_file)
   col1, col2, col3 = st.columns([1, 1, 2])
   with col3:
       st.image(image.resize((150, 150)), caption="Uploaded Image")
       
# Collect basic information
name = "Dr. ONAOLAPO Sunday Akintunde"
field = "Computational Chemistry"
institution = "University of Kwazulu-natal, South Africa"
summary = """As a computational chemist, my research focuses on designing and optimizing novel drugs and vaccines using computational methods. I develop and apply molecular modeling, simulation, and machine learning techniques to understand the behavior of biomolecules and their interactions with small molecules. My goal is to accelerate the discovery of effective treatments for infectious diseases, cancer, and neurological disorders.

My expertise spans molecular mechanics and dynamics simulations, quantum mechanics calculations, and machine learning algorithms. I utilize high-performance computing resources to perform large-scale simulations and virtual screening. By combining computational insights with experimental validation, I aim to identify novel drug and vaccine candidates that can be further developed and tested."""
qualification = """BSc Chemistry, MSc Chemistry (Physical/Inorganic), PhD Chemistry (computational)"""

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Summary:** {summary}")
st.write(f"**Qualification:** {qualification}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "js4heaven@gmail.com"
st.write(f"You can reach {name} at {email}.")


import streamlit as st
from subprocess import check_output


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.write("Diet Recommendation System Done by Sidharth Shanu and Anubhav Tandon ")

st.sidebar.success("Select a recommendation app.")

url = "https://nap.nationalacademies.org/catalog/10490/dietary-reference-intakes-for-energy-carbohydrate-fiber-fat-fatty-acids-cholesterol-protein-and-amino-acids"
st.markdown("Reference to [Dietary Reference Intakes Book](%s)" % url)

url_1 = "https://www.gov.uk/government/publications/sacn-dietary-reference-values-for-energy"
st.markdown("Reference to [Sacn-Dietary-Reference-Values-for-energy report](%s)" % url_1)

if st.button('First HTML Page'):
    file_path = f"Streamlit_Frontend\index.html"
    check_output(f"start {file_path}", shell=True)


st.markdown(
    """
    The Project is based on the Scientific Advisory Committee on Nutrition (SACN) documentation of a report about the Dietary Reference 
    Values for Food Energy and Nutrients for the United Kingdom 2011. We have used their method of estimation for dietary requirements 
    along with taking references to Dietary Reference Intakes Book for other nutrients. We have also used a kaggle dataset to take input 
    data for the rest of the nutrients except energy.   
    """
)

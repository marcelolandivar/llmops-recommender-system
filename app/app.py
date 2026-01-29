import streamlit as st
from pipeline.pipeline import RecommendationPipeline
from dotenv import load_dotenv
from utils.logger import get_logger



logger = get_logger(__name__)

st.set_page_config(page_title="Recommendation System", layout="wide")

load_dotenv()
@st.cache_resource
def init_pipeline():
    return RecommendationPipeline()

pipeline = init_pipeline()
st.title("Recommendation System")

query = st.text_input("Enter your query: Eg. Light hearted anime with school settings", "")

if st.button("Get Recommendations"):
    if query:
        with st.spinner("Generating recommendations..."):
            recommendations = pipeline.get_recommendations(query)
            st.subheader("Recommendations:")
            st.write(recommendations)
    else:
        st.warning("Please enter a query.")
else:
    st.warning("Please, write your query and click the 'Get Recommendations' button.")

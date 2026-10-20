import streamlit as st
from urllib.parse import urlparse
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="Youtube Video Analyzer",
    page_icon="🎥",
    layout="centered"
)


st.markdown("""
<style>
/* Dashboard background */
.stApp {
    background: linear-gradient(135deg, #0B1020, #151C30);
    color: #F8FAFC;
}

/* Main heading */
h1 {
    color: #A78BFA !important;
    text-align: center;
    font-weight: 800;
}

/* Input box */
.stTextInput input {
    background-color: #151C30;
    color: white;
    border: 1px solid #8B5CF6;
    border-radius: 10px;
}

/* Analyze button */
.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #A855F7);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.5rem;
    font-weight: bold;
    transition: 0.3s ease;
}

/* Button hover effect */
.stButton > button:hover {
    background: linear-gradient(90deg, #6D28D9, #9333EA);
    color: white;
    border: 1px solid #C4B5FD;
    transform: translateY(-2px);
}

/* Focus effect */
.stButton > button:focus {
    color: white;
    border: 1px solid #C4B5FD;
}

/* Analysis report */
.stMarkdown {
    color: #E2E8F0;
}
</style>
""", unsafe_allow_html=True)


st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

# input box
video_url = st.text_input("Enter a YouTube video link to generate a detailed analysis report.") # str
button = st.button("Analyze Video") # True/False

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)
import streamlit as st
import pandas as pd

# Load dataset
data = pd.read_csv("dataset/destinations.csv")

st.set_page_config(
    page_title="AI Vacation Planner",
    page_icon="✈",
    layout="centered"
)

# Background styling
page_bg = """
<style>
.stApp {
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1600&auto=format&fit=crop");
    background-size: cover;
}

.main {
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("✈ AI Vacation Planner")

st.write("Discover your perfect destination using AI recommendations 🌍")

# Inputs
travel_type = st.selectbox(
    "🌍 Select Travel Type",
    data["Type"].unique()
)

budget = st.selectbox(
    "💰 Select Budget",
    data["Budget"].unique()
)

season = st.selectbox(
    "🌤 Select Season",
    data["Season"].unique()
)

# Recommendation button
if st.button("🔍 Find My Destination"):

    filtered = data[
        (data["Type"] == travel_type) &
        (data["Budget"] == budget) &
        (data["Season"] == season)
    ]

    if filtered.empty:
        filtered = data[data["Type"] == travel_type]

    result = filtered.sample().iloc[0]

    st.success("🎯 Destination Found!")

    st.markdown(f"""
    ## 📍 {result['Destination']}

    ### 🎡 Activities
    {result['Activities']}

    ### 🏨 Hotel
    {result['Hotel']}

    ### ✈ Travel Mode
    {result['Travel_Mode']}
    """)
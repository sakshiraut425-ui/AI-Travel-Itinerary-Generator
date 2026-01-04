import streamlit as st
import sys

# Allow app.py to find the models folder
sys.path.append(".")

from models.itinerary_generator import generate_itinerary
from models.summarizer import summarize_itinerary

st.set_page_config(page_title="AI Travel Planner")

st.title("AI Travel Itinerary Generator")

destination = st.text_input("Enter Destination")
days = st.number_input("Number of Days", min_value=1, max_value=14)
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
travel_type = st.selectbox(
    "Travel Type", ["Solo", "Family", "Friends", "Couple"]
)

if st.button("Generate Itinerary"):
    with st.spinner("Generating itinerary..."):
        itinerary = generate_itinerary(
            destination, days, budget, travel_type
        )
        summary = summarize_itinerary(itinerary)

    st.subheader("Detailed Itinerary")
    st.write(itinerary)

    st.subheader("Short Summary")
    st.write(summary)

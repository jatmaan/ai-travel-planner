import streamlit as st
import time
from ai_client import ask_ai

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.sidebar.title("✈️ AI Travel Planner")
st.subheader("Example Trips")

col1, col2 = st.columns(2)

with col1:
    if st.button("🇯🇵  5 Days in Japan"):
        st.session_state.trip = "5 days in Japan under $3000"

    if st.button("🇫🇷 Weekend in Paris"):
        st.session_state.trip = "Weekend trip to Paris"

with col2:
    if st.button("🇮🇹 Food Tour of Italy"):
        st.session_state.trip = "7 day food tour of Italy"

    if st.button("🏖 Hawaii Vacation"):
        st.session_state.trip = "5 day family vacation to Hawaii"

st.sidebar.markdown("---")

st.sidebar.write("**Version:** 1.0")

st.sidebar.write("**Model:** llama3.2")

st.sidebar.markdown("---")

st.sidebar.write("Built with:")
st.sidebar.write("- Python")
st.sidebar.write("- Streamlit")
st.sidebar.write("- Ollama")
st.title("✈️ AI Travel Planner")

st.write("Generate travel itineraries using AI running locally with Ollama.")

trip_request = st.text_input(
    "Where would you like to go?",
    value=st.session_state.get("trip", ""),
)

if st.button("Generate Plan"):

    if not trip_request.strip():
        st.warning("Please enter a trip request.")
    else:

        with st.spinner("🛫 Contacting AI... Building your itinerary..."):

            try:
                start = time.time()
                result = ask_ai(trip_request)
                elapsed = time.time() - start
                st.success(f"Response generated in {elapsed:.1f} seconds")
                st.markdown(result)

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Cannot connect to Ollama.\n\n"
                    "Please make sure 'ollama serve' is running."
                )

            except Exception as e:

                st.error(f"Unexpected error:\n\n{e}")

st.markdown("---")

st.caption(
    "AI Travel Planner • Built with Python, Streamlit and Ollama"
)
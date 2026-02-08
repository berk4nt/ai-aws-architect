import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from crew.crew import get_crew

st.set_page_config(
    page_title = "AI AWS Cloud Architect",
    layout = "wide",
)

st.title ("☁️ AI Cloud Architect Assistant (AWS)")

with st.form("cloud_form") :
    description = st.text_area(
        "Describe your application",
        placeholder="e.g. SaaS web app with REST API and PostgreSQL"
    )

    users = st.number_input(
        "Expected monthly users",
        min_value=100,
        max_value=10000000,
        value=10000,
        step=1000
    )

    data_sensitivity = st.selectbox(
        "Data sensitivity",
        ["Low", "Medium","High"]
    )

    budget = st.slider(
        "Monthly budget (USD)",
        50, 5000, 500
    )

    submitted = st.form_submit_button("Generate AWS Architecture")

if submitted :
    crew = get_crew()

    result = crew.kickoff(
        inputs = {
            "description" : description,
            "users" : users,
            "data_sensitivity" : data_sensitivity,
            "budget" : budget
        }
    )

    st.markdown("## Architecture Report")
    st.markdown(str(result.raw))


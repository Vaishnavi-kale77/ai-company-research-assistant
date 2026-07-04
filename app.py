import streamlit as st

from services.serper import search_company
from services.crawler import crawl_website
from services.ai_service import analyze_company
from services.pdf_generator import generate_pdf


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Company Research Assistant",
    layout="wide"
)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("AI Research Settings")

    selected_model = st.selectbox(
        "Choose AI Model",
        [
            "deepseek/deepseek-chat",
            "openai/gpt-4o-mini"
        ]
    )

    st.info(
        "AI-powered company analysis tool"
    )

    st.markdown("---")

    st.markdown(
        """
        ### Features
        ✅ Website Detection  
        ✅ Website Crawling  
        ✅ AI Analysis  
        ✅ PDF Report Generation  
        """
    )


# ---------------- MAIN UI ---------------- #

st.title("AI Company Research Assistant")

st.write("Research any company using AI")

st.markdown(
    """
    ### Sample Companies
    - OpenAI
    - Nike
    - Infosys
    - Adobe
    - Tesla
    """
)


# ---------------- USER INPUT ---------------- #

user_input = st.chat_input(
    "Enter company name or website URL"
)


# ---------------- PROCESS ---------------- #

if user_input:

    progress_bar = st.progress(0)

    st.chat_message("user").write(user_input)

    # ---- FIND WEBSITE ---- #

    with st.spinner("Finding company website..."):

        if "http" in user_input:
            website = user_input
        else:
            website = search_company(user_input)

    progress_bar.progress(25)

    # ---- WEBSITE VALIDATION ---- #

    if not website or website == "Website not found":

        st.error(
            "Could not find company website."
        )

        st.stop()

    st.chat_message("assistant").write(
        f"Official Website: {website}"
    )

    # ---- CRAWL WEBSITE ---- #

    with st.spinner("Crawling website..."):

        website_content = crawl_website(
            website
        )

    progress_bar.progress(60)

    # ---- METRICS ---- #

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Website Found",
            "Yes"
        )

    with col2:
        st.metric(
            "Content Extracted",
            f"{len(website_content)} chars"
        )

    with col3:
        st.metric(
            "AI Model",
            selected_model
        )

    # ---- AI ANALYSIS ---- #

    with st.spinner(
        "Generating AI Analysis..."
    ):

        ai_response = analyze_company(
            website_content,
            selected_model
        )

    progress_bar.progress(100)

    st.success(
        "AI analysis completed successfully!"
    )

    # ---- TABS ---- #

    tab1, tab2 = st.tabs(
        [
            "Website Content",
            "AI Analysis"
        ]
    )

    # ---- WEBSITE CONTENT TAB ---- #

    with tab1:

        st.subheader(
            "Extracted Website Content"
        )

        st.write(
            website_content[:2000]
        )

    # ---- AI ANALYSIS TAB ---- #

    with tab2:

        st.subheader(
            "AI Company Analysis"
        )

        st.write(ai_response)

    # ---- PDF GENERATION ---- #

    pdf_file = generate_pdf(ai_response)

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="Download PDF Report",
            data=file,
            file_name="company_report.pdf",
            mime="application/pdf"
        )


# ---------------- FOOTER ---------------- #

st.markdown("---")

st.caption(
    "Built using Streamlit, Serper, OpenRouter, and AI"
)
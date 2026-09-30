import streamlit as st

st.set_page_config(
    page_title="Job Application Portal",
    page_icon="💼",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #e0f2fe, #fce7f3, #ede9fe);
}

.title {
    text-align: center;
    color: #4c1d95 !important;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #9d174d !important;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 30px;
}

.box {
    background: #ffffff !important;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
    margin-bottom: 20px;
}

.section {
    color: #5b21b6 !important;
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 15px;
}

label {
    color: #1f2937 !important;
    font-weight: bold !important;
}

input {
    color: #111827 !important;
    background-color: #ffffff !important;
}

textarea {
    color: #111827 !important;
    background-color: #ffffff !important;
}

[data-baseweb="select"] {
    background-color: #ffffff !important;
}

[data-baseweb="select"] * {
    color: #111827 !important;
}

.stRadio label {
    color: #1f2937 !important;
}

.stFileUploader label {
    color: #1f2937 !important;
}

.stFileUploader section {
    background-color: #ffffff !important;
}

.stFileUploader section * {
    color: #1f2937 !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #7c3aed, #db2777);
    color: #ffffff !important;
    border: none;
    border-radius: 25px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #db2777, #7c3aed);
}

.stSuccess {
    color: #166534 !important;
}

.stError {
    color: #991b1b !important;
}

.stInfo {
    color: #1e3a8a !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #4c1d95 !important;
}

p {
    color: #374151 !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="title">💼 Job Application Portal</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Apply for your dream job today 🚀</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="box"><div class="section">👤 Personal Information</div>',
    unsafe_allow_html=True
)

name = st.text_input(
    "Full Name",
    placeholder="Enter your full name"
)

email = st.text_input(
    "Email Address",
    placeholder="example@gmail.com"
)

phone = st.text_input(
    "Phone Number",
    placeholder="Enter your phone number"
)

address = st.text_area(
    "Address",
    placeholder="Enter your address"
)

st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    '<div class="box"><div class="section">🎓 Education</div>',
    unsafe_allow_html=True
)

qualification = st.selectbox(
    "Highest Qualification",
    [
        "10th",
        "12th",
        "Diploma",
        "B.Tech",
        "B.Sc",
        "B.Com",
        "BBA",
        "M.Tech",
        "MBA",
        "Other"
    ]
)

college = st.text_input(
    "College / University",
    placeholder="Enter your college or university"
)

graduation_year = st.selectbox(
    "Graduation Year",
    [
        "2024",
        "2025",
        "2026",
        "2027",
        "2028",
        "2029"
    ]
)

st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    '<div class="box"><div class="section">💼 Job Details</div>',
    unsafe_allow_html=True
)

job_role = st.selectbox(
    "Select Job Role",
    [
        "Software Developer",
        "Python Developer",
        "Web Developer",
        "Data Analyst",
        "Data Scientist",
        "Machine Learning Engineer",
        "AI Engineer",
        "HR Executive",
        "Marketing Executive"
    ]
)

experience = st.selectbox(
    "Experience",
    [
        "Fresher",
        "Less than 1 Year",
        "1-2 Years",
        "2-5 Years",
        "5+ Years"
    ]
)

skills = st.text_input(
    "Skills",
    placeholder="Python, Java, SQL, HTML..."
)

st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    '<div class="box"><div class="section">📄 Resume</div>',
    unsafe_allow_html=True
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    '<div class="box"><div class="section">📝 Application</div>',
    unsafe_allow_html=True
)

cover_letter = st.text_area(
    "Why should we hire you?",
    placeholder="Write a short introduction about yourself..."
)

job_type = st.radio(
    "Job Type",
    [
        "Full Time",
        "Part Time",
        "Internship"
    ],
    horizontal=True
)

location = st.selectbox(
    "Preferred Work Location",
    [
        "Remote",
        "Hyderabad",
        "Bangalore",
        "Chennai",
        "Mumbai",
        "Delhi",
        "Pune",
        "Other"
    ]
)

st.markdown("</div>", unsafe_allow_html=True)


if st.button("🚀 Submit Application"):

    if name and email and phone and resume:

        st.success("🎉 Application submitted successfully!")

        st.balloons()

        st.markdown(
            '<h3 style="color:#4c1d95 !important;">📋 Application Summary</h3>',
            unsafe_allow_html=True
        )

        st.info(f"👤 Name: {name}")
        st.info(f"📧 Email: {email}")
        st.info(f"💼 Job Role: {job_role}")
        st.info(f"⭐ Experience: {experience}")
        st.info(f"🎓 Qualification: {qualification}")
        st.info(f"📍 Preferred Location: {location}")
        st.info(f"🕒 Job Type: {job_type}")

    else:

        st.error(
            "⚠️ Please fill in your Name, Email, Phone Number and upload your Resume."
        )


st.markdown("""
<hr>

<div style="text-align:center;">
    <h3 style="color:#4c1d95;">💼 Job Application Portal</h3>
    <p style="color:#374151;">Apply • Connect • Grow 🚀</p>
</div>
""", unsafe_allow_html=True)
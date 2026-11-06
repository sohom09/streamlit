import streamlit as st
st.title("Student Registration Form")
with st.form("registration_form"):
    name = st.text_input("Student Name")
    reg_num = st.text_input("Register Number")
    programme = st.selectbox(
        "Programme",
        ["B.Tech", "BCA", "B.Sc", "M.Tech", "MCA", "MBA"]
    )
    semester = st.radio(
        "Semester",
        ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]
    )
    subjects = st.multiselect(
        "Subjects",
        ["Mathematics", "Data Structures", "Python Programming", "Web Development", "Database Systems", "Machine Learning"]
    )
    dob = st.date_input("Date of Birth")
    meeting_time = st.time_input("Preferred Meeting Time")
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
    uploaded_photo = st.file_uploader("Upload Student Photograph", type=["jpg", "jpeg", "png"])
    terms = st.checkbox("Accept Terms and Conditions")
    submitted = st.form_submit_button("Submit")

# Display the entered student information after submission
if submitted:
    if not terms:
        st.error("You must accept the Terms and Conditions to submit the form.")
    else:
        st.success("Form Submitted Successfully!")
        st.subheader("Registered Student Information:")

        st.write(f"**Student Name:** {name}")
        st.write(f"**Register Number:** {reg_num}")
        st.write(f"**Programme:** {programme}")
        st.write(f"**Semester:** {semester}")
        st.write(f"**Subjects:** {', '.join(subjects) if subjects else 'None selected'}")
        st.write(f"**Date of Birth:** {dob}")
        st.write(f"**Preferred Meeting Time:** {meeting_time}")
        st.write(f"**Age:** {age}")

        if uploaded_photo is not None:
            st.image(uploaded_photo, caption="Uploaded Photograph", width=150)
        else:
            st.write("**Photograph:** No file uploaded")

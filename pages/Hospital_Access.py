import streamlit as st

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(page_title="Hospital Access", layout="wide")

# ---------------------------------
# FAKE DOCTOR DATABASE
# ---------------------------------
doctor_db = {
    "DR001": {
        "password": "pass123",
        "hospital": "APOLLO",
        "role": "Cardiologist",
        "otp": "1111"
    },

    "DR002": {
        "password": "med456",
        "hospital": "FORTIS",
        "role": "General Physician",
        "otp": "2222"
    },

    "DR003": {
        "password": "health789",
        "hospital": "AIIMS",
        "role": "Emergency",
        "otp": "3333"
    }
}

# ---------------------------------
# TITLE
# ---------------------------------
st.title("🏥 Secure Hospital Access Portal")
st.caption("Prototype secure doctor verification system")

st.markdown("---")

# ---------------------------------
# LOGIN SECTION
# ---------------------------------
st.subheader("Doctor Authentication")

doctor_id = st.text_input("Doctor ID")
password = st.text_input("Password", type="password")
hospital = st.text_input("Hospital Code")

role = st.selectbox(
    "Select Role",
    ["Cardiologist", "General Physician", "Emergency"]
)

otp = st.text_input("Enter OTP")

st.markdown("---")

# ---------------------------------
# LOGIN BUTTON
# ---------------------------------
if st.button("🔐 Login Securely"):

    if doctor_id in doctor_db:

        doc = doctor_db[doctor_id]

        if (
            password == doc["password"]
            and hospital == doc["hospital"]
            and role == doc["role"]
            and otp == doc["otp"]
        ):

            st.success("✅ Access Granted")

            st.markdown("---")

            # ---------------------------------
            # PATIENT SEARCH
            # ---------------------------------
            st.subheader("Search Patient Record")

            patient_id = st.text_input("Enter Patient ID")

            if st.button("Search Patient"):

                st.subheader("Patient Emergency Summary")

                st.write("Patient ID: P203")
                st.write("Name: Ramesh Kumar")
                st.write("Age: 63")
                st.write("Blood Group: O+")
                st.write("Condition: Diabetes, Hypertension")
                st.write("Allergy: Penicillin")
                st.write("Medication: Metformin")
                st.write("Last Visit: 12 March 2026")

                st.info("🔍 Access Logged")
                st.write("Doctor:", doctor_id)
                st.write("Hospital:", hospital)
                st.write("Reason: Emergency Review")

                # Emergency button
                if st.button("🚨 Emergency Access"):
                    st.warning("Emergency Access Granted")
                    st.write("Full Record Unlocked")

        else:
            st.error("❌ Invalid Credentials")

    else:
        st.error("❌ Doctor Not Registered")


# ---------------------------------
# DEMO CREDENTIALS
# ---------------------------------
with st.expander("Demo Login Credentials"):

    st.write("Doctor ID: DR001")
    st.write("Password: pass123")
    st.write("Hospital Code: APOLLO")
    st.write("Role: Cardiologist")
    st.write("OTP: 1111")
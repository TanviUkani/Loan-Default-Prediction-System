import streamlit as st
import pickle
import pandas as pd

# Load model and preprocessor
model = pickle.load(open("loan_default_model.pkl", "rb"))
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))

# Page settings
st.set_page_config(
    page_title="Loan Default Prediction",
    page_icon="🏦",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>

.main{
padding-top:2rem;
}

h1{
text-align:center;
}

.subtitle{
text-align:center;
font-size:18px;
color:gray;
margin-bottom:30px;
}

.stButton > button{
width:100%;
height:3em;
font-size:18px;
font-weight:bold;
border-radius:10px;
}

.green-box{
padding:20px;
border-radius:10px;
background-color:#d4edda;
border-left:8px solid #28a745;
font-size:24px;
font-weight:bold;
text-align:center;
color:#155724;
}

.red-box{
padding:20px;
border-radius:10px;
background-color:#f8d7da;
border-left:8px solid #dc3545;
font-size:24px;
font-weight:bold;
text-align:center;
color:#721c24;
}

</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
"<h1>🏦 Loan Default Prediction System</h1>",
unsafe_allow_html=True
)

st.markdown(
"<p class='subtitle'>Predict whether a customer is likely to default on a loan</p>",
unsafe_allow_html=True
)

st.divider()

# Two columns

col1,col2=st.columns(2)

with col1:

    st.subheader("💰 Financial Information")

    age=st.number_input(
        "Age",
        min_value=18,
        max_value=100
    )

    income=st.number_input("Income")

    loan_amount=st.number_input(
        "Loan Amount"
    )

    credit_score=st.number_input(
        "Credit Score"
    )

    months_employed=st.number_input(
        "Months Employed"
    )

    num_credit_lines=st.number_input(
        "Number of Credit Lines"
    )

    interest_rate=st.number_input(
        "Interest Rate"
    )

    loan_term=st.number_input(
        "Loan Term"
    )

    dti_ratio=st.number_input(
        "DTI Ratio"
    )


with col2:

    st.subheader("👤 Personal Information")

    education=st.selectbox(
        "Education",
        ["Bachelor's","Master's",
         "High School","PhD"]
    )

    employment=st.selectbox(
        "Employment Type",
        ["Full-time",
         "Unemployed",
         "Self-employed",
         "Part-time"]
    )

    marital=st.selectbox(
        "Marital Status",
        ["Divorced","Married","Single"]
    )

    mortgage=st.selectbox(
        "Has Mortgage",
        ["Yes","No"]
    )

    dependents=st.selectbox(
        "Has Dependents",
        ["Yes","No"]
    )

    purpose=st.selectbox(
        "Loan Purpose",
        ["Other","Auto",
         "Business",
         "Home",
         "Education"]
    )

    cosigner=st.selectbox(
        "Has Co-Signer",
        ["Yes","No"]
    )


st.write("")
st.write("")

if st.button("🔍 Predict Loan Status"):

    new_data=pd.DataFrame({

        'Age':[age],
        'Income':[income],
        'LoanAmount':[loan_amount],
        'CreditScore':[credit_score],
        'MonthsEmployed':[months_employed],
        'NumCreditLines':[num_credit_lines],
        'InterestRate':[interest_rate],
        'LoanTerm':[loan_term],
        'DTIRatio':[dti_ratio],

        'Education':[education],
        'EmploymentType':[employment],
        'MaritalStatus':[marital],

        'HasMortgage':[mortgage],
        'HasDependents':[dependents],
        'LoanPurpose':[purpose],
        'HasCoSigner':[cosigner]

    })

    try:

        new_data_trf=preprocessor.transform(
            new_data
        )

        prediction=model.predict(
            new_data_trf
        )

        st.divider()

        if prediction[0]==1:

            st.markdown(
            """
            <div class='red-box'>
            ❌ High Risk: Customer likely to Default
            </div>
            """,
            unsafe_allow_html=True
            )

        else:

            st.markdown(
            """
            <div class='green-box'>
            ✅ Low Risk: Customer likely Non-default
            </div>
            """,
            unsafe_allow_html=True
            )

    except Exception as e:

        st.error(f"Error : {e}")
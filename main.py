import streamlit as st  
# for title
st.title('🔐 Password Strength Meter')

# Background Image CSS
st.markdown(
    """
    <style>
        .stApp {
            color:white;
            background-image: url('https://toppng.com/uploads/preview/textured-wall-background-11553984771wvzhzjb6q9.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        label{
        color : white !important;
        font-size:32px !important;
        font-weight: bold;
        }

        .warning-box {
            background-color: #ffe6e6;
            color:black;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        .warning-box2{
         background-color: #ffe6e6;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Guidelines Section
st.markdown("✅ Password Requirements:")
st.markdown(
    """
    -  At least **8 characters** long  
    -  Contains at least **one uppercase letter**  
    -  Contains at least **one lowercase letter**  
    -  Contains at least **one digit** (0-9)  
    -  Contains at least **one special character** (!@#$%^&*)  
    -  **No spaces** allowed  
    -  **No consecutive repeating characters**  
    """
)

# User se password input lena**
passw = st.text_input('🔑 Enter Your Password:', type="password")  

def check(password: str):
    # Conditions dictionary
    conditions = {
        "Minimum 8 characters": len(password) >= 8,
        "At least one uppercase letter": any(char.isupper() for char in password),
        "At least one lowercase letter": any(char.islower() for char in password),
        "At least one digit": any(char.isdigit() for char in password),
        "At least one special character (!@#$%^&*)": any(char in "!@#$%^&*" for char in password),
        "No spaces allowed": " " not in password
    }

    # ye conditions store karaha hai jo false hai 
    missing = [condition for condition, is_present in conditions.items() if not is_present]


 # Strength Calculation
    score = sum(conditions.values())  # ye sum karaha hai k kitni conditions true hai
    #ye level obj hai jis m password ka level dia hai
    strength_levels = {0: "Very Weak", 1: "Weak", 2: "Weak", 3: "Moderate", 4: "Good", 5: "Strong", 6: "Very Strong"}
    
    strength_text = strength_levels[score]

    # **Show Progress Bar**
    progress = score / 6  
    st.progress(progress)

    # **Display Strength Message**
    if score == 6:
        st.success(f'✅ {strength_text} Password!')
    else:
        st.markdown('<div class="warning-box">⚠️ Weak Password! Fix these: </div>', unsafe_allow_html=True)
        for issue in missing:
            st.markdown(f"- ❌ {issue}")
        st.markdown(f'<div class="warning-box">🔵 Password Strength: {strength_text}</div>',unsafe_allow_html=True)
if passw:
    check(passw)


st.markdown('Made with ❤️ by Aiman Khan')
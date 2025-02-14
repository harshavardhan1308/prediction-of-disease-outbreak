import base64
import os
import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Prediction of Disease Outbreaks',layout='wide',page_icon="doctor")
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the correct relative paths
diabetes_model_path = os.path.join(base_dir, "training_models", "diabetes_model.sav")
heart_model_path = os.path.join(base_dir, "training_models", "heart_model.sav")
parkinsons_model_path = os.path.join(base_dir, "training_models", "parkinsons_model.sav")

# Load models safely
try:
    with open(diabetes_model_path, 'rb') as f:
        diabetes_model = pickle.load(f)

    with open(heart_model_path, 'rb') as f:
        heart_model = pickle.load(f)

    with open(parkinsons_model_path, 'rb') as f:
        parkinsons_model = pickle.load(f)

    print("Models loaded successfully!")

except FileNotFoundError as e:
    print(f"Error: {e}")
#diabetes_model = pickle.load(open(r"C:\Users\Harsha\OneDrive\Desktop\pred_disease_outbreak\training_models\diabetes_model.sav",'rb'))
#heart_model = pickle.load(open(r"C:\Users\Harsha\OneDrive\Desktop\pred_disease_outbreak\training_models\heart_model.sav",'rb'))
#parkinsons_model = pickle.load(open(r"C:\Users\Harsha\OneDrive\Desktop\pred_disease_outbreak\training_models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                           menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
    
if selected == 'Diabetes Prediction':
    
    if selected == 'Diabetes Prediction':
        #set_background("diabetes-symptoms-and-treatment.jpg")

        st.title('Diabetes Prediction using ML')

    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        Bloodpressure = st.text_input('Blood pressure value')
    with col1:
        SkinThickness = st.text_input('Skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input = [float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'
    st.success(diab_diagnosis)

#Heart disease
if selected == 'Heart Disease Prediction':
    #set_background("images.jpg")
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Plessure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting electrocardiographic result value')
    with col2:
        thalach = st.text_input('Maximum Heart rate achieved')
    with col3:
        exang = st.text_input('Excercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression Induced by excercise')
    with col2:
        slope = st.text_input('Slope of the peak excercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        heart_prediction=heart_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis= 'The person is having heart disease'
        else:
            heart_diagnosis= 'The person does not heart disease'
    st.success(heart_diagnosis)



if selected == "Parkinsons prediction":
    
    st.title("Parkinson's Disease Prediction using ML")
    

    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')  # Fixed the typo from "apread1"
    with col5:
        spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        try:
            # Convert inputs to float, handle empty strings
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, 
                          Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            
            user_input = [float(x) if x.strip() else 0.0 for x in user_input]  # Replace empty inputs with 0.0

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

        except Exception as e:
            st.error(f"Error in prediction: {e}")

    st.success(parkinsons_diagnosis)  # Ensure this is inside the block




    
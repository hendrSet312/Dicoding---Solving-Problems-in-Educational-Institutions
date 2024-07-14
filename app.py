import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib

#import model
model = joblib.load('model/model.pkl')
cat_boost_encoder = joblib.load('model/cb_encoder.pkl')

#membersihkan data course
def clean_course_column(course):
    if course in ['Biofuel Production Technologies',
                    'Agronomy','Informatics Engineering'
                    ,'Equinculture']:
        return 'Science & Technology'
    elif course in ['Animation and Multimedia Design',
                    'Communication Design','Journalism and Communication', 
                    'Basic Education','Social Service']:
        return 'Social Science'
    elif course in ['Management','Advertising and Marketing Management','Tourism']:
        return 'Business & management'
    return 'Health Science'
    
#membersihkan data pekerjaan
def clean_occupation(occ):
    if occ == 'Management (Director, Legislative , Executive etc)':
        return 'Management'
    elif occ == 'Professional (Health Professional, Teacher, Specialist, etc)':
        return 'Professional'
    return occ

#class untuk data form
class form_handler:
    def __init__(self,data_dict):
        self.data_dict = data_dict
        self.dataframe = None

    #konversi ke dataframe pandas
    def convert_to_pandas(self):
        self.dataframe = pd.DataFrame(self.data_dict)

    #membersihkan data sebelum diprediksi
    def cleaning_data(self):
        self.dataframe['Mothers_occupation'] = self.dataframe['Mothers_occupation'].apply(lambda occu : clean_occupation(occu) )
        self.dataframe['Fathers_occupation'] = self.dataframe['Mothers_occupation'].apply(lambda occu : clean_occupation(occu) )
        self.dataframe['Course'] = self.dataframe['Course'].apply(lambda course : clean_course_column(course) )
        self.dataframe = self.dataframe.replace({
            'Gender':{'🚹 Male':1,'🚺 Female':0},
            'Debtor':{'✅ Yes':1,'❌ No':0},
            'Scholarship_holder':{'✅ Yes':1,'❌ No':0}
        })
        self.dataframe = cat_boost_encoder.transform(self.dataframe)
    
    #prediksi data 
    def predict(self):
        x = self.dataframe.values
        prediction_res = model.predict_proba(x).ravel()
        class_dict = {1:'Dropout',0:'Not Dropout'}
        max_index = np.argmax(prediction_res)

        return [class_dict[max_index],round(prediction_res[max_index]*100,2)]



#isi main page   
def main():
    st.header("🎓 Student Status Prediction")
    st.write('Predict whether the student dropout or not')

    #form untuk mengisi data
    with st.form("User Prediction"):
        st.subheader('**👤 Student\'s Profile**')

        st.write('Enter the student\'s information here 👇')
        name = st.text_input("Name",placeholder="Insert the student name...")
        gender = st.radio('Gender',['🚹 Male','🚺 Female'])
        age = st.number_input('🎂 Age (Must > 17 years old)',17,100)
        scolarship = st.radio('💵 Scholarship holder?',['✅ Yes','❌ No'])
        debtor = st.radio('🧾 Have a debt / loan ?',['✅ Yes','❌ No'])
        course = st.selectbox('📖 Course',(
            'Biofuel Production Technologies',
            'Animation and Multimedia Design',
            'Agronomy',
            'Communication Design',
            'Veterinary Nursing',
            'Informatics Engineering',
            'Equinculture',
            'Management',
            'Social Service',
            'Tourism',
            'Nursing',
            'Oral Hygiene',
            'Advertising and Marketing Management',
            'Journalism and Communication',
            'Basic Education'
        ))

        
        mother_occupation = st.selectbox(
            '💼 Mother occupation',
            ('Management (Director, Legislative , Executive etc)',
             'Professional (Health Professional, Teacher, Specialist, etc)'
             ,'Technician',
             'Administrative',
             'Service & sales','Armed Forces','Labour',
             'Unemployed'),
        )

        father_occupation = st.selectbox(
            '💼 Father occupation',
            ('Management (Director, Legislative , Executive etc)',
             'Professional (Health Professional, Teacher, Specialist, etc)'
             ,'Technician',
             'Administrative',
             'Service & sales','Armed Forces','Labour',
             'Unemployed'),
        )
        
        
        with st.container():
            st.subheader("🚀 Academic Performance")
            st.write('Enter the student\'s academic performance here 👇')
            with st.container():
                st.subheader('1️⃣ 1st Semester')

                sem1_enrolled_unit = st.number_input('📚 Enrolled units (0-99): ',0,99, key = 1)
                sem1_approved_unit = st.number_input('☑️ Approved unit (0-99):',0, 99, key = 2)
                sem1_evaluation_unit = st.number_input('✍ Evaluation units (0-99): ',0,99, key = 3)
                sem1_grade = st.number_input('💯 Grade units (0-20): ',0,20, key = 4)

            with st.container():
                st.subheader('2️⃣ 2nd Semester')
                sem2_enrolled_unit = st.number_input('📚 Enrolled units (0-99): ',0,99, key = 5)
                sem2_approved_unit = st.number_input('☑️ Approved unit (0-99):',0, 99, key = 6)
                sem2_evaluation_unit = st.number_input('✍ Evaluation units (0-99): ',0,99, key = 7)
                sem2_grade = st.number_input('💯 Grade units (0-20): ',0,20, key = 8)

        
        submitted = st.form_submit_button("✨ Predict")

        if submitted:

            #mengumpulkan data untuk diolah menjadi prediksi 
            app_unit = sem1_approved_unit+sem2_approved_unit
            enrolled_unit = sem1_enrolled_unit+sem2_enrolled_unit
            evaluated_unit = sem2_evaluation_unit+sem1_evaluation_unit
            unit_grade = np.mean([sem2_grade,sem1_grade]) * 5
            completion_unit_rate = (app_unit/enrolled_unit) if enrolled_unit > 0 else 0 
            sucess_eval_rate = (app_unit/evaluated_unit) if evaluated_unit > 0 else 0 
            
            data = {
                'Course': [course],
                'Mothers_occupation':[mother_occupation],
                'Fathers_occupation':[father_occupation],
                'Debtor':[debtor],
                'Gender' :[gender] , 
                'Age_at_enrollment' : [int(age)],
                'Scholarship_holder': [scolarship],
                '1st_yr_approved_unit':[app_unit],
                '1st_yr_enrolled_unit':[enrolled_unit],
                '1st_yr_evaluated_unit':[evaluated_unit],
                '1st_yr_unit_grade':[unit_grade],
                '1st_yr_Completion_unit_rate':[completion_unit_rate],
                '1st_yr_Success_evaluation_rate':[sucess_eval_rate]
            }

            submitted_data = form_handler(data)
            submitted_data.convert_to_pandas()
            submitted_data.cleaning_data()
            result,percentage = submitted_data.predict()

            #hasil prediksi
            st.write('**👉 Result :**')
            st.write(f'Student, {name} is predicted : **{result}** ({percentage}%)')
    

main()
            








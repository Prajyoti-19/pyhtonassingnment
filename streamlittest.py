import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


data = {
'Logical_Reasoning': [1, 3, 5, 1, 3, 5, 1, 3, 5],
'Frontend': [1, 1, 1, 0, 0, 1, 0, 1, 1],
'Backend': [0, 0, 0, 1, 1, 1, 1, 1, 1],
'QA_Testing': [0, 0, 0, 0, 1, 1, 0, 0, 1],
'Maths_Statistics': [1, 3, 5, 1, 3, 4, 1, 3, 5],
'AI': [0, 0, 0, 1, 1, 1, 0, 1, 1],
'Experience': [1, 1, 1, 1, 1, 1, 0, 1, 1],
'Hours': [1, 3, 4, 1, 3, 5, 1, 3, 5],
'resultskill': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
}

df = pd.DataFrame(data)

label_encoder = LabelEncoder()
df['resultskill_covertnumeric'] = label_encoder.fit_transform(df['resultskill'])

x = df[['Logical_Reasoning', 'Frontend', 'Backend', 'QA_Testing', 'Maths_Statistics', 'AI', 'Experience', 'Hours']]
y = df['resultskill_covertnumeric']

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)


st.title("Student Course & Skill Level Predictor")

lrs = st.slider("Logical Reasoning Skill", 0,5)
fd = st.radio("Interest in Frontend Development", ["Yes", "No"])
bd = st.radio("Interest in Backend Development", ["Yes", "No"])
qa = st.radio("Interest in QA/Testing", ["Yes", "No"])
ms = st.slider("Comfort with Math/Statistics", 0,5)
ai = st.radio("Interest in Artificial Intelligence", ["Yes", "No"])
ce = st.radio("Prior Coding Experience", ["Yes", "No"])
hd = st.slider("Hours Available for Study Daily", 0,5)

if fd == "Yes":
    fdv = 1
else:
    fdv = 0

if bd == "Yes":
    bdv = 1
else:
    bdv = 0

if qa == "Yes":
    qav = 1
else:
    qav = 0

if ai == "Yes":
    aiv = 1
else:
    aiv = 0

if ce == "Yes":
    cev = 1
else:
    cev = 0

    
give_input = np.array([[lrs, fdv, bdv, qav, ms, aiv, cev, hd]])
show_result = model.predict(give_input)
convert_num_to_label = label_encoder.inverse_transform(show_result)[0]
print(f"Result is {convert_num_to_label}")

output_in_word = {
 'a': ['Web Development', 'Beginner'],
 'b': ['Web Development', 'Intermediate'],
 'c': ['Web Development', 'Advanced'],
 'd': ['Artifical Intelligence', 'Beginner'],
 'e': ['Artifical Intelligence', 'Intermediate'],
 'f': ['Artifical Intelligence', 'Advanced'],
 'g': ['Data Science', 'Beginner'],
 'h': ['Data Science', 'Intermediate'],
 'i': ['Data Science', 'Advanced']
}


if st.button("Submit"):
    
    for key, value in output_in_word.items():
        if key == convert_num_to_label:
            st.success(f"Recommended Course: {value[0]}, Skill Level: {value[1]}")
    




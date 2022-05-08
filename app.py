import streamlit as st
import numpy as np 
import pandas as pd 

st.title("Workout Generator")

level=st.sidebar.selectbox("Choose level",['Beginner','Intermediate','Advanced'])
intensity=st.sidebar.selectbox("Choose intensity",['Low','Medium','Hardcore'])
muscle_group=st.sidebar.selectbox("Choose targeted muscle group",['Full Body','Abdominals','Back','Biceps','Calves','Chest','Legs','Shoulders','Triceps'])
exercises_n=st.sidebar.slider("Number of exercises",4,20)

if intensity=='Hardcore':
    pic='hardcore'
    st.image(pic, use_column_width=True)


if intensity=='Low':
    st.markdown("Perform the exercises below in a following manner 8-10 reps. 1 min-2 min breaks in between the exercises")
elif intensity=='Medium':
    st.markdown("Perform the exercises below in a following manner 8-12 reps. 1 min breaks in between the exercises")
elif intensity=='Hardcore':
    st.markdown("Perform the exercises below in a following manner 12-20 reps. Take no breaks in between the exercises and then die...")

df=pd.read_csv('exercises.csv')

#st.dataframe(df['Exercise'].sample(exercises_n))
try:
    if intensity=='Hardcore':
        if muscle_group=='Full Body':
            subset=df[df.Level==level].sample(exercises_n+5)
            st.dataframe(subset['Exercise'])
        else:
            subset=df[(df.Level==level) & (df['Muscle Group'].str.contains(muscle_group))].sample(exercises_n+5)
            st.dataframe(subset['Exercise'])
    else:
        if muscle_group=='Full Body':
            subset=df[df.Level==level].sample(exercises_n)
            st.dataframe(subset['Exercise'])
        else:
            subset=df[(df.Level==level) & (df['Muscle Group'].str.contains(muscle_group))].sample(exercises_n)
            st.dataframe(subset['Exercise'])
except:
    st.subheader("Change the mucle group,level or reduce the number of exercises")

    

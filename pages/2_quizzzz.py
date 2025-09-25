import streamlit as st

# Title of App
st.title("How Crazy Are You Quizzz")

st.write(""" Answer the question below to get your score.

""")
st.write("---")
st.write("---")

score = 0

st.header("Question 1")
subject = st.radio("What is your favorite subject:", ["Math➗", "English📗", "History📜"])#new
st.write("**You chose:**", subject)
if subject == "Math➗" or subject == 'History📜':
    score += 1

st.write("---")
st.write("---")


st.header("Question 2")
sport = st.selectbox("**Who is a better football team UGA or GA TECH:**", ["Georgia Tech✅", "Trash🗑", "More Trash🗑🗑"])#new
st.write("**You selected:**", sport)
if sport == "Georgia Tech✅":
    st.image("Images/football.jpg")
    score += 1

st.write("---")
st.write("---")

st.header("Question 3")
pizza = st.slider("**How much do you like PINEAPPLE on pizza🍕**", 0, 100, 25)#new
if pizza >= 60:
     st.write("**Your NUTS!!!**", pizza)
else:
    st.write("**This was the only correct answer**", pizza)
    score += 1
st.write("**You chose:**", pizza)

st.write("---")
st.write("---")

st.header("Question 4")
dogs = st.radio("**Which is the better animal:**", ["Dog🐶", "Cat🐈",])#new
st.write("**You chose:**", dogs)
if dogs == "Dog🐶":
    score += 1

st.write("---")
st.write("---")

st.header("Question 5")
fav = st.multiselect("**What are your favorite sports?**", ["Baseball⚾", "Football🏈", "Hockey🏒", "Soccer⚽", "Golf⛳", "Rugby🏉"])#new
st.write("**You picked:**", fav)
if "Golf⛳" in fav or " BaseBall⚾" in fav:
    score += 0
else:
    score += 1
    
st.write("---")


if st.button("Submit My Answers"):#new
    st.subheader(f" Congrats On Finishing The Quiz!!!")
    if score < 3:
        st.write (f' YOU ARE INSANE🤪🤪🤪🤪!!!. You got a score of {score} out of 5.')
        st.image("Images/crazy.jpg")
    else:
        st.write (f' I CAN TELL YOU ARE A NORMAL PERSON🔥🔥🔥🔥🔥.  You got a score of {score} out of 5.')
        st.image("Images/chad.jpg")
    st.balloons()#new

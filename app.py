#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌟")
st.title("🌱 Growth Mindset Challenge: Web App with Streamlit")
st.header("🚀 Welcome To Your Growth Journey!")
st.write("Welcome, brave soul! Embrace every challenge, learn from every mistake, and unlock your true potential. This AI-powered app is your companion in developing a resilient and unstoppable growth mindset. Let's grow together! 🌸")

#quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("“Success is not final, failure is not fatal: It is the courage to continue that counts.” — *Winston S. Churchill*")

#challenge section
st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("🧗 Describe a challenge you're facing today:")
if user_input:
    st.success(f"💪 You're facing: *{user_input}*. That's the spirit! Remember, every obstacle is a stepping stone to greatness.")
else:
    st.warning("Tell us about your challenge to begin your transformation!")

#reflection section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("🧠 What did you learn recently or from your challenge?")
if reflection: 
    st.success(f"✨ Beautiful reflection! Here's what you shared: {reflection}")
else: 
    st.info("Reflection fuels growth. Take a moment to think and share your learning.")

#achievements section
st.header("🏆 Celebrate Your Achievements")
achievement = st.text_input("🎯 Share something you've recently accomplished:")
if achievement:
    st.success(f"🎉 Amazing! You achieved: *{achievement}*. Keep celebrating your wins!")
else:
    st.info("No win is too small! Acknowledge your progress and share one now.")

#footer
st.write("---")
st.write("💖 Keep believing in yourself. Growth is a journey, not a destination.")
st.write("*©️ Created with passion by Syeda Aleeza Abbas*")
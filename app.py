import streamlit as st
import ollama

st.set_page_config(page_title="Menu Writer", page_icon="🍛")
st.title("🍛 Menu Description Writer")
st.write("Runs fully on this computer. No internet needed. Your menu stays private.")

english_name = st.text_input("Dish name (English)", "Chettinad Chicken")
tamil_name = st.text_input("Dish name (Tamil)", "செட்டிநாடு சிக்கன்")
notes = st.text_input("Short notes", "spicy, country chicken")

if st.button("Write description"):
	prompt = f"""You write menu descriptions for a small restaurant in Tamil Nadu.
Dish: {english_name}
Details: {notes}

Write ONE appetizing description in English, maximum 2 sentences.
Output only the description. No introduction, no questions, no notes.
"""
	with st.spinner("Writing... please wait"):
		response = ollama.chat(
			model="gemma3:4b",
			messages=[{"role": "user", "content": prompt}],
		)
	st.subheader(f"{tamil_name} / {english_name}")
	st.write(response["message"]["content"].strip())

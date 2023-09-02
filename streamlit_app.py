import streamlit as st
import openai

def set_openai_key():
    openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_short_story(prompt):
    try:
        # Adjusting the API call for chat-based interaction
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip(), None
    except Exception as e:
        return None, str(e)

st.title("OpenAI API Test with GPT-3.5 Turbo Model for Story Generation")

set_openai_key()

prompt = "Once upon a time in a land far, far away..."
story, error = generate_short_story(prompt)

if error:
    st.write(f"API test failed. Error: {error}")
else:
    st.write("API test passed!")
    st.write(prompt + story)

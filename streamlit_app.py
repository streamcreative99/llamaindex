import streamlit as st
import openai

# Set the OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

def test_openai_api():
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Using gpt-3.5-turbo
            prompt="Translate the following English text to French: 'Hello, how are you?'",
            max_tokens=60
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

st.title("OpenAI API Key Test with GPT-3.5 Turbo Model")

result = test_openai_api()

if "Translate the following English text to French:" in result:
    st.write("API test passed!")
    st.write(result)
else:
    st.write("API test failed. Error:", result)

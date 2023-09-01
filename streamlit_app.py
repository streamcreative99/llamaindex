import streamlit as st
import openai

# Initialize Streamlit
st.title("OpenAI API Key Test")

# Load the API key from Streamlit's secrets
if 'OPENAI_API_KEY' in st.secrets:
    openai.api_key = st.secrets['OPENAI_API_KEY']
    st.sidebar.success('API key successfully loaded from secrets!')
else:
    st.sidebar.error('Failed to load API key from secrets!')

# Test the OpenAI API with a simple completion
def test_openai_api():
    try:
        response = openai.Completion.create(
          engine="gpt-3.5-turbo",
          prompt="Translate the following English text to French: 'Hello World'",
          max_tokens=60
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Display the result or error
result = test_openai_api()
if "Translate the following English text to French:" in result:
    st.success(f"API is working correctly! Response: {result}")
else:
    st.error(f"API test failed. Error: {result}")

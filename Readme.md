# Generate Product Ideas from YT or Website

This Streamlit application allows users to generate innovative product ideas inspired by the content of a given YouTube video or website URL. It leverages the Groq API and LangChain models to process and analyze the content.

## Features

- **Generate Product Ideas**: Input a YouTube video or website URL to receive product ideas based on the content.
- **User-Friendly Interface**: Simple and intuitive interface powered by Streamlit.
- **Secure API Access**: Enter your Groq API key securely to access the model.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/srexrg/generate-ideas.git
   cd generate-ideas
   ```

2. **Install the required packages**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter your Groq API Key**: 
   - Navigate to the sidebar and input your Groq API key.

2. **Input a URL**:
   - Enter a valid YouTube video or website URL in the provided text box.

3. **Generate Ideas**:
   - Click the "Generate Product Ideas from YT or Website" button to receive product ideas.

## Requirements

- Python 3.8 or higher
- Streamlit
- Validators
- LangChain and related packages
- YouTube Transcript API


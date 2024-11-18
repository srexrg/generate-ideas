import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.schema import Document
import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_core.messages import HumanMessage, SystemMessage


## sstreamlit APP
st.set_page_config(
    page_title="Generate Product Ideas from YT Videos or Website", page_icon="💡"
)
st.title("💡 Generate Product Ideas from YT Videos or Website")
st.subheader("Generate Product Ideas from URL")

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

# Ensure the API key is set
if not groq_api_key.strip():
    st.error("Please provide a valid Groq API Key or get one from https://groq.com/")
else:

    llm = ChatGroq(
        model="gemma-7b-it",
        groq_api_key=groq_api_key,  
    )

    generic_url = st.text_input("URL", label_visibility="collapsed")

    system_message = SystemMessage(
        content="Generate innovative product ideas inspired by the content of the given YouTube video or website URL."
    )

    if st.button("Generate Product Ideas from YT or Website"):
  
        if not generic_url.strip():
            st.error("Please provide the information to get started")
        elif not validators.url(generic_url):
            st.error(
                "Please enter a valid Url. It can may be a YT video utl or website url"
            )
        else:
            try:
                with st.spinner("Waiting..."):
        
                    if "youtube.com" in generic_url:
                        video_id = generic_url.split("v=")[-1]
                        transcript = YouTubeTranscriptApi.get_transcript(
                            video_id=video_id
                        )
                        text = " ".join([entry["text"] for entry in transcript])
                        docs = [Document(page_content=text)]
                    else:
                        loader = UnstructuredURLLoader(
                            urls=[generic_url],
                            ssl_verify=True,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                            },
                        )
                        docs = loader.load()
                        text = " ".join([doc.page_content for doc in docs])

                    # Prepare the messages for the model
                    messages = [system_message, HumanMessage(content=text)]

                    ai_msg = llm.invoke(messages)

                    st.success(ai_msg.content)
            except Exception as e:
                st.exception(f"Exception:{e}")

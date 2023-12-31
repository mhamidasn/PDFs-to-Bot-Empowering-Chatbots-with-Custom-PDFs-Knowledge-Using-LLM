import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from html_temp import css, bot_template, user_template

def main():
    # load the secret (ex: key)
    load_dotenv()

    # build the UI
    st.set_page_config(page_title="PDFs to Bot",page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>📚 PDFs to Bot 📚</h1>", unsafe_allow_html=True)

    # initiate the session_state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # file uploader
    pdf_docs = st.file_uploader(
        "Upload your PDFs here and click the 'Start the Reading Process' button!", 
        accept_multiple_files=True,
        )
    
    # button
    if st.button("Start the Reading Process"):
        with st.spinner("Reading"):
            # get PDFs texts
            raw_text = get_pdfs_texts(pdf_docs)
            # get the texts chunks
            text_chunks = get_text_chunks(raw_text)
            # create vector store
            vectorstore = get_vectorestore(text_chunks)
            # create conversation chain
            st.session_state.conversation = get_conversation_chain(vectorstore)

    # user question
    user_question = st.text_input("Ask a question about your PDFs:")
    if user_question:
        handle_userinput(user_question)

def get_pdfs_texts(pdf_docs):
    texts = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            texts += page.extract_text()
    return texts

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorestore(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0.9, "max_length":512})
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


if __name__ == '__main__':
    main()
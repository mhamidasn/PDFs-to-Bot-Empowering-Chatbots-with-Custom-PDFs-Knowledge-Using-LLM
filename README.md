<div style="text-align:center;">
    <h1>PDFs to Bot: Empowering Chatbots with Custom PDFs Knowledge Using LLM</h1>
</div>

<div style="text-align:center;">
    <image src="docs/demo_gif.gif" controls title="Title"></image>
</div>

## Table of Contents
- [About the Project](#about-the-project)
- [Setup](#setup)
- [Usage](#usage)
- [Shoutout!](#shoutout)
- [Know more about me!](#know-more-about-me)

# About the Project
PDFs to Bot is a chatbot question answering application designed to empower users with customized knowledge extracted from uploaded PDF documents. Leveraging the capabilities of free embedding and the LLM from Hugging Face, specifically the [instructor text embeddings](https://huggingface.co/hkunlp/instructor-xl) and the [FLAN-T5 LLM model](https://huggingface.co/google/flan-t5-xxl). The user-friendly interface is built using [Streamlit](https://streamlit.io/), ensuring a seamless and intuitive experience. Powered by the [Langchain](https://python.langchain.com/docs/get_started/introduction.html) framework, PDFs to Bot delivers tailored responses and enhances document accessibility, making it a versatile tool for various knowledge-driven applications.

<div style="text-align:center;">
    <image src="docs/how it work.jpg" controls title="How it works"></image>
</div>

# Setup
1. install the dependecies needed\
   ```pip install -r requirements.txt```
2. Add yout huggingface API key to the `.env` file in your directory \
   ```HUGGINGFACEHUB_API_TOKEN=your_secrit_api_key```

# Usage
1. Ensure that you have installed the required dependencies adn added the huggingface API key to the `.env` file
2. In the terminal, run this command:\
   ```streamlit run app.py```
3. The app will launch in you default web, displaying the UI
4. Upload your PDF
5. Ask the question!
   
# Shoutout!
Special thanks to Alejandro AO for being an invaluable source of knowledge and guidance in helping me learn more about LLM and its applications. Be sure to check out his informative content on his [YouTube channel](https://www.youtube.com/@alejandro_ao)

# Know more about me!
website: [mhamidasn.github.io](https://mhamidasn.github.io/)\
linkedin: [linkedin.com/in/mhamidasn](https://www.linkedin.com/in/mhamidasn/)\
github: [github.com/mhamidasn](https://github.com/mhamidasn)

[**Check my other project here!**](https://mhamidasn.github.io/portfolio/)

<p align="center">
  <strong>🌌Here's to pushing boundaries, unraveling mysteries, and creating a future woven with the threads of innovation🌌</strong>
</p>
# pip install openai-agents
<!-- 🧠 Ye command `openai-agents` library install karti hai jo AI agents banane ke liye use hoti hai. 
is library ke zariye ap AI workflows (jaise translators, assistants, etc.) easily design kar sakti ho. -->

# pip install python-dotenv
<!-- 🧪 Ye command `.env` file ko read karne ke liye hoti hai jisme sensitive data hota hai jaise API keys. 
Iska faida ye hai ke API keys directly code me nahi likhte, .env file me save kar ke use secure rakhte hain. -->

# uv init .
<!-- 🧰 `uv` ek modern Python package manager hai (pip ki jagah use ho sakta hai).
`uv init .` command tumhare project ke liye virtual environment setup karta hai aur config files banata hai. -->

# uv venv
<!--  🔒 Ye command virtual environment banata hai jahan tumhare project ke dependencies install hongi.
Iska faida ye hai ke tumhara project doosre Python projects se isolated rehta hai. -->

# python -m streamlit run main.py 
 <!-- 📊 Ye command `Streamlit` app ko run karti hai.
`main.py` wo file hai jisme tumhara Streamlit-based web app likha hota hai.
Jab ye command chalayenge to browser me app open ho jata hai — jo interactive AI agent interface dikhata hai.  -->



for running this you need to run the following commands
.venv\Scripts\activate
streamlit run main.py if it is not working run this command python -m streamlit run main.py


prompt = f"Create a quiz (fill in the blanks or MCQs) to help the user learn this sentence in {target_lang}:\n{text_input}"
# 🤖 AEVI — Advanced Empathetic Virtual Intelligence

AEVI (pronounced *Ay-Vee*) is a multilingual, emotionally intelligent AI assistant designed to function like ChatGPT with an added layer of professional medical knowledge, empathetic interaction, and bilingual communication. Built to assist users in both **English** and **Tanglish** (Tamil-English hybrid), AEVI is capable of handling a wide range of queries—from health guidance and emotional support to academic help and current affairs.

---

## 🧠 Purpose

The primary goal of AEVI is to offer:
- **Empathetic responses** to users experiencing stress, anxiety, or discomfort.
- **Medically sound, general wellness advice** for non-critical symptoms.
- **Academic support** in various subjects like science, technology, history, etc.
- **Real-time, up-to-date answers** for current affairs and general questions.
- **Bilingual communication** in English and Tanglish for a personalized experience.

---

## ✨ Key Features

- ✅ **Medical & Emotional Intelligence**: Offers responsible, safe suggestions and reassurance.
- ✅ **ChatGPT-like Smartness**: Answers general queries, trending topics, and academic questions.
- ✅ **Bilingual Response Engine**: Communicates fluently in both English and Tanglish (Tamil-English).
- ✅ **Contextual Understanding**: Detects intent—medical, academic, emotional—and tailors replies.
- ✅ **Professional & Calm Tone**: Maintains respect, clarity, and professionalism in every response.

---

## 🏗️ Architecture Overview

### Tags Used:

#### 1. `Agent Instruction`
Defines the personality and behavior of AEVI.  
**Prompt Summary:**
- Acts like ChatGPT with an emotional and medical twist.
- Handles multiple domains (health, education, current affairs).
- Uses English and Tanglish professionally.
- Maintains empathy and professionalism.

#### 2. `Agent Response`
Handles the actual response generation based on user input.  
**Prompt Summary:**
- Understand the context (medical, study, news, emotional).
- Respond in structured, informative style.
- Close with a motivational or calming message in Tanglish.

---

## 🔧 How to Clone & Set Up

Follow the steps below to set up the AEVI project on your local system:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/aevi.git
cd aevi

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate     # For Linux/macOS
venv\Scripts\activate        # For Windows

# 3. Install required dependencies

pip install -r requirements.txt

# 4. (Optional) Add your API keys in a .env file
# Example content:
# OPENAI_API_KEY=your_openai_api_key

# 5. Run your AEVI application (custom command based on your interface)
# Example if using Streamlit:
streamlit run app.py
```

## 📌 Future Enhancements

- Integration with real-time medical databases (for more accurate symptom analysis).
- Voice-based interaction with Tamil speech synthesis.
- Deployment as a mobile/web chatbot interface.
- Personalized user context and memory (for returning users).

---

## ⚠️ Disclaimer

AEVI provides general advice and support only. For critical medical conditions or emergencies, users must consult a certified medical professional. This system is not a replacement for clinical consultation.

---

## 📄 License

MIT License – feel free to use, modify, and build upon this project with proper attribution.

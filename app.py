import streamlit as st
from transformers import pipeline

# Load a better model for chatbot emotions
emotion_classifier = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    return_all_scores=True  # Better for thresholding
)

responses = {
    "joy": ["That's great! Tell me more about it! 😊", "I'm happy to hear that!"],
    "sadness": ["I'm here for you. Want to talk more about it?", "That sounds tough. I'm here to listen."],
    "anger": ["I get why you're frustrated. Do you want to vent?", "It's okay to feel this way sometimes. What happened?"],
    "fear": ["That sounds scary! Do you want to talk about it?", "I'm here to support you."],
    "surprise": ["Wow! That’s unexpected! What happened next?", "That’s surprising! Tell me more."],
    "disgust": ["That sounds unpleasant! What made you feel that way?", "I see. That must have been uncomfortable."],
    "neutral": ["I see. Can you elaborate?", "Interesting! Tell me more."],
    "excitement": ["That sounds amazing! Tell me more! 🎉", "Wow, that's thrilling! What’s next?"],
    "annoyance": ["That sounds frustrating. Do you want to talk about it?", "Ugh, I get why that would be annoying."],
    "optimism": ["That’s a great perspective! Keep going! 💪", "I love your positive attitude!"],
    "grief": ["I’m really sorry to hear that. I’m here for you. 💙", "That must be really tough. Do you want to talk about it?"],
    "amusement": ["Haha, that’s funny! 😂 Tell me more!", "That sounds entertaining! What happened next?"],
    "curiosity": ["That’s an interesting thought! What do you think about it?", "I’d love to explore this idea more with you."],
    "disappointment": ["I'm sorry things didn’t go as expected. Want to talk about it?", "That must be really frustrating. What happened?"],
    "admiration": ["That’s inspiring! You should be proud of yourself. 👏", "I admire that! How did you do it?"],
    "approval": ["That’s a great idea! I completely agree.", "I like the way you think! Keep it up!"],
    "caring": ["That’s really thoughtful of you. 💕", "You have such a kind heart. I appreciate that!"],
    "confusion": ["I see how that could be confusing. Want to clarify?", "That sounds tricky! What’s making it unclear?"],
    "desire": ["That sounds exciting! I hope you get it. ✨", "That’s a great goal! How are you planning to achieve it?"],
    "disapproval": ["I see why that might not sit well with you.", "That doesn’t sound ideal. What do you think should be done?"],
    "embarrassment": ["I get it, that can be awkward! It happens to all of us.", "That must have been uncomfortable. Want to talk about it?"],
    "gratitude": ["You're very welcome! 😊", "That’s really kind of you to say. I appreciate it!"],
    "love": ["That’s so sweet! 💖", "Love is a beautiful thing! Tell me more!"],
    "nervousness": ["It’s okay to feel nervous. You’ve got this! 💪", "Deep breaths! What’s making you feel this way?"],
    "pride": ["You should be proud of yourself! 🎉", "That’s an amazing achievement! Congratulations!"],
    "realization": ["Oh, that’s an interesting insight! What does it mean for you?", "That’s a great realization! What will you do next?"],
    "relief": ["I’m so glad things worked out! 😌", "That must be a huge weight off your shoulders!"],
    "remorse": ["It's okay, we all make mistakes. What matters is learning from them.", "I hear you. Do you want to talk about how to make things right?"]
}


def detect_emotion(text):
    results = emotion_classifier(text)[0]  # Get all scores
    results = sorted(results, key=lambda x: x['score'], reverse=True)  
    return results[0]['label'] if results else "neutral"

def generate_response(emotion):
    return responses.get(emotion, ["I'm not sure how to respond to that."])[0]

# Streamlit UI
st.set_page_config(page_title="🧠 Emotion-Aware AI Chatbot", page_icon="🤖")
st.markdown("<h1 style='text-align: center;'>🧠 Emotion-Aware AI Chatbot</h1>", unsafe_allow_html=True)

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:")

if user_input:
    emotion = detect_emotion(user_input)
    response = generate_response(emotion)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Emotion", emotion))
    st.session_state.chat.append(("AI", response))

# Display chat
for speaker, msg in st.session_state.chat:
    if speaker == "You":
        st.markdown(f"**You:** {msg}")
    elif speaker == "Emotion":
        st.markdown(f"<div style='color:gray; font-size:12px;'>🧠 Detected Emotion: <b>{msg}</b></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"**AI:** {msg}")

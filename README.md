# Emotion-Aware AI Chatbot 🤖🧠
You can test the application deployed on hugging face space using the following link :

## https://huggingface.co/spaces/nikhiljycn/Emotion_Aware_Chatbot

Welcome to the **Emotion-Aware AI Chatbot**, a web application designed to detect emotions from user input and generate empathetic, emotion-specific responses. This project utilizes the power of **Transformers** for emotion classification and integrates it with **Streamlit** for creating a smooth user interface.

---

## Features

- **Emotion Detection**: The chatbot can detect a wide range of emotions from user input, including joy, sadness, anger, fear, and more.
- **Emotion-Specific Responses**: Based on the detected emotion, the AI generates a personalized response to improve engagement and create a more empathetic experience.
- **Interactive Chat**: Users can chat with the bot in real-time, and the chatbot will detect the emotion and respond accordingly.
  
---

## Model Selection and Justification

### **Model Used:**
The model used for emotion classification in this application is `SamLowe/roberta-base-go_emotions`. This model is a fine-tuned version of **RoBERTa** (Robustly Optimized BERT Pretraining Approach) for emotion recognition tasks. Specifically, the `go_emotions` dataset was used to fine-tune RoBERTa on 27 different emotion labels, making it capable of identifying subtle emotions like **grief**, **joy**, **disgust**, **fear**, **optimism**, **nervousness**, and others. 

### **Why this Model?**
- **Pretrained and Specialized**: This model is already trained on a robust emotion dataset and provides a good balance between general language understanding and fine-grained emotion classification.
- **State-of-the-art performance**: RoBERTa is one of the best models for natural language processing tasks. The model provides excellent results for emotion classification, which is essential to deliver appropriate responses based on the user's emotional state.
- **Efficient Use of Resources**: By leveraging a pre-trained model, the application minimizes the time spent on model training and hyperparameter tuning, allowing the focus to remain on real-time application and deployment.

---

## Key Components

### 1. **Emotion Detection**

The `transformers` library is used to load the emotion classifier pipeline with the `SamLowe/roberta-base-go_emotions` model. 

The function `detect_emotion(text)` passes the user input to the model, which returns a list of emotion labels along with their corresponding confidence scores. The emotion with the highest score is chosen as the detected emotion for that text. 

```python
emotion_classifier = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    return_all_scores=True  # For thresholding and better control over the prediction
)
```
### 2. Emotion-Specific Responses
A dictionary of predefined responses is created for each emotion detected by the chatbot. For example, if the model detects joy, the bot will respond with phrases like:

"That's great! Tell me more about it! 😊"

"I'm happy to hear that!"

The generate_response(emotion) function maps the detected emotion to a corresponding response from the dictionary.

```python
responses = {
    "joy": ["That's great! Tell me more about it! 😊", "I'm happy to hear that!"],
    "sadness": ["I'm here for you. Want to talk more about it?", "That sounds tough. I'm here to listen."],
    # Additional responses for other emotions
}
```

3. Streamlit User Interface
The application uses Streamlit to create an interactive chat interface where users can type their messages, and the bot will respond based on the emotion detected in the user's message. The chat history is stored in st.session_state to maintain the conversation flow.

```python
if "chat" not in st.session_state:
    st.session_state.chat = []
```

The chat history is displayed in the interface, including the detected emotion, so users can better understand the emotion that the chatbot is responding to.

```python
or speaker, msg in st.session_state.chat:
    if speaker == "You":
        st.markdown(f"**You:** {msg}")
    elif speaker == "Emotion":
        st.markdown(f"<div style='color:gray; font-size:12px;'>🧠 Detected Emotion: <b>{msg}</b></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"**AI:** {msg}")
```

Every time the user enters a message in the input box, the chatbot analyzes the input for emotions, selects the corresponding response, and updates the chat history. This makes the interaction dynamic and engaging.

```python
user_input = st.text_input("You:")

if user_input:
    emotion = detect_emotion(user_input)
    response = generate_response(emotion)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Emotion", emotion))
    st.session_state.chat.append(("AI", response))
```

This ensures that each interaction feels natural, with the chatbot understanding the emotional context and responding accordingly.

Installation
To run this project locally, you need to have Python and Streamlit installed.

#1 . Clone the repository:
 git clone https://github.com/yourusername/emotion-aware-chatbot.git

   cd emotion-aware-chatbot

#2. Install required dependencies:
 pip install -r requirements.txt

#3. Run the Streamlit app:
 streamlit run app.py

#4. Open the application in your web browser and interact with the Emotion-Aware AI Chatbot!


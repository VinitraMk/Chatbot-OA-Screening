import gradio as gd
import difflib

QA_DATASET = {
    "What is Thoughtful AI?": "Thoughtful AI is an initiative focused on building responsible and human-aligned artificial intelligence.",
    "What makes Thoughtful AI unique?": "Thoughtful AI emphasizes ethical development, explainability, and alignment with long-term human goals.",
    "Who founded Thoughtful AI?": "Thoughtful AI was founded by a group of interdisciplinary researchers passionate about safe and beneficial AI.",
    "What are the core values of Thoughtful AI?": "Transparency, collaboration, safety, and long-term impact are the core values of Thoughtful AI.",
}

def get_answer(message, threshold = 0.7):
    questions = list(QA_DATASET.keys())
    questions = [qstn.lower() for qstn in questions]
    closest_match = difflib.get_close_matches(message.lower(), questions, n=1, cutoff=threshold)
    #print(message, closest_match)
    if closest_match:
        for i,k in enumerate(questions):
            if k == closest_match[0]:
                qkey = list(QA_DATASET.keys())[i]
                qanswer = QA_DATASET[qkey]
                return qanswer
            else:
                None
    else:
        return None

def converse_with_chatbot_agent(message, message_history):
    answer = get_answer(message)
    if answer:
        return answer
    else:
        return "I'm not sure I understand the question. Could you rephrase or ask something else about Thoughtful AI"
    

#Chat interface
gd.ChatInterface(
    fn = converse_with_chatbot_agent,
    title = "Thought AI Assistant",
    description = "Ask me anything about chat AI"
).launch()




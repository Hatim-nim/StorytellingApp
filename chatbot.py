from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template= """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="llama3") # specifying the model to use
prompt= ChatPromptTemplate.from_template(template)
chain=prompt | model # the prompt here have the question and context inside it
# then it will be passed to the model to be invoked immeaadiatly 

def handle_conversation():
    context=""
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower()== "exit":
            break

        result=chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context+= f"\nUser: {user_input}\nAI: {result}"

if __name__== "__main__":
    handle_conversation()
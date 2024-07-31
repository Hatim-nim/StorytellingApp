import time
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
        start_time = time.time()  # Start the timer
        result=chain.invoke({"context": context, "question": user_input})
        end_time = time.time()  # End the timer

        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Bot: {result}")
        print(f"Time taken: {elapsed_time:.2f} seconds")  # Display time taken

        context += f"\nUser: {user_input}\nAI: {result}"

if __name__== "__main__":
    handle_conversation()
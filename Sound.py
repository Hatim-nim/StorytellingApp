import time
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Setup the conversation template
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the ElevenLabs and Ollama3 clients
elevenlabs_client = ElevenLabs(api_key="api_key")
ollama_model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | ollama_model

def handle_conversation():
    context = ""
    print("Welcome to the AI Storytelling App! Type 'exit' to end the session.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        start_time = time.time()
        result = chain.invoke({"context": context, "question": user_input})
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Bot: {result}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        
        context += f"\nUser: {user_input}\nAI: {result}"
        
        # Convert AI's text response to speech using ElevenLabs
        audio = elevenlabs_client.generate(
            text=result,
            voice="Rachel",
            model="eleven_multilingual_v2"
        )

        # Play the generated audio
        play(audio)

if __name__ == "__main__":
    handle_conversation()

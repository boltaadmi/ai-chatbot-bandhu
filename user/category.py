import openai
import os

token = os.environ.get("OPENAI_API_KEY")


# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. Divide each classify in finance or academic or abuse or mate problem"}
]

def start_conversation(user_input):
    global conversation_history
    
    conversation_history.append({"role": "user", "content": user_input})

    # Send the conversation to OpenAI API
    res = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.1,
        max_tokens=100
    )

    assistant_response = res.choices[0].message["content"]
    print(f"ChatGPT: {assistant_response}")

    conversation_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response

start_conversation("")



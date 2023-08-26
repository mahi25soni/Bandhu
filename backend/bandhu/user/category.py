import openai
import os

token = os.environ.get("OPENAI_API_KEY")


# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. Divide each classify in finance or academic or abuse or mate problem"}
]

def start_conversation(user_input):
    global conversation_history
    
    # Save the user's input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Send the conversation to OpenAI API
    res = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.1,
        max_tokens=100
    )

    # Extract the assistant's reply from the API response
    assistant_response = res.choices[0].message["content"]
    print(f"ChatGPT: {assistant_response}")

    # Save the assistant's reply to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response

# Initialize the conversation with the system message
start_conversation("")

# To continue the conversation externally, call start_conversation(user_input)
# Example: start_conversation("Me and my roomate fight a lot")

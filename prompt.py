from ollama import Client

# 1. Initialize the Ollama client
client = Client(host="http://localhost:11434")

# 2. Get the question from the user
question = input("User: ")

# 3. Generate a response using Qwen 3.5
completion = client.chat(
    model="qwen3.5:0.8b",
    messages=[
        {
            "role": "system",
            "content": (
                "Keep each sentence simple, clear, and informative. "
                "Do not use bullet points or numbering. "
            )
        },
        {
            "role": "user",
            "content": question
        }
    ],
    think=False,
    options={
        "temperature": 2,
    }
)

# 4. Extract the AI response
answer = completion.message.content.strip()

# 5. Display the response
print("\nAI:", answer)
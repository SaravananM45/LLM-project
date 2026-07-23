from groq import Groq

# Enter your Groq API Key
client = Groq(api_key="YOUR_GROQ_API_KEY")

company_name = "Nukuri"

while True:
    question = input("Ask about the company: ")

    if question.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"You are an AI assistant for {company_name}. Answer customer questions professionally."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nAnswer:")
    print(response.choices[0].message.content)
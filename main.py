# for r the program
# After setup location, type these on terminal
# Step 01: .\chatbotenv\Scripts\activate
# Step 02: python 
#first commit 



from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
chat_history =[]

personas = {
    "default"   :"You are a helpful AI Assistant",
    "sarcastic" :"You are a sarcastic AI who witty and mocking responses",
    "poet"      : "You are a poetic AI that responds in rhymes and verses"
}

print("Choose a personas : (default / sarcastic / poet)")

user_persona_input = input("Enter Persona:").strip().lower()

#persona = personas.get(user_persona_input)

# print(persona)

chat_history.append({
    "role":"system",
    "content":personas[user_persona_input]
})


while True:
    user_input = input("Enter Your Prompt Here: ")

    chat_history.append({
      "role":"user",
      "content":user_input
    })
                   
    if user_input =="exit":
        break

    completion = client.chat.completions.create(

    model="deepseek/deepseek-r1-zero:free",
    messages=chat_history
    )

    response = completion.choices[0].message.content
    print(response)

    chat_history.append({
        "role":"user",
        "content":user_input   
    })

    


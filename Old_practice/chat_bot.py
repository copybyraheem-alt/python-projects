import requests
from config import API_KEY

api_key= API_KEY
url="https://api.groq.com/openai/v1/chat/completions"
headers={"Authorization": f"Bearer {api_key}"}
messages = [{"role": "system", "content": "You are my math tutor"}]

def ask_ai(messages_list):
    payload={"model": "openai/gpt-oss-20b",
             "messages": messages_list}
    response=requests.post(url, headers=headers, json=payload)
    if response.status_code== 200:
        data= response.json()
        reply=data["choices"][0]["message"]["content"]
        return reply
    else:
        print(f"API error {response.status_code}: {response.text}")
        return None


while True:
    user_input=input("You: ").strip()

    if user_input.lower()=="quit":
        print("see you again my friend")
        break

    elif user_input=="":
        print("please type a message")
        continue
    messages.append({"role": "user", "content": user_input})


    ai_reply= ask_ai(messages)
    if ai_reply is not None:
        print(f"AI: {ai_reply}")
        messages.append({"role":"assistant", "content": ai_reply})




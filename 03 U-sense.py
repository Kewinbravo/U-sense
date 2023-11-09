from doctest import Example
import openai
import gradio as gr

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a expert that specializes in General knwoledge,weather forecast,current affairs,news and predicting"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "U-sense")

demo.launch(share=True)



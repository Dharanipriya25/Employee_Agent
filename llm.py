import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

os.environ["GOOGLE_API_KEY"] = "AIzaSyAsVP5AYO9XedGKevazUOoe0TZOER80OHU"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt = ChatPromptTemplate.from_template(
    "Explain {input} in plain text without markdown formatting."
)

chain = prompt | llm

response = chain.invoke({
    "input": "difference between narrow AI and general AI"
})

print(response.content)
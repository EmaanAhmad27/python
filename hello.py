from langchain_google_genai import GoogleGenerativeAI

# llm = GoogleGenerativeAI (model = "gemini-1.5-flash", google_api_key = GoogleApIKey)
# result = llm.invoke("what is the capital of Pakistan?")
# print (result)
# question = llm.invoke("what is seo?")
# print(question)

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
import os
load_dotenv()
llm = GoogleGenerativeAI (model = "gemini-1.5-flash", api_key= os.getenv("GoogleAPIKey"))
# result = llm1.invoke("What is programming")
# print (result)
# prompt1 = PromptTemplate(template= "Translate into urdu: {text}", input_variables= ["text"])
# prompt2 = PromptTemplate(template= "Give the menaing of this: {text}", input_variables= ["text"])
# chain1 = prompt1 | llm1
# chain2 = prompt2 | llm1
# chains = RunnableSequence (chain1, chain2)
# result = chains.invoke("What are you doing?")
# print (result)
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory, ConversationSummaryMemory, ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
# memory1 = ConversationBufferMemory()
# memory2 = ConversationBufferWindowMemory(k=2) 
# memory3 = ConversationSummaryMemory(llm = llm)
# memory4 = ConversationSummaryBufferMemory(llm=llm, max_token_limit = 1000)
# memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=1000)
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=1000)

chain = ConversationChain(llm=llm, memory=memory)

while True: 
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = chain.invoke(user_input)
    print("Final==>>",response)





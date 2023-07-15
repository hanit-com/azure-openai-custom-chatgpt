import os
import openai
from dotenv import load_dotenv
from vector_store_utils import create_vector_store, get_retriever
from chain_utils import run_conversational_chain


def setup_environment():
    load_dotenv()
    openai.api_type = "azure"
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    openai.api_base = os.getenv("OPENAI_API_BASE")
    openai.api_key = os.getenv("OPENAI_API_KEY")


setup_environment()
""" comment after running once """
# create_vector_store()
retriever = get_retriever()
chat_history = []

while True:
  prompt = input("Prompt: ")

  if prompt == "exit":
    break

  completion = run_conversational_chain(prompt, chat_history, retriever)

  print(completion)

  chat_history.append({"message": prompt, "type": "human"})
  chat_history.append({"message": completion, "type": "bot"})
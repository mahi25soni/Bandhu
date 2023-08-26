# backend.py
from gpt_index import GPTSimpleVectorIndex, LLMPredictor, PromptHelper, SimpleDirectoryReader
from langchain.chat_models import ChatOpenAI
import os
token = os.environ.get("OPENAI_API_KEY")

def construct_index(directory_path):
    max_input_size = 1500
    num_outputs = 100
    max_chunk_overlap = 20
    chunk_size_limit = 500

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index

def create_chatbot():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    return index

def get_answer(chatbot, input_text):
    response = chatbot.query(input_text, response_mode="compact")
    return response.response

# Construct the index and create the chatbot once when the backend is started
index = construct_index("docs/")
chatbot = create_chatbot()

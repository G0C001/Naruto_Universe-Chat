import os
import pickle
from IPython.display import display,Markdown
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# OPENAI_API_TOKEN = "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"
# os.environ["OPENAI_API_KEY"] = OPENAI_API_TOKEN

class QueryEngine:
    def __init__(self, index_file):
        self.index_file = index_file
        self.loaded_index = None

    def load_index(self):
        with open(self.index_file, 'rb') as f:
            self.loaded_index = pickle.load(f)

    def query(self, query):
        if self.loaded_index is None:
            self.load_index()
        query_engine = self.loaded_index.as_query_engine()
        response = query_engine.query(query)
        return response.response




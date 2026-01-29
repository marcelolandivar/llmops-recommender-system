from langchain_classic.chains import RetrievalQA # RetrievalQA chain for question answering with retrieval
from langchain_groq import ChatGroq
from src.prompt_template import get_prompt


class Recommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0) # Temperature is used to control randomness and creativity of the model's responses.
        self.prompt = get_prompt()
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff", #stuff: A simple chain type that stuffs all documents into the prompt. Other options include 'map_reduce' and 'refine'.
            retriever=retriever, # The retriever is responsible for fetching relevant documents from the vector store based on the user's query.
            return_source_documents=True, # Whether to return the source documents along with the answer.
            chain_type_kwargs={"prompt": self.prompt},
        )
    
    def get_recommendations(self, query: str):
        """Get anime recommendations based on the user's question."""
        result = self.qa_chain({"query": query})
        return result['result']
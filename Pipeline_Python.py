from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_qdrant import FastEmbedSparse, RetrievalMode
from langchain.chains.combine_documents import create_stuff_documents_chain

class RAGPipelineSetup:
    def __init__(self, qdrant_url, qdrant_api_key, qdrant_collection_name, huggingface_api_key, embeddings_model_name, groq_api_key):
        self.QDRANT_URL = qdrant_url
        self.QDRANT_API_KEY = qdrant_api_key
        self.QDRANT_COLLECTION_NAME = qdrant_collection_name
        self.HUGGINGFACE_API_KEY = huggingface_api_key
        self.EMBEDDINGS_MODEL_NAME = embeddings_model_name
        self.GROQ_API_KEY = groq_api_key
        self.embeddings = self.load_embeddings()
        self.retriever = self.load_retriever()
        self.pipe = self.load_model_pipeline()
        self.prompt = self.load_prompt_template()
        self.rag_pipeline = self.load_rag_pipeline(self.pipe, self.retriever, self.prompt)

    def load_embeddings(self):
        # Load HuggingFace embeddings
        bge_embeddings = HuggingFaceInferenceAPIEmbeddings(
            model_name=self.EMBEDDINGS_MODEL_NAME,
            api_key=self.HUGGINGFACE_API_KEY,
        )
        return bge_embeddings

    def load_retriever(self):
        # Initialize Qdrant client
        client = QdrantClient(
            url=self.QDRANT_URL,
            api_key=self.QDRANT_API_KEY,
            prefer_grpc=False
        )

        # Load sparse embedding (for hybrid retrieval)
        sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

        # Create vector store for retrieval
        db = QdrantVectorStore(
            client=client,
            embedding=self.embeddings,
            sparse_embedding=sparse_embeddings,
            sparse_vector_name="sparse_vector",
            collection_name=self.QDRANT_COLLECTION_NAME,
            retrieval_mode=RetrievalMode.HYBRID
        )

        # Configure retriever for maximum 5 results with MMR search
        retriever = db.as_retriever(search_kwargs={"k": 5}, search_type="mmr")
        return retriever

    def load_model_pipeline(self, max_new_tokens=1024):
        # Load model from Groq API (as per the provided API key)
        llm = ChatGroq(
            temperature=0,
            groq_api_key=self.GROQ_API_KEY,
            model_name="llama3-70b-8192"
        )
        return llm

    def load_prompt_template(self):
        # Prompt structure for assistant
        query_template = '''
        ### Context: 
        {context}

        ### User Question: 
        {input}

        ### Instructions for the Assistant:
        1. Carefully read the user's question and analyze the intent.
        2. Search the context provided above for the most accurate and relevant information.
        3. Formulate a clear and concise response to address the user's question.
        4. If the answer cannot be derived directly from the context, politely inform the user and suggest an alternative.

        ### Response:
        '''
        
        prompt = PromptTemplate(template=query_template, input_variables=["context", "input"])
        return prompt

    def load_rag_pipeline(self, llm, retriever, prompt):
        # Create a Retrieval Augmented Generation chain
        rag_chain = create_retrieval_chain(
            retriever=retriever,
            combine_docs_chain=create_stuff_documents_chain(llm, prompt)
        )
        
        return rag_chain

    def rag(self, question):
        # Prepare inputs for the pipeline
        inputs = {
            "input": question
        }
        
        # Execute the pipeline with the user question
        response = self.rag_pipeline.invoke(inputs)
        return response

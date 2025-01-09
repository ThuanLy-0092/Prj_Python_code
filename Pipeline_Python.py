from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_qdrant import FastEmbedSparse, RetrievalMode
from langchain.chains.combine_documents import create_stuff_documents_chain

class RAGPipelineSetup:
    def __init__(self, qdrant_url, qdrant_api_key, huggingface_api_key, embeddings_model_name, groq_api_key):
        self.QDRANT_URL = qdrant_url
        self.QDRANT_API_KEY = qdrant_api_key
        self.HUGGINGFACE_API_KEY = huggingface_api_key
        self.EMBEDDINGS_MODEL_NAME = embeddings_model_name
        self.GROQ_API_KEY = groq_api_key
        self.embeddings = self.load_embeddings()
        self.pipe = self.load_model_pipeline()
        self.prompt = self.load_prompt_template()
        self.current_source = None  # Khởi tạo source hiện tại là None

    def load_embeddings(self):
        # Load HuggingFace embeddings
        bge_embeddings = HuggingFaceInferenceAPIEmbeddings(
            model_name=self.EMBEDDINGS_MODEL_NAME,
            api_key=self.HUGGINGFACE_API_KEY,
        )
        return bge_embeddings

    def load_retriever(self, retriever_name):
        # Khởi tạo Qdrant client
        client = QdrantClient(
            url=self.QDRANT_URL,
            api_key=self.QDRANT_API_KEY,
            prefer_grpc=False
        )

        # Load sparse embedding (cho tìm kiếm kết hợp)
        sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

        # Tạo vector store cho truy vấn
        db = QdrantVectorStore(
            client=client,
            embedding=self.embeddings,
            sparse_embedding=sparse_embeddings,
            sparse_vector_name="sparse_vector",
            collection_name=retriever_name,  # Sử dụng retriever_name (source) làm collection name
            retrieval_mode=RetrievalMode.HYBRID
        )

        # Cấu hình retriever để lấy tối đa 5 kết quả với tìm kiếm MMR
        retriever = db.as_retriever(search_kwargs={"k": 5}, search_type="mmr")
        return retriever

    def load_model_pipeline(self, max_new_tokens=1024):
        # Load model từ API Groq (theo API key đã cung cấp)
        llm = ChatGroq(
            temperature=0,
            groq_api_key=self.GROQ_API_KEY,
            model_name="llama3-70b-8192"
        )
        return llm

    def load_prompt_template(self, source=None):
        # Cấu trúc prompt cho assistant
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
        # Tạo chuỗi Retrieval Augmented Generation
        rag_chain = create_retrieval_chain(
            retriever=retriever,
            combine_docs_chain=create_stuff_documents_chain(llm, prompt)
        )
        
        return rag_chain

    def rag(self, source):
        # Nếu source hiện tại chưa được thay đổi, trả về pipeline đã có
        if source == self.current_source:
            return self.rag_pipeline
        else:
            # Nếu source thay đổi, tái tạo lại các thành phần của pipeline
            self.retriever = self.load_retriever(retriever_name=source)  # Truyền source làm tên retriever (collection)
            self.pipe = self.load_model_pipeline()
            self.prompt = self.load_prompt_template(source)  # Tạo prompt với source
            self.rag_pipeline = self.load_rag_pipeline(llm=self.pipe, retriever=self.retriever, prompt=self.prompt)
            self.current_source = source  # Cập nhật source hiện tại
            return self.rag_pipeline

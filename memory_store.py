from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

class LongTermMemory:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        docs = [
            Document(page_content="To reset your password, click on 'Forgot Password' on the login page."),
            Document(page_content="If your internet is not working, restart the router and check cable connections."),
            Document(page_content="If the system is slow, close unused applications and restart the computer."),
            Document(page_content="Refunds are processed within 5 to 7 business days."),
            Document(page_content="For further support, contact support@company.com.")
        ]

        self.vectorstore = FAISS.from_documents(docs, self.embeddings)

    def search(self, query):
        results = self.vectorstore.similarity_search(query, k=2)
        return "\n".join([doc.page_content for doc in results])
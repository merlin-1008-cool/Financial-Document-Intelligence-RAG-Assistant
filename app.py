import streamlit as st
import sys
from pathlib import Path

# Allow Python to import modules from the src folder
SRC_DIR = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(SRC_DIR))

from rag_pipeline import RAGPipeline

# Configure the web page
st.set_page_config(
    page_title="Financial Document Intelligence",
    page_icon="🏦",
    layout="wide"
)

st.title("Financial Document Intelligence RAG Assistant")

st.write(
    "Ask questions about your financial documents. "
    "The assistant retrieves relevant passages and generates answers "
    "using the information available in those documents."
)

st.divider()


@st.cache_resource
def load_rag_pipeline():
    return RAGPipeline()


try:
    rag = load_rag_pipeline()
    st.write("Indexed document chunks:", rag.vector_store.collection.count())

    question = st.text_input(
        "Enter your question:",
        placeholder="What documents are required for a personal loan?"
    )

    if st.button("Get Answer", type="primary"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Searching documents and generating an answer..."):
                response = rag.answer_question(question)

            st.subheader("Answer")

            if response["answer"]:
                st.success(response["answer"])
            else:
                st.warning(response["message"])

            st.caption(f"Status: {response['message']}")

            if response["context"]:
                with st.expander("View Retrieved Document Passages"):
                    for index, item in enumerate(response["context"], start=1):
                        st.markdown(f"**Passage {index}**")
                        st.write(f"Page: {item['page_number']}")
                        st.write(f"Source: {item.get('source')}")
                        st.write(item["text"])
                        st.write(f"Retrieval distance: {item['distance']:.4f}")
                        st.divider()

except Exception as error:
    st.error("The application could not initialize the RAG pipeline.")
    st.code(str(error))

st.divider()

st.caption(
    "Demo application using a sample financial policy document. "
    "The sample document is fictional and does not represent an actual bank."
)

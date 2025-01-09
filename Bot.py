import streamlit as st
from dotenv import load_dotenv
import os
import logging
import time
from Pipeline_Python import RAGPipelineSetup

st.set_page_config(page_title="Python Simple RAG Bot", page_icon="logo.jpg")

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSS để ẩn các phần không mong muốn
hide_elements_css = """
<style>
/* Ẩn biểu tượng GitHub và các lớp liên quan */
.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK {
  display: none !important;
}

/* Ẩn menu chính (MainMenu) */
#MainMenu {
  visibility: hidden !important;
}

/* Ẩn footer */
footer {
  visibility: hidden !important;
}

/* Ẩn header */
header {
  visibility: hidden !important;
}
</style>
"""
st.markdown(hide_elements_css, unsafe_allow_html=True)

# Khởi tạo đối tượng RAGPipelineSetup
rag_pipeline_setup = RAGPipelineSetup(
    qdrant_url="https://9ba55ee0-09ef-4c78-8d04-72c6392c0425.us-east4-0.gcp.cloud.qdrant.io",
    qdrant_api_key="GYme2qX9Tzjdl6o-Y4i1ci23mDT_lbLBJ6LAxETpGU7FOVdeaI_T7w",
    huggingface_api_key="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",
    embeddings_model_name="BAAI/bge-m3",
    groq_api_key="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"
)

# Định nghĩa ánh xạ giữa lựa chọn cơ sở dữ liệu và tên collection
database_map = {
    "database_by_topic": "Python_simple_rag2",  # Mỗi lựa chọn sẽ ánh xạ tới tên collection phù hợp
    "database_chunksize": "Python_simple_rag"
}

# Main title
st.title("Python Simple RAG Assistant")

# Tạo selectbox trong sidebar để chọn database
with st.sidebar:
    st.header("Giới thiệu Sản phẩm")
    st.write("""
    **Python Simple RAG Bot** là một ứng dụng chatbot thông minh, kết hợp giữa việc truy xuất dữ liệu và khả năng tạo ra văn bản tự động thông qua công nghệ **Retrieval-Augmented Generation (RAG)**. 
    Chatbot này giúp người dùng tìm kiếm thông tin và giải đáp các câu hỏi nhanh chóng và hiệu quả.
    """)
    
    st.write("### Nhóm tác giả")
    st.write("""
    - **Lý Vĩnh Thuận**
    - **Nguyễn Nhựt Trường**
    - **Nguyễn Phạm Anh Văn**
    """)
    
    database_options = list(database_map.keys())  # Lấy danh sách các lựa chọn từ map
    selected_database = st.selectbox("Chọn cơ sở dữ liệu:", database_options)

# Cập nhật RAG pipeline theo lựa chọn của người dùng
selected_collection = database_map[selected_database]  # Lấy collection từ map dựa trên lựa chọn của người dùng
rag_pipeline = rag_pipeline_setup.rag(source=selected_collection)

# Hiển thị các tin nhắn từ lịch sử
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    avatar_url = 'https://github.com/ThuanLy-0092/Prj_Python/raw/main/logo.jpg' if message["role"] == "assistant" else 'https://raw.githubusercontent.com/ThuanLy-0092/Sindia_House_Price_Regression/refs/heads/main/user.png'
    with st.chat_message(message["role"], avatar=avatar_url):
        st.markdown(message["content"])

# Streamed response generator with context (chat history)
def response_generator(prompt):
    try:
        start_time = time.time()  # Start timing
        
        inputs = {"input": prompt}  # Tạo inputs với câu hỏi từ người dùng
        
        # Thực thi pipeline
        response = rag_pipeline.invoke(inputs)  # Lấy kết quả từ pipeline

        # Tính thời gian phản hồi
        end_time = time.time()  # End timing
        elapsed_time = end_time - start_time
        formatted_response = f"Thời gian phản hồi: {elapsed_time:.2f} giây\n\n{response['answer']}"  # Kết quả trả về từ pipeline
        
        logger.info(f"Response generated: {formatted_response}")
        return formatted_response
    except Exception as e:
        logger.error(f"Error in response generation: {str(e)}")
        return f"Error: {str(e)}"

# Input user question
if prompt := st.chat_input("Nhập câu hỏi của bạn:"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user", avatar='https://raw.githubusercontent.com/ThuanLy-0092/Sindia_House_Price_Regression/refs/heads/main/user.png'):
        st.markdown(prompt)

    # Display assistant's response with loading indicator
    with st.chat_message("assistant", avatar='https://github.com/ThuanLy-0092/Prj_Python/raw/main/logo.jpg'):
        with st.spinner("Đang xử lý câu hỏi của bạn..."):
            # Get formatted response
            response = response_generator(prompt)
            # Display response using st.markdown for proper formatting
            st.markdown(response)
        # Add assistant's response to history
        st.session_state.messages.append({"role": "assistant", "content": response})

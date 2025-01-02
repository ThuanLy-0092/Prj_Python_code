import streamlit as st

# Cài đặt tiêu đề và bố cục của trang
st.set_page_config(
    page_title="Trang chủ",
    layout="centered",  # Căn giữa nội dung
    page_icon="E:\DSC-A\logo.jpg"
)

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
st.markdown('<h1 class="title">Ứng Dụng WSE College Assistant</h1>', unsafe_allow_html=True)
# Sidebar với thông báo
st.sidebar.success("Chọn trang bạn muốn!!")

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

# Áp dụng CSS để điều chỉnh kích thước chữ và màu sắc
st.markdown(
    """
    <style>
    .title {
        font-size: 36px !important;
        color: #2C3E50;
    }
    .subtitle {
        font-size: 24px !important;
        color: #16A085;
    }
    .text {
        font-size: 18px;
        line-height: 1.6;
        color: #34495E;
    }
    .highlight {
        color: #E74C3C;
        font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Phần giới thiệu
st.markdown('<h2 class="subtitle">Chào mừng đến với ứng dụng Trợ Lí Làng Đại Học!</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
Ứng dụng này được thiết kế để hỗ trợ học sinh và sinh viên có nhu cầu tìm hiểu về các trường đại học, các ngành học và các thông tin liên quan khác như học phí, cơ hội việc làm, ký túc xá, và nhiều dịch vụ hữu ích khác.
Dù bạn đang chuẩn bị bước vào kỳ tuyển sinh hay đã trở thành sinh viên, ứng dụng này sẽ cung cấp cho bạn thông tin cần thiết và đưa ra các khuyến nghị dựa trên nguyện vọng của bạn.
</div>
""", unsafe_allow_html=True)

# Thêm hình ảnh hoặc logo (thay thế đường dẫn với hình ảnh của bạn)
st.image("E:\DSC-A\logo.jpg", use_column_width=True)

# Phần tính năng chính
st.markdown('<h2 class="subtitle">Các tính năng chính:</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
- <span class="highlight">Tư vấn ngành học:</span> Giới thiệu chi tiết các ngành học, bao gồm yêu cầu tuyển sinh, cơ hội việc làm sau khi tốt nghiệp, và những môn học chính.<br>
- <span class="highlight">Thông tin học phí:</span> Cung cấp thông tin về học phí của trường đại học.<br>
- <span class="highlight">Cơ hội việc làm:</span> Đánh giá cơ hội việc làm của các ngành sau khi ra trường dựa trên các lời khuyên và thông tin của các anh chị đi trước, xu hướng ngành nghề.<br>
- <span class="highlight">Ký túc xá và cơ sở vật chất:</span> Thông tin về ký túc xá và các tiện ích gần trường như căng tin, phòng gym, khu tự học...<br>
- <span class="highlight">Khuyến nghị nguyện vọng:</span> Gợi ý lựa chọn ngành học dựa trên điểm số và sở thích cá nhân của bạn.<br>
- <span class="highlight">Câu hỏi thường gặp:</span> Giải đáp các câu hỏi phổ biến từ học sinh và sinh viên.
</div>
""", unsafe_allow_html=True)

# Phần kêu gọi hành động
st.markdown('<h2 class="subtitle">Bắt đầu ngay bây giờ!</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
Hãy bắt đầu ngay bằng cách đặt câu hỏi của bạn hoặc tìm hiểu các ngành học tại các trường đại học mà bạn quan tâm.<br>
Ứng dụng của chúng tôi sẽ giúp bạn có những thông tin đầy đủ nhất để đưa ra quyết định đúng đắn về con đường học vấn và sự nghiệp tương lai.
</div>
""", unsafe_allow_html=True)

# Thêm nút bắt đầu hoặc điều hướng
if st.button("Khám phá ngay"):
    st.write("Bạn có thể bắt đầu bằng cách chọn các trường hoặc ngành học mà bạn quan tâm trong menu bên cạnh.")

# Thêm hyperlink tới Messenger phiên bản của ứng dụng
st.markdown("""
<div class="text">
Để sử dụng phiên bản trên Messenger của ứng dụng, vui lòng truy cập:
<a href="https://www.facebook.com/profile.php?id=61564356523160&mibextid=LQQJ4d" target="_blank"><strong>WSE College Assistant on Messenger</strong></a>.
</div>
""", unsafe_allow_html=True)

# Liên hệ hỗ trợ
st.markdown('<h2 class="subtitle">Liên hệ hỗ trợ</h2>', unsafe_allow_html=True)
st.markdown("""
Nếu bạn có bất kỳ câu hỏi hoặc cần hỗ trợ, hãy liên hệ với chúng tôi qua email: **usdsc91@gmail.com**.
""", unsafe_allow_html=True)

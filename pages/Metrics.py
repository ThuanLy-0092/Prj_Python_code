import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
QA1 = pd.read_csv(r"https://raw.githubusercontent.com/VinhThuan-hehe/kkk/refs/heads/main/questions_answers_with_llm_dtbchunksize_metrics.csv")
QA2 = pd.read_csv(r"https://raw.githubusercontent.com/VinhThuan-hehe/kkk/refs/heads/main/questions_answers_with_llm_dtbtopic_metrics.csv")

# Tính trung bình của các metrics cho cả hai bộ dữ liệu
average_metrics_QA1 = QA1[['Precision', 'Recall', 'F1']].mean()
average_metrics_QA2 = QA2[['Precision', 'Recall', 'F1']].mean()

# Thiết lập giao diện Streamlit
st.title('Dashboard for Metrics Evaluation')

st.header('Comparison of Average Metrics')

# Hiển thị các bảng metric trung bình cho cả hai bộ dữ liệu
col1, col2 = st.columns(2)

with col1:
    st.subheader('Average Metrics (Using Chunksize)')
    st.bar_chart(average_metrics_QA1)

with col2:
    st.subheader('Average Metrics (Using Topic)')
    st.bar_chart(average_metrics_QA2)

# Tạo biểu đồ so sánh
fig, ax = plt.subplots(figsize=(10, 6))
average_metrics_df = pd.DataFrame({
    'Metrics': ['Precision', 'Recall', 'F1'],
    'Using Chunksize': average_metrics_QA1.values,
    'Using Topic': average_metrics_QA2.values
})
average_metrics_df.set_index('Metrics').plot(kind='bar', ax=ax, color=['blue', 'orange'])

# Thiết lập tiêu đề và nhãn
ax.set_title('Comparison of Average Metrics (Precision, Recall, F1)', fontsize=16, fontweight='bold')
ax.set_ylabel('Score', fontsize=12)
ax.set_ylim(0, 1)

# Cài đặt nhãn cho các trục x và y
ax.set_xticklabels(average_metrics_df['Metrics'], fontsize=12)

# Đặt vị trí legend ngoài biểu đồ
ax.legend(title='Dataset', loc='lower left', bbox_to_anchor=(1.05, 0), frameon=False)

# Thêm số liệu chính xác trên mỗi cột
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', label_type='edge', fontsize=10, padding=3)

# Tối ưu hóa layout trước khi hiển thị
fig.tight_layout()

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)

st.header('Details of Metrics')

# Tạo các tabs để hiển thị chi tiết của từng bộ dữ liệu
tab1, tab2 = st.tabs(['Using Chunksize', 'Using Topic'])

with tab1:
    st.subheader('Details (Using Chunksize)')
    st.dataframe(QA1)

with tab2:
    st.subheader('Details (Using Topic)')
    st.dataframe(QA2)

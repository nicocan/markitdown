import streamlit as st
import os
from gui_utils import get_markitdown_instance

st.set_page_config(page_title="MarkItDown Web", layout="wide")

st.sidebar.title("Configuración")
api_key = st.sidebar.text_input("Gemini API Key", type="password")
model = st.sidebar.selectbox("Modelo", ["gemini-1.5-flash", "gemini-1.5-pro"])
enable_plugins = st.sidebar.checkbox("Activar Plugins", value=False)
enable_ocr = st.sidebar.checkbox("Activar OCR/Descripciones", value=True)

st.title("📄 MarkItDown Web")
st.markdown("Convierte tus documentos a Markdown fácilmente.")

uploaded_file = st.file_uploader("Sube un archivo", type=["pdf", "docx", "pptx", "xlsx", "jpg", "png", "mp3", "wav"])

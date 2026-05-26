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

if uploaded_file is not None:
    st.info(f"Archivo cargado: {uploaded_file.name} ({uploaded_file.size} bytes)")
    with st.spinner("Procesando archivo..."):
        try:
            # Save temp file
            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Initialize MarkItDown
            md = get_markitdown_instance(
                api_key=api_key if enable_ocr else None,
                model=model,
                enable_plugins=enable_plugins
            )

            # Convert
            result = md.convert(temp_path)

            # UI Tabs
            tab1, tab2 = st.tabs(["Vista Previa", "Código Markdown"])

            with tab1:
                st.markdown(result.text_content)

            with tab2:
                st.code(result.text_content, language="markdown")

            # Download button
            st.download_button(
                label="Descargar .md",
                data=result.text_content,
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
                mime="text/markdown"
            )

            # Cleanup
            os.remove(temp_path)

        except ValueError as ve:
            st.warning(f"Error de configuración: {ve}. ¿Has puesto la API Key?")
        except Exception as e:
            st.error(f"Error inesperado: {e}")

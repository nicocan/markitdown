# MarkItDown Streamlit GUI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a web-based GUI using Streamlit to convert documents to Markdown using MarkItDown, featuring Gemini 1.5 Flash for OCR.

**Architecture:** A standalone Streamlit script (`markitdown_gui.py`) that uses the `markitdown` library. It maintains state for configuration and handles file processing with real-time feedback.

**Tech Stack:** Python, Streamlit, MarkItDown, Google Generative AI (Gemini).

---

### Task 1: Environment & Dependency Setup

**Files:**
- Create: `packages/markitdown/src/markitdown/gui_requirements.txt`

- [ ] **Step 1: Create requirements file for GUI**

```text
streamlit
google-generativeai
python-dotenv
```

- [ ] **Step 2: Install dependencies**

Run: `pip install streamlit google-generativeai python-dotenv`
Expected: Success

- [ ] **Step 3: Commit**

```bash
git add packages/markitdown/src/markitdown/gui_requirements.txt
git commit -m "chore: add gui dependencies"
```

---

### Task 2: Core Logic Wrapper with Gemini Integration

**Files:**
- Create: `packages/markitdown/src/markitdown/gui_utils.py`

- [ ] **Step 1: Write helper for initializing MarkItDown with Gemini**

```python
import google.generativeai as genai
from markitdown import MarkItDown

def get_markitdown_instance(api_key=None, model="gemini-1.5-flash", enable_plugins=False):
    llm_client = None
    if api_key:
        genai.configure(api_key=api_key)
        llm_client = genai.GenerativeModel(model)
    
    return MarkItDown(
        llm_client=llm_client,
        llm_model=model,
        enable_plugins=enable_plugins
    )
```

- [ ] **Step 2: Commit**

```bash
git add packages/markitdown/src/markitdown/gui_utils.py
git commit -m "feat: add gui utility for markitdown initialization"
```

---

### Task 3: Base Streamlit UI Structure

**Files:**
- Create: `packages/markitdown/src/markitdown/markitdown_gui.py`

- [ ] **Step 1: Create the basic Streamlit layout (Sidebar and Header)**

```python
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
```

- [ ] **Step 2: Verify app starts**

Run: `streamlit run packages/markitdown/src/markitdown/markitdown_gui.py`
Expected: Browser opens with the UI.

- [ ] **Step 3: Commit**

```bash
git add packages/markitdown/src/markitdown/markitdown_gui.py
git commit -m "feat: initial streamlit ui structure"
```

---

### Task 4: File Processing and Preview

**Files:**
- Modify: `packages/markitdown/src/markitdown/markitdown_gui.py`

- [ ] **Step 1: Add processing logic and preview tabs**

```python
if uploaded_file is not None:
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
            
        except Exception as e:
            st.error(f"Error en la conversión: {e}")
```

- [ ] **Step 2: Test with a small PDF or text file**

Run: `streamlit run packages/markitdown/src/markitdown/markitdown_gui.py`
Action: Upload a file and verify preview appears.

- [ ] **Step 3: Commit**

```bash
git add packages/markitdown/src/markitdown/markitdown_gui.py
git commit -m "feat: add file processing and preview to gui"
```

---

### Task 5: Final Polish and Error Handling

**Files:**
- Modify: `packages/markitdown/src/markitdown/markitdown_gui.py`

- [ ] **Step 1: Add better error messages and file info**

```python
# Add at the top of processing block
st.info(f"Archivo cargado: {uploaded_file.name} ({uploaded_file.size} bytes)")

# Refine exception handling
except ValueError as ve:
    st.warning(f"Error de configuración: {ve}. ¿Has puesto la API Key?")
except Exception as e:
    st.error(f"Error inesperado: {e}")
```

- [ ] **Step 2: Final Verification**

Run: `streamlit run packages/markitdown/src/markitdown/markitdown_gui.py`
Expected: Fully functional app.

- [ ] **Step 3: Commit**

```bash
git add packages/markitdown/src/markitdown/markitdown_gui.py
git commit -m "feat: polish gui error handling and info"
```

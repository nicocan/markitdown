# Design Spec: MarkItDown Web Interface (Gemini Edition)

## Overview
A web-based interface for the MarkItDown library using **Streamlit**. It allows users to upload various document formats, preview the converted Markdown in real-time, and download the resulting file. It features a special integration with **Gemini 1.5 Flash** for OCR and image descriptions.

## Architecture & Components
- **Frontend/Backend:** Streamlit (Python-based).
- **Core Engine:** `markitdown` library.
- **AI Integration:** Google Generative AI (Gemini) for OCR and multi-modal analysis.

### UI Components
1. **Sidebar (Configuration):**
   - **AI Settings:**
     - Provider Selection (Default: Gemini).
     - Model Selection (Default: `gemini-1.5-flash`).
     - API Key input (Password masked).
   - **Conversion Options:**
     - Enable Plugins (Toggle).
     - Enable OCR/Image Descriptions (Toggle).
2. **Main Layout (Workspace):**
   - **File Uploader:** Supports PDF, DOCX, PPTX, XLSX, Images, Audio, etc.
   - **Processing Indicator:** Visual feedback (spinner) while MarkItDown is working.
   - **Preview Tabs:**
     - **Rendered:** Markdown rendered as HTML.
     - **Source:** Raw Markdown text in a code block.
3. **Actions:**
   - **Download Button:** Downloads the generated Markdown as a `.md` file.

## Data Flow
1. User configures settings in the sidebar.
2. User uploads a file.
3. The app initializes `MarkItDown` with the specified configuration (Gemini client).
4. `markitdown.convert()` is called.
5. If OCR/Descriptions are enabled, Gemini is invoked for visual elements.
6. The resulting `DocumentConverterResult` is displayed in the preview tabs.
7. User downloads the final file.

## Success Criteria
- Clean, "premium" look following the Streamlit design patterns.
- Successful conversion of at least PDF, Images, and DOCX.
- Functional OCR using Gemini 1.5 Flash.
- One-click download of the result.

## Testing Strategy
- Manual testing with sample files provided in the `markitdown/tests/test_files/` directory.
- Verify that toggling plugins/OCR correctly changes the output.
- Ensure the API Key is handled securely and not logged.

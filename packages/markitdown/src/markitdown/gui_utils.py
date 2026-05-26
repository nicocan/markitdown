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

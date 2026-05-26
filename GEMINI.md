# MarkItDown

Lightweight Python utility for converting various files to Markdown for use with LLMs and text analysis pipelines. Developed by the AutoGen Team (Microsoft).

## Project Overview

MarkItDown is designed to preserve document structure (headings, lists, tables, links) during conversion, making it ideal for LLM consumption. It supports a wide range of formats including PDF, Office (Word, Excel, PowerPoint), Images, Audio, HTML, and more.

### Architecture
- **Monorepo:** Uses a `packages/` structure:
  - `packages/markitdown`: Core package.
  - `packages/markitdown-mcp`: Model Context Protocol (MCP) server integration.
  - `packages/markitdown-ocr`: OCR plugin support using LLM Vision.
  - `packages/markitdown-sample-plugin`: Reference implementation for plugins.
- **Orchestration:** The `MarkItDown` class (in `_markitdown.py`) acts as the main entry point, delegating to specialized `DocumentConverter` implementations.
- **File Detection:** Uses `magika` for robust MIME type detection.
- **Extensibility:** Supports 3rd-party plugins via Python entry points (`markitdown.plugin`).

## Tech Stack
- **Language:** Python 3.10+
- **Build System:** [Hatch](https://hatch.pypa.io/)
- **Core Libraries:** `beautifulsoup4`, `requests`, `markdownify`, `magika`, `charset-normalizer`.
- **Optional Dependencies:** `python-pptx`, `mammoth`, `pandas`, `openpyxl`, `pdfminer.six`, `azure-ai-documentintelligence`, etc.
- **System Dependencies:** `ffmpeg` (audio), `exiftool` (metadata).

## Building and Running

### Development Environment
It is recommended to use `hatch` for managing environments and dependencies.

```bash
# Enter the package directory
cd packages/markitdown

# Run tests
hatch test

# Run type checking
hatch run types:check

# Enter a shell with all dependencies installed
hatch shell
```

### CLI Usage
```bash
markitdown path-to-file.pdf > document.md
```

### Docker
```bash
docker build -t markitdown:latest .
docker run --rm -i markitdown:latest < ~/your-file.pdf > output.md
```

## Development Conventions

### Code Structure
- **Converters:** Specialized converters are located in `packages/markitdown/src/markitdown/converters/`.
- **Base Class:** All converters should inherit from `DocumentConverter` defined in `_base_converter.py`.
- **Registration:** Converters are registered in `_markitdown.py` with specific priorities.

### Practices
- **Type Hinting:** Mandatory for all new code. Use `hatch run types:check` to verify.
- **Testing:** Add tests in `packages/markitdown/tests/` for any new converter or feature.
- **Linting:** Use `pre-commit` to ensure code quality.
  ```bash
  pre-commit run --all-files
  ```
- **Plugins:** When developing plugins, follow the pattern in `packages/markitdown-sample-plugin`.

## Security Considerations
- MarkItDown performs I/O with process privileges.
- Always sanitize inputs in untrusted environments.
- Use the narrowest possible API (e.g., `convert_local()`, `convert_stream()`) when the source is known.

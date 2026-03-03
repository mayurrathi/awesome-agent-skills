---
name: 4.1.1 Document Skills
description: Specialized scripts and logic for file manipulation. Generating professional reports or slide decks directly from text prompts.
version: 1.0.0
---

# 4.1.1 Document Skills

Use these specialized methods when the user requests the generation of professional file formats from raw text or data.

## 1. PDF Generation
- **HTML to PDF:** For structured reports, first generate a well-formatted HTML document with print-specific CSS (`@media print`), then convert it using headless browsers (e.g., Puppeteer) or specialized libraries.
- **Direct PDF Writing:** For simple text/image reports, use libraries like `pdf-lib` or `jsPDF`. Ensure typography and margins maintain a professional appearance.

## 2. DOCX Generation
- **Programmatic Assembly:** Use libraries like `docx` (Node.js) or `python-docx` (Python) to scaffold document structures.
- **Styles:** Always apply systematic Word styles (Heading 1, Normal, etc.) rather than manual formatting, so the user can easily switch themes globally.

## 3. PPTX (Slide Deck) Generation
- **Slide Architecture:** Map content to standard presentation flows: Title slide, Agenda, Content slides (Key points + graphic), Conclusion.
- **Libraries:** Use `pptxgenjs` (Node.js) or `python-pptx` (Python).
- **Automated Layouts:** Ensure bullet points are concise. Leave ample whitespace. Don't crowd slides with walls of text.

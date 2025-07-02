# ML Document Redactor

A simple Python tool to redact sensitive information from text files using Named Entity Recognition (NER) with spaCy.

This project provides a command-line tool to read a text file, identify named entities (like persons, organizations, and locations), and replace them with a [REDACTED] placeholder.

## Repository Structure

```
ml_document_redactor/
├── README.md
├── data/
│   └── sample.txt
├── main.py
├── redactor.py
├── main.py
└── .gitignore
```

## Machine Learning Components
This tool uses:
- **Named Entity Recognition (NER)**: Identifies and categorizes entities in text.
  - "John Doe visited Paris": PERSON = John Doe, LOCATION = Paris
- **spaCy**: Library for NLP in Python used to processing the text.
- **Pre-trained Model** (``en_core_web_sm``): This project uses en_core_web_sm, a pre-trained English language model provided by spaCy trained to recognize entities like people, organizations, locations, and dates. The script loads this model and uses it to find the sensitive information in the input files.

## Setup
1. Create and activate a virtual environment
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install spaCy
   ```
   pip install spacy
   ```
4. Download the spaCy language model
   ```
   python3 -m spacy download en_core_web_sm
   ```

## Usage
Run the script from your terminal:
```
python3 main.py --input-file data/sample.txt --output-file redacted_output.txt
```
- ``--input-file``: The path to the source .txt file.
- ``--output-file``: The path where the redacted text will be saved.

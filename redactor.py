import spacy

# Load the English model.
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print(
        "spaCy model 'en_core_web_sm' not found. "
        "Please run 'python -m spacy download en_core_web_sm' to install it."
    )
    exit()

def redact_text(text: str) -> str:
    """
    Identifies and redacts named entities in a given text.

    Args:
        text: The input string to be redacted.

    Returns:
        A string with named entities replaced by '[REDACTED]'.
    """
    doc = nlp(text)
    redacted_text = text

    for ent in reversed(doc.ents):
        redacted_text = (
            redacted_text[:ent.start_char] + "[REDACTED]" + redacted_text[ent.end_char:]
        )

    return redacted_text


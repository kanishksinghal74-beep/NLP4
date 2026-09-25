from collections import Counter
from typing import Any, Dict, List

import spacy
from nltk.stem import PorterStemmer
from spacy import displacy


# =========================================================
# LOAD NLP MODELS
# =========================================================

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError(
        "spaCy English model is not installed. "
        "Run: python -m spacy download en_core_web_sm"
    )

stemmer = PorterStemmer()


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_token_data(doc) -> List[Dict[str, Any]]:
    """
    Extract token-level NLP information.
    """

    tokens = []

    for token in doc:

        if token.is_space:
            continue

        morphology = str(token.morph)

        if not morphology:
            morphology = "N/A"

        tokens.append({
            "Token ID": token.i,
            "Token": token.text,
            "Lemma": token.lemma_,
            "Stem": stemmer.stem(token.text),
            "POS": token.pos_,
            "Fine-Grained Tag": token.tag_,
            "Morphology": morphology,
            "Dependency": token.dep_,
            "Head": token.head.text,
            "Head POS": token.head.pos_,
            "Stop Word": "Yes" if token.is_stop else "No",
            "Punctuation": "Yes" if token.is_punct else "No"
        })

    return tokens


# =========================================================
# NAMED ENTITY RECOGNITION
# =========================================================

def get_entities(doc) -> List[Dict[str, Any]]:
    """
    Extract named entities from the document.
    """

    entities = []

    for entity in doc.ents:

        description = spacy.explain(entity.label_)

        entities.append({
            "Entity": entity.text,
            "Type": entity.label_,
            "Description": description or entity.label_,
            "Start": entity.start_char,
            "End": entity.end_char
        })

    return entities


# =========================================================
# ENTITY RELATIONSHIPS
# =========================================================

def get_entity_relationships(doc) -> List[Dict[str, str]]:
    """
    Create a simple relationship view between entities
    occurring within the same sentence.

    This is an interpretable heuristic rather than a
    trained relation-extraction model.
    """

    relationships = []

    for sentence in doc.sents:

        sentence_entities = [
            entity
            for entity in doc.ents
            if entity.start >= sentence.start
            and entity.end <= sentence.end
        ]

        if len(sentence_entities) < 2:
            continue

        for i in range(len(sentence_entities) - 1):

            source = sentence_entities[i]
            target = sentence_entities[i + 1]

            relationships.append({
                "Source Entity": source.text,
                "Source Type": source.label_,
                "Relationship": "co-occurs in sentence",
                "Target Entity": target.text,
                "Target Type": target.label_,
                "Sentence": sentence.text
            })

    return relationships


# =========================================================
# POS DISTRIBUTION
# =========================================================

def get_pos_distribution(doc) -> Dict[str, int]:
    """
    Calculate POS tag frequency distribution.
    """

    counter = Counter(
        token.pos_
        for token in doc
        if not token.is_space
        and not token.is_punct
    )

    return dict(
        sorted(
            counter.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


# =========================================================
# DEPENDENCY INFORMATION
# =========================================================

def get_dependencies(doc) -> List[Dict[str, str]]:
    """
    Extract syntactic dependency information.
    """

    dependencies = []

    for token in doc:

        if token.is_space:
            continue

        children = ", ".join(
            child.text
            for child in token.children
        )

        meaning = spacy.explain(token.dep_)

        dependencies.append({
            "Token": token.text,
            "Dependency": token.dep_,
            "Meaning": meaning or token.dep_,
            "Head": token.head.text,
            "Head POS": token.head.pos_,
            "Children": children
        })

    return dependencies


# =========================================================
# COMPLETE ANALYSIS
# =========================================================

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Perform all NLP operations.
    """

    if not text or not text.strip():

        return {
            "error": "Please enter some text."
        }

    text = text.strip()

    doc = nlp(text)

    tokens = get_token_data(doc)
    entities = get_entities(doc)
    relationships = get_entity_relationships(doc)
    pos_distribution = get_pos_distribution(doc)
    dependencies = get_dependencies(doc)

    words = [
        token
        for token in doc
        if not token.is_space
        and not token.is_punct
    ]

    sentences = list(doc.sents)

    statistics = {
        "Characters": len(text),
        "Words": len(words),
        "Sentences": len(sentences),
        "Unique Words": len(
            set(
                token.text.lower()
                for token in words
            )
        ),
        "Named Entities": len(entities)
    }

    return {
        "text": text,
        "statistics": statistics,
        "tokens": tokens,
        "entities": entities,
        "relationships": relationships,
        "pos_distribution": pos_distribution,
        "dependencies": dependencies
    }


# =========================================================
# DEPENDENCY VISUALIZATION
# =========================================================

def dependency_visualization(text):
    doc = nlp(text)

    svg = displacy.render(
        doc,
        style="dep",
        page=False,
        jupyter=False,
        options={
            "compact": False,
            "collapse_punct": True,
            "color": "#111827",
            "bg": "#ffffff",
            "font": "Arial",
            "distance": 120,
            "offset_x": 50,
        }
    )

    # Force the SVG to use a dark, readable color.
    svg = svg.replace(
        'style="',
        'style="color: #111827 !important; ',
        1
    )

    # Also force currentColor elements inside the SVG to dark.
    svg = svg.replace(
        'currentColor',
        '#111827'
    )

    return svg
# =========================================================
# ENTITY VISUALIZATION
# =========================================================

def entity_visualization(text: str) -> str:
    """
    Generate spaCy named entity visualization.
    """

    if not text or not text.strip():

        return """
        <div style="padding:20px;">
            Please enter some text and click Analyze.
        </div>
        """

    doc = nlp(text.strip())

    html = displacy.render(
        doc,
        style="ent",
        page=False,
        jupyter=False
    )

    return html

import os

import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

from model1 import (
    analyze_text,
    dependency_visualization,
    entity_visualization
)


# =========================================================
# SAMPLE TEXT
# =========================================================

DEFAULT_TEXT = (
    "Microsoft was founded by Bill Gates and Paul Allen "
    "in Albuquerque. The company developed innovative "
    "software technologies and changed the computer industry."
)


# =========================================================
# POS DISTRIBUTION CHART
# =========================================================

def create_pos_chart(pos_distribution):

    if not pos_distribution:
        return None

    labels = list(pos_distribution.keys())
    values = list(pos_distribution.values())

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.bar(labels, values)

    ax.set_title("Part-of-Speech Distribution")
    ax.set_xlabel("Part of Speech")
    ax.set_ylabel("Frequency")

    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    return fig


# =========================================================
# MAIN ANALYSIS FUNCTION
# =========================================================

def run_analysis(text):

    result = analyze_text(text)

    if "error" in result:

        empty_df = pd.DataFrame()

        return (
            f"## ⚠️ {result['error']}",
            empty_df,
            empty_df,
            empty_df,
            None,
            empty_df,
            empty_df,
            empty_df,
            empty_df,
            entity_visualization(""),
            dependency_visualization("")
        )

    # -----------------------------------------------------
    # Statistics
    # -----------------------------------------------------

    stats = result["statistics"]

    overview = f"""
# 📊 Analysis Overview

| Metric | Value |
|---|---:|
| Characters | {stats["Characters"]} |
| Words | {stats["Words"]} |
| Sentences | {stats["Sentences"]} |
| Unique Words | {stats["Unique Words"]} |
| Named Entities | {stats["Named Entities"]} |
"""

    # -----------------------------------------------------
    # Token dataframe
    # -----------------------------------------------------

    token_df = pd.DataFrame(result["tokens"])

    # -----------------------------------------------------
    # NER dataframe
    # -----------------------------------------------------

    entity_df = pd.DataFrame(result["entities"])

    if entity_df.empty:

        entity_df = pd.DataFrame(
            columns=[
                "Entity",
                "Type",
                "Description",
                "Start",
                "End"
            ]
        )

    # -----------------------------------------------------
    # Relationship dataframe
    # -----------------------------------------------------

    relationship_df = pd.DataFrame(
        result["relationships"]
    )

    if relationship_df.empty:

        relationship_df = pd.DataFrame(
            columns=[
                "Source Entity",
                "Source Type",
                "Relationship",
                "Target Entity",
                "Target Type",
                "Sentence"
            ]
        )

    # -----------------------------------------------------
    # POS dataframe
    # -----------------------------------------------------

    pos_df = token_df[
        [
            "Token ID",
            "Token",
            "POS",
            "Fine-Grained Tag"
        ]
    ].copy()

    # -----------------------------------------------------
    # POS distribution
    # -----------------------------------------------------

    pos_distribution_df = pd.DataFrame(
        [
            {
                "POS": pos,
                "Count": count
            }
            for pos, count
            in result["pos_distribution"].items()
        ]
    )

    pos_chart = create_pos_chart(
        result["pos_distribution"]
    )

    # -----------------------------------------------------
    # Lemmatization
    # -----------------------------------------------------

    lemma_df = token_df[
        [
            "Token",
            "Lemma"
        ]
    ].copy()

    # -----------------------------------------------------
    # Stemming
    # -----------------------------------------------------

    stem_df = token_df[
        [
            "Token",
            "Stem"
        ]
    ].copy()

    # -----------------------------------------------------
    # Morphology
    # -----------------------------------------------------

    morphology_df = token_df[
        [
            "Token",
            "POS",
            "Fine-Grained Tag",
            "Morphology"
        ]
    ].copy()

    # -----------------------------------------------------
    # Dependencies
    # -----------------------------------------------------

    dependency_df = pd.DataFrame(
        result["dependencies"]
    )

    # -----------------------------------------------------
    # Visualizations
    # -----------------------------------------------------

    entity_html = entity_visualization(text)

    dependency_html = dependency_visualization(text)

    return (
        overview,
        entity_df,
        relationship_df,
        pos_df,
        pos_chart,
        pos_distribution_df,
        lemma_df,
        stem_df,
        morphology_df,
        dependency_df,
        entity_html,
        dependency_html
    )


# =========================================================
# CLEAR FUNCTION
# =========================================================

def clear_dashboard():

    return (
        "",
        "Enter text and click **Analyze Text**.",
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        None,
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        "",
        ""
    )


# =========================================================
# CUSTOM CSS
# =========================================================

CUSTOM_CSS = """

#title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 5px;
}

#subtitle {
    text-align: center;
    margin-bottom: 25px;
}

/* ===== Dependency Visualization & Table Readability ===== */

.dependency-table,
#dependency-table {
    color: #111827 !important;
}

.dependency-table table,
#dependency-table table {
    width: 100% !important;
    border-collapse: collapse !important;
    background: white !important;
    color: #111827 !important;
}

.dependency-table th,
#dependency-table th {
    background: #e5e7eb !important;
    color: #111827 !important;
    font-weight: 700 !important;
    padding: 10px !important;
    border: 1px solid #9ca3af !important;
    text-align: left !important;
}

.dependency-table td,
#dependency-table td {
    background: white !important;
    color: #111827 !important;
    padding: 10px !important;
    border: 1px solid #d1d5db !important;
}

.dependency-table tr:nth-child(even) td,
#dependency-table tr:nth-child(even) td {
    background: #f9fafb !important;
}

/* Make dependency graph labels clearly visible */
.dependency-graph text {
    fill: #111827 !important;
}

/* SVG dependency labels */
svg text {
    fill: #111827 !important;
}

svg .displacy-label {
    fill: #374151 !important;
}

"""

# =========================================================
# GRADIO APPLICATION
# =========================================================

with gr.Blocks(
    title="NLP Linguistic Analysis Dashboard"
) as demo:

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    gr.Markdown(
        "# 🧠 NLP Linguistic Analysis Dashboard",
        elem_id="title"
    )

    gr.Markdown(
        """
        **Named Entities · POS Tagging · POS Distribution ·
        Lemmatization · Stemming · Morphology · Dependencies**
        """,
        elem_id="subtitle"
    )

    # -----------------------------------------------------
    # INPUT
    # -----------------------------------------------------

    with gr.Row():

        with gr.Column(scale=4):

            text_input = gr.Textbox(
                label="Enter English Text",
                value=DEFAULT_TEXT,
                placeholder="Type or paste text here...",
                lines=8
            )

        with gr.Column(scale=1):

            gr.Markdown(
                """
### 🔎 Operations

This dashboard performs:

**1.** Named-Entity Relationship

**2.** POS Tagging

**3.** POS Distribution

**4.** Lemmatization

**5.** Stemming

**6.** Morphology

**7.** Dependency Parsing
"""

            )

    # -----------------------------------------------------
    # BUTTONS
    # -----------------------------------------------------

    with gr.Row():

        analyze_button = gr.Button(
            "🚀 Analyze Text",
            variant="primary"
        )

        clear_button = gr.Button(
            "🗑️ Clear"
        )

    # -----------------------------------------------------
    # OUTPUT TABS
    # -----------------------------------------------------

    with gr.Tabs():

        # =================================================
        # OVERVIEW
        # =================================================

        with gr.Tab("📊 Overview"):

            overview_output = gr.Markdown(
                "Enter text and click **Analyze Text**."
            )

        # =================================================
        # NER
        # =================================================

        with gr.Tab("🏷️ Named Entities"):

            gr.Markdown(
                """
### Named Entity Recognition

Entities detected by the spaCy NLP pipeline.
"""
            )

            entity_visual_output = gr.HTML()

            entity_output = gr.Dataframe(
                label="Detected Entities",
                interactive=False,
                wrap=True
            )

        # =================================================
        # ENTITY RELATIONSHIP
        # =================================================

        with gr.Tab("🔗 Entity Relationships"):

            gr.Markdown(
                """
### Named-Entity Relationship

Entities appearing in the same sentence are
shown together as an interpretable relationship
view.

**Note:** This is a co-occurrence relationship,
not a trained semantic relation-extraction model.
"""
            )

            relationship_output = gr.Dataframe(
                interactive=False,
                wrap=True
            )

        # =================================================
        # POS TAGGING
        # =================================================

        with gr.Tab("🔤 POS Tagging"):

            gr.Markdown(
                """
### Part-of-Speech Tagging

Shows the grammatical category and
fine-grained POS tag of every token.
"""
            )

            pos_output = gr.Dataframe(
                interactive=False,
                wrap=True
            )

        # =================================================
        # POS DISTRIBUTION
        # =================================================

        with gr.Tab("📈 POS Distribution"):

            gr.Markdown(
                """
### Part-of-Speech Distribution

Frequency of each POS category in the input.
"""
            )

            with gr.Row():

                with gr.Column():

                    pos_chart_output = gr.Plot(
                        label="POS Distribution"
                    )

                with gr.Column():

                    pos_distribution_output = gr.Dataframe(
                        label="POS Frequency",
                        interactive=False
                    )

        # =================================================
        # LEMMATIZATION
        # =================================================

        with gr.Tab("📚 Lemmatization"):

            gr.Markdown(
                """
### Lemmatization

Maps words to their dictionary/base forms
using linguistic information.
"""
            )

            lemma_output = gr.Dataframe(
                interactive=False,
                wrap=True
            )

        # =================================================
        # STEMMING
        # =================================================

        with gr.Tab("✂️ Stemming"):

            gr.Markdown(
                """
### Stemming

Reduces words to stems using
the Porter stemming algorithm.
"""
            )

            stem_output = gr.Dataframe(
                interactive=False,
                wrap=True
            )

        # =================================================
        # MORPHOLOGY
        # =================================================

        with gr.Tab("🧬 Morphology"):

            gr.Markdown(
                """
### Morphological Analysis

Displays grammatical features such as:

- Tense
- Number
- Person
- VerbForm
- Voice
- Degree
- Case
"""
            )

            morphology_output = gr.Dataframe(
                interactive=False,
                wrap=True
            )

        # =================================================
        # DEPENDENCIES
        # =================================================

        with gr.Tab("🌳 Dependencies"):

            gr.Markdown(
                """
### Dependency Parsing

Syntactic dependency visualization generated
using spaCy's:

`style="dep"`
"""
            )

            dependency_visual_output = gr.HTML()

            gr.Markdown(
                "### Dependency Table"
            )

            dependency_output = gr.Dataframe(
                interactive=False,
                wrap=True
            )

    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    analyze_button.click(
        fn=run_analysis,
        inputs=text_input,
        outputs=[
            overview_output,
            entity_output,
            relationship_output,
            pos_output,
            pos_chart_output,
            pos_distribution_output,
            lemma_output,
            stem_output,
            morphology_output,
            dependency_output,
            entity_visual_output,
            dependency_visual_output
        ]
    )

    # =====================================================
    # ENTER KEY
    # =====================================================

    text_input.submit(
        fn=run_analysis,
        inputs=text_input,
        outputs=[
            overview_output,
            entity_output,
            relationship_output,
            pos_output,
            pos_chart_output,
            pos_distribution_output,
            lemma_output,
            stem_output,
            morphology_output,
            dependency_output,
            entity_visual_output,
            dependency_visual_output
        ]
    )

    # =====================================================
    # CLEAR BUTTON
    # =====================================================

    clear_button.click(
        fn=lambda: (
            "",
            "Enter text and click **Analyze Text**.",
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
            None,
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
            "",
            ""
        ),
        inputs=[],
        outputs=[
            text_input,
            overview_output,
            entity_output,
            relationship_output,
            pos_output,
            pos_chart_output,
            pos_distribution_output,
            lemma_output,
            stem_output,
            morphology_output,
            dependency_output,
            entity_visual_output,
            dependency_visual_output
        ]
    )

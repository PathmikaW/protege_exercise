"""Abans Ontology Competency Question Explorer - Streamlit frontend.

Talks to the FastAPI backend (backend/main.py) over HTTP to run the
14 competency questions, or arbitrary ad-hoc SPARQL, against the
Abans ontology and display results as a table.
"""

import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="Abans Ontology Explorer",
    page_icon="🛍️",
    layout="wide",
)
# Abans' real brand color (pink/magenta from buyabans.com) and the
# reduced top padding both come from .streamlit/config.toml / here via
# a small, targeted CSS tweak - not fighting Streamlit's own component
# styling, just trimming the default block-container padding.
st.markdown(
    "<style>.block-container { padding-top: 2rem; }</style>",
    unsafe_allow_html=True,
)

NS = "http://www.abans.lk/ontology/abans.owl#"


def rows_to_dataframe(rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    return df.map(lambda v: v.replace(NS, "") if isinstance(v, str) else v)


def show_results(container, df: pd.DataFrame) -> None:
    if df.empty:
        container.info("No results.")
    else:
        container.success(f"{len(df)} result{'s' if len(df) != 1 else ''} found")
        container.dataframe(df, use_container_width=True, hide_index=True)


# --- Sidebar: connection settings + compact ontology stats ---
with st.sidebar:
    st.header("🛍️ Abans Explorer")
    backend_url = st.text_input("Backend URL", value="http://127.0.0.1:8010")

    backend_ok = False
    try:
        health = requests.get(f"{backend_url}/health", timeout=5).json()
        backend_ok = True
        st.success("Connected")
        c1, c2 = st.columns(2)
        c1.metric("Triples", health.get("triples", "—"))
        c2.metric("Individuals", health.get("individuals", "—"))
    except requests.RequestException as exc:
        st.error(f"Unreachable: {exc}")

BACKEND_URL = backend_url

# --- Main area ---
st.title("Abans Ontology - Competency Question Explorer")
st.caption("SPARQL competency questions against the Abans product ontology, via FastAPI + rdflib.")

tab_cq, tab_sparql = st.tabs(["📋 Competency Questions", "⚙️ Raw SPARQL"])

with tab_cq:
    left, right = st.columns([1, 1.4], gap="large")

    questions = {}
    if backend_ok:
        try:
            cq_resp = requests.get(f"{BACKEND_URL}/competency-questions", timeout=5)
            cq_resp.raise_for_status()
            questions = cq_resp.json()
        except requests.RequestException as exc:
            left.error(f"Could not load competency questions: {exc}")

    with left:
        if questions:
            cq_id = st.selectbox(
                "Choose a competency question",
                options=list(questions.keys()),
                format_func=lambda k: f"{k.upper()} — {questions[k]['text']}",
            )
            st.caption(f"Query type: **{questions[cq_id]['type']}**")

            run_cq = st.button("▶ Run", key="run_cq", type="primary", use_container_width=True)

            with st.expander("Show SPARQL query"):
                st.code(
                    "PREFIX abans: <http://www.abans.lk/ontology/abans.owl#>\n\n"
                    + questions[cq_id]["query"],
                    language="sparql",
                )
        else:
            run_cq = False

    with right:
        st.subheader("Results")
        if questions and run_cq:
            resp = requests.get(f"{BACKEND_URL}/competency-questions/{cq_id}/run", timeout=10)
            if resp.ok:
                show_results(right, rows_to_dataframe(resp.json()["results"]))
            else:
                right.error(f"Backend error: {resp.text}")
        elif questions:
            right.caption("Choose a question on the left and click Run.")

with tab_sparql:
    left, right = st.columns([1, 1.4], gap="large")

    with left:
        st.write("Run any SPARQL query directly. The `abans:` prefix is pre-bound.")
        default_query = (
            "SELECT ?product ?price WHERE {\n"
            "  ?product a abans:PremiumProduct .\n"
            "  ?product abans:hasPrice ?price .\n"
            "}"
        )
        query_text = st.text_area(
            "SPARQL query body (no need to include PREFIX)", value=default_query, height=220
        )
        run_sparql_clicked = st.button("▶ Run", key="run_sparql", type="primary", use_container_width=True)

    with right:
        st.subheader("Results")
        if run_sparql_clicked:
            resp = requests.post(f"{BACKEND_URL}/sparql", json={"query": query_text}, timeout=10)
            if resp.ok:
                show_results(right, rows_to_dataframe(resp.json()["results"]))
            else:
                right.error(f"Backend error: {resp.text}")
        else:
            right.caption("Write a query on the left and click Run.")

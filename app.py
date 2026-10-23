from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Grapple Escape",
    page_icon="🪝",
    layout="centered",
)

st.title("🪝 Grapple Escape")
st.caption("Swing, climb, and escape the rising lava.")

html = Path(__file__).with_name("game.html").read_text(
    encoding="utf-8"
)

components.html(html, height=900, scrolling=True)

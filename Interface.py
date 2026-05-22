# interface.py
import streamlit as st
from lexicon import VISUAL_STYLES, LIGHTING_PROFILES, MATERIAL_MODIFIERS
from engine import PromptEngine

def launch_ui():
    st.set_page_config(page_title="Dark Machinery Generator", layout="wide")
    st.title("Dark Machinery Asset Prompt Generator")
    st.write("Streamline your creative pipeline by combining structured architectural parameters.")

    engine = PromptEngine(VISUAL_STYLES, LIGHTING_PROFILES, MATERIAL_MODIFIERS)

    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input("Core Subject", "An ancient mechanical throne")
        style = st.selectbox("Visual Style Matrix", list(VISUAL_STYLES.keys()))
        lighting = st.selectbox("Lighting Profile", list(LIGHTING_PROFILES.keys()))
        materials = st.multiselect("Material Modifiers", MATERIAL_MODIFIERS, default=[MATERIAL_MODIFIERS[0]])
        intensity = st.slider("Detail Intensity Weight", 1.0, 2.0, 1.0, 0.1)

    with col2:
        st.subheader("Generated Output")
        if st.button("Synthesize Prompt"):
            result = engine.construct_prompt(subject, style, lighting, materials, intensity)
            st.text_area("Copy Ready Prompt", result, height=200)
            st.success("Prompt synthesized successfully based on architectural parameters.")

if __name__ == "__main__":
    launch_ui()

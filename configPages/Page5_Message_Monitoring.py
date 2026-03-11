import streamlit as st
import streamlit.components.v1 as components

def render(current_time, temp_interval, PAGES_URL, kakao_api_key):
    st.header(f"♿ MOVE / 운영 타임라인")
    st.markdown('##### MOVE (Mobility On-demand for Vulnerable & Elderly)')
    st.markdown('---')

    st.subheader("🔍 운영 타임라인")
    components.iframe("https://drt-scheduling.vercel.app/", height=800, scrolling=True)

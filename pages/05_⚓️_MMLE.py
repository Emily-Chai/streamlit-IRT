import streamlit as st

st.set_page_config(page_title = "length calculator")
st.sidebar.markdown("Length calculator")
st.sidebar.write(f"hello {st.session_state['user']}")


st.markdown("Length calculator")
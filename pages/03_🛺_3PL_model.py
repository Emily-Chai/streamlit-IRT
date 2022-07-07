import streamlit as st


st.set_page_config(page_title = "temperature calculator")
st.markdown("Temperature calculator")
st.sidebar.markdown("Temperature calculator")
st.sidebar.write(f"hello {st.session_state['user']}")

temp_var = st.number_input('enter celcius')

st.write(f'fahrenheit is: {temp_var*9/5+32}F')
st.write(st.session_state)
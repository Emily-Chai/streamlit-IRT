st.markdown("A bunch of calculators🖩")


user = st.text_input('enter your name')
update = st.button('update user')

if 'user' not in st.session_state:
    st.session_state['user'] = user

if update:
    st.session_state['user'] = user

    
st.sidebar.write(f"hello {st.session_state['user']}")

st.write(st.session_state)
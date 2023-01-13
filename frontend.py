import streamlit as st
import Subnet_Calculator as sc
st.title("Subnet Calculator")
st.write("Easily get the network blocks calculated by the app")

user_input=st.text_input(label= "Input the CIDR", placeholder="enter the subnet in CIDR format")
button=st.button(label="button", key="button")

if button:
    output = (sc.subnet(user_input))

    output=list(output)
    hh=f'''
    ****************************************
    The Network Block Size is **{output[2]}**
    ****************************************
    '''

    st.markdown(hh)
    st.markdown(":red[The Network Blocks are]")
    for i in output[0]:
        st.write(i)





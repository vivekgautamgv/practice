import streamlit as st
#st.image("https://static.streamlit.io/examples/cat.jpg", caption="A cat")
#title

st.title("Streamlit App")
st.write("This is a simple Streamlit app.")


#header

st.header("Header")
st.write("This is a header.")

#subheader  
st.subheader("Subheader")
st.write("This is a subheader.")

st.info("Hey brother")

st.warning("yops")

st.success("Succhhess")
st.write(range(50))


#error msg

st.error("Error")


st.markdown("**bold**")
st.markdown("### bold")

st.markdown(":moon:")

#to write caption

st.latex(r'''a^2 + b^2 = c^2''')

#widgets

st.checkbox("Login")

st.button("hi")

st.radio("Pick your gender", ["Male","female"])

#select box


st.selectbox("PIck your courses ", ["Python","Java","C++"], index=1)

#multiselect

st.multiselect("choose somethin", ["Python","Java","C++"], default=["Python"])
st.button("Submit")

#selectslider

st.select_slider("Pick a number", options=range(1, 10), value=5)

#sliderview

st.slider("Pick a number", min_value=1, max_value=10, value=5)

#bum_input

st.number_input("Enter the numbner : ",0,100,1)

#test_inout

st.text_input("Enter your name : ", "")

#sidebar

st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar.")
st.sidebar.radio("Select a Page:", ["Home", "Stock Screener", "Options Pricing", "Option Chain Analysis"])


#data

import pandas as pd
import numpy as np
st.title("DataFrame")

data = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])
st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)
st.dataframe(data, width=1000, height=500)
st.table(data)
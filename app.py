import streamlit st
import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1, 2, size = 20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)



#import streamlit as st

#x = st.slider('Select a value')
#st.write(x, 'squared is ', x * x)

#콤마는 코드를 이어지게 하기위한.

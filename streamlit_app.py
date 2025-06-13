import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# st.header('st.button')


# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')


st.header('st.write')

# Example 1
st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame({'first column': [1, 2, 3, 4]
                   , 'second column': [10, 20, 30, 40]})

st.write(df)

# Example 4
st.write('Below is a dataframe', df, 'Above is a dataframe')

# Example 5

df2 = pd.DataFrame(
    np.random.rand(200, 3),  # Use np.random.rand instead of np.random(200, 3)
    columns=['a', 'b', 'c']
)

# Create scatter plot using seaborn
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data=df2,
    x='a', y='b',
    size='c',
    hue='c',
    palette='viridis',
    sizes=(20, 200),  # Adjust point size scale
    legend='brief'
)

# plt.title("Seaborn Scatter Plot with Size and Color Encoding")
# plt.show()
st.pyplot(plt.gcf())

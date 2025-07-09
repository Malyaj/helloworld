import streamlit as st
import pandas as pd

# Example data
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C', 'B'],
  'Store': ['S1', 'S1', 'S2', 'S2', 'S1'],
    'Value': [10, 20, 15, 25, 30],
    'Status': ['Open', 'Closed', 'Open', 'Closed', 'Open']
})

# Initialize session state for filters
if 'filter_count' not in st.session_state:
    st.session_state.filter_count = 0
if 'filters' not in st.session_state:
    st.session_state.filters = []

# Add Filter Button
if st.button("➕ Add Filter"):
    st.session_state.filter_count += 1
    st.session_state.filters.append({'column': None, 'value': None})

# Show each filter block
columns = df.columns.tolist()

for i in range(st.session_state.filter_count):
    with st.expander(f"Filter #{i+1}", expanded=True):
        col = st.selectbox(
            f"Select column for Filter #{i+1}",
            columns,
            key=f'col_{i}'
        )

        if df[col].dtype == 'object':
            # Multiselect for categorical columns
            values = st.multiselect(
                f"Select values for {col}",
                options=df[col].unique().tolist(),
                key=f'val_{i}'
            )
        else:
            # Range slider for numeric columns
            min_val, max_val = int(df[col].min()), int(df[col].max())
            values = st.slider(
                f"Select range for {col}",
                min_val,
                max_val,
                (min_val, max_val),
                key=f'val_{i}'
            )

# Apply filters to DataFrame
filtered_df = df.copy()
for i in range(st.session_state.filter_count):
    col = st.session_state.get(f'col_{i}')
    val = st.session_state.get(f'val_{i}')

    if col is not None and val is not None:
        if isinstance(val, list):  # Categorical filter
            if val:
                filtered_df = filtered_df[filtered_df[col].isin(val)]
        elif isinstance(val, tuple):  # Numeric range
            filtered_df = filtered_df[filtered_df[col].between(val[0], val[1])]

# Show result
st.markdown("### 🔍 Filtered Data")
st.dataframe(filtered_df)

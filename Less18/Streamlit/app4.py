import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
st.title('Tips Pairplot')
st.sidebar.header('Features')
st.dataframe(tips)

features1 = st.sidebar.multiselect(
                                    'Select features for pairplot',
                                    options=tips.columns.tolist(),
                                    default=['total_bill', 'tip', 'sex', 'smoker']
                                )

features2 = st.sidebar.selectbox(
                                'Select features for pairplot',
                                options=tips.columns.tolist(),
                            )
if st.button('make pariplot'):
    if len(features1) >= 2:
        pairplot = sns.pairplot(tips[features1])
        st.pyplot(pairplot)
    else:
        st.warning('Please select at least two features to display the pairplot.')

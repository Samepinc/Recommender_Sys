import streamlit as st
import pickle
import pandas as pd

def recommend(product_id):
    distances = sorted(list(enumerate(similarity[product_id])), reverse=True, key=lambda x: x[1])
    recommended_product_id=[]
    for i in distances[1:6]:
        recommended_product_id.append(i[0])
    return recommended_product_id
content_dict=pickle.load(open('content_df.pkl', 'rb'))
content=pd.DataFrame(content_dict)
similarity = pickle.load(open('content_similarity.pkl', 'rb'))
st.title("Fashion Recommender System ")
selected_product_id = st.selectbox(
    "Select Product_ID Which You Like",
    (content['Product ID'].values)
)
if st.button("Recommend"):
    recommadations=recommend(selected_product_id)
    st.write("The Product_ID of the Products That Should be Recommended:")
    for i in range(5):
        st.write(str(i+1) + ". " + str(recommadations[i]))
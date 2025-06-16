import streamlit as st
import langchain_model

# Set page title and layout
st.set_page_config(page_title="🍽️ Restaurant Name Generator", layout="centered")

# Title with emoji
st.title("🍽️ Restaurant Name & Menu Generator")

# Sidebar for cuisine selection
st.sidebar.markdown("### 🧭 Select Cuisine")
cuisine = st.sidebar.selectbox("Pick a Cuisine:", ("Indian", "Chinese", "Japanese", "Italian", "Korean"))

# Main content
if cuisine:
    response = langchain_model.generate_restaurant_details(cuisine)
    print(response)
    restaurant_name = response['restaurant_name'].strip()
    menu_items = response['menu'].strip().split(',')

    # Display restaurant name
    st.markdown(f"## 🏷️ **{restaurant_name}**")

    # Display menu
    st.markdown("### 📋 **Menu**")
    for item in menu_items:
        st.markdown(f"- 🍴 {item.strip()}")

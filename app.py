import streamlit as st
import re
import pandas as pd
import google.generativeai as genai
from PIL import Image

# Function to clean the input text
def clean_text(text):
    # Remove special characters and punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove single characters
    text = re.sub(r"\b[a-zA-Z]\b", " ", text)

    # Remove HTML tags
    text = re.sub(r"<[^>]*>", " ", text)

    # Lowercase the text
    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Trim leading and trailing spaces
    text = text.strip()

    return text

# Function to get prediction from LLM API
def get_sentiment_prediction(review, api_key):
    genai.configure(api_key=api_key)

    # Clean the review
    cleaned_review = clean_text(review)

    # Create JSON format with the cleaned review for the model input
    json_data = f'[{{"clean_reviews": "{cleaned_review}", "pred_label": ""}}]'

    # Create the prompt for the LLM API
    prompt = f"""
    You are an expert linguist, who is good at classifying customer review sentiments into Positive/Negative labels.
    Help me classify customer reviews into: Positive(label=1), and Negative(label=0).
    Customer reviews are provided between three back ticks.
    In your output, only return the Json code back as output - which is provided between three backticks.
    Your task is to update predicted labels under 'pred_label' in the Json code.
    Don't make any changes to Json code format, please.

    ```
    {json_data}
    ```
    """

    # Send the prompt to the model and get the response
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)

    # Extract the predicted label from the response
    json_data = response.text.strip("`")
    df_sample = pd.read_json(json_data)
    
    # Return the predicted label
    return df_sample['pred_label'][0]

# Dictionary to store reviews and their labels
if 'reviews_data' not in st.session_state:
    st.session_state['reviews_data'] = {
        'Magic Cream Light': {'reviews': [], 'labels': []},
        'Bubble Makeup Remover': {'reviews': [], 'labels': []},
        'Glowy Skin Serum': {'reviews': [], 'labels': []}
    }

# Define the home page content (Submit Reviews)
def show_home():
    st.title("Skincare Products - Leave a Review")

    # Load and resize images
    image_paths = ['images/product1.jpg', 'images/product2.jpg', 'images/product3.jpg']
    images = [Image.open(img_path).resize((200, 300)) for img_path in image_paths]

    # Display images with titles and review inputs
    product_titles = ["Magic Cream Light", "Bubble Makeup Remover", "Glowy Skin Serum"]
    reviews = ["", "", ""]
    api_key = "YOUR_API_KEY"  # Replace with your API key

    # Layout for displaying the products side by side
    cols = st.columns(3)

    for i in range(3):
        with cols[i]:
            st.image(images[i], caption=product_titles[i], use_column_width=True)
            reviews[i] = st.text_area(f"Leave a review for {product_titles[i]}:", key=f"review_{i}")

            # Submit review
            if st.button(f"Submit Review for {product_titles[i]}", key=f"submit_{i}"):
                if reviews[i]:
                    # Append review to session state
                    st.session_state['reviews_data'][product_titles[i]]['reviews'].append(reviews[i])
                    # Perform sentiment analysis and store the result
                    label = get_sentiment_prediction(reviews[i], api_key)
                    st.session_state['reviews_data'][product_titles[i]]['labels'].append("Positive" if label == 1 else "Negative")
                    st.success(f"Your review for {product_titles[i]} has been submitted!")
                else:
                    st.warning("Please enter a review before submitting.")

# Define the dashboard page content (View Reviews with Sentiment)
def show_dashboard():
    st.title("Dashboard: Product Reviews & Sentiment Analysis")

    # Load and resize images
    image_paths = ['images/product1.jpg', 'images/product2.jpg', 'images/product3.jpg']
    images = [Image.open(img_path).resize((200, 300)) for img_path in image_paths]

    # Display products with reviews and sentiments
    product_titles = ["Magic Cream Light", "Bubble Makeup Remover", "Glowy Skin Serum"]

    cols = st.columns(3)

    for i in range(3):
        with cols[i]:
            st.image(images[i], caption=product_titles[i], use_column_width=True)
            reviews = st.session_state['reviews_data'][product_titles[i]]['reviews']
            labels = st.session_state['reviews_data'][product_titles[i]]['labels']

            # Display reviews with their corresponding sentiment
            st.write(f"### Reviews for {product_titles[i]}:")
            if reviews:
                for review, label in zip(reviews, labels):
                    # Add color to the sentiment label
                    color = "green" if label == "Positive" else "red"
                    st.markdown(f"<p>{review} - <span style='color:{color}; font-weight:bold;'>{label}</span></p>", unsafe_allow_html=True)
            else:
                st.write("No reviews submitted yet.")

# Main app with navigation
def main():
    # Sidebar navbar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Dashboard"])

    # Navigation logic
    if page == "Home":
        show_home()
    elif page == "Dashboard":
        show_dashboard()

# Run the main app
if __name__ == '__main__':
    main()

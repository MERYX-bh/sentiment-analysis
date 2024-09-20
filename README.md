
# Skincare Product Reviews and Sentiment Analysis

This project is a web application built with Streamlit that allows users to leave reviews for skincare products and provides sentiment analysis on these reviews using an API. The application uses Google Generative AI for sentiment prediction and classifies the reviews as either "Positive" or "Negative".

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- Users can submit reviews for three skincare products: Magic Cream Light, Bubble Makeup Remover, and Glowy Skin Serum.
- Real-time sentiment analysis of submitted reviews is performed using Google Generative AI, classifying reviews as "Positive" or "Negative".
- A dashboard displaying the reviews with their corresponding sentiment.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/skincare-reviews.git
```

2. Navigate to the project directory:

```bash
cd skincare-reviews
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Replace the placeholder API key in the code with your actual Google Generative AI API key.

```python
api_key = "your-api-key-here"
```

5. Run the Streamlit application:

```bash
streamlit run app.py
```

## Usage

1. Navigate to the Home page.
2. Leave a review for one of the available skincare products.
3. Submit the review and the sentiment analysis will be displayed.
4. Switch to the Dashboard to view all submitted reviews along with their sentiment classification.

## Screenshots

### Submit a Review
![Submit Review](https://github.com/MERYX-bh/sentiment-analysis/blob/main/proejt2.png)

### Sentiment Analysis Dashboard
![Sentiment Analysis Dashboard](https://github.com/MERYX-bh/sentiment-analysis/blob/main/projet1.png)

## Technologies Used

- **Streamlit**: Framework for building web applications.
- **Google Generative AI**: API for sentiment analysis of customer reviews.
- **Pandas**: Data manipulation and analysis library.
- **PIL (Pillow)**: Python Imaging Library for image manipulation.
- **Regular Expressions**: For text cleaning.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

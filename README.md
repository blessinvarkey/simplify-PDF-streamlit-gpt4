# Learning Made Easy: Simplifying Educational PDF Content using GPT4

The Learning Made Easy is a Streamlit application designed to simplify educational content for students. Using the power of OpenAI's GPT models, this app takes a chapter or any educational text uploaded in the form of a PDF and provides a simplified version of the content, making learning accessible and more manageable.

## Features

- **PDF Upload**: Users can upload educational material in PDF format.
- **Content Simplification**: Leverages OpenAI's GPT models to simplify the uploaded content into easy-to-understand language.
- **Educational Focus**: Tailored to enhance the learning experience by breaking down complex topics.

## How It Works

1. **PDF Processing**: The app reads the uploaded PDF and extracts its text.
2. **Text Simplification**: The extracted text is then processed by OpenAI's GPT models, which have been instructed to simplify the content and highlight chapter details.

## Setup and Installation

### Prerequisites

- Python 3.6+
- Streamlit
- PyMuPDF (fitz)
- OpenAI Python SDK

### Installation Steps

### 1. Clone the Repository
```git clone https://github.com/blessinvarkey/pdfreader-education-gpt4.git```

### 2. Install Dependencies

Install the required Python packages:
```pip install -r requirements.txt```

### 3. Set Up OpenAI API Key

Get your API key from [OpenAI](https://openai.com/) and set it as an environment variable.

### 4. Run your file
```streamlit run app.py```


## Usage
Upon launching the app, you'll be presented with an interface to upload a PDF file.
- Select a PDF file containing educational material you wish to simplify.
- Click on "Simplify Content" to process the uploaded file.
- The app will display a simplified version of the content, focusing on making it more understandable.

## Security Note
Please ensure that your OpenAI API key is kept secure and not exposed in the source code. It's recommended to use environment variables or secure vaults for API keys. 

## Contributions
Contributions to improve the repo are welcome.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



# J.A.R.V.I.S - Just A Rather Very Intelligent System

J.A.R.V.I.S is a Streamlit-based chatbot application powered by Google's Gemini multi-modal AI language models. It allows users to interact with the AI in various modes including chat, image captioning, text embedding, and Q&A.

## Features

- **ChatBot:** Engage in conversation with the AI, powered by Gemini's conversational model.
- **Image Captioning:** Upload an image and let the AI generate a caption for it.
- **Embed Text:** Get embeddings for textual input using Gemini's embedding model.
- **Ask me anything:** Ask questions and get responses from the AI model.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

2. Open the provided URL in your web browser.

3. Choose the desired mode (ChatBot, Image Captioning, Embed Text, Ask me anything) from the sidebar.

4. Interact with J.A.R.V.I.S by following the instructions in each mode.

## Configuration

1. Obtain a Google API key and update the `config.json` file with your key:

   ```json
   {
       "GOOGLE_API_KEY": "YOUR_GOOGLE_API_KEY"
   }
   ```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

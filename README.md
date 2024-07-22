# Paper Agent 
**Paper-agent** is a conversational agent designed to assist users in answering questions about academic papers , tis project leverages cutting-edge AI technologies to provide insightful and accurate responses to inquiries related to academic literature , the main components of this project include the **Llama-index 🦙** framework, `claude-3-opus` as the Large Language Model (LLM), `BAAI/bge-small-en-v1.5` as the embedding model, and a user-friendly interface created with the **👓 Mesop** framework.

## Key Features
- **Conversational Agent**: paper-agent uses `claude-3-opus` to generate natural and contextually relevant responses to user queries about academic papers.
- **Embedding Model**: The `BAAI/bge-small-en-v1.5` embedding model ensures efficient and effective retrieval of information from the indexed papers.
- **User Interface**: A simple and intuitive UI built with the `mesop` framework allows users to interact seamlessly with the agent.

## Usage

### Installation
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Data Setup
2. Move your `papers` into the `data` folder.

### Configuration
3. setup your `ANTHROPIC_API_KEY` in the `.env` file.

### Running the UI
4. Start the UI application:
   ```bash
   mesop src/app.py
   ```

**Note**: You can update the names of the embedding and LLM models in the `settings.py` file.

![Screenshot from 2024-07-23 00-29-38](https://github.com/user-attachments/assets/0951db5f-627c-4a1b-bbaa-7c8d2b4f074d)

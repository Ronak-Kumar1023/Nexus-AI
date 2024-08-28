# Nexus AI

Nexus AI is a Streamlit application that leverages the OpenAI API to create an interactive chatbot experience. The application supports chat history management, customizable chat contexts, and a user-friendly customizable theme interface with a default dark theme. 

## Features

- **Interactive Chat Interface**: Communicate with the chatbot and receive real-time responses.
- **Chat History Management**: Start new chats and manage previous conversations.
- **Default Dark Theme**: A visually appealing dark mode for improved readability.
- **Custom Themes**: Users can create their own custom theme for the application
- **Responsive Design**: Adaptable layout for various screen sizes.
- **Message Timestamping**: Automatically generated timestamps for messages.

## Technologies Used

- **Streamlit**: For creating the web application interface.
- **OpenAI API**: To handle chatbot responses and interactions.
- **Python**: The programming language used for backend logic.
- **dotenv**: For loading environment variables securely.
- **HTML/CSS**: Custom styling for the user interface.

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Ronak-Kumar1023/Nexus-AI.git 
```

2. **Set up a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install required packages:**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables: Create a .env file in the root directory and add your OpenAI API key:**

```
OPENAI_API_KEY=your_openai_api_key
```

5. **Run the Streamlit application:**

```bash
streamlit run app.py
```

## Usage
- Starting a New Chat: Click the "Start New Chat" button in the sidebar.
- Sending a Message: Type your message in the input field and press Enter.
- Viewing Chat History: Access and manage previous chats from the sidebar.
- Deleting Chats: Use the delete button next to each chat in the sidebar to remove it.

## Future Improvements
- Performance Optimization: Optimize response time and handling of large volumes of messages.
- Extended Functionality: Add support for more complex interactions and integrations.
- UI/UX Enhancements: Improve the interface design and user interactions based on feedback.





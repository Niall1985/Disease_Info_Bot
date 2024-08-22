# Disease Info Bot

**Disease Info Bot** is a Flask-based web application that provides detailed information about various diseases. The bot interacts with users via natural language queries and extracts relevant disease information, such as symptoms, treatments, complications, transmission, and prevention, from a JSON-based disease database. The program also uses  Google's generative AI (Gemini Pro) to generate additional content relevant to the query.

## Features

- **Disease Information:** Provides detailed information on diseases, including symptoms, treatments, complications, transmission, and prevention.
- **Generative AI Integration:** Utilizes Google's Gemini Pro model to generate additional content and extract disease names from user queries.
- **Interactive Chat:** Users can interact with the bot through a chat interface where they can ask questions about specific diseases.
- **Dynamic Response:** The bot responds with relevant information based on the user's query, even generating additional content if the requested information is not directly available in the database.

## Installation

### Prerequisites

- Python 3.7+
- Flask
- Google Generative AI SDK (`google-generativeai`)
- Python `dotenv` package

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/disease-info-bot.git
   cd disease-info-bot
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   - Create a `.env` file in the root directory of the project.
   - Add your Google Generative AI API key in the `.env` file:

     ```plaintext
     key=your_google_genai_api_key
     ```

5. **Add the disease database:**

   - Ensure you have a `disease_database.json` file in the root directory containing the disease data in the required format.

### Running the Application

1. **Start the Flask app:**

   ```bash
   python app.py
   ```

2. **Access the app:**

   - Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

- **Ask Questions:** Users can type queries related to disease symptoms, treatments, complications, transmission, prevention, and more.
- **Dynamic Responses:** The bot will parse the query, extract the relevant disease name, and return the requested information. If needed, additional information will be generated using the AI model.

## Example Queries

- "What are the symptoms of malaria?"
- "How is tuberculosis transmitted?"
- "What are the treatments for diabetes?"

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or bug fixes.

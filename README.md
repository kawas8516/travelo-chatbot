
# Travelo - Museum Ticketing Chatbot

Travelo is a chatbot-based ticketing system for museums. It provides a convenient way for users to book, cancel, and reschedule museum tickets, as well as get museum information such as location and amenities. The chatbot uses a Large Language Model (LLM) for dynamic responses to user queries and integrates with MongoDB for ticket management.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- **Python** (>= 3.8)
- **MongoDB** for ticket data storage. You can use a local MongoDB instance or MongoDB Atlas for a cloud-based solution.
- **Node.js** and **npm** (if using frontend frameworks that require them)

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/travelo.git
    cd travelo
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up MongoDB**:
    - Ensure MongoDB is running on your system.
    - You can use the MongoDB Compass or the MongoDB shell to create the database and collection.
    - Create a new database named `museum_ticketing_system` and a collection named `museum_info` and `ticket_info` .
    - For cloud setup, create a MongoDB Atlas account, create a database cluster, and note down the connection URI.(by deault it's localhost)

5. **Add Environment Variables**:
    - Create a `.env` file in the root directory and add the following:
      ```plaintext
      MONGODB_URI=mongodb+srv://your_mongo_uri
      DJANGO_SECRET_KEY=your_secret_key
      HUGGINGFACE_TOKEN=your_huggingface_api_token
      ```

### Tokens Required

- **Hugging Face Token**: For LLM integration, sign up for a Hugging Face account, create an API token, and add it to your `.env` file as shown above.
- **Django Secret Key**: Generate a secret key for Django (you can use a tool like `https://djecrety.ir/` to create one) and add it to `.env`.

## Running the Project

1. **Start the Django Server**:
    ```bash
    python manage.py runserver
    ```

2. **Access the Application**:
    - Open your browser and navigate to `http://localhost:8000` to view the chatbot interface.

3. **Using API Endpoints**:
    - You can access various endpoints like booking, canceling, and rescheduling tickets. Check the [API Endpoints](#api-endpoints) section for more details.

## API Endpoints

| Endpoint                    | Method | Description                          |
|-----------------------------|--------|--------------------------------------|
| `/api/chatbot_response/`    | POST   | Get a chatbot response               |
| `/api/book_ticket/`         | POST   | Book a museum ticket                 |
| `/api/cancel_ticket/`       | POST   | Cancel a booked ticket               |
| `/api/reschedule_ticket/`   | POST   | Reschedule a booked ticket           |

## Project Structure

- **bookings**: Handles booking, cancellation, and rescheduling of tickets.
- **llm_integration**: Manages LLM responses using Hugging Face and provides chatbot services.
- **travelo**: Main project configuration files and settings.

## Contributing

We welcome contributions from the community to improve Travelo! Here’s how you can get involved:

1. **Fork the Repository**: Click the "Fork" button on the repository page to create your copy.
2. **Create a New Branch**: For each feature or bug fix, create a new branch.
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make Your Changes**: Work on your changes in your branch.
4. **Run Tests**: Make sure your changes pass any tests and do not break the project.
5. **Submit a Pull Request**: Push your changes to your forked repository, then submit a pull request to the main repository.

### Potential Contributions
- **Enhancing UI/UX**: Improve the chatbot interface or add new visual features.
- **Adding New Endpoints**: Expand chatbot functionalities, such as retrieving detailed museum information or upcoming events.
- **Improving LLM Integration**: Add more advanced AI response handling or fine-tune models for specific use cases.
- **Bug Fixes and Documentation**: Identify and fix bugs, or improve project documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

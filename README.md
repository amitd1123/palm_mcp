# 🔮 Palmistry AI - Your Future in Your Hands

A powerful AI-powered palmistry service that reveals insights about your future career, relationships, and life path by analyzing your palm lines. Using advanced Gemini AI technology, this service provides personalized readings based on the ancient art of palmistry.

✨ **Get answers to questions like:**
- When will I get my first job?
- Which company will I work for?
- What will be my salary range?
- What does my love line reveal?
- What does the future hold for me?

## Features

- Accepts base64-encoded palm images
- Processes images using Google's Gemini AI model
- Provides astrological insights based on palm readings
- Saves uploaded images with timestamps for reference
- RESTful API endpoints for easy integration

## Prerequisites

- Python 3.8+
- Google API Key with access to Gemini AI
- Required Python packages (see [Installation](#installation))

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd palm_mcp
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your configuration:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   AUTH_TOKEN=your_auth_token_here
   MY_NUMBER=your_phone_number
   ```

## ✨ Try It Now!

1. **Click this link to try our WhatsApp bot**: [https://puch.ai/mcp/BZcGzgRluO](https://puch.ai/mcp/BZcGzgRluO)

2. **How to use**:
   - Send a clear photo of your palm
   - Ask your question (e.g., "When will I get my first job?")
   - Receive your personalized reading!

## 🚀 Local Development

1. Start the MCP server:
   ```bash
   python app.py
   ```
   The server will start on `http://0.0.0.0:8086` by default.

2. Make a POST request to the `/read_my_palm` endpoint with a base64-encoded image:
   ```http
   POST /read_my_palm
   Content-Type: application/json
   
   {
     "puch_image_data": "base64_encoded_image_data",
     "query": "Tell me about my future"
   }
   ```

## API Endpoints

### Read Palm
- **URL**: `/read_my_palm`
- **Method**: `POST`
- **Authentication**: Bearer Token
- **Request Body**:
  ```json
  {
    "puch_image_data": "string (base64)",
    "query": "string"
  }
  ```
- **Success Response**:
  ```json
  {
    "type": "text",
    "text": "Your palm reading result..."
  }
  ```

## Project Structure

- `app.py` - Main FastMCP application with API endpoints
- `geminihelper.py` - Helper functions for Gemini AI integration
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (not in version control)

## Error Handling

The API returns appropriate HTTP status codes and error messages in case of failures:

- `400 Bad Request`: Invalid input parameters
- `401 Unauthorized`: Missing or invalid authentication token
- `500 Internal Server Error`: Server-side error during processing

## Security

- Always keep your Google API key and authentication tokens secure
- Do not commit `.env` files to version control
- Use HTTPS in production environments

## License

[Your License Here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

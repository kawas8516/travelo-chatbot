# llm_integration/utils.py

import os
import requests
import logging
from difflib import get_close_matches

# Configure logging for LLM interactions
logging.basicConfig(filename="llm_integration_log.log", level=logging.INFO)
logger = logging.getLogger(__name__)

# Hugging Face API setup
HF_API_URL = "https://api-inference.huggingface.co/microsoft/DialoGPT-medium"  # Replace with the specific model name
HF_API_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Predefined intent-response pairs
INTENTS = [
    {"prompt": "Hello", "response": "Hi there! How can I assist you today?"},
    {"prompt": "I want to book a ticket", "response": "Sure! Which museum would you like to visit?"},
    {"prompt": "Museum of Natural History", "response": "Got it! How many tickets would you like to book?"},
    {"prompt": "Two tickets", "response": "Great! What date would you like to visit?"},
    {"prompt": "This Friday", "response": "Perfect. And which type of ticket do you need? We have adult, senior, and child tickets."},
    {"prompt": "Two adult tickets", "response": "Thank you. Would you like to proceed with the payment?"},
    {"prompt": "Yes", "response": "Your booking is confirmed! Thank you for choosing us."},
    {"prompt": "I want to cancel my ticket", "response": "Please provide your ticket ID to proceed with the cancellation."},
    {"prompt": "My ticket ID is 12345", "response": "Ticket 12345 has been canceled. If you need further assistance, let me know."},
    {"prompt": "I want to reschedule my ticket", "response": "Please provide your ticket ID and the new date you want to reschedule to."},
    {"prompt": "Where is the Museum of Modern Art?", "response": "The Museum of Modern Art is located at 11 W 53rd St, New York, NY 10019."},
    {"prompt": "What is the payment process?", "response": "You can pay via credit card, PayPal, or bank transfer. Let me know if you’re ready to proceed."},
    {"prompt": "Thank you", "response": "You're welcome! Let me know if there's anything else I can help with."},
    {"prompt": "Goodbye", "response": "Goodbye! Have a wonderful day!"}
]

def get_intent_response(user_message):
    """
    Check if the user's message matches any predefined intent.
    
    Args:
        user_message (str): The message from the user.
    
    Returns:
        str: The predefined response if a match is found, else None.
    """
    prompts = [intent["prompt"] for intent in INTENTS]
    closest_match = get_close_matches(user_message, prompts, n=1, cutoff=0.6)
    
    if closest_match:
        matched_prompt = closest_match[0]
        for intent in INTENTS:
            if intent["prompt"] == matched_prompt:
                return intent["response"]
    
    return None  # No close match found

def get_llm_response(prompt, max_length=50):
    """
    Generate a response from the LLM using the Hugging Face Inference API.
    
    Args:
        prompt (str): The input text prompt to send to the LLM.
        max_length (int): The maximum length for the generated response.
    
    Returns:
        str: The generated response text or error message.
    """
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": prompt, "parameters": {"max_length": max_length}}

    try:
        logger.info(f"Querying LLM API with prompt: {prompt}")
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return process_llm_response(response.json())
    except requests.RequestException as e:
        logger.error(f"Error querying LLM API: {e}")
        return "API connection failed. Please try again later."

def process_llm_response(response_json):
    """
    Extract and clean text from LLM response.
    
    Args:
        response_json (dict): The raw response from the Hugging Face API.
    
    Returns:
        str: Cleaned text from the API response or error message.
    """
    try:
        if "error" in response_json:
            error_message = response_json["error"]
            logger.error(f"LLM API returned an error: {error_message}")
            return f"LLM API error: {error_message}"

        generated_text = response_json[0].get("generated_text", "No response generated.")
        logger.info(f"Processed response: {generated_text}")
        return generated_text.strip() if generated_text else "No response generated."
    except (IndexError, KeyError) as e:
        logger.error(f"Error extracting LLM response text: {e}")
        return "Error extracting response text."

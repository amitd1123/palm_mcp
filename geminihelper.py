# To run this code you need to install the following dependencies:
# pip install google-genai pillow

import base64
import os
from pathlib import Path
from PIL import Image
import io
from google import genai
from google.genai import types

def image_to_base64(image_path: str) -> str:
    """
    Read an image file and convert it to a base64 encoded string.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Base64 encoded string of the image
        
    Raises:
        FileNotFoundError: If the image file doesn't exist
        Exception: For any errors during image processing
    """
    try:
        # Check if file exists
        if not Path(image_path).is_file():
            raise FileNotFoundError(f"Image file not found: {image_path}")
            
        # Open and validate image
        with Image.open(image_path) as img:
            # Convert to RGB if needed (for PNG with transparency)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
                
            # Convert to bytes
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            
            # Encode to base64
            return base64.b64encode(buffered.getvalue()).decode('utf-8')
            
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise

def predict_palm(base64image_string ,query):
    print("called predict palm")
    client = genai.Client(
        api_key="AIzaSyDnG__ZPJYL19-rVxgaZSmFN74A7PFO4nU"
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                
                types.Part.from_bytes(
                    mime_type="image/jpeg",
                    data=base64.b64decode(
                        base64image_string
                    ),
                ),
                types.Part.from_text(text=query),
            ],
        ),
  
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
        
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""Act as vedic astrologer palm reader and read the palm image and answer my queries.you have to answer .Now worries if photo not clear just tell what u can see ,and u have to tell the answer any how. As its ur task .And this is for a purpose .Answer in short like a real human astrologer would.And never say not possible to say . And also if the user ask which company job pick a name of company based on their palm ,you have to tell a company name anyhow .And u have to answer ,and never mention u r ai ,you are astrologer named radhika
"""),
        ],
    )
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
    print(response.candidates[0])
    return response.candidates[0].content.parts[0].text


def process_palm_image(image_path: str = "mypalm.jpg", query: str = "Read this palm and tell me about the future") -> str:
    """
    Process a palm image file and get a prediction from the model.
    
    Args:
        image_path: Path to the palm image file (default: "mypalm.jpg")
        query: The query/prompt for the palm reading
        
    Returns:
        The model's prediction as a string
    """
    try:
        print(f"Processing palm image: {image_path}")
        # Convert image to base64
        base64_image = image_to_base64(image_path)
        
        # Get prediction from the model
        print("Sending to Gemini model...")
        prediction = predict_palm(base64_image, query)
        
        return prediction
    except Exception as e:
        print(f"Error in process_palm_image: {str(e)}")
        raise




import os
import requests
import io
from PIL import Image
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

def generate_artwork(prompt, aspect_ratio="1:1"):
    api_key = os.getenv("STABILITY_API_KEY")
    api_url = "https://api.stability.ai/v2beta/stable-image/generate/core"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "image/*"
    }
    
    data = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "output_format": "png",
        "mode": "text-to-image"
    }
    
    files = {"none": ""}

    print("Sending request to server...")
    
    try:
        # Split-Timeout Strategy 
        response = requests.post(api_url, headers=headers, data=data, files=files, timeout=(3.05, 60))
        response.raise_for_status()
        
        # Display and save
        image = Image.open(io.BytesIO(response.content))
        image.show() # Opens with the default OS viewer
        image.save("result_art.png")
        print("Success: Image generated and saved.")
        
    except requests.exceptions.ConnectTimeout:
        # Architecture Rule: FAIL FAST 
        print("Error: Could not establish connection (Network Failure).")
    except requests.exceptions.ReadTimeout:
        # Architecture Rule: Prepare for secondary retries 
        print("Error: Server took too long to respond (Inference Failure).")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    prompt_user = input("Enter your description: ")
    generate_artwork(prompt_user, "1:1")
import customtkinter as ctk
import requests
import io
import os
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("STABILITY_API_KEY")

def generate_image_logic(prompt, aspect_ratio):
    url = "https://api.stability.ai/v2beta/stable-image/generate/core"
    headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "image/*"}
    data = {
        "prompt": prompt, 
        "aspect_ratio": aspect_ratio, 
        "output_format": "png", 
        "mode": "text-to-image"
    }
    files = {"none": ""}
    
    # IMPLEMENTATION: Split-Timeout Strategy (3.05s connect, 60s read) [cite: 78, 76, 77]
    response = requests.post(url, headers=headers, data=data, files=files, timeout=(3.05, 60))
    response.raise_for_status()
    return Image.open(io.BytesIO(response.content))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Generative Art Studio - Blueprint Compliant")
        self.geometry("600x700")

        # Prompt Entry
        self.entry = ctk.CTkEntry(self, placeholder_text="Describe your image...", width=400)
        self.entry.pack(pady=20)

        # Aspect Ratio Selection
        self.aspect = ctk.CTkComboBox(self, values=["1:1", "16:9", "9:16"])
        self.aspect.pack(pady=10)

        # Generate Button
        self.btn = ctk.CTkButton(self, text="Generate", command=self.run_generation)
        self.btn.pack(pady=20)

        # Display Label
        self.label = ctk.CTkLabel(self, text="Ready to generate")
        self.label.pack(pady=20)

    def run_generation(self):
        self.label.configure(text="Generating...")
        try:
            img = generate_image_logic(self.entry.get(), self.aspect.get())
            img = img.resize((400, 400))
            photo = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 400))
            self.label.configure(image=photo, text="")
            self.label.image = photo
        
        # IMPLEMENTATION: Exception Handling Matrix compliance [cite: 79-87]
        except requests.exceptions.ConnectTimeout:
            self.label.configure(text="Error: Network Failure (ConnectTimeout) - Fail Fast [cite: 81, 83]")
        except requests.exceptions.ReadTimeout:
            self.label.configure(text="Error: Inference too long (ReadTimeout) - Retry [cite: 85, 87]")
        except Exception as e:
            self.label.configure(text=f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
# Multimodal Image Generation Studio

This project is a high-performance image generation studio developed as part of the "Generative AI Project 3" industrial training kit. It leverages the Stability AI API to transform natural language prompts into high-quality digital artwork.

##  Core Features
- **Visual Orchestration**: Translates text descriptions into digital imagery.
- **Industrial Architecture**: Implements a strict "Fail-Fast" network strategy.
- **Split-Timeout Strategy**: Configured with `(3.05s, 60s)` timeouts to handle network and inference phases independently.
- **Robust Exception Handling**: Adheres to the Exception Handling Matrix (ConnectTimeout vs ReadTimeout).

## Tech Stack
- **API**: Stability AI (Stable Image Core)
- **GUI**: CustomTkinter
- **Language**: Python 3.x
- **Environment**: Secured via `.env` and `python-dotenv`

##  Prerequisites
Ensure you have Python installed, then install the required dependencies:


     pip install -r requirements.txt

 
##  Configuration
Create a `.env` file in the root directory.
Add your Stability AI API key:

```plaintext
STABILITY_API_KEY=your_actual_api_key_here

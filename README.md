Email Classification and Analysis AI Project with python.

This project aims to classify different types of emails and automatically redirect them to the appropriate area.

Installation Guide

To run the Email Classification and Analysis AI Project, follow the steps below:

1. Clone the Repository
   https://github.com/Wesleyr66/ia-email.git
   cd ia-email

3. Set Up a Virtual Environment
   python -m venv venv (Windowns)
   .\venv\Scripts\activate

4. Install Dependencies
   pip install -r requirements.txt

5. Create a .env File
   In the root of the project and add your credentials and API keys.
   {
    EMAIL=your-email@gmail.com
    SENHA=your-app-password
    OPENAI_API_KEY=your-openai-api-key
   }
   
6. Run the Project
   python main.py

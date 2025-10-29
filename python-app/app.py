# app.py
import os

def connect_to_service():
    # ❌ Hardcoded API key — will be caught by GitLeaks (generic-api-key / AWS / Token patterns)
    API_KEY = "ghp_abCDeFgHijKLMNOPqrstuVWxyZ012345678"
    
    print("Connecting to external services with the provided API key...")
    print(f"Using API_KEY: {API_KEY[:6]}********")

    return True

if __name__ == "__main__":
    connect_to_service()
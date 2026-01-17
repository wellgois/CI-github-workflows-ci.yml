import os

def main():
    print("OPENAI_API_KEY:", bool(os.getenv("OPENAI_API_KEY")))
    print("ANTHROPIC_API_KEY:", bool(os.getenv("ANTHROPIC_API_KEY")))
    print("GROQ_API_KEY:", bool(os.getenv("GROQ_API_KEY")))
    print("DEEPSEEK_API_KEY:", bool(os.getenv("DEEPSEEK_API_KEY")))
    print("GEMINI_API_KEY:", bool(os.getenv("GEMINI_API_KEY")))

if __name__ == "__main__":
    main()

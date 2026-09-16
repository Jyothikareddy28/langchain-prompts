from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model = ChatGroq(model = "openai/gpt-oss-20b",temperature=0.7)

result = model.invoke("Wrire a short poem about the beauty of nature.")

print(result.content)
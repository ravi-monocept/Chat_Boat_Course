from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
)
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import torch
from typing import Annotated
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Initialize FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Ensure this path is correct


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# Initialize chat log
chat_log = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    }
]

chat_responses = []

# Initialize the text generation pipeline once at startup
pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-7b-alpha",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)


@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    message = {"role": "user", "content": user_input}
    chat_log.append(message)
    chat_responses.append(user_input)

    try:
        # Prepare prompt for the model using chat log
        prompt = "\n".join(f"{msg['role']}: {msg['content']}" for msg in chat_log)

        # Generate response from the model
        outputs = pipe(
            prompt,
            max_new_tokens=50,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )
        assistant_text = outputs[0]["generated_text"].split("assistant:")[-1].strip()

        # Append the generated response to chat log
        assistant_message = {
            "role": "assistant",
            "content": assistant_text,
        }

        chat_log.append(assistant_message)
        chat_responses.append(assistant_text)
        return templates.TemplateResponse(
            "home.html", {"request": request, "chat_responses": chat_responses}
        )

        return assistant_message

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@app.get("/chat-history")
async def read_chat_history():
    return chat_log

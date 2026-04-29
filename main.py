import os
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/env.js")
def get_env_js():
    # Only expose safe/necessary keys to the frontend
    # Note: Deepgram API key is exposed here for the frontend WebSocket prototype. 
    # In production, Deepgram STT should use short-lived temporary tokens or a backend proxy.
    env_content = f"""
    window.ENV = {{
        SUPABASE_URL: "{os.getenv('SUPABASE_URL', '')}",
        SUPABASE_KEY: "{os.getenv('SUPABASE_KEY', '')}",
        BLOB_BASE_URL: "{os.getenv('BLOB_BASE_URL', '')}",
        BLOB_SAS_TOKEN: "{os.getenv('BLOB_SAS_TOKEN', '')}",
        DEEPGRAM_API_KEY: "{os.getenv('DEEPGRAM_API_KEY', '')}"
    }};
    """
    return Response(content=env_content, media_type="application/javascript")

# Mount the static 'app' directory to the root path
app.mount("/", StaticFiles(directory="app", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)

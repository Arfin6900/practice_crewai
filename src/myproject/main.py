from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .crew import run_crew

app = FastAPI()

# Set up templates
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/run-crew")
async def execute_crew():
    print("Starting Crew AI...")
    try:
        flow = run_crew()
        # First get the topic
        topic = await flow.generate_topic()
        # Then get the outline using the topic
        outline = await flow.generate_outline(topic)
        return {"result": {"topic": topic, "outline": outline}}
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("myproject.main:app", host="127.0.0.1", port=8000, reload=True)

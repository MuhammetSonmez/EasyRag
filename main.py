from fastapi import FastAPI
from routes import router
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request



app = FastAPI(title="Easy RAG API")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.include_router(router)


@app.get("/", response_class=HTMLResponse)
async def serve(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, reload=True)

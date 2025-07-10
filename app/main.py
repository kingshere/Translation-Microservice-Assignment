from fastapi import FastAPI
from app.routes import translation, health
from app.db.database import init_db

app = FastAPI(
    title="Translation Microservice",
    description="A lightweight translation service using Google Translate API",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    await init_db()

# Include routers
app.include_router(translation.router)
app.include_router(health.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
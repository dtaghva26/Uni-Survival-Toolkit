from fastapi import FastAPI
from config.lifespan import lifespan
app = FastAPI(lifespan=lifespan)

# Root route (test)
@app.get("/")
async def root():
    return {"message": "Uni Survival Toolkit API running"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from core.config import Settings


# We are handling settings like this so we can test other settings via dependency injection.
# lru_cache will only create the settings object once, so there is not a constant need to read the .env file.
# https://fastapi.tiangolo.com/advanced/settings/?h=sett#creating-the-settings-only-once-with-lru-cache
@lru_cache
def get_settings() -> Settings:
    return Settings()


app = FastAPI(
    title=get_settings().app_name,
    description=get_settings().app_description,
    version=get_settings().app_version,
    docs_url=get_settings().app_docs_url,
    redoc_url=get_settings().app_redoc_url,
)

# TODO: Define a list of origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

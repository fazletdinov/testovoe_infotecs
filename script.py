import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi_pagination import add_pagination

from src.handlers import router_v1

app = FastAPI(title="Geoname App")
add_pagination(app)

main_router = APIRouter()
main_router.include_router(router_v1,
                           prefix="/api/v1",
                           tags=["geoname"])

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app="script:app", host="127.0.0.1", port=8000, reload=True)

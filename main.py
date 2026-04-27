from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import farms, shipments, routes, disruptions

app = FastAPI(title="AgriRoute API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  #frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(farms.router, prefix="/api/farms", tags=["Farms"])
app.include_router(shipments.router, prefix="/api/shipments", tags=["Shipments"])
app.include_router(routes.router, prefix="/api/routes", tags=["Routes"])
app.include_router(disruptions.router, prefix="/api/disruptions", tags=["Disruptions"])

@app.get("/")
def root():
    return {"message": "AgriRoute API is running 🌱"}
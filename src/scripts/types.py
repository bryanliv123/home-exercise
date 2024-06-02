from pydantic import BaseModel


class RouteInfo(BaseModel):
    distance: float
    duration: float

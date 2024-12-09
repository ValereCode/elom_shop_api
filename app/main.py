from .utils.database import app
from .routes import task_routes
from .routes import user_routes
from .routes import product_routes


app.include_router(user_routes.router)
app.include_router(product_routes.router)



app.include_router(task_routes.router)


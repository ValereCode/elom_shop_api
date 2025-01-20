from .utils.database import app
from .routes import task_routes, user_routes, product_routes, category_routes, auth_routes



app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(category_routes.router)
app.include_router(product_routes.router)



app.include_router(task_routes.router)


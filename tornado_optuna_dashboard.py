import asyncio
import tornado.wsgi
import optuna
from optuna_dashboard import wsgi


storage = optuna.storages.InMemoryStorage()
dashboard_app = wsgi(storage)


async def main():
    container = tornado.wsgi.WSGIContainer(dashboard_app)
    app = tornado.httpserver.HTTPServer(container)
    app.listen(8888)
    print("Started to listen http://localhost:8888/")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

from litestar import Litestar, get
import uvicorn


@get("/")
def read_root() -> dict:
    return {"message": "Hello, World!"}

app = Litestar([read_root])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def get():
    print("请求到达")
    return "天下大势，为我所控"


uvicorn.run(app, port=1234)

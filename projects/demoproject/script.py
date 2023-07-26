import uvicorn


def start():
    uvicorn.run("demoproject.main:app", port=8001, log_level="debug")

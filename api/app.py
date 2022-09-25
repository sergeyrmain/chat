from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")



if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5000, debug=True)
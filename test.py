from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def default() -> dict:
    return {
        'health' : 'Good'
    }
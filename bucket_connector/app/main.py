import uvicorn
from app.Server import Server

def main():
    server = Server().start()
    # TODO: replace with env
    uvicorn.run(server.app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
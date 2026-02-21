import uvicorn

if __name__ == "__main__":
    print("\n🚀 CodeArena starting...")
    print("📦 Make sure MongoDB is running and connected via .env")
    print("🌐 Open: http://localhost:8000\n")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

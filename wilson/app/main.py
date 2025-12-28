import asyncio
from wilson.app.wiring import build_app

async def main():
    print("--- W.I.L.S.O.N. Initialized (Refactored) ---")
    
    app = build_app()
    
    print("Listening for voice input... (Say 'exit' to quit)")
    await app.run_loop()

if __name__ == "__main__":
    asyncio.run(main())

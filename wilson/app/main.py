import asyncio
from wilson.app.wiring import build_app

async def main():
    print("--- W.I.L.S.O.N. Initialized (Refactored) ---")
    
    app = build_app()
    
    # Test Interaction
    user_input = "Hello Wilson. I am currently stranded on an island of code. Who are you?"
    await app.process_user_input(user_input)

if __name__ == "__main__":
    asyncio.run(main())

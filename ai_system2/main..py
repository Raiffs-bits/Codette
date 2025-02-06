import asyncio
from ai_system.ai_core import AICore  

async def main():
    ai_core = AICore(config_path="config.json")
    user_id = 1  # Example user ID
    query = "What is the impact of quantum computing on artificial intelligence?"
    response = await ai_core.generate_response(query, user_id)
    print(response)
    await ai_core.shutdown()

if __name__ == "__main__":
    asyncio.run(main())

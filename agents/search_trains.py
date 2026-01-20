import asyncio
from droidrun import DroidAgent
from droidrun.config_manager.config_manager import (
    DroidrunConfig,
    TracingConfig,
    LoggingConfig,
    AgentConfig,
)
from llama_index.llms.google_genai import GoogleGenAI
from agents.prompts import prompts
from dotenv import load_dotenv
import os
import subprocess
import time

load_dotenv()

async def force_launch_app(package_name: str):
    """Force launch app via ADB (more reliable than UI)"""
    print(f"🚀 Force-launching {package_name}...")
    try:
        subprocess.run(
            ["adb", "shell", "monkey", "-p", package_name, 
             "-c", "android.intent.category.LAUNCHER", "1"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        await asyncio.sleep(3)
        print("✅ App launched successfully")
        return True
    except Exception as e:
        print(f"⚠️ ADB launch failed: {e}")
        return False

async def search_trains(from_station: str, to_station: str):
    """Agent to search for trains on ConfirmTkt"""
    
    # First force launch the app
    await force_launch_app("com.confirmtkt.lite")
    
    llm = GoogleGenAI(
        api_key=os.environ["GEMINI_API_KEY"],
        model="gemini-2.0-flash",
    )
    
    config = DroidrunConfig(
        agent=AgentConfig(reasoning=True, max_steps=25),
        tracing=TracingConfig(enabled=False),
        logging=LoggingConfig(debug=True, save_trajectory="action"),
    )
    
    agent = DroidAgent(
        goal=prompts.SEARCH_TRAINS_GOAL(from_station, to_station),
        config=config,
        llms=llm,
    )
    
    result = await agent.run()
    
    print(f"🔍 Search Status: {'✅ Success' if result.success else '❌ Failed'}")
    print(f"Steps: {result.steps}")
    
    if result.success:
        print(f"✅ Train search completed: {from_station} → {to_station}")
        return True
    
    print(f"❌ Train search failed: {result.reason}")
    return False

if __name__ == "__main__":
    async def test():
        await search_trains("Nellore", "Vijayawada")
    
    asyncio.run(test())
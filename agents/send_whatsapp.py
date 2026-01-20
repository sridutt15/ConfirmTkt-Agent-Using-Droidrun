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

load_dotenv()

async def send_whatsapp_message(contact_name: str, screenshot_path: str):
    """Agent to send screenshot via WhatsApp"""
    
    # Force launch WhatsApp
    print("🚀 Opening WhatsApp...")
    subprocess.run(
        ["adb", "shell", "monkey", "-p", "com.whatsapp",
         "-c", "android.intent.category.LAUNCHER", "1"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    await asyncio.sleep(2)
    
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
        goal=prompts.SEND_WHATSAPP_GOAL(contact_name, screenshot_path),
        config=config,
        llms=llm,
    )
    
    result = await agent.run()
    
    print(f"📱 WhatsApp Status: {'✅ Success' if result.success else '❌ Failed'}")
    print(f"Steps: {result.steps}")
    
    if result.success:
        print(f"✅ Screenshot sent to {contact_name}")
        return True
    
    print(f"❌ Failed to send WhatsApp: {result.reason}")
    return False

if __name__ == "__main__":
    async def test():
        await send_whatsapp_message("Sridutt", "/sdcard/Pictures/test.png")
    
    asyncio.run(test())
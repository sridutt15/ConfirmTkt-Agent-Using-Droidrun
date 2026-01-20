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

async def take_screenshot_via_adb(filepath: str):
    """Take screenshot using ADB and refresh gallery"""
    print("📸 Taking screenshot via ADB...")
    try:
        # Take screenshot
        subprocess.run(["adb", "shell", "screencap", "-p", filepath])
        
        # Refresh gallery to see it
        subprocess.run([
            "adb", "shell", "am", "broadcast",
            "-a", "android.intent.action.MEDIA_SCANNER_SCAN_FILE",
            "-d", f"file://{filepath}"
        ], stdout=subprocess.DEVNULL)
        
        print(f"✅ Screenshot saved: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Screenshot failed: {e}")
        return False

async def find_and_expand_train(screenshot_path: str):
    """Agent to find available train and take screenshot"""
    
    llm = GoogleGenAI(
        api_key=os.environ["GEMINI_API_KEY"],
        model="gemini-2.0-flash",
    )
    
    config = DroidrunConfig(
        agent=AgentConfig(reasoning=True, max_steps=20),
        tracing=TracingConfig(enabled=False),
        logging=LoggingConfig(debug=True, save_trajectory="action"),
    )
    
    agent = DroidAgent(
        goal=prompts.FIND_AVAILABLE_TRAIN_GOAL(),
        config=config,
        llms=llm,
    )
    
    result = await agent.run()
    
    print(f"🔍 Find Train Status: {'✅ Success' if result.success else '❌ Failed'}")
    
    if result.success:
        # Take screenshot via ADB (more reliable)
        screenshot_success = await take_screenshot_via_adb(screenshot_path)
        
        if screenshot_success:
            print("✅ Train found and screenshot captured")
            return screenshot_path
        else:
            print("❌ Screenshot failed")
            return None
    
    print(f"❌ Failed to find train: {result.reason}")
    return None

if __name__ == "__main__":
    async def test():
        await find_and_expand_train("/sdcard/Pictures/test_screenshot.png")
    
    asyncio.run(test())
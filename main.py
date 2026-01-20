#!/usr/bin/env python3
import asyncio
import os
import json
from colorama import init, Fore, Style
from agents.search_trains import search_trains, force_launch_app
from agents.find_train import find_and_expand_train
from agents.send_whatsapp import send_whatsapp_message

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     🚂  CONFIRMTKT TRAIN AGENT  🤖                      ║
║     📱  Auto Search + WhatsApp Sharing                  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.YELLOW}Automated train search & WhatsApp sharing{Style.RESET_ALL}
{Fore.GREEN}Press Enter to start...{Style.RESET_ALL}
"""
    print(banner)

def print_step(step_name: str, color: str = Fore.BLUE):
    print(f"\n{color}{Style.BRIGHT}➤ {step_name}{Style.RESET_ALL}")
    print(f"{color}{'─' * 60}{Style.RESET_ALL}")

def load_config():
    """Load configuration from JSON file"""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Fore.RED}❌ config.json not found!{Style.RESET_ALL}")
        return None

async def run_train_agent_cycle():
    """Main workflow: Search → Find → Screenshot → WhatsApp"""
    
    config = load_config()
    if not config:
        return
    
    print(f"{Fore.GREEN}👤 Welcome to Train Agent!{Style.RESET_ALL}")
    
    # Get route (use first one for demo)
    route = config["train_routes"][0]
    from_station = route["from"]
    to_station = route["to"]
    contact = config["whatsapp_contact"]
    screenshot_path = config["screenshot_path"]
    
    max_retries = 2
    
    # STEP 1: Search Trains
    search_success = False
    for attempt in range(max_retries):
        try:
            print_step(f"SEARCHING TRAINS (Attempt {attempt + 1})", Fore.CYAN)
            print(f"Route: {from_station} → {to_station}")
            
            search_success = await search_trains(from_station, to_station)
            
            if search_success:
                print(f"{Fore.GREEN}✅ Train search successful!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}❌ Search failed{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
    
    if not search_success:
        print(f"{Fore.RED}❌ Could not search trains. Exiting.{Style.RESET_ALL}")
        return
    
    # STEP 2: Find Available Train & Screenshot
    screenshot_file = None
    for attempt in range(max_retries):
        try:
            print_step("FINDING AVAILABLE TRAIN", Fore.YELLOW)
            
            screenshot_file = await find_and_expand_train(screenshot_path)
            
            if screenshot_file:
                print(f"{Fore.GREEN}✅ Screenshot captured!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}❌ Failed to capture screenshot{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
    
    if not screenshot_file:
        print(f"{Fore.RED}❌ Could not get screenshot. Exiting.{Style.RESET_ALL}")
        return
    
    # STEP 3: Send via WhatsApp
    whatsapp_success = False
    for attempt in range(max_retries):
        try:
            print_step("SENDING VIA WHATSAPP", Fore.GREEN)
            print(f"Contact: {contact}")
            print(f"File: {screenshot_file}")
            
            whatsapp_success = await send_whatsapp_message(contact, screenshot_file)
            
            if whatsapp_success:
                print(f"{Fore.GREEN}✅ WhatsApp sent successfully!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}❌ WhatsApp failed{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
    
    # Summary
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}📊 Workflow Complete{Style.RESET_ALL}")
    print(f"{Fore.CYAN}   Train Search: {'✅ Success' if search_success else '❌ Failed'}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}   Screenshot: {'✅ Captured' if screenshot_file else '❌ Failed'}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}   WhatsApp: {'✅ Sent' if whatsapp_success else '❌ Failed'}{Style.RESET_ALL}")
    
    if whatsapp_success:
        print(f"\n{Fore.GREEN}🎉 Train details sent to {contact} on WhatsApp!{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}👋 Agent session complete.{Style.RESET_ALL}")

async def main():
    """Main entry point"""
    print_banner()
    input()  # Wait for Enter
    
    print(f"{Fore.GREEN}🚀 Starting Train Agent...{Style.RESET_ALL}")
    
    # Check requirements
    if not os.path.exists("config.json"):
        print(f"{Fore.RED}❌ config.json not found!{Style.RESET_ALL}")
        return
    
    if not os.getenv("GEMINI_API_KEY"):
        print(f"{Fore.RED}❌ GEMINI_API_KEY not set in .env{Style.RESET_ALL}")
        return
    
    # Check ADB connection
    try:
        import subprocess
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "device" not in result.stdout:
            print(f"{Fore.YELLOW}⚠️  No Android device connected via ADB{Style.RESET_ALL}")
    except:
        print(f"{Fore.YELLOW}⚠️  ADB not available{Style.RESET_ALL}")
    
    print(f"{Fore.GREEN}✅ Starting automation...{Style.RESET_ALL}")
    
    await run_train_agent_cycle()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}💥 Critical error: {str(e)}{Style.RESET_ALL}")
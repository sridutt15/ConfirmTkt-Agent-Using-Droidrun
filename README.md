# 🚆 ConfirmTkt Train Agent 🤖💬  
### AI-Powered Train Search + WhatsApp Sharing Automation (Android)

> ⚡ A fully automated Android AI Agent that searches train availability on ConfirmTkt, captures the best options, and instantly shares them via WhatsApp — **without manual effort**.

⭐ If you're into **Agentic AI**, **Mobile Automation**, or **Android Vision Agents**, this project will blow your mind.

---

## 🔥 Why This Repo is Special?

Most automation projects break when UI changes.  
This one doesn’t.

✅ **Vision-Based AI Agent**  
✅ **Natural Language Control**  
✅ **Real Android Interaction** (not simulated UI selectors)  
✅ **Multi-App Workflow** (ConfirmTkt ➝ WhatsApp)  
✅ **Resilient + Retry-ready**

---

## 🎯 What It Can Do (Features)

✨ **Smart Train Search**
- Enter source & destination automatically
- Select travel date smoothly
- Pick preferred class (Sleeper/3AC/etc.)

👁️ **Availability Detection**
- Detect trains with available seats using screenshot intelligence  
- Choose the best train option like a human would

📸 **Auto Screenshot Capture**
- Opens train details
- Captures important info
- Saves it for sharing/logging

💬 **WhatsApp Auto Sharing**
- Opens WhatsApp
- Selects contact
- Shares screenshot instantly

🔁 **Retry + Resilience**
- Handles UI delays
- Works even if screens load slowly
- Built-in fallback strategies

📊 **Live Terminal Monitoring**
- Color-coded logs
- Clear progress status
- Easy to debug

⚙️ **Fully Configurable**
- Routes
- Contacts
- Class preferences
- Screenshot locations

---

## 🎥 Demo Video (Must Watch)

📌 Watch here: https://youtu.be/sYuRD4RcvHs  
*(This demo alone makes it worth a ⭐ 😄)*

---

## 🧠 Tech Stack

- **DroidRun** → Vision-first Android AI automation  
- **Gemini Vision + LLM** → Understanding screen + making decisions  
- **ADB** → Executes taps, swipes, typing, app switching  
- **Python Async Agent Workflow** → Modular multi-step execution

---

## Quick Start

### Prerequisites
- Android device/emulator with USB debugging enabled
- Python 3.8+
- Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
- ConfirmTkt and WhatsApp installed on device

### Installation
1. **Clone & Setup**
   ```bash
   git clone https://github.com/sridutt15/ConfirmTkt-Agent-Using-Droidrun.git
   cd ConfirmTktTrainAgent
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
```
2. **Configure Environment**
```bash
# Add your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env
   
# Customize your settings
nano config.json  # Edit routes, WhatsApp contact, etc.
```
3. **Setup DroidRun**
```bash
droidrun setup
# Follow on-screen instructions to grant accessibility permissions
```
4. **Run the Agent**
```bash
python main.py
```
**Architecture**

ConfirmTkt Train Agent follows a modular agent-based architecture powered by DroidRun:
``` bash
ConfirmTktTrainAgent/
├── main.py                 # Central orchestrator & workflow manager
├── config.json             # User preferences & train routes
├── agents/
│   ├── search_trains.py    # Searches trains on ConfirmTkt
│   ├── find_train.py       # Identifies available trains & captures screenshots
│   ├── send_whatsapp.py    # Shares screenshots via WhatsApp
│   └── prompts/
│       └── prompts.py      # Natural language instructions for AI agents
├── screenshots/            # Auto-saved train detail captures
└── trajectories/           # DroidRun automation logs (for debugging)
```
### How It Works
1. **Vision-Based Interaction**: Uses screenshot analysis instead of brittle UI selectors
2. **LLM-Powered Decisions**: Gemini AI interprets visual context and decides next actions
3. **ADB Execution**: Performs precise taps, scrolls, and text input on the Android device
4. **State Management**: Maintains context across multiple apps and screens

## Configuration

Edit `config.json` to match your preferences:

```json
{
  "user_name": "Your Name",
  "whatsapp_contact": "Travel Buddy",
  "train_routes": [
    {"from": "Nellore", "to": "Vijayawada"},
    {"from": "Mumbai Central", "to": "Delhi"}
  ],
  "preferred_class": "Sleeper",
  "screenshot_path": "/sdcard/Pictures/train_details.png"
}
## About DroidRun

[DroidRun](https://github.com/droidrun-ai/droidrun) is the core automation framework that enables this project's capabilities:

- **Vision-First Approach**: Uses screenshot analysis instead of traditional UI selectors
- **Natural Language Automation**: Converts plain English instructions into Android actions
- **ADB Integration**: Direct device communication for reliable execution
- **Trajectory Recording**: Saves automation sequences for debugging and optimization

## Sample Workflow

### What Happens Automatically:
1. **ConfirmTkt Launch**: App opens automatically via ADB
2. **Route Input**: Enters "From" and "To" stations with date selection
3. **Train Search**: Executes search and loads results
4. **Availability Scan**: Identifies trains with seat availability
5. **Detail Capture**: Expands train details and takes screenshot
6. **WhatsApp Sharing**: Sends screenshot to specified contact
7. **Completion**: Returns to home screen with success confirmation

### Time Estimate: Approximately 2.5 minutes total
## Troubleshooting

### Common Issues
- **App not found**: Verify package names in `prompts.py`
- **Screenshot fails**: Ensure storage permissions are granted
- **WhatsApp contact missing**: Check exact contact name in address book
- **ADB connection issues**: Verify USB debugging is enabled

### Debug Mode
```bash
# Run with detailed logging
python main.py --verbose

# Test individual components
python -c "from agents.search_trains import test; import asyncio; asyncio.run(test())"
## License & Ethics

This project is for educational demonstration only. Users must:
- Respect ConfirmTkt and WhatsApp terms of service
- Use automation responsibly and ethically
- Not overload services with excessive requests
- Comply with all applicable laws and regulations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/Improvement`)
3. Commit changes (`git commit -m 'Add some Improvement'`)
4. Push to branch (`git push origin feature/Improvement`)
5. Open a Pull Request

## Acknowledgments

- **DroidRun Team** for the revolutionary automation framework
- **Google Gemini** for powerful vision-language capabilities
- **ConfirmTkt** for train booking services
- **WhatsApp** for messaging platform integration

# 🚆 ConfirmTkt Train Agent 🤖💬

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![DroidRun](https://img.shields.io/badge/Powered%20By-DroidRun-green)](https://github.com/droidrun-ai/droidrun)
[![Android](https://img.shields.io/badge/Platform-Android-3DDC84.svg)](https://www.android.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **AI-Powered Train Search + WhatsApp Sharing Automation**

A fully automated Android AI Agent that searches train availability on ConfirmTkt, captures the best options via screenshot, and instantly shares them via WhatsApp—**without manual effort**.

---

## 🔥 Overview

Most automation projects break when UI changes. This one doesn't.

By leveraging **Gemini Vision** and **DroidRun**, this agent "sees" the screen like a human, making it resilient to layout updates.

* ✅ **Vision-Based AI Agent** (No brittle XML selectors)
* ✅ **Natural Language Control**
* ✅ **Multi-App Workflow** (ConfirmTkt ➝ WhatsApp)
* ✅ **Real Android Interaction** via ADB

---

## 🎯 Features

### ✨ Smart Train Search
* Inputs source & destination stations automatically.
* Selects travel dates and preferred travel class (Sleeper, 3AC, etc.).

### 👁️ Availability Detection
* Uses Gemini Vision to detect seat availability from the screen.
* Intelligently selects the best train option based on status.

### 📸 Auto Screenshot & Sharing
* Captures train details automatically.
* Opens WhatsApp, finds your specified contact, and shares the screenshot.

### 🔁 Resilience
* Handles UI delays and slow loading screens.
* Includes built-in retry mechanisms and fallback strategies.

---

## 🎥 Demo

**[📺 Watch the Demo Video on YouTube](https://youtu.be/sYuRD4RcvHs)**

---

## 🧠 Tech Stack

| Component | Description |
| :--- | :--- |
| **DroidRun** | Vision-first Android automation framework |
| **Gemini Vision** | Multimodal LLM for screen understanding & reasoning |
| **ADB** | Executes taps, swipes, and text input on the device |
| **Python** | Async agent workflow orchestration |

---

## 🚀 Quick Start

### Prerequisites
* Android device or Emulator with **USB Debugging Enabled**.
* Python 3.8+.
* **ConfirmTkt** and **WhatsApp** installed on the device.
* A Google **Gemini API Key** ([Get it here](https://aistudio.google.com/app/apikey)).

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/sridutt15/ConfirmTkt-Agent-Using-Droidrun.git](https://github.com/sridutt15/ConfirmTkt-Agent-Using-Droidrun.git)
    cd ConfirmTktTrainAgent
    ```

2.  **Set Up Virtual Environment**
    ```bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```ini
    GEMINI_API_KEY=your_actual_api_key_here
    ```

5.  **Initialize DroidRun**
    ```bash
    droidrun setup
    # Follow on-screen instructions to grant accessibility permissions
    ```

---

## ⚙️ Configuration

Edit `config.json` to customize your routes and contacts. Ensure the WhatsApp name matches your phone contacts exactly.

```json
{
  "user_name": "Sridutt",
  "whatsapp_contact": "Travel Buddy",
  "train_routes": [
    {"from": "Nellore", "to": "Vijayawada"},
    {"from": "Mumbai Central", "to": "Delhi"}
  ],
  "preferred_class": "Sleeper",
  "screenshot_path": "/sdcard/Pictures/train_details.png"
}

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
**Project Architecture**

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
```
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
python main.py --verbose
```

# **Test individual components**
```
python -c "from agents.search_trains import test; import asyncio; asyncio.run(test())"
```

## **License & Ethics**

```
This project is for educational demonstration only. Users must:
- Respect ConfirmTkt and WhatsApp terms of service
- Use automation responsibly and ethically
- Not overload services with excessive requests
- Comply with all applicable laws and regulations

```

## **Contributing**

```
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/Improvement`)
3. Commit changes (`git commit -m 'Add some Improvement'`)
4. Push to branch (`git push origin feature/Improvement`)
5. Open a Pull Request
```

## Acknowledgments

```
- DroidRun Team for the revolutionary automation framework
- Google Gemini for powerful vision-language capabilities
- ConfirmTkt for train booking services
- WhatsApp for messaging platform integration
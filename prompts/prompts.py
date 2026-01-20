def LAUNCH_CONFIRMTKT_GOAL():
    return """
1. Open ConfirmTkt app (package name com.confirmtkt.lite)
2. If app is already open, bring it to foreground
3. Close any "Rate Us" or advertisement popups immediately
4. Wait for app to load completely
5. Return success when ConfirmTkt home screen is visible
"""

def SEARCH_TRAINS_GOAL(from_station: str, to_station: str):
    return f"""
1. On ConfirmTkt home screen, locate and tap "From" station field
2. Type "{from_station}"
3. Select "{from_station} (NLR)" from suggestions
4. Tap "To" station field
5. Type "{to_station}"
6. Select "Vijayawada Junction (BZA)" from suggestions
7. Tap date selector and choose "Tomorrow"
8. Tap "SEARCH TRAINS" button
9. Wait for train list to load completely
10. Return success when train list is visible on screen
"""

def FIND_AVAILABLE_TRAIN_GOAL():
    return """
1. On train list screen, scroll down slowly
2. Look for trains with green "AVAILABLE" text
3. If found, tap on that train to expand details
4. If no "AVAILABLE" trains found, tap any train to expand details
5. Make sure train details (schedule, classes) are visible
6. Take screenshot via notification panel (swipe down → screenshot)
7. Return success when screenshot is taken
"""

def SEND_WHATSAPP_GOAL(contact_name: str, screenshot_path: str):
    return f"""
1. Open WhatsApp app (package name com.whatsapp)
2. Tap search icon (magnifying glass)
3. Type "{contact_name}"
4. Tap contact "{contact_name}" from results
5. Tap attachment icon (paperclip/plus)
6. Tap "Gallery" or "Photos"
7. Select most recent image (should be train screenshot)
8. Tap send button (paper plane icon)
9. Wait for message to be delivered
10. Return success when message shows one tick (sent)
"""

def TAKE_SCREENSHOT_GOAL():
    return """
1. Take screenshot using Android's native method:
   - Swipe down from top edge to open notification panel
   - Find and tap "Screenshot" tile (camera icon)
   - Wait for screenshot animation/sound
2. Return to previous app (ConfirmTkt)
"""
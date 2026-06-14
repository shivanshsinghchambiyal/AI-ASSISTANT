import pyautogui
import pygetwindow as gw
import pytesseract
import pyttsx3

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_screenshot():
    

    chrome = gw.getWindowsWithTitle("LeetCode")[0]

    left = chrome.left
    top = chrome.top
    width = chrome.width
    height = chrome.height

    img = pyautogui.screenshot(
        region=(left, top, width, height)
    )

    img.save("leetcode.png")

def extract_text():
    text = pytesseract.image_to_string("leetcode.png")
    return text.lower()

def detect_pattern(problem_text):

    if "sorted array" in problem_text:
        return "Two Pointer or Binary Search"

    elif "substring" in problem_text:
        return "Sliding Window"

    elif "maximum profit" in problem_text:
        return "Greedy"

    elif "shortest path" in problem_text:
        return "Graph"

    elif "longest common subsequence" in problem_text:
        return "Dynamic Programming"

    elif "tree" in problem_text:
        return "Tree Traversal"

    return "Pattern not identified"

take_screenshot()

text = extract_text()
print("\n========== OCR TEXT ==========\n")
print(text)
print("\n==============================\n")

pattern = detect_pattern(text)

speak(f"This looks like {pattern}")
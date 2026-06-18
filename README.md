# Coding Assistant

A Python-based coding assistant that captures screenshots, extracts text using OCR, and analyzes coding-related content such as programming problems and compiler errors. The project helps users understand coding concepts, identify common DSA patterns, and interpret compiler errors through automated screen analysis.

## Features

* Capture screenshots automatically from the screen
* Extract text using Tesseract OCR
* Detect common DSA patterns from coding problems
* Analyze compiler and coding errors
* Provide beginner-friendly error explanations
* Generate debugging suggestions
* Support coding interview preparation

## Technologies Used

* Python
* PyAutoGUI
* PyTesseract
* Pillow (PIL)
* Tesseract OCR

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd Coding-Assistant
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Install Tesseract OCR and update the Tesseract path in the code if required.

5. Run the project

```bash
python main.py
```

## How It Works

```text
Screen Capture
      ↓
OCR Text Extraction
      ↓
Content Analysis
      ↓
Pattern Detection / Error Analysis
      ↓
Result Display
```

## Example Output

### DSA Pattern Detection

Input:

```text
Longest Substring Without Repeating Characters
```

Output:

```text
Pattern: Sliding Window
Complexity: O(n)
Hint: Maintain a window of unique characters.
```

### Error Analysis

Input:

```text
error: no matching function for call to push_back
```

Output:

```text
Error Type: Type Mismatch

Explanation:
Function arguments do not match expected datatype.

Suggested Fix:
Check parameter types carefully.
```



## Future Improvements

* Voice command support
* Advanced compiler error analysis
* More DSA pattern detection rules
* Code complexity estimation
* Smart debugging suggestions
* Support for additional programming languages

## Purpose

## Purpose

The purpose of this project is to help programmers and coding enthusiasts learn more effectively by providing instant assistance while solving coding problems. The assistant analyzes coding-related content directly from the screen, identifies common DSA patterns, and explains compiler errors in a simple and understandable way.

By reducing the time spent identifying problem-solving approaches and understanding error messages, the tool helps users focus on learning concepts, improving debugging skills, and strengthening their problem-solving abilities. It serves as a learning companion for students, beginners, and interview candidates who want to practice coding more efficiently and gain a better understanding of programming concepts.
# JARVIS AI Voice Assistant

JARVIS is an advanced AI voice assistant developed in Python that automates tasks, processes voice commands, and provides intelligent responses using natural language processing.

## ✨ Features
- **Voice Control**: Execute 20+ voice commands (web search, WhatsApp, calls, etc.)
- **AI Conversations**: Integrated Hugging Chat API for smart responses
- **Real-time Dashboard**: Web interface for command tracking (HTML/CSS/JS + Bootstrap)
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Modular Design**: Easy to extend with new features

## 🛠️ Tech Stack
| Category       | Technologies |
|----------------|--------------|
| **Core**       | Python 3.8+  |
| **Voice**      | SpeechRecognition, PyAudio |
| **AI**         | HuggingChat API |
| **Frontend**   | HTML5, CSS3, JavaScript, Bootstrap |
| **Tools**      | VS Code, Git |

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Microphone
- Stable internet connection

### Setup
```bash
# Clone repository
git clone https://github.com/viteshthakre/Jarvis.git
cd Jarvis

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run JARVIS
python main.py


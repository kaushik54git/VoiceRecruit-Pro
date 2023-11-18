# VoiceRecruit Pro

VoiceRecruit Pro is an interactive interview application that leverages Azure Cognitive Services Speech SDK for speech recognition and the OpenAI GPT model to generate responses. This application provides a seamless interface for conducting and reviewing interviews.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Starting the Application](#starting-the-application)
  - [Interview Process](#interview-process)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Speech recognition for interview questions.
- Real-time display of interview questions and applicant responses.
- Integration with OpenAI GPT for generating responses.
- Transparent Tkinter GUI for an unobtrusive user experience.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.x
- Azure Cognitive Services Speech SDK
- Tkinter (usually included with Python installations)
- Nice internet connectivity 

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kaushik54git/VoiceRecruit-Pro.git
   ```

2. Install dependencies:

   ```bash
   cd VoiceRecruit-Pro
   pip install -r requirements.txt
   ```

## Usage

### Starting the Application

To start the VoiceRecruit Pro application:

```bash
python VoiceRecruit-Pro.py
```

### Interview Process

1. Speak into your microphone when prompted.
2. Interview questions will be displayed in the Tkinter window.
3. Applicant responses will be recorded and displayed in real-time.
4. GPT-generated responses will be shown in the GUI.

## Configuration

VoiceRecruit Pro can be configured using the following:

- **Azure Cognitive Services Speech SDK**: Set the subscription key and region in the `recognize_from_microphone` function.
## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

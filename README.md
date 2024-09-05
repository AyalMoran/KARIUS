
![chrome_wCbLhEp59f](https://github.com/user-attachments/assets/b150dbb0-9c97-4ae3-bcbe-f11bbd85ea0b)


# KARIUS Dental App

### Overview

The **Karius Dental App** is a specialized application designed to help dental professionals manage patient data and provide diagnostic assistance. It integrates **Speech-to-Text (STT)** capabilities with **Natural Language Understanding (NLU)** to allow hands-free data input and analysis, making the workflow more efficient.

This project uses technologies such as:
- **Google Cloud Speech API** for transcription of dental data.
- **PyQt5** for building the GUI (Graphical User Interface).
- **Natural Language Understanding (NLU)** to parse and understand dental diagnostic terms.
- **Pocketsphinx** for voice activation.

### Features
- **Speech Recognition**: Automatically transcribes spoken words related to dental diagnostics into structured data.
- **Natural Language Understanding**: Processes transcriptions to identify tooth numbers, symptoms, and free text comments.
- **Graphical User Interface**: A table-based UI for viewing and managing teeth information.
- **Allergy Alerts**: Alerts the user when an allergy is detected in the input.
- **Sound Feedback**: Plays audio cues for success, failure, or alerts.

---

### Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/karius-dental-app.git
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scriptsctivate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Google Cloud credentials:
    - Create a project in [Google Cloud](https://console.cloud.google.com/) and enable the Speech-to-Text API.
    - Download the `JSON` credentials file and update the path in the code:
        ```python
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_your_json_file.json'
        ```

5. Run the application:
    ```bash
    python main.py
    ```

---

### Configuration

To use the Google Speech API, make sure you update the configuration with your project credentials.

Additionally, customize phrases and keywords in `STT.py` to enhance the recognition of dental terms.

---

### Usage

1. **Start the App**:
    - The app starts listening for the "wake word" using `pocketsphinx`. Once triggered, it begins recording.
  
2. **Voice Commands**:
    - Speak tooth numbers, diagnoses, and other patient information. The app transcribes and updates the UI in real-time.
  
3. **UI Features**:
    - Manually enter patient details and diagnostic information using the table.
    - Play alerts and confirm diagnoses through the integrated sound system.

---

### Dependencies

- Python 3.8+
- PyQt5
- Google Cloud Speech API
- Pocketsphinx
- SoundDevice
- SoundFile
- Logging

You can install all dependencies using:
```bash
pip install -r requirements.txt
```

---

### Contributing

Feel free to fork the repository, create pull requests, or open issues for new features, bugs, or documentation improvements.

---


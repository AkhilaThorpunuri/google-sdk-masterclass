# Installation

> Venkata Bhattaram (c) 2026

## Contents

- Checking the Python Version
- Creating a Python Virtual Environment
- Installing Dependencies
- Installing the Google Gen AI Python SDK
- Verifying the Installation
- Installation Checklist

## Overview

This Masterclass uses a shared Python environment for all lessons. The environment is configured once and reused throughout the tutorial.

The installation consists of:

- **Python 3.13** — the recommended Python version for this Masterclass.
- **Google Gen AI Python SDK** — the official Python library for interacting with Google's Gemini models.
- **Virtual Environment** — isolates project dependencies inside `.venv`.
- **Requirements File** — records the packages needed to reproduce the environment.

Python 3.13 is selected as the recommended baseline for this Masterclass. Use a supported Python version compatible with the SDK and its dependencies.

## 1. Check the Python Version

Check the Python versions installed on your machine:

```powershell
py --list
```

Check the active Python interpreter:

```powershell
python --version
```

For this Masterclass, Python 3.13 is the recommended baseline.

If Python 3.13 is installed, select it explicitly when creating the virtual environment.

If it is not installed, install Python 3.13 before proceeding.

## 2. Create a Virtual Environment

Open PowerShell in the root directory of the repository.

Create the virtual environment:

```powershell
py -3.13 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Verify the active interpreter:

```powershell
python --version
```

The terminal should display the `(.venv)` prefix when the virtual environment is active.

## 3. Install the Google Gen AI Python SDK

The Google Gen AI SDK is installed using the `google-genai` package.

Install the SDK directly:

```powershell
python -m pip install google-genai
```

Verify the installed package:

```powershell
python -m pip show google-genai
```

Verify that Python can import the SDK:

```powershell
python -c "from google import genai; print('Google Gen AI SDK imported successfully.')"
```

Expected output:

```text
Google Gen AI SDK imported successfully.
```

**Important:** The package name is `google-genai`, but its Python import path is `google.genai`. Do not install the legacy `google-generativeai` package for this Masterclass.

## 4. Verify the Installation

Add the following code to `01-get-started/code/verify_installation.py`:

```python
import sys
from importlib.metadata import version

from google import genai


def main():
    print("Python version:")
    print(sys.version)

    print("\nGoogle Gen AI SDK installation:")
    print(f"Google Gen AI SDK version: {version('google-genai')}")

    print("\nImport verification:")
    print("Google Gen AI SDK imported successfully.")

    print("\nInstallation verified.")


if __name__ == "__main__":
    main()
```

Run the script from the repository root:

```powershell
python 01-get-started/code/verify_installation.py
```

Expected output will resemble:

```text
Python version:
3.13.x ...

Google Gen AI SDK installation:
Google Gen AI SDK version: <installed-version>

Import verification:
Google Gen AI SDK imported successfully.

Installation verified.
```

The version number and detailed Python version will depend on your local environment.

This verification checks the Python interpreter, installed SDK package, and import functionality. It does not make an API request or verify API credentials.

## 5. Installation Checklist

Before proceeding to the next lesson, verify the following:

```text
[ ] Python 3.13 installed
[ ] Python version checked
[ ] Virtual environment created
[ ] Virtual environment activated
[ ] pip upgraded
[ ] Google Gen AI Python SDK installed
[ ] SDK import verified
[ ] verify_installation.py executed successfully
```

## Conclusion

The installation process for this Masterclass is:

```text
Python 3.13
     ↓
Virtual Environment
     ↓
Dependency Configuration
     ↓
Google Gen AI Python SDK
     ↓
Installation Verification
    
```

The core installation is complete when `verify_installation.py` prints:

```text
Installation verified.
```

You can now proceed to the next lesson and begin exploring Google's Gemini models using Python.
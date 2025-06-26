# prints.py

def success(message: str):
    print(f"\033[92m  ✅  {message}\033[00m")

def error(message: str):
    print(f"\033[91m  ❌  {message}\033[00m")

def info(message: str):
    print(f"\033[96m  ℹ️  {message}\033[00m")

def warning(message: str):
    print(f"\033[93m  ⚠️  {message}\033[00m")
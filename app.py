
from datetime import datetime
import platform
import socket

print("=" * 50)
print("AWS JENKINS AUTOMATIC BUILD TEST")
print("=" * 50)

print("Status: Python execution successful")
print("Machine:", socket.gethostname())
print("Python Version:", platform.python_version())
print("Execution Time:", datetime.now())

print("\nJenkins successfully executed app.py!")
print("=" * 50)

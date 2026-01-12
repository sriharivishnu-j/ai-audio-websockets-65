# Real-time AI Audio Analysis with Python and WebSockets

## Overview

This project demonstrates a real-time audio analysis service using FastAPI and WebSockets. The service receives audio data, analyzes it using AI techniques, and returns the analysis results.

## Setup and Installation

1. Clone the repository:
    bash
    git clone <repository_url>
    cd <repository_directory>
    

2. Install dependencies:
    bash
    pip install -r requirements.txt
    

3. Run the service:
    bash
    ./run.sh
    

4. Access the WebSocket endpoint at `ws://localhost:8000/ws/audio`.

## Testing

Run the unit tests to verify the functionality:
bash
python -m unittest discover -s tests

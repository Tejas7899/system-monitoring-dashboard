# System Monitoring Dashboard

## Overview
A lightweight Python-based monitoring system designed to track CPU and memory usage through REST APIs. The project focuses on system visibility, runtime monitoring, and backend reliability.

## Features
- Real-time CPU monitoring
- Memory usage tracking
- REST API endpoint
- JSON-based responses
- Runtime behavior analysis

## Tech Stack
- Python
- Flask
- psutil
- REST APIs
- Linux

## Project Structure

```bash
system-monitoring-dashboard/
│
├── app.py
├── requirements.txt
└── README.md
```

## API Endpoint

```bash
/system
```

### Sample Response

```json
{
  "cpu_percent": 15.4,
  "memory_percent": 42.1
}
```

## Setup Instructions

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run application

```bash
python app.py
```

## Future Improvements
- Docker deployment
- Real-time dashboard
- Alert notification system
- Database integration
- Process-level analytics

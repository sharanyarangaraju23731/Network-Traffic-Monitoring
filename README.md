# Network Traffic Monitoring and Anomaly Detection Simulator

## Overview

The Network Traffic Monitoring and Anomaly Detection Simulator is a Python-based Computer Networks project that demonstrates client-server communication, simulated network traffic generation, and rule-based anomaly detection.

The client generates 500 traffic records at approximately one-second intervals and sends them to a server using TCP socket programming. The server analyses the traffic rates, classifies unusual records, and stores the results in a log file. A Streamlit dashboard displays traffic statistics, visualizations, and detected anomalies, refreshing approximately every two seconds.

## Features

- **Traffic Simulation:** Generates 500 traffic records with source IP, destination IP, protocol, packet size, and traffic rate.
- **TCP Socket Communication:** Transfers traffic records between the client and server.
- **Anomaly Detection:** Identifies traffic records with rates exceeding 150 packets per second.
- **Traffic Logging:** Stores processed records in a JSON Lines file.
- **Interactive Dashboard:** Displays traffic statistics, protocol distribution, and traffic grouped by source IP.
- **Anomaly Visualization:** Displays records classified as anomalous.
- **CSV Export:** Allows users to download traffic data as a CSV file.
- **Automatic Dashboard Refresh:** Updates the dashboard approximately every two seconds.

## Technologies Used

- Python
- TCP Socket Programming
- JSON
- Pandas
- Streamlit

## Project Structure

```text
Network-Traffic-Monitoring/
├── server.py
├── client.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `traffic_log.jsonl` file is generated automatically when the server processes traffic records. It is excluded from Git using `.gitignore`.

## System Architecture

1. **Client (`client.py`):** Generates simulated traffic records and sends them to the server.
2. **Server (`server.py`):** Receives records, applies the anomaly detection rule, and saves the processed data.
3. **Traffic Log (`traffic_log.jsonl`):** Stores each processed record as a separate JSON line.
4. **Dashboard (`app.py`):** Reads the log and displays traffic statistics and detected anomalies.

## Anomaly Detection Method

The project uses a fixed threshold-based rule to classify traffic records.

| Traffic Rate | Classification |
|---|---|
| 150 packets per second or less | Normal |
| Greater than 150 packets per second | Anomaly |

The client generates traffic rates between 10 and 100 for most records. Approximately 20% of records are assigned higher rates between 200 and 500 to demonstrate anomaly detection.

This is a rule-based approach and does not use a machine-learning model.

## Installation and Setup

### Prerequisites

- Python 3 installed
- Git installed
- Internet connection for installing the required Python packages

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Network-Traffic-Monitoring.git
cd Network-Traffic-Monitoring
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the Server

Open a terminal in the project directory and run:

```bash
python server.py
```

Keep the server running.

### 4. Start the Client

Open a second terminal in the same project directory and run:

```bash
python client.py
```

The client sends 500 traffic records, with approximately a one-second delay between records.

### 5. Launch the Dashboard

Open a third terminal and run:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

http://localhost:8501

The dashboard refreshes approximately every two seconds to display newly processed records.

## Expected Output

The dashboard displays:

- Total number of traffic records
- Sum of recorded traffic-rate values
- Number of detected anomalies
- Protocol distribution chart
- Traffic grouped by source IP
- Detected anomaly records
- Complete traffic log
- CSV download option

## Limitations

- The project simulates network traffic rather than capturing actual network packets.
- IP addresses, packet sizes, and protocol labels are generated for demonstration.
- The client-server connection uses TCP, even though the simulated records may contain either TCP or UDP as their protocol label.
- Anomaly detection uses a fixed threshold and does not confirm real cyberattacks.
- The dashboard visualizes the generated records rather than monitoring a live external network.

## Future Enhancements

- Add real network packet capture.
- Introduce additional traffic analysis rules.
- Implement statistical or machine-learning-based anomaly detection.
- Store traffic records in a database.
- Add more advanced visualizations and filtering options.

## Project Purpose

This project demonstrates fundamental Computer Networks concepts, including TCP socket programming, client-server architecture, traffic logging, and basic anomaly detection through a visual monitoring interface.

## Author

Developed as a Computer Networks academic project.

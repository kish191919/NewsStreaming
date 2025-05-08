# 🕴️ News Streaming Pipeline

A real-time news ingestion pipeline built on **Python → Kafka → Logstash → Elasticsearch → Kibana**, running on an AWS EC2 instance.

---

## 📌 Overview

This project scrapes top U.S. headlines using [NewsAPI.org](https://newsapi.org), sends them to an Apache Kafka topic, and uses Logstash to forward structured JSON data to Elasticsearch. Kibana is used to visualize and analyze the data.

---

## 🔧 Tech Stack

* **Python** — News scraping and Kafka producer
* **Apache Kafka + Zookeeper** — Real-time messaging
* **Logstash** — Kafka to Elasticsearch connector
* **Elasticsearch** — Full-text search and storage
* **Kibana** — Data visualization and dashboards
* **Ubuntu 24.04** — EC2 instance OS

---

## 🚀 Setup Guide
### 1. git clone this repo
### 2. Create Python Virtual Environment

```bash
sudo apt update
sudo apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
pip install -U pip dotenv requests kafka-python
```

### 3. Run the News Scraper

```python
# See full code in the repo
```

This script fetches news every second and pushes JSON-formatted data to Kafka.

### 4. Install & Start Kafka and Zookeeper

```bash
sudo apt install openjdk-11-jdk
wget https://downloads.apache.org/kafka/3.7.2/kafka_2.12-3.7.2.tgz
tar -xzf kafka_2.12-3.7.2.tgz && mv kafka_2.12-3.7.2 kafka
```

```bash
# Start services
nohup kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties &
nohup kafka/bin/kafka-server-start.sh kafka/config/server.properties &
```

Create topic:

```bash
kafka/bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 5. Logstash + Elasticsearch + Kibana Setup

```bash
# Add Elastic GPG and Repo
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
sudo apt update

# Install tools
sudo apt install elasticsearch logstash kibana
```

#### Elasticsearch Configuration

```bash
sudo vi /etc/elasticsearch/elasticsearch.yml
# Add:
xpack.security.enabled: false
sudo systemctl restart elasticsearch
```

#### Kibana Configuration

```bash
sudo vi /etc/kibana/kibana.yml
# Add:
server.host: "0.0.0.0"
elasticsearch.hosts: ["http://localhost:9200"]
sudo systemctl start kibana
```

### 6. Create `logstash.conf`

```bash
sudo /usr/share/logstash/bin/logstash -f /home/ubuntu/news/logstash.conf
```

---

## 📊 Visualizing with Kibana

* Go to `http://<your-ec2-ip>:5601`
* Create Index Pattern: `news-articles*`
* Use `publishedAt` as time field
* Navigate to Discover to view real-time news flow


---

## 🧭 Final Goal

Stream real-time news to Kafka → Analyze with Elasticsearch → Visualize via Kibana

---

## 📄 License

MIT License © 2025


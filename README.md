# Search with Elasticsearch


## 1. [Local development installation](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/local-development-installation-quickstart)
* Try Elasticsearch and Kibana locally
* [Start local](https://github.com/elastic/start-local)
```
$curl -fsSL https://elastic.co/start-local | sh

  ______ _           _   _      
 |  ____| |         | | (_)     
 | |__  | | __ _ ___| |_ _  ___ 
 |  __| | |/ _` / __| __| |/ __|
 | |____| | (_| \__ \ |_| | (__ 
 |______|_|\__,_|___/\__|_|\___|
-------------------------------------------------
🚀 Run Elasticsearch and Kibana for local testing
-------------------------------------------------

ℹ️  Do not use this script in a production environment

⌛️ Setting up Elasticsearch and Kibana v9.1.3-arm64...

- Generated random passwords
- Created the elastic-start-local folder containing the files:
  - .env, with settings
  - docker-compose.yml, for Docker services
  - start/stop/uninstall commands
- Running docker compose up --wait
```

## 2. Read ans store data in Elasticsearch
* Local LLM with Ollama

```
$pip install -r requirements.txt
$python step_01_read_and_store_data.py
```
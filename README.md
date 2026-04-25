# python_docker_sample

## 1. Environment
- macOS（MacBook Pro / Apple Silicon）
- Docker Desktop（Apple Silicon対応）
- Python 3.11（Dockerコンテナ内）
- Libraries
    - numpy
    - pandas
    - matplotlib
    - opencv-python

## 2. Install and Build
### 2.1 Clone the repository
```
git clone git@github.com:TakuKarasawa/python_docker_sample.git
cd python_opencv_docker_sample
```

### 2.2 Start and enter the container
```
docker compose up -d --build
docker exec -it python_env bash
```

### 2.3 Confirm the environment
```
python --version
pip list
```

## 3. How to use
### 3.1 Move to script directory
```
cd /workspace/script
```

### 3.2 Run sample code
```
python normal_distribution.py
```

## 4. Clean up
```
docker compose down
```

イメージも削除する場合は
```
docker compose down --rmi all
```
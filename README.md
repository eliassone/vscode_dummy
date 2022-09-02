# Virtual environment
## 1. Setting up your virtual environment
```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

## 2. Running an entry point script
```bash
python3 src/entries/helloapp.py

python3 src/entries/env.py

python3 src/entries/cwd.py -c ..

python3 src/entries/secrets.py -A

python3 src/entries/logging_sensitive.py
```

## 3. Running interactive notebook
```bash
pip install ipykernel
```
Execute the different cells in `interactive/py1.py` and `interactive/py2.py`

# Docker
## 1. Building the image
```bash
export TAG=helloapp1:local-test

docker build -t $TAG .
```

## 2. Running the image
Sample commands:
```bash
docker run $TAG bash -c "python entries/helloapp.py"

docker run -v $PWD/secrets-store:/app/secrets-store $TAG bash -c "python entries/secrets.py -A"
```

## 3. Running the image interactively
```bash
docker run -v $PWD/secrets-store:/app/secrets-store -t -i --rm $TAG bash
```
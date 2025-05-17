# FastAPI Dummy ML Service
+
This repository demonstrates a minimal FastAPI application wired to a dummy ML model. The model simply doubles input values.
+
## Project Structure
+
```
.
├── api/                   # FastAPI application & schemas
├── ml/                    # ML model code & loader utility (dummy)
├── requirements.txt       # Python dependencies
└── pyenv/                 # Python virtual environment (ignored by git)
```
+
## Installation
+
1. **Create and activate** the Python virtual environment:
+
   ```bash
   python -m venv pyenv
   # Linux/macOS
   source pyenv/bin/activate
   # Windows
   pyenv\Scripts\activate
   ```
+
2. **Install** dependencies:
+
   ```bash
   pip install -r requirements.txt
   ```
+
## Usage
+
Start the FastAPI server:
+
```bash
uvicorn api.main:app --reload
```
+
Open your browser and navigate to `http://127.0.0.1:8000/docs` for the interactive API docs.
+
### Example
+
```bash
curl -X POST "http://127.0.0.1:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"data":[1,2,3]}'
```
+
Response:
+
```json
{"predictions":[2,4,6]}
```
+
## Next Steps
+
- Replace the dummy model with your actual ML artifact.
- Add input validation and error handling.
- Implement unit and integration tests.
- Harden the API (authentication, rate limiting, etc.).
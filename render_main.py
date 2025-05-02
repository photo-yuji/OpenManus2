import sys
import os
sys.path.append(os.path.dirname(__file__))

# render_main.py

from app.server import app  # ← OpenManus の本体 FastAPI アプリ

# これで uvicorn が app を認識できるようになる

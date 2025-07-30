#!/usr/bin/env python3
"""
VeriVigil Banking Fraud Detection API - Render Production Starter
Optimized for Render.com deployment
"""

import os
import uvicorn
from fraud_detection_api.api.main_simple import app

if __name__ == "__main__":
    # Render ortam değişkenlerini al
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    print(f"🏦 VeriVigil Banking API starting on {host}:{port}")
    print(f"🌍 Environment: {os.environ.get('ENVIRONMENT', 'production')}")
    
    # Production-ready settings
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info",
        access_log=True,
        workers=1  # Render free tier için optimize
    )

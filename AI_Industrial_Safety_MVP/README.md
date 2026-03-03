# AI Industrial Safety MVP

Enterprise-level Industrial Safety Monitoring System with:
- Multi-camera support
- Helmet & Mask compliance logic
- Violation logging
- REST API backend (FastAPI)
- Streamlit dashboard

Run main engine:
python app/main.py

Run API:
uvicorn app.api:app --reload

Run dashboard:
streamlit run dashboard/dashboard.py

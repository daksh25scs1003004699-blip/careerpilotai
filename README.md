# CareerPilot AI — Job Role Recommendation System

A Streamlit and scikit-learn KNN nearest-neighbor educational career recommender.

## Setup (Windows)

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

Select skills in the sidebar, then explore role matches, employer career portals, interview tips, hackathon ideas, and 30/60/90-day roadmaps.

## Model

Uses MultiLabelBinarizer for skills, a small interest weighting, NearestNeighbors with cosine distance, and all 12 curated role profiles. Similarity is not a probability or evidence of hiring readiness. This is a content-based recommender; it is not trained on employment outcomes.

## Limitations and next steps

- Skill profiles and employer-role associations are illustrative, not sourced from a labor market dataset.
- Employer links go to general career pages; live job vacancies are not checked.
- Guidance is curated templates, not generative AI.
- Expand and validate datasets, test with held-out profiles and user feedback, and optionally integrate an LLM with appropriate privacy controls.

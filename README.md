# LLM Evaluation Platform

Automated quality assurance platform for evaluating LLM prompt–response datasets. Built to demonstrate LLM Ops, evaluation pipelines, and responsible AI practices for AI/ML engineering roles.

## Features

- **Semantic similarity scoring** using `sentence-transformers`
- **Response quality checks** (empty, too short, repetition, prompt overlap)
- **Toxicity screening** with rule-based detection
- **Overall pass/fail score** with weighted metrics
- **Model comparison dashboard** by `model_name`
- **CSV report export** for audit trails

## Tech Stack

- Python
- Streamlit
- sentence-transformers
- pandas, scikit-learn, plotly

## Project Structure

```
llm-eval-platform/
├── app.py
├── evaluator/
│   ├── similarity.py
│   ├── quality.py
│   ├── toxicity.py
│   └── report.py
├── data/
│   └── sample.csv
├── requirements.txt
└── README.md
```

## Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501`.

## CSV Format

Your upload must include these columns:

| Column | Required | Description |
|---|---|---|
| `prompt` | Yes | Input prompt given to the model |
| `response` | Yes | Model-generated answer |
| `expected` | Yes | Reference / gold answer |
| `model_name` | No | Model label for comparison |

## Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo and set main file to `app.py`
4. Add live URL to your resume

## Resume Bullet Examples

- Built an LLM evaluation platform with automated semantic, quality, and toxicity scoring for 1,000+ prompt–response pairs
- Implemented side-by-side model comparison dashboard and exportable QA reports for LLM training workflows
- Deployed a Streamlit-based LLM QA tool supporting batch evaluation and pass-rate analytics

## Author

**Rushikesh Kolhe** — 3rd Year B.Tech AI & DS, Sanjivani University  
GitHub: [mgneropj](https://github.com/mgneropj)

## License

MIT

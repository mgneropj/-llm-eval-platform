# 🧠 LLM Evaluation Platform

> **Automated quality assurance platform for evaluating LLM prompt–response datasets.**

Built to demonstrate practical **LLM Ops, evaluation pipelines, model comparison, and responsible AI practices** for AI/ML engineering roles.

---

## 🚀 Overview

Large Language Models can generate thousands of responses, making manual quality checking difficult and inconsistent.

This project provides an automated evaluation pipeline that analyzes prompt–response datasets using multiple quality and safety signals.

The platform calculates individual evaluation metrics, produces an overall **pass/fail assessment**, compares model performance, and exports results for further analysis or auditing.

---

## ✨ Features

### 🧠 Semantic Similarity

Measures the semantic similarity between the model-generated response and the expected/reference answer using:

* `sentence-transformers`
* Embedding-based similarity scoring

### ⭐ Response Quality Checks

Automatically checks responses for common quality issues:

* Empty responses
* Very short responses
* Repetitive content
* Prompt overlap

### 🛡️ Toxicity Screening

Performs rule-based toxicity detection to identify potentially problematic language in generated responses.

### 📊 Overall Evaluation Score

Combines evaluation metrics using weighted scoring to produce an overall result:

```text
Prompt + Response + Expected Answer
                │
                ▼
       ┌─────────────────┐
       │ Evaluation      │
       │ Pipeline        │
       └────────┬────────┘
                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
 Similarity  Quality   Toxicity
      │         │         │
      └─────────┼─────────┘
                ▼
        Weighted Scoring
                │
                ▼
          PASS / FAIL
```

### ⚖️ Model Comparison

Compare evaluation performance across different models using the `model_name` field.

This helps identify differences in:

* Average evaluation score
* Pass rate
* Semantic similarity
* Response quality
* Safety signals

### 📄 CSV Report Export

Export evaluation results as CSV files to support:

* Audit trails
* Offline analysis
* Model benchmarking
* Reporting

---

## 🛠️ Tech Stack

| Technology                | Purpose                          |
| ------------------------- | -------------------------------- |
| **Python**                | Core programming language        |
| **Streamlit**             | Interactive evaluation dashboard |
| **sentence-transformers** | Semantic similarity              |
| **Pandas**                | Dataset processing               |
| **Scikit-learn**          | Similarity/scoring utilities     |
| **Plotly**                | Interactive visualizations       |

---

## 🏗️ Project Structure

```text
llm-eval-platform/
│
├── app.py
│
├── evaluator/
│   ├── similarity.py    # Semantic similarity scoring
│   ├── quality.py       # Response quality checks
│   ├── toxicity.py      # Toxicity screening
│   └── report.py        # Report generation/export
│
├── data/
│   └── sample.csv       # Example evaluation dataset
│
├── requirements.txt
└── README.md
```

---

## 🔄 Evaluation Pipeline

The application follows a modular evaluation workflow:

```text
CSV Dataset
     │
     ▼
Data Validation
     │
     ▼
┌───────────────────────────┐
│     Evaluation Engine     │
├───────────────────────────┤
│ • Semantic Similarity     │
│ • Quality Checks          │
│ • Toxicity Screening      │
│ • Weighted Scoring        │
└─────────────┬─────────────┘
              │
              ▼
       Model Comparison
              │
              ▼
     Dashboard + Reports
```

---

## 📁 CSV Format

The uploaded CSV file must include the following columns:

| Column       | Required | Description                     |
| ------------ | :------: | ------------------------------- |
| `prompt`     |     ✅    | Input prompt given to the model |
| `response`   |     ✅    | Model-generated answer          |
| `expected`   |     ✅    | Reference / gold answer         |
| `model_name` | Optional | Model label used for comparison |

### Example

```csv
prompt,response,expected,model_name
"What is machine learning?","Machine learning is a branch of AI...","Machine learning is a subset of AI...","Model-A"
"Explain RAG","RAG combines retrieval with generation...","RAG retrieves relevant information before generation...","Model-B"
```

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/mgneropj/-llm-eval-platform.git
cd -llm-eval-platform
```

### 2. Create a virtual environment

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

Open the application at:

```text
http://localhost:8501
```

---

## ☁️ Deploy on Streamlit Community Cloud

The application can be deployed using Streamlit Community Cloud.

### Steps

1. Push the project to GitHub
2. Connect the repository to Streamlit Community Cloud
3. Select the `main` branch
4. Set the main application file to:

```text
app.py
```

5. Deploy the application
6. Add the live application URL to your resume and portfolio

---

## 🎯 Use Cases

This platform can be used for:

* LLM response quality assurance
* Prompt engineering experiments
* Model benchmarking
* Batch evaluation of LLM outputs
* Responsible AI testing
* LLM Ops experimentation
* Comparing different model versions
* Creating evaluation datasets and audit reports

---

## 💼 Resume Highlights

This project demonstrates experience with:

* LLM evaluation pipelines
* Semantic similarity
* Automated quality assurance
* Responsible AI concepts
* Model benchmarking
* Data processing
* Interactive dashboards
* Modular Python architecture
* Batch evaluation workflows

### Example Resume Bullets

* **Built an LLM evaluation platform** with automated semantic similarity, response quality, and toxicity scoring for large prompt–response datasets.

* **Developed a model comparison dashboard** for analyzing LLM performance using weighted evaluation metrics and pass-rate analytics.

* **Implemented exportable evaluation reports** to support reproducible QA workflows, model benchmarking, and audit trails.

---

## 🔮 Future Improvements

Planned improvements include:

* [ ] LLM-as-a-Judge evaluation
* [ ] Hallucination detection
* [ ] RAG-specific evaluation metrics
* [ ] BLEU / ROUGE metrics
* [ ] Support for additional LLM providers
* [ ] Evaluation history and database storage
* [ ] Advanced analytics dashboard
* [ ] Automated benchmark datasets
* [ ] CI/CD integration
* [ ] Production deployment

---

## 👨‍💻 Author

### Rushikesh Kolhe

**3rd Year B.Tech — Artificial Intelligence & Data Science**
**Sanjivani University**

GitHub: **[@mgneropj](https://github.com/mgneropj)**

---

## ⭐ Project

If you find this project interesting, consider giving the repository a ⭐.

**Repository:**
https://github.com/mgneropj/-llm-eval-platform

---

## 📄 License

This project is licensed under the **MIT License**.

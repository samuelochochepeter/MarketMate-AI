# MarketMate AI
## AI-assisted Sales Analytics and Social Media Planning for Nigerian Small Businesses

Prepared for Samuel Ochoche Peter, AI Skills Development, a 3MTT & Meta programme delivered by RAIN Nigeria. Independent learner prototype, not an official programme product.

## Start here

1. Install Python 3.11 or newer (Python 3.11 recommended for the pinned packages).
2. Extract the entire ZIP and open a terminal in the `MarketMate_AI` folder.
3. Create an environment: `python -m venv .venv`
4. Activate it on Windows: `.venv\Scripts\activate` or macOS/Linux: `source .venv/bin/activate`
5. Install dependencies: `python -m pip install -r requirements.txt`
6. Run: `python app/server.py`
7. Open **http://127.0.0.1:8501** in your browser. Keep the terminal open.

On Windows, you can also double-click `Start_Windows.bat` after installing Python. The first run installs dependencies and requires an internet connection. On macOS/Linux, run `sh start.sh`.

The app loads a fictional bakery dataset immediately. It calculates KPIs, compares social formats, evaluates a random forest against a mean baseline, estimates next-day demand and builds evidence-based content prompts. You can upload your own matching CSV files. The program is intended for a single user on a local computer.

## Optional genuine Llama generation

Install Ollama using https://ollama.com/download and start it. In a separate terminal:

```
ollama pull llama3.2
ollama pull llama3.2-vision
```

The second download is optional and substantially larger. Confirm that your computer has sufficient memory and disk space before downloading. The text model supports Content Studio generation. The vision model supports Product Lens image analysis. The app calls only `http://127.0.0.1:11434/api/chat`. It has no cloud account or API key requirement. Llama inference was not executed during package verification because model weights were unavailable. The connection and error handling are implemented. Test these features on your machine before demonstrating them.

Without Ollama, use **Build content prompt**, copy it into Meta AI, review the generated response, and save evidence of the prompt and output. The app does not pretend that a prepared prompt is an AI-generated result.

## Contents

- `app/`: web interface, Python local server and analytics/ML source.
- `data/`: 120 synthetic daily sales rows and 36 synthetic social posts.
- `docs/Project_Report.pdf` and `.md`: report and editable text source.
- `docs/Pitch_Deck.pptx`: editable five-slide pitch with presenter notes.
- `docs/Pitch_Deck.pdf`: presentation copy.
- `docs/Demo_and_Defence.md`: demonstration steps, pitch and defence questions.
- `docs/Prompt_Library.md`: reusable prompts, comparison rubric and iteration log.
- `docs/Validation_Workbook.md`: user research and usability worksheets to complete honestly.
- `docs/Campaign_Plan.csv`: seven-day illustrative marketing plan.
- `docs/demo_analysis.json`: reproducible numerical outputs.
- `docs/Test_Results.txt`: results of automated package checks.
- `tests/`: meaningful arithmetic, input and temporal leakage tests.
- `analysis.ipynb`: notebook that reproduces the analytics and model evaluation.

## Data definitions

Sales: `date,units,unit_price,promo,ad_spend`. One product, one daily record. Price and spend are NGN. `promo` is 0 or 1. Units are nonnegative whole numbers. Revenue is calculated as units × unit price, before costs. Gaps are allowed and are not silently filled with zero sales.

Social: `date,platform,format,reach,likes,comments,shares,saves,clicks,leads,spend`. Each row represents one post. Numeric counts must be nonnegative whole numbers. Spend is NGN. `leads` means enquiries attributed in the source record; the app cannot verify the attribution. Do not join the datasets and claim post-level sales attribution because they lack a reliable linking identifier. Summed post reach is not deduplicated audience reach.

Exact duplicate rows are removed and counted. Invalid dates, missing required values, conflicting sales dates, negative values and non-finite numbers are rejected. Social posts that happen to have completely identical rows are treated as duplicates; add distinct timestamps or post IDs in a future version if needed. Extra columns are ignored. Uploaded records and images are not saved by the app. The downloaded JSON contains sales history: review it before sharing.

## Reproduce checks

```
python -m unittest discover -s tests -v
```

For the optional notebook interface, install JupyterLab separately with `python -m pip install jupyterlab` and launch `jupyter lab`. Run notebook cells from the project folder or follow the notebook's path detection. Use the report to understand why the split is chronological and why synthetic-data results do not prove commercial effectiveness.

## Before submission

Read the full project and run the demo yourself. Check the organiser's rubric, required tools, file format and deadline. Complete real user testing if required. Add screenshots and authentic Meta AI/Llama interaction evidence. Disclose AI assistance according to programme policy. No interviews, customer adoption, revenue improvement, programme endorsement or successful Llama inference are claimed in this package.

## Technical references

- Course slides provided by the learner: `1a.pdf`–`4d.pdf`, particularly `3a.pdf` p4, `3d.pdf` p27, `4b.pdf` p11–19, `4c.pdf` p15–21 and `4d.pdf` p6–18.
- https://docs.ollama.com/api/chat
- https://ollama.com/library/llama3.2-vision
- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html

References checked 4 November 2026. Demo records are synthetic and generated with random seed 42. Python dependencies are pinned to the versions used during numerical verification.

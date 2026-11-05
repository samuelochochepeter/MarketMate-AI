# Demonstration and defence guide

## Five-minute demonstration

1. Start `python app/server.py` and open http://127.0.0.1:8501. Explain that Sunrise Bakes is fictional and all supplied records are synthetic.
2. Explain the revenue total and engagement formula. Compare Reels and Images. Note that the Facebook Image group has more leads than either Reel group even though its engagement rate is lower. The best format depends on the objective.
3. Open Demand Lab. Explain the 96/24 chronological split, MAE in units and mean baseline. Estimate the next day with a different promotion setting. Explain that this is an association learned from synthetic records, not an experiment proving a promotion causes more sales.
4. Open Content Studio, enter your own business brief and select Build content prompt. Point out Role, Context, Task, Constraints and Format. Download the prompt. If Ollama is running, select Generate with local Llama. Otherwise show an authentic, saved Meta AI response you produced yourself.
5. If you have tested Llama 3.2 Vision successfully, choose a non-sensitive product photo and demonstrate alt text and caption drafting. Otherwise explain the implemented connection and its unverified local-inference status. Do not claim you ran it.
6. Download the analysis JSON. Explain one next experiment, the privacy choices and the remaining real-user validation.

## 90-second pitch

Many small-business owners keep sales in one place and social media results in another. Our project investigates whether combining these records with a clear content workflow could help them plan their next business action. This problem is a hypothesis awaiting customer validation.

MarketMate AI is my prototype for that workflow. It calculates sales and content metrics, compares social formats, evaluates a demand model and turns the evidence into a structured prompt for a seven-day campaign. Optional local Llama generation supports text drafting, while Llama 3.2 Vision can support product descriptions and alt text on suitable hardware.

The current demonstration uses 120 synthetic daily sales records and 36 synthetic social posts. On the chronological test set, the model's mean absolute error is 2.902 units, compared with 7.715 units for a mean baseline. These results verify the demonstration pipeline. They do not prove commercial impact.

The initial target is small businesses selling one main product and maintaining basic records. A proposed monthly subscription is only a pricing hypothesis. My next step is to test the workflow with five owners, record where they struggle and measure whether it helps them complete a campaign plan. I am seeking access to those pilot users and feedback on the prototype.

## Likely questions

**What problem does the project solve?** It brings separate sales and social-post summaries into one planning workflow. Whether owners value this enough to adopt or pay remains untested.

**Where did the data come from?** A reproducible random seed generated fictional bakery records. They are not customer data or programme-provided market evidence.

**Which parts are actually AI?** RandomForestRegressor learns a demand-estimation function from historical features. Optional Llama generates text from a structured prompt and optional Llama 3.2 Vision interprets an image. Basic KPI calculations and prompt assembly are deterministic code.

**Why random forest?** It handles nonlinear relationships and mixed numerical/binary predictors without scaling. It is straightforward to compare against a simple baseline. It can overfit and extrapolates poorly beyond the observed feature range.

**How did you avoid leakage?** Sort dates first, use the first 80% for training and last 20% for evaluation, exclude units/revenue from inputs, and finish evaluation before refitting for the next-day scenario. A test changes holdout target values and confirms that holdout predictions remain unchanged.

**Why not call the MAE an accuracy percentage?** This is regression. MAE measures error in units. It is not classification accuracy.

**Can you prove social posts caused the sales?** No. The files have no valid conversion-level linking key and the project makes no causal attribution claim.

**What happens without Ollama?** Numerical analysis and prompt preparation still work. The user can run the prompt manually in Meta AI. The app reports local model unavailability instead of fabricating a response.

**Does Llama 3.2 text handle images?** The app uses a separate `llama3.2-vision` model for images. The text-only model does not perform the vision task.

**What was tested?** Numerical formulas, invalid inputs, duplicate handling, chronology, leakage resistance, prompt structure, local HTTP routes and local-model error handling. Successful model inference and external customer effectiveness remain unverified.

**How does this align with responsible AI?** Minimise data, avoid personal identifiers, label synthetic records, disclose AI assistance, treat labels/images as untrusted input and require human review before publishing.

**How would you improve it?** Collect consented real records, add post identifiers, compare time-series baselines, evaluate across several temporal splits, measure forecast intervals, test with actual owners and then decide whether persistence or authentication is needed.

## Suggested AI-use disclosure

I developed this project with AI assistance for planning, code drafting, documentation and presentation preparation. I am responsible for reviewing, running and understanding the submitted work. The supplied dataset is synthetic. I have not claimed real customer interviews, measured business improvement or live Llama inference unless supported by additional evidence I attach. I will follow the programme's AI-use and attribution rules.

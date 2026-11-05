# MarketMate AI
## AI-assisted Sales Analytics and Social Media Planning for Nigerian Small Businesses

Samuel Ochoche Peter
4 November 2026


# Project overview


## Abstract

MarketMate AI is a local prototype that combines business analytics, a machine-learning demonstration and structured generative-AI prompting for small Nigerian businesses. The workflow begins with daily sales and social-post records, calculates auditable metrics, evaluates a demand-estimation model and prepares an evidence-led content brief. Optional local Llama inference supports text drafting and product-image interpretation. The demonstration uses 120 synthetic daily sales records and 36 synthetic social posts. No real customer validation or measured business impact is claimed.


## Project identity

Prepared for Samuel Ochoche Peter. Programme: AI Skills Development, a 3MTT & Meta programme delivered by RAIN Nigeria. Project title: AI-assisted Sales Analytics and Social Media Planning for Nigerian Small Businesses. Prototype name: MarketMate AI. Prepared 4 November 2026. This is an independent learner project and does not imply programme endorsement.


## Scope and status

Implemented: CSV validation, deterministic KPIs, content-format comparison, chronological model evaluation, next-day scenarios, reusable prompt assembly, local text/vision connection code and export. Verified: numerical calculations and software behaviour described in the test record. Not yet verified: successful local Llama inference, real-user usefulness, willingness to pay or business outcomes. The organiser's formal final-project rubric was not available when this package was prepared.


## Keywords

Generative AI, data analytics, social media marketing, random forest regression, prompt engineering, Llama 3.2 Vision, responsible AI, small businesses.


# Problem and objectives


## Problem hypothesis

Some owner-managers may keep sales records and social media metrics in separate tools and struggle to turn them into a clear campaign plan. The hypothesised root cause is a gap between record collection, interpretation and action. This statement requires evidence from owners. It is not presented as a verified market finding.


## Target user hypothesis

The initial persona is an owner-manager selling one main product, keeping daily sales records and promoting the business on Facebook or Instagram. A fictional Port Harcourt bakery, Sunrise Bakes, provides a consistent demonstration context. Laptop access and the ability to install Python remain adoption assumptions. The product does not assume that every owner has these resources.


## Objectives

1. Validate daily sales and post-level marketing records. 2. Calculate understandable sales and campaign indicators. 3. Compare a demand model with a simple baseline on unseen dates. 4. Produce structured prompts grounded in calculated evidence. 5. Offer an optional product-image workflow using Llama 3.2 Vision. 6. Define real-user experiments and responsible-AI controls.


## Research questions

Can owners provide the required data? Can they understand the metrics and complete a content-planning task? Does the model outperform a baseline beyond the synthetic demonstration? Can generated drafts remain grounded and culturally appropriate after human review? Would the proposed workflow fit owners' devices and current routines?


# Alignment with the course


## GenAI in Data Analytics

The prototype calculates metrics in code before asking a language model to interpret them. It separates numerical evidence from generated language and makes its formulas inspectable. The prompt explicitly rejects invented figures and causal claims.


## GenAI in Social Media Marketing

The content studio supports an audience-specific, seven-day campaign brief with caption, CTA, KPI and accessibility ideas. The package includes an illustrative campaign calendar, a video storyboard and a controlled A/B-test plan. No campaign has been published or measured.


## Machine Learning

A random forest regressor uses weekday, unit price, promotion status and ad spend to estimate daily units. The project defines the prediction target, a time-ordered holdout, a mean baseline and error metrics. The notebook reproduces the evaluation.


## Prompt Engineering with Llama 2 & 3

The prompt library applies Role, Context, Task, Constraints and Format, along with examples, revision and prompt chaining. Llama 3.2 is the selected text runtime for the optional local connection. Llama 2 is not separately integrated. Weak-to-strong prompt versions are designed examples pending authentic execution and scoring.


## Introducing Multimodal Llama 3.2

A separate image endpoint sends a resized product image and instructions to llama3.2-vision through local Ollama. It requests visible features, alt text and a cautious caption. Text Llama 3.2 and Llama 3.2 Vision have different roles. The implemented connection requires local model installation and has not been inference-tested here.


## Build the Future

The project follows the course's sequence of problem, assumptions, customer persona, business model, prototype, feedback and pitch. Validation worksheets preserve the distinction between a proposed experiment and collected evidence.


# Data and preparation


## Source and boundaries

All supplied records are synthetic. A pseudorandom generator with seed 42 constructs a single-product bakery scenario. Sales cover 1 July to 28 October 2026. The 36 social posts cover a subset of that period. Record counts represent demonstration choices, not research sample sizes or market estimates. The datasets cannot establish post-level sales attribution.


## Sales schema

date: day in YYYY-MM-DD format. units: whole units sold. unit_price: NGN per unit. promo: promotion flag 0 or 1. ad_spend: daily NGN advertising spend. One row represents one day for one product. Revenue is derived as units multiplied by unit price. It is not profit.


## Social schema

date, platform and format identify the recorded post context. reach, likes, comments, shares, saves, clicks and leads are nonnegative counts. spend is NGN spent on the post. Summed post reach may count the same person repeatedly. Reported leads are accepted from the input and their attribution is not independently verified.


## Quality rules

Remove and count exact duplicate rows. Reject empty datasets, more than 10,000 rows, invalid dates, missing required numeric values, non-finite numbers, negative counts, fractional counts and promotion flags outside 0/1. Reject conflicting daily sales rows. Ignore extra fields. Warn when leads exceed clicks. Do not fill unrecorded dates with zero sales.


## Limitations

Daily records must describe a single consistent product. A changing product mix would confound unit price and demand. Identical social rows are treated as duplicates because the current schema has no post identifier. Real use needs explicit post IDs, collection guidance and attribution definitions.


# System design and implementation


## Architecture

A browser interface calls a local Python HTTP server. The server validates request sizes and data, passes analytical work to core.py and returns JSON. Pandas handles tabular preparation. Scikit-learn trains and evaluates the model. The browser renders the results without external JavaScript libraries. Optional generative requests go to the fixed local Ollama endpoint.


## Application modules

Overview displays sales KPIs and descriptive social comparisons. Your Data accepts matching CSV files and displays cleaning notes. Demand Lab presents holdout metrics and a next-day scenario. Content Studio prepares an evidence-led prompt and can request local Llama text. Product Lens can request local vision analysis. Exports support inspection outside the app.


## Local workflow

Install Python dependencies, run python app/server.py and open http://127.0.0.1:8501. The default server binds to the local computer. No login, shared database, social-account integration, scheduled publishing or production hosting is included. The prototype is designed for one local user.


## Generative connection

Text requests use model llama3.2 and image requests use llama3.2-vision. Both call /api/chat with stream=false. The app resizes images in memory and does not save uploads. A missing local service or model produces an explicit error. Preparing a prompt does not count as model generation.


## Reproducibility

The package includes pinned numerical dependencies, source code, a notebook, sample inputs, calculated JSON output and automated checks. Training uses random_state=42. No model weights or credentials are bundled. Dependency installation requires connectivity. Llama setup is optional and requires suitable hardware.


# Analytics and model evaluation


## Metric definitions

Revenue = sum(units x unit_price). Engagement rate = sum(likes + comments + shares + saves) / sum(post reach) x 100. Click-to-lead rate = reported leads / clicks x 100. Cost per lead = social spend / reported leads. Zero leads produce an undefined cost per lead. Zero reach or clicks produce a displayed zero rate with the denominator limitation explained.


## Demonstration outputs

The synthetic records produce NGN 13,401,800 revenue and 5,519 units sold. Aggregate engagement rate is 3.62%. Reported click-to-lead conversion is 23.14%, with NGN 116.07 cost per lead. These values describe the supplied synthetic files only.


## Evaluation design

Sort daily records by date, then train on the first 96 records and test on the last 24. Training ends 4 October 2026 and testing starts 5 October 2026. Exclude units and revenue from predictors. Fit the mean baseline and random forest only on training records. Calculate MAE and RMSE on holdout dates. Finish evaluation before refitting on all history for the next-day scenario.


## Results

Random forest MAE: 2.902 units. RMSE: 3.699 units. Mean-baseline MAE: 7.715 units. MAE is a regression error in units, not an accuracy percentage. The model is smaller-error on this synthetic holdout. This does not establish real-world forecast quality.


## Interpretation

Synthetic generation deliberately embeds relationships among weekday, price, promotion and ad spend. The model can learn these constructed patterns. A real evaluation needs consented historical records, repeated temporal splits, seasonal baselines, uncertainty estimates and monitoring for changing demand. Changing a scenario input does not prove a causal effect.


# Content strategy and prompt design


## Evidence before generation

The app calculates the metrics and inserts them into an RCTCF prompt. The prompt treats business labels as untrusted data and asks for observations tied to supplied figures. It prohibits invented prices, discounts, testimonials, research and causal attribution. Generated captions remain drafts for owner review.


## Choosing the right objective

Reel groups have about 5.5% engagement in the synthetic data, compared with about 1.8% for Image groups. However, the Facebook Image group records 39 leads, more than either individual Reel group. A format with lower engagement can still be relevant to a lead-generation objective. The campaign plan therefore tests content against a declared primary KPI.


## Seven-day illustrative campaign

The calendar includes a bakery introduction, a product carousel, an enquiry-focused image, a preparation Reel, an FAQ carousel, a customer-question prompt and a weekly review. Captions avoid unsupported prices or discounts. The calendar is a human-reviewed example for a fictional business, not a record of AI generation or publication.


## A/B-test proposal

Compare two opening hooks while keeping the body, visual, audience and CTA constant. Primary KPI: enquiries per reached account, with the attribution method recorded. Use a suitable observation window and adequate volume before interpreting differences. Sequential organic posts differ in timing and audience, so they provide exploratory signals rather than a clean randomised experiment.


## Prompt iteration and multimodality

Run weak, medium and strong prompts and score grounding, audience fit, constraint compliance, usefulness and clarity. Save outputs and human edits. For image tasks, inspect visible features and request accessible alt text. Do not infer ingredients, authenticity, health benefits or hidden product properties.


# Business model and validation plan


## Value proposition hypothesis

MarketMate AI aims to help small-business owners turn existing sales and social records into a measurable campaign plan through understandable metrics and structured prompts. Whether the workflow saves time, improves decisions or merits payment remains a hypothesis.


## Initial market approach

Start with five consenting owner-managers who sell one main product and keep records. Observe current planning, access to devices, data quality and adoption barriers. Recruit through willing business communities or referrals. This is a pilot recruitment plan, not a quantified market-size claim.


## Illustrative economics

Assume NGN 5,000 monthly price and NGN 1,500 variable service cost. Contribution would be NGN 3,500 per account per month. At NGN 35,000 monthly fixed cost, contribution break-even would be 10 accounts. An illustrative NGN 7,000 acquisition cost implies two months of contribution payback. These are arithmetic assumptions, not observed business results. Taxes, founder salary and equipment need explicit treatment.


## Customer experiments

Test whether at least three of five owners can provide anonymised required fields. Observe setup and campaign-planning tasks. Record completion, time, errors, interpretation and requested changes. Explore actual payment commitments without treating polite interest as demand. The supplied workbook contains consent wording and blank evidence logs.


## Roadmap

Week 1: interviews and data feasibility. Week 2: observed usability and prompt-quality evaluation. Week 3: revise the workflow and retest. Week 4: decide whether to continue, change or stop. Add hosting, persistence and authentication only after the pilot establishes a need.


# Verification, responsibility and limits


## Verification approach

Automated tests check independent arithmetic expectations, weighted engagement rates, zero denominators, invalid values, duplicate handling, temporal splitting, target-leakage resistance, scenario validation and prompt structure. HTTP checks exercise the server interface, rejected origins, malformed payloads and local-model error paths. See Test_Results.txt for actual execution results.


## Privacy and data minimisation

The workflow needs business counts, not customer identities. The app keeps uploads in memory, omits request-body logging and uses a fixed local model address. Downloads can contain sales history and should be reviewed before sharing. Local model software may maintain its own logs or caches outside this application. Use anonymised data and check local settings.


## Responsible-AI controls

Disclose synthetic inputs and AI assistance. Keep calculations deterministic. Treat data labels and images as untrusted content. Verify generated claims, respect image permissions, provide alt text and preserve human editorial control. Prompt constraints reduce risk but do not guarantee compliance or eliminate hallucinations.


## Material limitations

No representative customer study, measured time saving, improved revenue or paid adoption is established. Numerical results use synthetic data and a single temporal split. Successful Llama inference remains unverified in this build environment. Browser-based visual and interaction QA could not run because the managed preview environment lacked the Python runtime. Source and HTTP behaviour were checked separately. This local prototype is not production software.


## Submission readiness

Run the application yourself, learn the formulas and model choices, test optional models on your machine and attach authentic interaction evidence. Complete required field validation and check the organiser's rubric. Adjust claims to match the evidence you actually collect. Do not submit unverified activities as completed work.


# References and reproducibility


## Course materials

Learner-supplied Meta AI Academy PDFs in Documents.zip: Module 1 (1a-1e), Module 2 (2a-2d), Module 3 (3a-3d), Module 4 (4a-4d). Specific anchors: 3a p4 for RCTCF, 3d p27 for the content portfolio, 4b p11-19 for persona and validation, 4c p15-21 for prototype measurement, and 4d p6-18 for pitch structure.


## Technical references

Ollama, Generate a chat message: https://docs.ollama.com/api/chat. Ollama, Llama 3.2 Vision: https://ollama.com/library/llama3.2-vision. Scikit-learn, RandomForestRegressor: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html. Accessed 4 November 2026. These sources describe interfaces and algorithms, not evidence of this prototype's customer impact.


## Reproduction steps

Extract the package. Create a Python environment and install requirements.txt. Run python -m unittest discover -s tests -v. Start python app/server.py. Review the sample analysis, rebuild the prompt and compare with docs/demo_analysis.json. The included notebook reproduces the analytical steps and stores no invented model output.


## AI-use statement

This package was prepared with AI assistance for planning, software drafting, documentation and presentation. Samuel Ochoche Peter should review, execute and understand the submitted work and follow the programme's attribution requirements. All synthetic inputs and unperformed field activities are labelled. No customer interviews, measured adoption or successful local-model execution have been fabricated.


## Further evidence to attach

A screen recording of your own demonstration, saved authentic Meta AI or local Llama outputs, your prompt-scoring table and real user feedback if required. Include only material you have actually produced or collected with appropriate permission.

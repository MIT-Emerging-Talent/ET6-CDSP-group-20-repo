# DataCure

DataCure is a diverse, cross-cultural research team. United by a passion for
mental health and data-driven solutions, we combine expertise in data science,
natural language processing, and social research to tackle real-world
health challenges.
Our goal is to create insights that lead to more empathetic, ethical, and
effective digital mental health tools.

___

## 👥 Meet the team on Github
<!-- markdownlint-disable MD033 -->

| GitHub Profile |
| :--- |
| [Huda Alamassi](https://github.com/hudaalamassi) |
| [Malak Battat](https://github.com/malakbattat) |
| [Sadam Husen Ali](https://github.com/Urz1) |
| [Chrismy Augustin](https://github.com/likechrisss) |
| [F. Ismail SAHIN](https://github.com/fevziismailsahin) |
| [Aziz Azizi](https://github.com/Azizsin7) |
| [Ayham Hasan](https://github.com/ayhm01) |

___

## 🔍 Project Focus

* **Track:** Collaborative Data Science Project (CDSP)
* **Team Name:** DataCure 🧬
* **Title:** The Public Failure Analysis: Identifying Conversational Failures in
Mental Health Chatbots
* **Domain:** Digital Mental Health & Emotional Support Technologies
* **Timeline:** May to August 2025
* **Current Status:** 🛠️ In Progress (Milestone 5)

___

## Project Story & Domain

### **Problem Statement**

Mental health apps are bridging global care gaps, especially where stigma, cost,
or shortages limit traditional access. Three main support models exist:

* 🤖 Chat-bots – 24/7, private, and scalable, but lack emotional depth

* 🧑‍⚕️ Humans – empathetic and nuanced, yet costly and less available

* 🔁 Hybrids – blend both, offering balance but may confuse users

* Each model has pros and cons, with success shaped by user context and needs.

#### **Why it Matters**

* Mental health affects 1 in 8 people globally, but access remains unequal

* Chat-bots provide scalable support but may lack empathy

* Humans provide depth but are less scalable

* Hybrids aim to combine both—but their effectiveness is underexplored

#### **Goals**

* Systematically identify and categorize the most common user-reported failures in
  mental health chat-bots

* Quantify prevalence of failure themes using public app store and forum data

* Compare failures between purely conversational AIs and a baseline wellness app
  to isolate unique “conversational” failures

In Summary: This project explores how mental health support—via chat-bots,
humans, or hybrid systems—is experienced across cultures, aiming to inform more
empathetic, effective, and inclusive digital care.

___

## **Summary of Problem Understanding**

📄 Full version:
[Summary of problem](0_domain_study/summary_of_our_understanding_of_the_problem_domain.md)

We applied divergent thinking to explore broad problem areas, then convergent
thinking to narrow our focus using feasibility and impact criteria. The chosen
focus: chatbot vs human support in mental health apps.

Idea Evaluation: All proposed project ideas and their comparison scores are
documented in this spreadsheet, which guided our topic selection.

### **Iceberg Model Overview**

* **Event:** Users interact with chat-bots—some feel helped, others feel unheard

* **Pattern:** Mental health apps are growing; many rely on chat-bots

* **Structure:** Cost and scale drive chatbot use; regulation is limited

* **Mental Model:** Belief in AI as a fix for care gaps and stigma sustains the
    system

## **Research Question**

📄 Full version: [research_question](0_domain_study/research_question.md)

📄 Full version: [problem_statement](0_domain_study/problem_statement.md)

Refined Question:

  >What are the most prevalent themes of user-reported conversational failure in
  leading mental health chat-bots, and what do these themes reveal about the
  gap between user expectations for emotional support and current algorithmic
  capabilities?

This ensures a focused, measurable analysis using public data while respecting privacy.

___

## 📁 **Directory Structure**
<!-- markdownlint-disable MD046 -->
``` terminal
/
├── README.md                   - Project overview and main instructions
├── guide.md                    - Detailed guide on using this template
├── /collaboration/             - Team norms, strategies, and retrospectives
├── /notes/                     - Shared resources and learning materials
├── /0_domain_study/            - Domain research and background
├── /1_datasets/                - Raw and processed datasets
├── /2_data_preparation/        - Scripts for cleaning and processing data
├── /3_data_exploration/        - Scripts for initial data understanding
├── /4_data_analysis/           - Scripts for in-depth analysis
├── /5_communication_strategy/  - Materials for communicating findings
└── /6_final_presentation/      - Final presentation materials
````

## 🤝 Our Working Agreements

* 🔹 [Team Norms](collaboration/group_norms.md)
* 🔹 [Communication Plan](collaboration/communication.md)
* 🔹 [Constraints](collaboration/constraints.md)
* 🔹 [Learning Goals](collaboration/learning_goals.md)

___

## ⏳ Milestones & Timeline

| Milestone | Description                   | Progress     | Target Date |
|-----------|-------------------------------|--------------|-------------|
| 0         | Team Setup & Collaboration    | ✅ Complete   | June 2      |
| 1         | Define Research Question      | ✅ Complete    | June 16     |
| 2         | Data Collection               | ✅ Complete    | June 30     |
| 3         | Analysis & Modeling           | ✅ Complete    | July 21     |
| 4         | Communication Strategy        | ✅ Complete    | August 11   |
| 5         | Final Presentation            | ⏳ Upcoming   | August 25   |

___

## 🔍 Explore Milestones

* 🔹 [Milestone 0: Cross-Cultural Collaboration](collaboration/README.md)
* 🔹 [Milestone 1: Problem Identification](0_domain_study/README.md)
* 🔹 [Milestone 2: Data Collection](1_datasets/README.md)
* 🔹 [Milestone 3: Data Analysis](4_data_analysis/README.md)
* 🔹 [Milestone 4: Communicating Results](5_communication_strategy/README.md)
* 🔹 [Milestone 5: Final Presentation](6_final_presentation/README.md)
  
___

### Replication

[Method](Method.md) holds the technical workflow → reproducible but not
overwhelming for a non-technical reader.

#### 1. Clone the Repository

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-20-repo.git

cd ET6-CDSP-group-20-repo
```

#### 2. Create Python Environment

```bash
python -m venv mentalhealth
```

* Activate environment Using pip

 Windows (PowerShell)

```bash
.\mentalhealth\Scripts\activate
```

macOS/Linux

```bash
source mentalhealth/bin/activate
```

* Using conda

```bash
conda env create -f environment.yml
conda activate mentalhealth
```

#### 3. Install the requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**All enriched datasets are saved in:**

[`1_datasets/all_datasets/`](1_datasets/all_datasets/)

Examples:

* conversational_apps_themed_and_scored.csv

* baseline_app_themed_and_scored.csv

* ...

These files include:

* review_text

* app_name

* theme

* Sentiment scores

* Additional metadata

**Reproduce Analysis:**

Follow notebooks and scripts in:
[`2_data_preparation`](2_data_preparation)

  ⬇️

[`4_data_analysis`](4_data_analysis) in order
___

### ➕ **Contributing**

  We’re excited to collaborate! To get involved, please check out our
  [CONTRIBUTING.md](CONTRIBUTING.md) for
  guidelines.
___

#### 🔑 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
for details.

___

> “There is no health without mental health.” – *World Health Organization*

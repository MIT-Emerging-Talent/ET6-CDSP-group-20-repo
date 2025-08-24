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

[Huda Alamassi](https://github.com/hudaalamassi),
[Malak Battatt](https://github.com/malakbattat),
[Sadam Husen Ali](https://github.com/Urz1),
[Chrismy Augustin](https://github.com/likechrisss),
[F. Ismail SAHIN](https://github.com/fevziismailsahin),
[Aziz Azizi](https://github.com/Azizsin7)
[Ayham Hasan.](https://github.com/ayhm01)

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

## 🔍 Explore Our Project

   **📄** To read the full background and detailed version, see
   [Milestone 1: Problem Identification](0_domain_study/README.md)
   [Milestone 2: Data Collection](1_datasets/README.md)

### 🔹Problem Statement

  **📄** To read the full Problem Statement, see [Problem Statement](0_domain_study/problem_statement.md)

* **Chatbot vs Human vs Hybrid Support in Mental Health Apps**

Mental health apps are bridging global care gaps, especially where stigma, cost,
or shortages limit traditional access. Three main support models exist:

* 🤖 **Chatbots**: 24/7, private, and scalable, but lack emotional depth.  
* 🧑‍⚕️ **Humans**: Empathetic and nuanced, yet costly and less available.  
* 🔁 **Hybrids**: Blend both, offering balance but may confuse users.

Each model has pros and cons, with success shaped by user context and needs.
  
* **Why It Matters**

  * Mental health affects 1 in 8 people globally, but access remains unequal.

  * Chatbots offer 24/7 low-cost support, but may lack empathy.

  * Humans provide depth, but are less scalable.

  * Hybrids aim to combine both—but how well do they work?

* **Goals**

  * Systematically identify and categorize the most common user-reported failures
   of mental health chatbots.
  * Quantify the prevalence of these failure themes using public app store and
  forum data.
  * Compare failure themes between purely conversational AIs and a baseline
  wellness app to isolate unique "conversational" failures.
* **In Summary**

To explores how mental health support—via chat-bots, humans, or hybrid
systems—is experienced across cultures. Our aim: to inform more empathetic,
effective, and inclusive digital care.

### 🔹Summary of Problem Understanding

  **📄** To read the full Summary of Problem Understanding,
  see [Summary of Problem Understanding](0_domain_study/summary_of_our_understanding_of_the_problem_domain.md)

We used **divergent thinking** to explore broad problem areas, then applied  
**convergent thinking** to narrow our focus using feasibility and impact criteria.
We chose to explore chatbot vs human support in mental health apps.

* **Idea Evaluation Sheet**

  All proposed project ideas and their comparison scores are documented in this
  [spreadsheet](https://tinyurl.com/3r5a5jee)
  This helped us select the most impactful and feasible topic.

### Iceberg Model Overview

* **Event**: Users interact with chatbots—some feel helped, others feel unheard.
* **Pattern**: Mental health apps are growing; many now rely on chatbots.  
* **Structure**: Cost and scale drive chatbot use; regulation is limited.  
* **Mental Model**: Belief in AI as a fix for care gaps and stigma sustains the system.

### 🔹Research Question

   **📄** To read the full Research Questions, see
 [Research Question](0_domain_study/research_question.md)

Our refined research question, which is achievable through public data analysis,
is:  

**What are the most prevalent themes of user-reported conversational failure in
leading mental health chatbots, and what do these themes reveal about the gap
between user expectations for emotional support and current algorithmic capabilities?**

This helps us focus our research on a specific, measurable aspect of the problem.

___

## 📁 **Directory Structure**

```text
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

```

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

These files include:

* review_text

* app_name

* theme

* Sentiment scores

* Additional metadata

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

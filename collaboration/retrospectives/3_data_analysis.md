# Milestone 3: Data Analysis (Due [Date])

This milestone was the analytical core of our project. We transformed our clean
datasets into a compelling, evidence-based narrative through a multi-layered NLP
pipeline, culminating in a series of powerful comparative visualizations.

## Group Retrospective

*(This section should reflect the collective experience. It acknowledges the challenges
of asynchronous work while celebrating the final integrated outcome.)*

* **What went well? (The "Wins")**
  * **Successful Division of Labor:** We successfully divided complex analytical
  tasks.The main BERTopic pipeline, the app-specific deep dive, and the model validations
  were all completed in parallel, which was a huge success.
  * **Methodological Depth:** As a group, we produced an incredibly deep analysis,
  employing multiple advanced techniques (BERTopic, Transformers, Time Series) that
  went beyond the initial project plan.
  * **Integration into a Coherent Story:** We successfully consolidated multiple,
  complex individual analyses into a single, cohesive master notebook that tells
  a clear and powerful story.

* **What could have gone better? (The "Learnings")**
  * **Communication & Synchronization:** There were periods where individual team
  members were working in isolation, leading to some initial challenges in aligning
  methodologies and avoiding redundant work. More frequent, short check-ins could
  have streamlined this.
  * **Initial Analysis Complexity:** Our initial analyses were sometimes too complex
  for their own good (e.g., the cluttered charts). We learned the valuable lesson
  that the simplest, clearest visualization is often the most powerful one for
  communicating a finding.
  * **Defining the "Final" Product:** We spent a lot of time in individual exploration.
  Defining the structure and key visualizations for the "final master notebook"
  earlier in the process could have focused our efforts even sooner.

* **What will we do differently for the Final Presentation? (The "Action Items")**
  * **Assign Clear Presentation Roles Early:** We will assign specific sections
  of the final presentation to each team member early on to ensure everyone has
  ownership and we have a smooth, well-rehearsed delivery.
  * **Focus on the "Story First":** For the final report and slides, we will start
  with the key narrative points and insights, and then select the best charts and
  quotes to support them, rather than just presenting every analysis we did.
  * **Conduct a Full Dry-Run:** We will schedule at least one full, timed practice
  run of our final presentation to get feedback on flow, clarity, and timing.

### Individual Retrospective:  Sadam Husen

* **What did I accomplish during this milestone?**
  * I took the lead in architecting and executing the entire end-to-end advanced
  analysis pipeline. This included configuring and training the BERTopic models
  for both the conversational and baseline datasets, which became the foundation
  of the project.
  * I developed and refined the "Super-Topic" thematic grouping, which was the
  key step in transforming the raw model output into an understandable narrative.
  * I engineered and debugged the complex time series analysis, which produced
  the project's "smoking gun" visualization linking the Replika update to the
  spike in complaints.
  * I spearheaded the creation of the final comparative visualizations, iterating
  on feedback to create clear, compelling charts that tell the project's core story.
  I drove the project forward by proposing and implementing these advanced analytical
  steps.

* **What did I learn?**
  * I learned that the real work of data science happens *after* the model runs.
  The process of interpreting, validating, and theming the topics was far more
  critical than the coding itself.
  * I gained a deep appreciation for the power of comparative analysis. The
  baseline dataset wasn't just a control group; it was the key that unlocked the
  meaning and significance of all our other findings.
  * I learned the importance of balancing analytical depth with communicative clarity.
  A complex chart isn't useful if the audience can't understand it. The process of
  simplifying our visualizations was a crucial lesson in data storytelling.

* **What am I worried about, or what do I need help with for the next milestone?**
  * My main focus for the final milestone is ensuring that our team can effectively
  translate our complex, multi-layered analysis into a concise, clear, and powerful
  5-10 minute presentation. My concern is condensing so much good work without losing
  the key insights.
  * I will need the team's help in practicing this story. I've been very deep in
  the technical details, and I'll need their feedback to ensure the narrative
  I've constructed resonates with a general audience and that we all present it
  as a cohesive unit.

### Individual Retrospective Aziz Azizi

* **What Went Well (My Wins)**

  * Team Engagement:

    It was motivating to see different members contributing distinct pieces to
    the analytical puzzle. While we worked asynchronously, I appreciated how
    ideas from others often sparked new directions in my own work. For example,
    building on the BERTopic pipeline and layering VADER sentiment analysis
    allowed me to uncover nuanced emotional themes in reviews that might have
    otherwise gone unnoticed. I hope that the final presentation will capture
    the richness of these shared efforts.

  * Tool Mastery & Technical Confidence:
    On a personal level, this was the phase where I truly developed comfort
    with complex tools like BERTopic, VADER, and TF-IDF visualizations.
    Troubleshooting issues like MIME rendering, kernel mismatches, and formatting
    errors in Jupyter helped me better understand the mechanics behind data
    science environments. It felt good to go from struggling with basic errors
    to being able to debug, configure, and successfully visualize emotional
    patterns in the app reviews.

* **What Could’ve Gone Better**
  * Complexity Over Clarity:
    At times, we leaned toward overly advanced techniques when simpler ones
    would’ve been more effective and inclusive for all team members.

  * Unclear Task Distribution:
    We didn’t define individual responsibilities clearly early on, which led to
    duplicated efforts in some places and last-minute crunch in others. I found
    myself scrambling to finalize plots and clean up notebooks late in the
    process, which could have been avoided with better upfront planning and more
    frequent check-ins.

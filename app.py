import streamlit as st
from model import ALL_SKILLS, ALL_INTERESTS, COMPANIES, ROLES, recommend


st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
)


# -------------------- DESIGN --------------------

st.markdown(
    """
<style>
.stApp {
    background:
        radial-gradient(
            ellipse at 80% 10%,
            rgba(103, 74, 255, 0.18),
            transparent 45%
        ),
        linear-gradient(
            rgba(56, 189, 248, 0.035) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(56, 189, 248, 0.035) 1px,
            transparent 1px
        ),
        #080d1b;
    background-size: auto, 40px 40px, 40px 40px, auto;
    color: #e6edf7;
}

section[data-testid="stSidebar"] {
    background: #0d1426;
    border-right: 1px solid #22314d;
}

header[data-testid="stHeader"] {
    background: rgba(8, 13, 27, 0.9);
}

h1, h2, h3 {
    color: #f0f5ff !important;
    letter-spacing: -0.6px;
}

.stApp p,
.stApp label,
.stApp li,
[data-testid="stCaptionContainer"] {
    color: #b9c9df !important;
}

[data-baseweb="select"] > div,
[data-baseweb="input"] > div,
[data-baseweb="base-input"],
.stTextArea textarea {
    background-color: #111d32 !important;
    color: #edf4ff !important;
    border-color: #304363 !important;
}

input {
    color: #edf4ff !important;
}

[data-baseweb="select"] span {
    color: #edf4ff;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"] {
    background-color: #111d32 !important;
    color: #edf4ff !important;
}

[role="option"] {
    color: #edf4ff !important;
}

[data-baseweb="tag"] {
    background-color: #16465b !important;
    color: #91edff !important;
}

.stButton > button {
    background: linear-gradient(110deg, #2563eb, #7c3aed);
    color: white !important;
    border: 1px solid #7b83ff;
    border-radius: 12px;
    font-weight: 700;
    padding: 0.7rem 1.2rem;
    box-shadow: 0 4px 22px #413bd833;
    transition: transform 0.2s, box-shadow 0.2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 28px #6366f166;
    border-color: #67e8f9;
}

.stButton > button p {
    color: white !important;
}

[data-testid="stExpander"] {
    background: rgba(16, 27, 48, 0.94);
    border: 1px solid #2b3c59;
    border-radius: 16px;
    overflow: hidden;
}

[data-testid="stExpander"] summary:hover {
    background: rgba(56, 189, 248, 0.06);
}

[data-testid="stAlert"] {
    background: #10253a;
    border: 1px solid #21516b;
    border-radius: 12px;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #112038, #171b35);
    border: 1px solid #293d5c;
    border-radius: 16px;
    padding: 20px;
}

[data-testid="stMetricValue"] {
    color: #67e8f9 !important;
}

[data-baseweb="tab-list"] {
    gap: 12px;
    border-bottom: 1px solid #293d5c;
}

[data-baseweb="tab"] {
    color: #b9c9df !important;
}

[data-baseweb="tab"][aria-selected="true"] {
    color: #67e8f9 !important;
}

[data-testid="stLinkButton"] a {
    background: #15253c;
    color: #a5edff !important;
    border: 1px solid #345270;
    border-radius: 10px;
}

[data-testid="stLinkButton"] a:hover {
    border-color: #67e8f9;
    background: #1c3450;
}

.hero {
    position: relative;
    padding: 36px;
    margin-bottom: 24px;
    border: 1px solid #33496d;
    border-radius: 22px;
    background: linear-gradient(120deg, #11253b, #211637);
    box-shadow: 0 16px 60px rgba(0, 0, 0, 0.2);
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    top: -100px;
    right: -60px;
    border: 1px solid rgba(103, 232, 249, 0.25);
    border-radius: 50%;
    box-shadow:
        0 0 0 35px rgba(103, 232, 249, 0.04),
        0 0 0 70px rgba(103, 232, 249, 0.025);
    pointer-events: none;
}

.hero .eyebrow {
    color: #67e8f9;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
}

.hero h1 {
    font-size: clamp(30px, 5vw, 52px);
    margin: 12px 0;
    line-height: 1.15;
}

.hero p {
    max-width: 600px;
    font-size: 16px;
    line-height: 1.7;
}

.hero .badge {
    display: inline-block;
    margin-top: 10px;
    padding: 6px 12px;
    border: 1px solid #37516d;
    border-radius: 30px;
    color: #a5edff;
    font-size: 12px;
}

@media (max-width: 640px) {
    .hero {
        padding: 24px;
    }
}

@media (prefers-reduced-motion: reduce) {
    .stButton > button {
        transition: none;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# -------------------- HEADER --------------------

st.markdown(
    """
<div class="hero">
    <div class="eyebrow">CAREERPILOT / CAREER EXPLORER</div>
    <h1>Your skills.<br>Your next chapter.</h1>
    <p>
        Explore career matches, discover skills to develop,
        and build a clear roadmap for your future.
    </p>
    <div class="badge">SKILL ANALYSIS · CAREER DISCOVERY · LEARNING ROADMAPS</div>
</div>
""",
    unsafe_allow_html=True,
)

st.caption(
    "Skill-based AI/ML career advisor • "
    "Educational prototype using KNN nearest neighbors"
)


# -------------------- PROFILE --------------------

with st.sidebar:
    st.markdown("## 🚀 CareerPilot AI")
    st.caption("Build a direction for your next move.")
    st.divider()

    st.header("Your profile")

    skills = st.multiselect(
        "Your current skills",
        ALL_SKILLS,
        default=[
            skill
            for skill in ["Python", "SQL", "Excel"]
            if skill in ALL_SKILLS
        ],
    )

    interests = st.multiselect(
        "Your interests",
        ALL_INTERESTS,
        default=["Data"] if "Data" in ALL_INTERESTS else [],
    )

    level = st.selectbox(
        "Experience",
        ["Student / Beginner", "Intermediate", "Experienced"],
    )

    location = st.text_input(
        "Preferred job location",
        value="India",
    )

    if len(ROLES) > 1:
        limit = st.slider(
            "Number of career recommendations",
            min_value=1,
            max_value=len(ROLES),
            value=min(8, len(ROLES)),
        )
    else:
        limit = len(ROLES)

    st.button(
        "Find my careers →",
        type="primary",
        use_container_width=True,
    )

    st.caption("Matches update automatically when your profile changes.")


# -------------------- RECOMMENDATIONS --------------------

if not skills:
    st.info("Choose at least one skill in the sidebar to get started.")
    st.stop()

if not ROLES:
    st.warning("No career profiles are available in model.py.")
    st.stop()

results = list(recommend(skills, interests, limit))

if not results:
    st.info("No career matches were returned. Try changing your profile.")
    st.stop()

st.info(
    "Recommendations are illustrative, not hiring or eligibility predictions. "
    "Company links lead to official career portals; openings are not checked live."
)

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("Your skills", len(skills))

with metric2:
    st.metric("Career paths", len(results))

with metric3:
    best_score = max(float(result["score"]) for result in results)
    st.metric("Top similarity", f"{best_score:g}%")

st.markdown("")
st.subheader(f"{len(results)} career paths matched to your profile")
st.caption(
    "Similarity measures closeness to our curated job-skill profiles, "
    "not employment probability."
)

for index, result in enumerate(results, start=1):
    score = float(result["score"])
    progress_value = max(0.0, min(1.0, score / 100))
    matched = result["matched"]
    missing = result["missing"]
    projects = result["projects"]

    with st.expander(
        f"#{index} {result['name']} — {score:g}% similarity",
        expanded=index == 1,
    ):
        st.progress(progress_value)

        column1, column2 = st.columns(2)

        with column1:
            st.markdown("**Your matching skills**")
            st.write(
                ", ".join(matched)
                if matched
                else "No direct matches yet"
            )

        with column2:
            st.markdown("**Skills to develop**")
            st.write(
                ", ".join(missing)
                if missing
                else "All listed skills covered"
            )

        tabs = st.tabs(
            ["Companies", "Interview prep", "Hackathons", "Career roadmap"]
        )

        with tabs[0]:
            st.write(
                "Potential employers to explore "
                "(not verified current vacancies):"
            )

            for name in result["companies"]:
                if name in COMPANIES:
                    st.link_button(
                        f"Explore {name} careers ↗",
                        COMPANIES[name],
                    )

            st.caption(
                f"Check {location or 'your preferred'} locations, "
                "internship/graduate filters, and eligibility on each portal."
            )

        with tabs[1]:
            st.markdown("**Interview preparation checklist**")

            for tip in result["interview"]:
                st.write("• " + tip)

            st.write(
                "• Prepare a 60-second introduction and explain "
                "your strongest project."
            )
            st.write(
                "• Practice communicating your approach before writing code."
            )

        with tabs[2]:
            st.write("Build one of these projects in a hackathon:")

            for project in projects:
                st.write("• " + project)

            st.write(
                "Hackathon approach: define a problem → build an MVP → "
                "test → prepare a 3-minute demo."
            )

            st.link_button(
                "Find hackathons on Devpost ↗",
                "https://devpost.com/hackathons",
            )

            st.caption(
                "Browse by theme and verify each event’s dates, "
                "rules and eligibility."
            )

        with tabs[3]:
            st.markdown("**30-day plan**")
            st.write(
                "Learn fundamentals: "
                + (
                    ", ".join(missing[:2])
                    if missing
                    else "strengthen existing skills"
                )
            )

            st.markdown("**60-day plan**")
            st.write(
                "Build and publish: "
                + (
                    projects[0]
                    if projects
                    else "a project that demonstrates your target role's skills"
                )
            )

            st.markdown("**90-day plan**")

            next_project = (
                projects[1]
                if len(projects) > 1
                else "an improved version of your first project"
            )

            st.write(
                f"Complete {next_project}, polish your resume, "
                "practice interviews, and review entry-level/"
                "internship openings."
            )

            priority = missing[0] if missing else "advanced projects"

            st.write(
                f"**Personalized advice:** As a {level.lower()}, "
                "focus on demonstrable projects, GitHub documentation, "
                "and consistent practice. Your next priority for this "
                f"role is {priority}."
            )

# -------------------- CAREER ANALYTICS --------------------

import html
import re
from urllib.parse import quote_plus

import pandas as pd


def safe_text(value):
    return html.escape(str(value))


# Learning links are searches on these platforms.
# Individual courses are not automatically verified or endorsed.
def learning_links(skill):
    query = quote_plus(f"{skill} tutorial")

    return {
        "Video lessons": (
            f"https://www.youtube.com/results?search_query={query}"
        ),
        "Courses": (
            "https://www.coursera.org/search?"
            f"query={quote_plus(skill)}"
        ),
        "Practice and tutorials": (
            "https://www.google.com/search?"
            f"q={quote_plus(skill + ' exercises official documentation')}"
        ),
    }


st.divider()
st.header("Career insights")
st.caption(
    "Compare your current skill fit, explore learning resources, "
    "and download your career report."
)

analytics_tab, resources_tab, report_tab = st.tabs(
    ["📊 Career comparison", "📚 Learning resources", "📥 Download report"]
)


# -------------------- COMPARISON GRAPHS --------------------

comparison_rows = []

for result in results:
    matched_count = len(result["matched"])
    missing_count = len(result["missing"])
    total_count = matched_count + missing_count

    coverage = (
        round(matched_count / total_count * 100, 1)
        if total_count
        else 0
    )

    comparison_rows.append(
        {
            "Career": result["name"],
            "Similarity (%)": float(result["score"]),
            "Skill coverage (%)": coverage,
            "Matching skills": matched_count,
            "Missing skills": missing_count,
        }
    )

comparison_df = pd.DataFrame(comparison_rows)

with analytics_tab:
    st.subheader("Which careers fit your profile?")

    st.info(
        "These graphs compare your profile with the app's curated roles. "
        "They do not measure job vacancies, salary, future demand, "
        "or your probability of getting hired."
    )

    graph_left, graph_right = st.columns(2)

    with graph_left:
        st.markdown("**Career similarity**")
        st.bar_chart(
            comparison_df.set_index("Career")[["Similarity (%)"]]
        )
        st.caption(
            "Similarity comes from the existing recommendation model."
        )

    with graph_right:
        st.markdown("**Skills you have vs skills to develop**")
        st.bar_chart(
            comparison_df.set_index("Career")[
                ["Matching skills", "Missing skills"]
            ]
        )
        st.caption(
            "Counts refer only to skills listed in the curated role profiles."
        )

    st.markdown("**Detailed career comparison**")

    st.dataframe(
        comparison_df,
        hide_index=True,
        use_container_width=True,
    )

    best_fit = max(
        results,
        key=lambda item: float(item["score"]),
    )

    smallest_gap = min(
        results,
        key=lambda item: (
            len(item["missing"]),
            -float(item["score"]),
        ),
    )

    insight_left, insight_right = st.columns(2)

    with insight_left:
        st.success(
            f"Highest similarity: **{best_fit['name']}** "
            f"({float(best_fit['score']):g}%)"
        )

    with insight_right:
        st.success(
            f"Fewest listed skill gaps: **{smallest_gap['name']}** "
            f"({len(smallest_gap['missing'])} skills)"
        )

    st.caption(
        "Fewer missing skills does not necessarily mean an easier career. "
        "Roles differ in depth, qualifications, and experience requirements."
    )

    st.download_button(
        label="Download comparison data — CSV",
        data=comparison_df.to_csv(index=False).encode("utf-8"),
        file_name="CareerPilot_Comparison.csv",
        mime="text/csv",
        key="download_career_comparison",
    )


# -------------------- LEARNING RESOURCES --------------------

with resources_tab:
    st.subheader("Turn skill gaps into a learning plan")

    selected_career = st.selectbox(
        "Choose a career",
        options=[result["name"] for result in results],
        key="learning_career",
    )

    selected_result = next(
        result
        for result in results
        if result["name"] == selected_career
    )

    skills_to_learn = selected_result["missing"]

    if not skills_to_learn:
        st.success(
            "You cover all skills listed for this role. "
            "Use the project ideas to practise them in greater depth."
        )
    else:
        st.caption(
            "Links open platform search results. Check course level, "
            "cost, and syllabus before choosing a resource."
        )

        for skill_index, skill in enumerate(skills_to_learn, start=1):
            with st.expander(
                f"{skill_index}. Learn {skill}",
                expanded=skill_index == 1,
            ):
                st.write(
                    f"Start with {skill} fundamentals, complete practice "
                    "exercises, then apply what you learn in a small project."
                )

                resource_columns = st.columns(3)

                for column, (label, url) in zip(
                    resource_columns,
                    learning_links(skill).items(),
                ):
                    with column:
                        st.link_button(label, url)

    st.markdown("**Projects for this career**")

    for project in selected_result["projects"]:
        st.write("• " + project)


# -------------------- DOWNLOADABLE REPORT --------------------

with report_tab:
    st.subheader("Your personal career report")

    st.write(
        "Download a formatted report containing your profile, "
        "career comparisons, skill gaps, project ideas, "
        "learning links, and a 30/60/90-day roadmap."
    )

    report_name = st.text_input(
        "Name on report — optional",
        placeholder="Enter your name",
        key="career_report_name",
    )

    # Build a standalone HTML report.
    # Escape text before placing it into HTML.
    report_sections = []

    for position, result in enumerate(results, start=1):
        matched_text = (
            ", ".join(result["matched"])
            if result["matched"]
            else "No direct matches yet"
        )

        missing_text = (
            ", ".join(result["missing"])
            if result["missing"]
            else "All listed skills covered"
        )

        project_items = "".join(
            f"<li>{safe_text(project)}</li>"
            for project in result["projects"]
        )

        interview_items = "".join(
            f"<li>{safe_text(tip)}</li>"
            for tip in result["interview"]
        )

        resource_items = []

        for skill in result["missing"]:
            links = learning_links(skill)

            link_html = " · ".join(
                (
                    f'<a href="{safe_text(url)}">'
                    f"{safe_text(label)}</a>"
                )
                for label, url in links.items()
            )

            resource_items.append(
                f"<li><strong>{safe_text(skill)}</strong>: "
                f"{link_html}</li>"
            )

        resources_html = (
            "<ul>" + "".join(resource_items) + "</ul>"
            if resource_items
            else "<p>Practise existing skills through deeper projects.</p>"
        )

        projects = result["projects"]

        first_project = (
            projects[0]
            if projects
            else "a practical project for this role"
        )

        second_project = (
            projects[1]
            if len(projects) > 1
            else "an improved version of your first project"
        )

        first_skills = (
            ", ".join(result["missing"][:2])
            if result["missing"]
            else "your existing skills in greater depth"
        )

        score = max(0, min(100, float(result["score"])))

        report_sections.append(
            f"""
<section class="career">
    <h2>{position}. {safe_text(result["name"])}</h2>
    <p class="score">{score:g}% profile similarity</p>
    <div class="track">
        <div class="fill" style="width:{score}%"></div>
    </div>

    <h3>Matching skills</h3>
    <p>{safe_text(matched_text)}</p>

    <h3>Skills to develop</h3>
    <p>{safe_text(missing_text)}</p>

    <h3>Project ideas</h3>
    <ul>{project_items}</ul>

    <h3>Learning resources</h3>
    {resources_html}

    <h3>Interview preparation</h3>
    <ul>{interview_items}</ul>

    <h3>Suggested roadmap</h3>
    <p><strong>Days 1–30:</strong>
        Learn {safe_text(first_skills)}.</p>
    <p><strong>Days 31–60:</strong>
        Build and publish {safe_text(first_project)}.</p>
    <p><strong>Days 61–90:</strong>
        Complete {safe_text(second_project)}, improve your resume,
        practise interviews, and review suitable opportunities.</p>
</section>
"""
        )

    comparison_table = comparison_df.to_html(
        index=False,
        border=0,
        escape=True,
        classes="comparison",
    )

    report_html = (
        """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CareerPilot Career Report</title>
<style>
    body {
        margin: 0;
        background: #eef2f8;
        color: #17243b;
        font-family: Arial, sans-serif;
        line-height: 1.65;
    }
    main {
        max-width: 960px;
        margin: 32px auto;
        padding: 40px;
        background: white;
        border-radius: 18px;
    }
    header {
        padding: 28px;
        background: #101d36;
        color: white;
        border-radius: 14px;
    }
    header h1 { margin: 0 0 8px; }
    header p { margin: 4px 0; color: #c5d8f2; }
    h2 { color: #203f70; }
    h3 { margin-bottom: 6px; }
    a { color: #2459be; }
    .career {
        margin-top: 26px;
        padding: 24px;
        border: 1px solid #dce4ef;
        border-radius: 12px;
    }
    .score { color: #4056b8; font-weight: bold; }
    .track {
        height: 10px;
        background: #e8edf5;
        border-radius: 8px;
        overflow: hidden;
    }
    .fill {
        height: 100%;
        background: linear-gradient(90deg, #178ba6, #7354cd);
    }
    .table-wrap { overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; }
    th, td {
        border-bottom: 1px solid #dce4ef;
        padding: 10px;
        text-align: left;
    }
    th { background: #edf3fb; }
    .note { font-size: 13px; color: #53657e; }
    @media print {
        body { background: white; }
        main { margin: 0; padding: 0; max-width: none; }
        header {
            background: white;
            color: #17243b;
            border: 1px solid #dce4ef;
        }
        header p { color: #53657e; }
        h2, h3 { break-after: avoid; }
        li { break-inside: avoid; }
    }
</style>
</head>
<body>
<main>
<header>
    <h1>CareerPilot AI</h1>
    <p>Personal career exploration report</p>
</header>
"""
        + f"""
<h2>Your profile</h2>
<p><strong>Name:</strong>
    {safe_text(report_name.strip() or "Not provided")}</p>
<p><strong>Skills:</strong> {safe_text(", ".join(skills))}</p>
<p><strong>Interests:</strong>
    {safe_text(", ".join(interests) or "Not selected")}</p>
<p><strong>Experience:</strong> {safe_text(level)}</p>
<p><strong>Preferred location:</strong>
    {safe_text(location or "Not specified")}</p>

<h2>Career comparison</h2>
<div class="table-wrap">{comparison_table}</div>

<p class="note">
    Similarity is based on curated role profiles, not market demand,
    hiring probability, or eligibility. Skill coverage is the percentage
    of listed role skills present in your profile. Experience and location
    do not affect the current model's ranking.
</p>
"""
        + "".join(report_sections)
        + """
<p class="note">
    Academic prototype. Roadmaps are suggested templates, not guaranteed
    completion timelines. Resource links open searches; check suitability
    and pricing yourself. Live vacancies and salaries have not been checked.
</p>
</main>
</body>
</html>
"""
    )

    filename_name = re.sub(
        r"[^A-Za-z0-9_-]+",
        "_",
        report_name.strip(),
    ).strip("_")

    filename = (
        f"CareerPilot_Report_{filename_name}.html"
        if filename_name
        else "CareerPilot_Report.html"
    )

    st.download_button(
        label="📥 Download my career report",
        data=report_html.encode("utf-8"),
        file_name=filename,
        mime="text/html",
        key="download_full_career_report",
        use_container_width=True,
    )

    st.caption(
        "For a PDF: open the downloaded HTML file in your browser → "
        "press Ctrl + P → choose Save as PDF."
    )
# -------------------- ABOUT --------------------

st.divider()

with st.expander("How this system works"):
    st.write(
        "KNN nearest-neighbor search compares your skills and interests "
        "with curated role profiles using cosine distance. Results are "
        "ranked by similarity. Interview advice, company links and "
        "learning plans are curated templates, not generative AI output."
    )
    st.caption(
        "Experience changes the advice text. Location is a reminder "
        "for checking company portals; neither filters the similarity ranking."
    )

st.caption(
    "CareerPilot AI • Academic prototype • "
    "Profile selections are used for this session and are not saved by this code."
)
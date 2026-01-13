import streamlit as st

st.set_page_config(page_title="How to beat the winter blues", page_icon="❄️", layout="centered")

import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        /* Фон страницы */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Карточка с контентом */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 2.5rem;
            border-radius: 18px;
            max-width: 900px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background2.png")

st.markdown("""
<style>
/* Неактивная часть шкалы */
.stSlider [data-baseweb="slider"] [data-baseweb="track"] {
  background: #E6E6E6 !important;  /* светло-серый */
}

/* Активная (заполненная) часть */
.stSlider [data-baseweb="slider"] [data-baseweb="track"] > div {
  background: #A8D8F0 !important;  /* мягкий голубой */
}

/* Ползунок */
.stSlider [role="slider"] {
  background-color: #A8D8F0 !important;
  border-color: #A8D8F0 !important;
  box-shadow: none !important;
}

/* Hover */
.stSlider [role="slider"]:hover {
  background-color: #7EC3E6 !important;
  border-color: #7EC3E6 !important;
}
</style>
""", unsafe_allow_html=True)



st.title("❄️ How to beat the winter blues — A Collection of Tips")
st.caption("Answer the questions on a 1–5 scale (1 = false, 5 = true). At the end you’ll get your result and tips.")

QUESTIONS_V2 = [
    "I feel tired and sad a lot.",
    "It's difficult for me to do basic tasks (making my bed, going outside, brushing my teeth, household chores, etc.).",
    "I'm spending too much time on my phone and scrolling a lot.",
    "Even though I sleep a lot, I'm still tired.",
    "I'm not interested in most things in life.",
    "I feel lonely most of the time.",
    "It's hard for me to do cognitively demanding tasks (concentrating, studying, etc.).",
]

SCALE_HELP_EN = "1 — false • 2 — mostly false • 3 — not sure/50-50 • 4 — mostly true • 5 — true"


def result_for_score_v2(total: int) -> tuple[str, str]:
    # total is 7..35
    if 7 <= total <= 10:
        title = "🛡️ Winter Warrior"
        text = (
            "You’re OK — winter blues don’t affect you that much.\n\n"
            "**Tips to stay strong:**\n"
            "- Tip 1.\n"
            "- Tip 2.\n"
            "- Tip 3.\n"
        )
        return title, text

    if 11 <= total <= 21:
        title = "🧑‍🚀 Homo sapiens"
        text = (
            "It’s quite natural to feel a bit down during winter.\n"
            "You are somewhat affected by winter blues — hard things feel heavier, but you still do them.\n\n"
            "**Tips that usually work:**\n"
            "- Tip 1.\n"
            "- Tip 2.\n"
            "- Tip 3.\n"
        )
        return title, text

    if 22 <= total <= 28:
        title = "🌳 A dormant tree"
        text = (
            "You’re standing, but winter takes a toll.\n"
            "Sometimes you resist winter blues, but it still gets you.\n\n"
            "**Supportive plan:**\n"
            "- Tip 1.\n"
            "- Tip 2.\n"
            "- Tip 3.\n"
        )
        return title, text

    # 29–35
    title = "🐻 Fuzzy bear"
    text = (
        "Winter doesn’t come naturally to you — it feels like hibernation mode.\n"
        "Everything seems hard and it may be difficult to cope alone.\n\n"
        "**What to do (gently):**\n"
        "- Tip 1.\n"
        "- Tip 2.\n"
        "- Tip 3.\n"
    )
    return title, text


with st.form("winter_blues_form_v2"):
    st.subheader("Questions")
    st.caption(SCALE_HELP_EN)

    answers = []
    for i, q in enumerate(QUESTIONS_V2, start=1):
        answers.append(
            st.slider(f"{i}) {q}", 1, 5, 3, 1, key=f"v2_q{i}")
        )

    submitted = st.form_submit_button("Get my result", key="v2_submit")

if submitted:
    total = sum(answers)
    title, tips = result_for_score_v2(total)

    st.divider()
    st.subheader("Your result")
    st.metric("Your score", total)
    st.markdown(f"### {title}")
    st.write(tips)

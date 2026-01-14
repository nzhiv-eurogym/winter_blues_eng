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


def result_for_score_v2(total: int) -> tuple[str, str, str]:

    # total is 7..35
    if 7 <= total <= 10:
        title = "Winter Warrior"
        text = (
            "You're ok, winter blues don't affect you that much. You sometimes feel tired, but you manage well.\n\n"
            "**Tips:**\n"
            "- A warrior with a working mind on the strategy will be more successful in his battle.\n**Why it helps**: That is why you too should engage in some mindful practices to keep your thoughts organised and focused. **First tiny step**: Practice mindfulness or meditation for 10 minutes daily.\n"
            "- A good warrior also needs some rest. Visit some exciting event (concert, theatre, cinema).\n**Why it helps**: Quality rest can increase your productivity, and interacting with the outside world can help you find new, meaningful connections, which is an effective mood lifter. **First tiny step**: Buy tickets and text your friends to invite them to join you.\n"
        )
        return title, text, "pic1.jpg"

    if 11 <= total <= 21:
        title = "Homo sapiens"
        text = (
            "It's quite natural for people to feel a bit down during the winter months. You are a bit affected by winter blues. It is overwhelming for you to do hard things, but you still do them, just with more effort.\n"
            "You are somewhat affected by winter blues — hard things feel heavier, but you still do them.\n\n"
            "**Tips:**\n"
            "- For all homo sapiens sleep schedule is really important. That is why you should be mindful with it. **Why it helps**: In winter, the reduced sunlight can scramble your internal clock. A consistent schedule, especially a fixed wake-up time, acts like an anchor, syncing your circadian rhythm with the outside world. **First tiny step**: Make yourself a schedule of when you would like to go to bed and when to wake up every day."
            "- As a Homo sapiens, your mind is your greatest survival tool, but in winter, it can turn into a battlefield of worrying thoughts. **Why it helps**: To start a journal means to let your thoughts flow freely and connect with your inner self. Writing down one's thoughts helps a person to understand and see their inner intentions and deep desires, which leads to a better overall understanding of their own life. **First tiny step**: Place a notebook near your bed. Don't write anything yet. Just create the possibility.\n"
        )
        return title, text, "pic2.jpg"

    if 22 <= total <= 28:
        title = "A dormant tree"
        text = (
            "You still stand, but your leaves fall during the colder months.\n"
            "You are affected by winter blues. It can get pretty rough for you during winter; sometimes you resist winter blues, but it still gets you.\n\n"
            "**Tips:**\n"
            "- Your energy is conserved inward, like a dormant tree. To gently signal for spring, send out one small \"root\" by researching one local club or online community related to your hobbies (e.g., book club, language exchange). **Why it helps**: Trees need each other to survive, which is why joining a club will stand you in good stead. By connecting with others through hobbies, you keep your energy up and follow your interests. **First tiny step**: Research what clubs are available and reach out to them."
            "- Just like a tree shedding its leaves to conserve energy, you need to get rid of the excessive use of social media to lower your stress levels. **Why it helps**: The constant stream of stressful news and comparison-driven social media drains your vital resources and casts a shadow over your already low light. Reducing time online reduces the cognitive and emotional "noise," making space for quieter thoughts. **First tiny step**: Set a time limit on your phone or find activities apart from social media.\n"
        )
        return title, text, "pic3.jpg"

    # 29–35
    title = "🐻 Fuzzy bear"
    text = (
        "Winter doesn't come naturally to you, and your body goes into hibernation mode.\n"
        "You are affected a lot by winter blues. Everything seems hard for you, and you can't cope with it on your own. You might need to ask for help from a professional.\n\n"
        "**Tips:**\n"
        "- Like a bear preparing its den, your first step is to check a critical internal resource: vitamin D. **Why it helps**: When you're in deep hibernation mode, everything feels hard. Vitamin D is a hormone crucial for serotonin production, immune function, and energy. **First tiny step**: ask your doctor to check your vitamin D levels.\n"
        "- Talk openly with your family or friends about how SAD affects you and what helps. **Why it helps**: In the wild, bear cubs hibernate with their mothers for warmth and safety. Reaching out makes you feel less isolated.**First tiny step**: try to connect with some of your relatives or friends, text them, and invite them to spend some time together..\n"
    )
    return title, text, "pic4.jpg"


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
    title, text, image_path = result_for_score_v2(total)

    st.divider()
    st.subheader("Your result")
    
    st.image(image_path, use_container_width=True)
    
    st.metric("Your score", total)
    st.markdown(f"### {title}")
    st.write(text)


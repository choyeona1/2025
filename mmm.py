import streamlit as st

# -----------------------------
# 직업 추천 데이터 (같음)
# -----------------------------
career_db = {
    "데이터/AI 연구": {
        "분석적": ["데이터 과학자 🧑‍💻", "머신러닝 연구원 🤖", "AI 알고리즘 엔지니어 📊", "딥러닝 전문가 🧠", "데이터 엔지니어 💾"],
        "창의적": ["AI 서비스 기획자 💡", "데이터 기반 UX 디자이너 🎨", "AI 스타트업 창업가 🚀"],
        "사교적": ["AI 윤리 컨설턴트 ⚖️", "AI 정책 분석가 🏛️", "데이터 컨설턴트 🤝"]
    },
    "로봇/하드웨어": {
        "분석적": ["로봇 제어 엔지니어 🤖", "자율주행 AI 연구원 🚗", "스마트 팩토리 엔지니어 🏭"],
        "창의적": ["휴머노이드 로봇 디자이너 🦾", "웨어러블 디바이스 개발자 ⌚"],
        "사교적": ["로봇 교육 전문가 📚", "AI 하드웨어 세일즈 엔지니어 💼"]
    },
    "예술/창작": {
        "분석적": ["AI 음악 데이터 분석가 🎼", "예술 트렌드 데이터 전문가 📊"],
        "창의적": ["AI 아트 디자이너 🎨", "가상현실 스토리텔러 🕶️", "AI 작곡가 🎹", "게임 AI 기획자 🎮"],
        "사교적": ["인터랙티브 공연 예술가 🎭", "메타버스 이벤트 기획자 🌐"]
    },
    "의료/보건": {
        "분석적": ["AI 헬스케어 연구원 🧬", "의료 데이터 분석가 💉", "바이오인포매틱스 전문가 🔬"],
        "창의적": ["AI 재활 로봇 디자이너 🦿", "디지털 치료 콘텐츠 개발자 📱"],
        "사교적": ["AI 헬스케어 상담사 💊", "원격 진료 코디네이터 🩺", "스마트 헬스 코치 🏃‍♂️"]
    },
    "교육": {
        "분석적": ["AI 학습 분석가 📖", "교육 데이터 전문가 📊"],
        "창의적": ["AI 교육 콘텐츠 디자이너 🖥️", "VR 가상 교실 개발자 🕶️"],
        "사교적": ["AI 튜터 👩‍🏫", "온라인 학습 코치 🎓", "교육 메타버스 운영자 🌍"]
    },
    "환경/에너지": {
        "분석적": ["기후 데이터 분석가 🌎", "스마트 에너지 시스템 연구원 🔋"],
        "창의적": ["지속가능 AI 디자이너 🌱", "친환경 도시 개발자 🏙️"],
        "사교적": ["환경 정책 컨설턴트 📢", "에코테크 홍보 전문가 🌿"]
    },
    "금융/비즈니스": {
        "분석적": ["AI 금융 분석가 💹", "핀테크 데이터 사이언티스트 🏦"],
        "창의적": ["AI 기반 투자 전략가 📈", "스마트 비즈니스 기획자 💼"],
        "사교적": ["AI 마케팅 전문가 📣", "AI 경영 컨설턴트 🧑‍💼"]
    },
    "게임/엔터테인먼트": {
        "분석적": ["게임 AI 프로그래머 👾", "e스포츠 데이터 분석가 🏆"],
        "창의적": ["게임 시나리오 디자이너 ✍️", "AI 게임 아티스트 🎨"],
        "사교적": ["VR 게임 기획자 🕶️", "메타버스 커뮤니티 매니저 👥"]
    },
    "보안/국방": {
        "분석적": ["사이버 보안 AI 연구원 🔐", "AI 기반 위협 분석가 🛡️"],
        "창의적": ["보안 시뮬레이션 디자이너 🎮", "AI 기반 방어 전략가 🛰️"],
        "사교적": ["사이버 보안 컨설턴트 🧑‍💼", "AI 국방 전략 기획자 ⚔️"]
    },
    "교통/스마트시티": {
        "분석적": ["자율주행 데이터 과학자 🚘", "스마트 교통 분석가 🚦"],
        "창의적": ["스마트시티 디자이너 🏙️", "AI 교통 시스템 기획자 🛣️"],
        "사교적": ["스마트 모빌리티 코디네이터 🚍", "자율주행 서비스 운영자 🚖"]
    }
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI 미래 직업 추천", page_icon="🌸", layout="centered")

# CSS (파스텔톤 + 귀여움)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7, #c1dfc4, #fefbd8);
        background-size: 400% 400%;
        animation: pastelBG 12s ease infinite;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #444;
    }
    @keyframes pastelBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stButton>button {
        background: linear-gradient(90deg, #ffb6b9, #fae3d9, #bbded6);
        color: #333;
        border-radius: 30px;
        font-size: 18px;
        font-weight: bold;
        padding: 0.7em 1.4em;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.15);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background: linear-gradient(90deg, #bbded6, #fae3d9, #ffb6b9);
    }

    .card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin: 12px 0;
        box-shadow: 3px 6px 12px rgba(0,0,0,0.15);
        text-align: center;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: scale(1.05) rotate(-1deg);
        background: #fff8fb;
    }

    h1, h2 {
        text-align: center;
        color: #ff69b4;
        text-shadow: 1px 1px 2px #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown("<h1>🌸🐰 AI 미래 직업 추천 🐰🌸</h1>", unsafe_allow_html=True)
st.write("✨ 관심분야와 성격을 선택하면 미래 직업을 추천해드려요! ✨")

# 입력
interest = st.selectbox("🌈 관심분야를 선택해 주세요", list(career_db.keys()))
personality = st.selectbox("😃 성격 유형을 선택해 주세요", ["분석적", "창의적", "사교적"])

# 결과
if st.button("💖 직업 추천 받기 💖"):
    recommendations = career_db[interest][personality]
    st.markdown("<h2>🌟 당신에게 찰떡인 직업 🌟</h2>", unsafe_allow_html=True)

    for job in recommendations:
        st.markdown(f"<div class='card'><h4>{job}</h4></div>", unsafe_allow_html=True)

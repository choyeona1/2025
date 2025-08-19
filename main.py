import streamlit as st

# 🎨 Streamlit 기본 설정
st.set_page_config(page_title="💘 MBTI 궁합 테스트 💘", page_icon="💞", layout="centered")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 궁합 데이터 예시
compatibility = {
    ("ENFP", "INFJ"): {"score": 95, "desc": "🌈✨ 서로의 부족함을 채워주는 환상적인 💞 소울메이트 조합! ✨🌈"},
    ("ENTP", "INTJ"): {"score": 90, "desc": "🧠⚡ 끝없는 지적 자극! 서로에게 도전과 영감을 주는 커플 💡🔥"},
    ("ISTJ", "ESFP"): {"score": 85, "desc": "📚🤹 안정과 자유의 완벽한 밸런스! 🎶💃"},
}

# 헤더
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>💘 MBTI 궁합 테스트 💘</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>✨ 나와 상대방의 MBTI로 우리의 💕 케미 지수를 확인해보세요 ✨</h3>", unsafe_allow_html=True)
st.markdown("---")

# 입력창
col1, col2 = st.columns(2)

with col1:
    my_mbti = st.selectbox("😎 내 MBTI", mbti_types)

with col2:
    partner_mbti = st.selectbox("😍 상대방 MBTI", mbti_types)

# 버튼
if st.button("💞 궁합 확인하기 💞"):
    key = (my_mbti, partner_mbti)
    rev_key = (partner_mbti, my_mbti)

    if key in compatibility:
        result = compatibility[key]
    elif rev_key in compatibility:
        result = compatibility[rev_key]
    else:
        result = {"score": 70, "desc": "🤝 무난한 조합! ✨ 서로 노력하면 💗 더 특별해질 수 있어요 🌟"}

    # 결과 출력
    st.markdown(f"<h2 style='text-align: center; color: #ff69b4;'>💝 궁합 점수: {result['score']}점 💝</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px; text-align:center;'> {result['desc']} </p>", unsafe_allow_html=True)

    # 🔥 Progress Bar
    st.progress(result['score'] / 100)

    # 🎉 이모지 폭죽 애니메이션 느낌
    st.markdown(f"<h1 style='text-align: center;'>🎊🎉✨💖🌈🔥🌟💫🍀🌸</h1>", unsafe_allow_html=True)

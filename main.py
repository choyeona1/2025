import streamlit as st

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 궁합 데이터 (예시)
compatibility = {
    ("ENFP", "INFJ"): {"score": 95, "desc": "서로의 부족함을 잘 채워주는 환상적인 조합!"},
    ("ENTP", "INTJ"): {"score": 90, "desc": "서로 도전적이고 지적 자극을 주는 관계."},
    ("ISTJ", "ESFP"): {"score": 85, "desc": "안정적인 ISTJ와 자유로운 ESFP의 균형 잡힌 조화."},
    # ... 여기에 더 추가 가능
}

st.title("💞 MBTI 궁합 테스트")
st.write("내 MBTI와 상대방 MBTI를 선택하면 궁합을 알려드립니다!")

col1, col2 = st.columns(2)

with col1:
    my_mbti = st.selectbox("내 MBTI", mbti_types)

with col2:
    partner_mbti = st.selectbox("상대방 MBTI", mbti_types)

if st.button("궁합 보기"):
    key = (my_mbti, partner_mbti)
    rev_key = (partner_mbti, my_mbti)

    if key in compatibility:
        result = compatibility[key]
    elif rev_key in compatibility:
        result = compatibility[rev_key]
    else:
        result = {"score": 70, "desc": "보통의 궁합이에요. 서로 노력하면 좋은 관계로 발전할 수 있어요!"}

    st.subheader(f"궁합 점수: {result['score']}점")
    st.write(result["desc"])

    # 시각화 (게이지 느낌)
    st.progress(result['score'] / 100)

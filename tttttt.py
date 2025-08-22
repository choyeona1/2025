import streamlit as st

st.title("💧 운동 후 수분 손실 & 보충량 계산기")

st.write("""
운동 전후 체중을 입력하면, 운동 중 손실된 수분량과 필요한 수분 보충량을 계산합니다.  
👉 일반적으로 땀으로 손실된 체중은 대부분 수분 손실로 간주합니다.
""")

# 입력값
weight_before = st.number_input("🏋️ 운동 전 체중 (kg)", min_value=1.0, step=0.1, value=60.0)
weight_after = st.number_input("🏋️‍♂️ 운동 후 체중 (kg)", min_value=1.0, step=0.1, value=59.3)
exercise_time = st.number_input("⏱️ 운동 시간 (분)", min_value=1.0, step=1.0, value=60.0)

if weight_after < weight_before:
    # 수분 손실 계산
    water_loss = weight_before - weight_after  # kg 단위 (≈ L 단위와 동일)
    # 땀 손실율 (운동 시간 대비 체중 손실 비율)
    sweat_rate = water_loss / (exercise_time / 60)  # L/hr
    # 보충 권장량 (손실 수분량의 150% 보충 권장)
    water_intake = water_loss * 1.5  

    st.subheader("📊 결과")
    st.metric("운동 중 수분 손실량", f"{water_loss:.2f} L")
    st.metric("땀 손실률", f"{sweat_rate:.2f} L/hr")
    st.metric("권장 수분 보충량", f"{water_intake:.2f} L")

    # 안내 메시지
    if water_loss < 0.5:
        st.success("✅ 수분 손실이 크지 않습니다. 물 한두 컵 정도로 충분합니다.")
    elif water_loss < 1.0:
        st.warning("⚠️ 수분 손실이 중간 정도입니다. 충분히 수분을 섭취하세요.")
    else:
        st.error("🚨 수분 손실이 큽니다! 운동 직후 충분히 수분을 보충해야 합니다.")

else:
    st.info("ℹ️ 운동 후 체중이 운동 전보다 적어야 수분 손실 계산이 가능합니다.")


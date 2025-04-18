import streamlit as st
from blog_generator import generate_blog_post
from cardnews_generator import make_card_image

st.set_page_config(page_title="AI 블로그 콘텐츠 생성기", layout="wide")

# 개인 보안을 위해 비밀번호 확인
PASSWORD = st.secrets["APP_PASSWORD"]
input_password = st.text_input("평범 사용자는 입이 안됩니다. 비밀번호를 입력해주세요.", type="password")
if input_password != PASSWORD:
    st.warning("허가된 비밀번호를 입력해주세요.")
    st.stop()

st.title("플랫폼 보너스 복합 AI 블로그 작성 기")

platform = st.selectbox("제작할 플랫폼을 선택해주세요.", ["네이버 블로그", "티스토리", "에스코 블로그"])
industry = st.text_input("어느 업종인가요? (예: 간판, 방송, 인터넷 서비스)")
content_type = st.selectbox("무엇을 쓰고 싶으시나요?", ["정보형", "후기형", "자랑형"])
writing_style = st.selectbox("원하는 문체를 선택해주세요.", ["대학원법 전문성", "후기형 간단한 말하기", "반려체 편집형", "잘일하는 것 같은 말하기"])
title = st.text_input("블로그 제목을 입력해주세요")
extra_instruction = st.text_area("(선택) 추가 요청사항이 있으면 입력해주세요")

if st.button(":pencil2: 블로그 작성 시작"):
    with st.spinner(":writing_hand: AI를 통해 블로그 결과를 생성하는 중..."):
        result = generate_blog_post(
            platform=platform,
            industry=industry,
            content_type=content_type,
            writing_style=writing_style,
            title=title,
            extra_instruction=extra_instruction
        )
        st.success(":white_check_mark: 블로그 작성 완료!")
        st.markdown(result, unsafe_allow_html=True)

        if st.button(":framed_picture: 카드뉴스 생성"):
            with st.spinner(":art: 카드뉴스 생성 중..."):
                make_card_image(title, result)

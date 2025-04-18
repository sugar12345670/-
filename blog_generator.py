from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_blog_post(platform, industry, content_type, writing_style, title, extra_instruction):
    system_prompt = "너는 플랫폼별 맞춤형 SEO 블로그 콘텐츠를 작성하는 마케팅 전문가야. 각 플랫폼 스타일에 맞춰줘."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"플랫폼: {platform}\n업종: {industry}\n형태: {content_type}\n문체: {writing_style}\n제목: {title}\n추가요청: {extra_instruction}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages
    )
    return response.choices[0].message.content

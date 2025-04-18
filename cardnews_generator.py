import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap

def make_card_image(title, blog_content):
    card = Image.new("RGB", (1024, 1024), color="white")
    draw = ImageDraw.Draw(card)
    font_title = ImageFont.truetype("arial.ttf", 50)
    font_text = ImageFont.truetype("arial.ttf", 30)
    
    draw.text((50, 30), title, font=font_title, fill="black")

    wrapped_text = textwrap.fill(blog_content, width=45)
    draw.text((50, 150), wrapped_text[:1000], font=font_text, fill="black")

    card.save("/tmp/card_output.png")
    st.image("/tmp/card_output.png", caption="카드뉴스 미리보기")

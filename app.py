import streamlit as st
from datetime import date
import base64
import os
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="Happy Birthday, Ma'am!", page_icon="🌸", layout="centered")

def set_background_image(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100vh;
            color: white;
            text-shadow: 1px 1px 2px black;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def display_image_in_square(image_path, caption="Image", size=450):
    if not os.path.exists(image_path):
        st.error(f"Image not found: {image_path}")
        return
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .image-container {{
            text-align: center;
            margin-top: 20px;
        }}
        .birthday-image {{
            width: {size}px;
            height: {size}px;
            border-radius: 50%;
            object-fit: cover;
            margin: 0 auto;
        }}
        .caption {{
            font-size: 18px;
            font-family: 'Poppins', sans-serif;
            color: white;
            margin-top: 10px;
        }}
        </style>
        <div class="image-container">
            <img src="data:image/jpeg;base64,{encoded_image}" class="birthday-image" alt="{caption}" />
            <div class="caption">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@400;700&display=swap');

    h1, h2, h3 {
        font-family: 'Dancing Script', cursive;
        color: #FF69B4;
        text-align: center;
    }

    p, div, span, ul, li {
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
    }

    .stButton>button {
        background-color: #FF69B4;
        color: white;
        font-size: 18px;
        border-radius: 15px;
        font-family: 'Poppins', sans-serif;
        padding: 12px 25px;
        border: 2px solid #FF1493;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        background-color: #FF1493;
        color: white;
        border: 2px solid #FF69B4;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.4);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

set_background_image("hardik.webp")

st.title("🌸 To the Most Beautiful Soul – Happy 20th Birthday! 🎂")
st.write("Hey Janhvi, this is a little something to make your day extra special! ✨")

st.markdown("## 💖 You Make the World Shine Brighter!")
st.markdown(
    """
    <p style='text-align: center; font-size: 20px;'>
    May your birthday be filled with love, joy, and all the wonderful surprises you deserve. 
    You are truly one of a kind! 🌟
    </p>
    """,
    unsafe_allow_html=True,
)

display_image_in_square("a.jpg", caption="The Birthday Queen 👑", size=450)

st.write("")

if st.button("🎉 Click for Your Birthday Message! 🎁"):
    st.balloons()
    st.snow()
    st.write(
        """
        🌟I know you must be receiving countless greetings, but I wanted to take a moment to personally write to you (without ChatGPT) and express how truly amazing you are. May this year bring you immense joy, happiness, and success. You’re an incredible person, and I’m confident you’ll continue to reach new heights. As I always say, your courage is your strength. Stay bold, stay gutsy, and always stay true to yourself—just as you are today.

I’ve never met anyone like you—so dedicated to your work and passionate about your goals. Most people I’ve encountered tend to get lost in dreamy, fanciful worlds, but you stand out with your practicality and determination. Your courage and commitment are truly your strengths, and I feel incredibly grateful to have a friend like you.

Your dedication to your book club is remarkable, and the way you manage everything—your studies, work, and passions—is genuinely inspiring. Although I don’t read many books, I deeply respect what you do and draw inspiration from your unwavering focus.

You’re the first woman I’ve met who approaches life with such a grounded and practical mindset. I wish you a brilliant future ahead and want you to know that I’ll always be your well-wisher.

Oh, and I remember the story you told last summer about how helpers in school make life so much easier. That story really stayed with me and made me respect you even more. It showed how thoughtful you are and how much you appreciate the little things that often get overlooked. You're really inspiring.
        """
    )

st.write("---")
st.markdown(
    f"<p style=\"text-align: center; font-family: Poppins, sans-serif;\">Today's date: <strong>{date.today().strftime('%B %d, %Y')}</strong></p>",
    unsafe_allow_html=True,
)

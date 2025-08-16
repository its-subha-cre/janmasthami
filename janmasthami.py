import streamlit as st
import base64
import time

st.set_page_config(page_title="Happy Janmashtami", layout="centered")

# === Encode local images to base64 ===
def encode_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

krishna_img = encode_image("srikrishna.jpg")
feather_img = encode_image("peacockfeather.png")

# === Feather Loading Animation ===
st.markdown(f"""
    <style>
    /* Fullscreen loader */
    #loader {{
        position: fixed;
        width: 100%;
        height: 100%;
        background-color: white;
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        animation: fadeOut 1s ease-in-out 3s forwards;
    }}

    /* Diagonal movement */
    .feather {{
        width: 750px;
        animation: flyFeather 3s ease-in-out forwards;
    }}

    @keyframes flyFeather {{
        0% {{
            transform: translate(-600px, 400px) rotate(0deg);
            opacity: 0;
        }}
        30% {{
            opacity: 1;
        }}
        100% {{
            transform: translate(0, 0) rotate(360deg);
            opacity: 0;
        }}
    }}

    @keyframes fadeOut {{
        to {{
            opacity: 0;
            visibility: hidden;
        }}
    }}
    </style>

    <div id="loader">
        <img src="data:image/png;base64,{feather_img}" class="feather" />
    </div>
""", unsafe_allow_html=True)

# === Delay real content until feather fades out ===
# time.sleep(3.5)  # Must match fadeOut animation duration

# === Main Krishna Image ===
st.markdown(f"""
    <style>
        .krishna-container {{
            display: flex;
            justify-content: center;
            animation: float 3s ease-in-out infinite;
            margin-bottom: 20px;
        }}

        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-20px); }}
            100% {{ transform: translateY(0px); }}
        }}
    </style>
    <div class="krishna-container">
        <img src="data:image/jpeg;base64,{krishna_img}" width="800">
    </div>
""", unsafe_allow_html=True)


            


# === Greeting Header ===
st.markdown("<h1 style='text-align:center; color:#5C2E7E;'>🌼 Happy Janmashtami! 🌼</h1>", unsafe_allow_html=True)

# === User Input ===
name = st.text_input("Enter your name to create a personalized greeting:")

if st.button("Create My Greeting"):
    base_url = "https://your-deployed-url.streamlit.app"  # Change this after deployment
    share_url = f"{base_url}/?from={name}"

    st.markdown(f"<h2 style='text-align:center;'>🎉 Happy Janmashtami, {name}! 🎉</h2>", unsafe_allow_html=True)

    # Create Share Links
    import urllib.parse
    share_text = f"🌸 Happy Janmashtami from {name}! 🌸\nMake your own greeting: {share_url}"
    encoded_text = urllib.parse.quote(share_text)

    whatsapp = f"https://wa.me/?text={encoded_text}"
    facebook = f"https://www.facebook.com/sharer/sharer.php?u={urllib.parse.quote(share_url)}"
    twitter = f"https://twitter.com/intent/tweet?text={encoded_text}"

    # Share Buttons
    st.markdown("### 📲 Share with your friends:")
    st.markdown(f"""
        <div style="display: flex; gap: 20px; font-size: 20px;">
            <a href="{whatsapp}" target="_blank">📱 WhatsApp</a>
            <a href="{facebook}" target="_blank">📘 Facebook</a>
            <a href="{twitter}" target="_blank">🐦 Twitter</a>
        </div>
    """, unsafe_allow_html=True)
st.markdown("""
    <hr style="margin-top: 50px;">
    <p style='text-align: center; color: #8B0000; font-size: 18px; font-family: "Segoe UI", sans-serif;'>
        ✨ Made with love ❤️ for <strong>Krishna</strong> by <strong>Subhayan</strong> 🙏
    </p>
""", unsafe_allow_html=True)

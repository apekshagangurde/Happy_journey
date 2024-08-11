import streamlit as st
from PIL import Image

# Set the page configuration
st.set_page_config(page_title="Bon Voyage to Switzerland!", page_icon="🎈")

# Title of the page
st.title("Bon Voyage to Switzerland! 🎉")

# Display balloons
st.balloons()

# Add an image of Switzerland (you can use any image URL or local image)
image = Image.open("switzerland.webp")  # Make sure you have this image in the same directory
st.image(image, caption="Beautiful Switzerland", use_column_width=True)

# Add a personalized message
st.write("""
## Dear Mansi,

Wishing you an amazing trip to Switzerland! May your journey be filled with incredible experiences, breathtaking views, and unforgettable memories. Don't forget to take lots of pictures and share your adventures with us!

Safe travels and see you soon!

Best Wishes,
Apeksha Gangurde & srushti Ahire
""")

# Add a fun interactive element - a slider to guess how much chocolate they'll eat!
chocolate = st.slider("How much Swiss chocolate do you think you'll eat? (in kg)", 0, 10, 3)
st.write(f"Wow! That's {chocolate} kg of delicious Swiss chocolate! 🍫")

# Add a map to show Switzerland
st.map({"lat": [46.8182], "lon": [8.2275]})

# Add a final wish
st.subheader("Don't forget to enjoy every moment and take in all the beauty Switzerland has to offer! 🇨🇭")

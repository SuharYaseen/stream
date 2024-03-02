import streamlit as st

def main():
    st.title("Image Viewer")

    # Displaying a locally stored image
    st.header("Local Image")
    local_image_path = "IMG_20230403_134230.jpg"  # Replace with the path to your local image
    st.image(local_image_path, caption="Example Image", use_column_width=True)

    # Displaying an image from URL
    st.header("Online Image")
    online_image_url = "https://www.example.com/example_image.jpg"  # Replace with the URL of your online image
    st.image(online_image_url, caption="Example Image", use_column_width=True)

if __name__ == "__main__":
    main()

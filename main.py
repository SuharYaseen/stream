import streamlit as st
import os
import base64

def read_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("Book Library")

    books_dir = "books"
    book_files = os.listdir(books_dir)
    selected_book = st.sidebar.selectbox("Select a book", book_files)

    if selected_book:
        st.sidebar.markdown("---")
        st.sidebar.write("You are currently reading:")
        st.sidebar.write(selected_book)
        read_pdf(os.path.join(books_dir, selected_book))

if __name__ == "__main__":
    main()

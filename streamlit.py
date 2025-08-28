import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO
import textwrap

st.set_page_config(page_title="Python 101 - Interactive Classroom", page_icon="🍎", layout="wide")

#Header
st.title("🍎 Python 101 - Interactive Classroom - page header")
st.caption("An all-in-one Streamlit app to teach beginners the core Python concepts, step by step.")

# Helper function to pretty print code blocks alongside output
def show_code(title: str, code: str, run_fn=None):
    with st.expander(f"📦 {title} — see code & run"):
        st.code(code, language="python")
        if run_fn:
            st.markdown("**Run it here:**")
            run_fn()

st.sidebar.header("Lesson Navigator")

section = st.sidebar.radio(
    "Jump to a section",
    [
        "Welcome",
        "1) Python Basics",
        "2) Lists & Loops",
        "3) Functions & Errors",
        "4) Files & CSV",
        "5) Data Visualization (Matplotlib)",
        "6) Call an API (GET/POST)",
        "7) Mini Quiz"
    ],
    index=0
)

if section == "Welcome":
    st.subheader("How to use this app")
    st.markdown(
        '''
        - Use the left sidebar to move through lessons.
        - Each lesson has **live examples** you can run.
        - Keep things playful — change inputs and see what happens.
        - By the end, you’ll have touched variables, lists, loops, functions, files, charts, and simple APIs.
        '''
    )
    st.info("Tip: Press **R** to rerun the app after editing widgets")

#Python Basics

if section == "1) Python Basics":
    st.subheader("Variables, Types and Printing")
    name = st.text_input("What's your name?", value="Adem")
    age = st.number_input("How old are you?", min_value=5, max_value=120, value=18, step=1)

    def run_basics():
        st.write(f"Hello, **{name}**! In python we can store your age like this:")
        python_code = f'name = "{name}"\nage = {age}\nprint("Hi", name, "- you are", age, "years old!")'
        st.code(python_code, language="python")
        st.write("Output: ")
        st.write(f"Hi {name} - you are {age} years old!")

        st.markdown("**Common Types**: `int`, `float`, `str`, `bool`, `list`, `dict`.")

    basics_code = textwrap.dedent('''
        name = "Adem",
        age = 18,
        print("Hi", name, "- you are", age, "years old!")
    ''')

    show_code("Variables & print()", basics_code, run_fn=run_basics)

    st.divider()
    st.subheader("Type Conversion")
    number_str = st.text_input("Enter a number (as text):", "42")

    def run_casting():
        try:
            as_int = int(number_str)
            st.write(f"`int('{number_str}')` -> ", as_int, type(as_int).__name__)
        except ValueError:
            st.error("That text is not an integer. Try 42 or 19 etc.")

    casting_code = textwrap.dedent('''
        text_number = "42"
        as_int = int(text_number) # -> 42
        print(as_int, type(as_int))
    ''')
    show_code("Casting text to numbers", casting_code, run_fn=run_casting)

#Lists & Loops

if section == "2) Lists & Loops":
    st.subheader("Build a List, Loop it, Slice it")
    fruits = st.multiselect("Pick some fruits", ["apple", "banana", "orange", "pear"], default=["apple", "banana"])

    def run_lists():
        st.write("Your list: ", fruits)
        st.write("First item (index 0): ", fruits[0] if fruits else "-")
        st.write("Slice first two: ", fruits[:2])
        st.write("Looping:")

        for idx, fruit in enumerate(fruits):
            st.write(f"{idx}: {fruit}")
        
    lists_code = textwrap.dedent('''
    fruits = ["apple", "banana", "orange"]
    print(fruits[0])     # index
    print(fruits[:2])    # slice
    for i, f in enumerate(fruits):
        print(i, f)      # loop
''')
    show_code("Lists, indexing, slicing, enumerate()", lists_code, run_fn=run_lists)


    st.divider()
    st.subheader("List Comprehensions")
    base = st.slider("Base Number", 1, 12, 3)
    limit = st.slider("How many squares?", 3, 20, 5)

    def run_comprehension():
        squares = [n**2 for  n in range(base, base + limit)]
        st.write("Squares", squares)
    comp_code = textwrap.dedent('''
        base, limit = 3, 5
        squares = [n**2 for n in range(base, base+limit)]
        print(squares)  # [9, 16, 25, 36, 49]
    ''')
    show_code("List comprehensions", comp_code, run_fn=run_comprehension)


if section == "3) Functions & Errors":
    st.subheader("Write and call functions")
    a = st.number_input("a", value=5)
    b = st.number_input("b", value=2)

    def run_functions():
        def safe_divide(x,y):
            if y == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return x / y

        st.write("`a + b` = ", a + b)
        try:
            st.write("`a / b` = ", safe_divide(a, b))
        except ZeroDivisionError as error:
            st.error(str(error))
    
    func_code = textwrap.dedent('''
        def safe_divide(x, y):
            if y == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return x / y

        print(safe_divide(10, 2))  # 5.0
    ''')
    show_code("Defining functions & raising errors", func_code, run_fn=run_functions)

if section == "4) Files & CSV":
    st.subheader("Read CSV into Pandas")
    csv_text = st.text_area(
        "Paste small CSV here",
        value="name,age\nAda,18\nBob,21",
        height=120
    )

    def run_csv():
        try:
            df = pd.read_csv(StringIO(csv_text))
            st.write("Preview dataframe: ")
            st.dataframe(df, use_container_width=True) 
        except Exception as e:
            st.error(f"Error parsing csv: {e}")
    csv_code = textwrap.dedent('''
        import pandas as pd
        from io import StringIO

        csv_text = "name,age\nAda,18\nBob,21"
        df = pd.read_csv(StringIO(csv_text))
        print(df.head())
    ''')
    show_code("Reading CSV text", csv_code, run_fn=run_csv)

    st.divider()

    st.subheader("Upload a CSV file")
    upload = st.file_uploader("Choose a CSV", type=["csv"])
    if upload:
        try:
            df = pd.read_csv(upload)
            st.success("Loaded!")
            st.dataframe(df, use_container_width=True)
        
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")


if section == "5) Data Visualization (Matplotlib)":
    st.subheader("Plot a simple chart")
    n = st.slider("How many points?", 5, 100, 20)
    x = np.arange(n)
    y = np.random.randn(n).cumsum()

    def run_plot():
        fig, ax = plt.subplots()
        ax.plot(x, y, marker="o")
        ax.set_title("Random Walk")
        ax.set_xlabel("Step")
        ax.set_ylabel("Value")
        st.pyplot(fig)

    plot_code = textwrap.dedent('''
        import numpy as np
        import matplotlib.pyplot as plt

        n = 20
        x = np.arange(n)
        y = np.random.randn(n).cumsum()

        fig, ax = plt.subplots()
        ax.plot(x, y, marker="o")
        ax.set_title("Random Walk")
        ax.set_xlabel("Step")
        ax.set_ylabel("Value")
        plt.show()
    ''')
    show_code("Matplotlib line chart", plot_code, run_fn=run_plot)


if section == "6) Call an API (GET/POST)":
    st.subheader("Use requests to talk to a public API")
    st.caption("We'll use JSONPlaceholder (fake API for testing).")
    endpoint = st.selectbox("Endpoint", ["users", "posts", "comments"], index=0)
    base_url = "https://jsonplaceholder.typicode.com"

    def run_get():
        url = f"{base_url}/{endpoint}"
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()[:5]  # show a few
            st.json(data)
        except Exception as e:
            st.error(f"GET failed: {e}")

    get_code = textwrap.dedent('''
        import requests
        url = "https://jsonplaceholder.typicode.com/[select_option]"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        print(r.json())
    ''')
    show_code("GET request", get_code, run_fn=run_get)

    st.divider()
    st.subheader("POST (send data)")
    title = st.text_input("Title", "Hello world")
    body = st.text_area("Body", "This is a test post.")
    user_id = st.number_input("userId", 1, 10, 1, step=1)

    def run_post():
        url = f"{base_url}/posts"
        payload = {"title": title, "body": body, "userId": user_id}
        try:
            r = requests.post(url, json=payload, timeout=10)
            r.raise_for_status()
            st.json(r.json())
        except Exception as e:
            st.error(f"POST failed: {e}")

    post_code = textwrap.dedent('''
        import requests
        payload = {"title": "Hello world", "body": "This is a test", "userId": 1}
        r = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, timeout=10)
        r.raise_for_status()
        print(r.json())
    ''')
    show_code("POST request", post_code, run_fn=run_post)
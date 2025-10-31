import streamlit as st 
st.set_page_config(page_title="To-Do list :D ", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #FFD5CD 0%, #F5F0D4 20%, #D4F0D1 40%, #D1EEF0 60%, #F5D4E8 80%, #FFD5CD 100%);
        }
        
        .main-container {
            background-color: white;
            padding: 2rem;
            border-radius: 2rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: 3rem auto;
        }


        h1 {
            color: #F5A9B8;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            color: #A8C5C0;
            text-align: center;
            font-size: 0.9rem;
            margin-bottom: 2rem;
        }

        div[data-testid="stTextInput"] > div > div > input {
            border-radius: 2rem;
            border: 2px solid #D4F0D1;
            background-color: #FEFEFE;
        }

        .stButton > button {
            border-radius: 2rem;
            background: linear-gradient(135deg, #FFD5CD, #F5A9B8);
            color: white; 
            border: none;
            padding: 0.5rem 2rem;
            font-weight: 500;
        }

        .stButton > button:hover {
            box-shadow: 0 5px 15px rgba(245, 169, 184, 0.4);
        }

        .stats {
            text-align: center; 
            color: #A8C5C0;
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid #F0F0F0;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)


if 'todos' not in st.session_state:
    st.session_state.todos = []

st.markdown("<h1> To-Do List </h1>", unsafe_allow_html=True)
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'> let's get these things over with! </p>", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
with col1:
    new_todo = st.text_input("", placeholder="add a new task...", label_visibility="collapsed", key="new_todo_input")
with col2:
    if st.button("+ add"):
        if new_todo.strip():
            st.session_state.todos.append({"text": new_todo, "completed": False})
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("</div", unsafe_allow_html=True)


if not st.session_state.todos:
    st.markdown("""
    <div style='text-align: center; padding: 3rem; color: #C4C4C4;'>
        <p style='font-size: 1.2rem;'>no tasks yet!</p>
        <p style='font-size: 0.9rem;'>add one above to get started</p>
    </div>
    """, unsafe_allow_html=True)

else: 
    for idx, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([0.5, 4, 0.5])

        with col1: 
            if st.checkbox("", value=todo["completed"], key=f"check_{idx}", label_visibility="collapsed"):
                st.session_state.todos[idx]["completed"] = True
            else: 
                st.session_state.todos[idx]["completed"] = False

        with col2: 
            text_style = "text-decoration: line-through; color: #A8C5C0;" if todo["completed"] else "color: #666;"
            st.markdown(f"<p style='{text_style} margin: 0; padding: 0.5rem 0;'>{todo['text']}</p>", unsafe_allow_html=True)

        with col3: 
            if st.button("🗑️", key=f"delete_{idx}"):
                st.session_state.todos.pop(idx)
                st.rerun()

    completed = sum(1 for tod in st.session_state.todos if tod["completed"])
    total = len(st.session_state.todos)
    celebration = "done" if completed == total and total > 0 else "" 

    st.markdown(f""" 
    <div class='stats'> 
        {completed} of {total} completed {celebration}
    </div>
    """, unsafe_allow_html=True)

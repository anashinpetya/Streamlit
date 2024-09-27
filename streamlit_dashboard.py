import streamlit as st
from streamlit_option_menu import option_menu
from views import overdue_stats
from views import closed_tasks_stats, general_stats, unclosed_tasks_stats, conclusions

#code to run:
#cd C:\test tasks\VkusVill\streamlit dashboard
#python -m streamlit run streamlit_dashboard.py
#for requirements: python -m pipreqs.pipreqs

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": None
    })

with st.sidebar:
    selected=option_menu(
        menu_title="Анализ количества и решения багов",
        options=["Общая статистика", "Статистика по просроченным задачам", 
                 "Статистика по незакрытым задачам", "Статистика по закрытию задач", "Выводы"],
        icons=["bi-caret-right-fill", "bi-caret-right-fill", "bi-caret-right-fill", "bi-caret-right-fill", "bi-caret-right-fill"],
        menu_icon="bi-graph-up",
        default_index=0,
        styles={
        "nav-link-selected": {"background-color": "#039BE5"},
        "menu-title": {"font-weight": "bold"}
    }
    )

if selected=="Статистика по закрытию задач":
    closed_tasks_stats.CreatePage()

if selected=="Общая статистика":
    general_stats.CreatePage()

if selected=="Статистика по просроченным задачам":
    overdue_stats.CreatePage()

if selected=="Статистика по незакрытым задачам":
    unclosed_tasks_stats.CreatePage()

if selected=="Выводы":
    conclusions.CreatePage()

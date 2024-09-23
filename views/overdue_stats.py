import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import pandas as pd

overdue_tasks_teams=pd.read_excel("VkusVill_analysis_results.xlsx", sheet_name="overdue_tasks_teams", index_col=0)
overdue_tasks_teams=overdue_tasks_teams.reset_index()
overdue_tasks_teams=overdue_tasks_teams.head(10)
overdue_tasks_teams=overdue_tasks_teams.sort_values(by="outdated_bugs_share", ascending=True)
overdue_tasks_teams["outdated_bugs_share"]=overdue_tasks_teams["outdated_bugs_share"].round(3)
overdue_tasks_teams["outdated_bugs_share"]=overdue_tasks_teams["outdated_bugs_share"]*100

def CreatePage():
    
    st.title("Статистика по просроченным задачам")

    st.markdown("""---""")

    # Creating columns with metric widgets
    box_1, box_2, box_3 = st.columns(3)

    box_1.metric("Процент просроченных задач", "21.1%")
    box_2.metric("Средняя длина просрочки", "24 дня")
    box_3.metric("Максимальная длина просрочки", "129 дней")

    style_metric_cards(border_left_color="#039BE5", box_shadow=False)

    fig_overdue_tasks_teams = px.bar(
            overdue_tasks_teams,
            x="outdated_bugs_share",
            y="team",
            orientation="h",
            color_discrete_sequence=["#039BE5"] * len(overdue_tasks_teams),
            template="plotly_white",
            labels={'outdated_bugs_share': 'Процент просроченных задач', 'team':'Команда'},
            width=900, height=600
        )

    fig_overdue_tasks_teams.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=True, ticksuffix="%")),
            title={
            'text': "<b>Топ-10 команд, участвовавших в просроченных задачах</b>",
            'font': dict(size=20),
            'y':0.96,
            'x':0.62,
            'xanchor': 'center',
            'yanchor': 'top'} 
        )

    st.plotly_chart(fig_overdue_tasks_teams)

    return True
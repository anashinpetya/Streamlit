import streamlit as st
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd

unclosed_bugs_teams=pd.read_excel("VkusVill_analysis_results.xlsx", sheet_name="unclosed_bugs_teams", index_col=0)
unclosed_bugs_teams=unclosed_bugs_teams.reset_index()
unclosed_bugs_teams=unclosed_bugs_teams.head(10)
unclosed_bugs_teams=unclosed_bugs_teams.sort_values(by="unclosed_bugs_share", ascending=True)
unclosed_bugs_teams["unclosed_bugs_share"]=unclosed_bugs_teams["unclosed_bugs_share"].round(3)
unclosed_bugs_teams["unclosed_bugs_share"]=unclosed_bugs_teams["unclosed_bugs_share"]*100
print(unclosed_bugs_teams.head(2))

unclosed_tasks_microservices=pd.read_excel("VkusVill_analysis_results.xlsx", sheet_name="unclosed_tasks_microservices", index_col=0)
unclosed_tasks_microservices=unclosed_tasks_microservices.reset_index()
unclosed_tasks_microservices=unclosed_tasks_microservices.head(10)
unclosed_tasks_microservices=unclosed_tasks_microservices.sort_values(by="bugs_number", ascending=True)

def CreatePage():
    
    st.title("Статистика по незакрытым задачам, у которых прошёл дедлайн")

    st.markdown("""---""")

    box_1, box_2 = st.columns(2)

    box_1.metric("Процент незакрытых задач", "5.6%")
    box_2.metric("Общее количество незакрытых задач", "100")

    style_metric_cards(border_left_color="#039BE5", box_shadow=False)

    fig_unclosed_bugs_teams = px.bar(
            unclosed_bugs_teams,
            x="unclosed_bugs_share",
            y="team",
            orientation="h",
            color_discrete_sequence=["#039BE5"] * len(unclosed_bugs_teams),
            template="plotly_white",
            labels={'unclosed_bugs_share': 'Процент незакрытых задач', 'team':'Команда'},
            width=900, height=600
        )

    fig_unclosed_bugs_teams.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=True, ticksuffix="%")),
            title={
            'text': "<b>Топ-10 команд, участвовавших в незакрытых задачах</b>",
            'font': dict(size=20),
            'y':0.96,
            'x':0.61,
            'xanchor': 'center',
            'yanchor': 'top'} 
        )

    st.plotly_chart(fig_unclosed_bugs_teams)

    fig_unclosed_tasks_microservices = px.bar(
            unclosed_tasks_microservices,
            x="bugs_number",
            y="microservice",
            orientation="h",
            color_discrete_sequence=["#039BE5"] * len(unclosed_tasks_microservices),
            template="plotly_white",
            labels={'bugs_number': 'Количество незакрытых задач', 'microservice':'Микросервис'},
            width=900, height=600
        )

    fig_unclosed_tasks_microservices.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=True)),
            title={
            'text': "<b>Топ-10 микросервисов с наибольшим количеством незакрытых задач</b>",
            'font': dict(size=20),
            'y':0.96,
            'x':0.57,
            'xanchor': 'center',
            'yanchor': 'top'} 
        )

    st.plotly_chart(fig_unclosed_tasks_microservices)

    return True
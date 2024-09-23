import streamlit as st
import plotly.express as px
import pandas as pd

closed_tasks_teams=pd.read_excel("VkusVill_analysis_results.xlsx", sheet_name="closed_tasks_teams", index_col=0)
closed_tasks_teams=closed_tasks_teams.reset_index()
closed_tasks_teams["closed_tasks_share"]=closed_tasks_teams["closed_tasks_share"].round(3)
closed_tasks_teams["closed_tasks_share"]=closed_tasks_teams["closed_tasks_share"]*100
closed_tasks_teams=closed_tasks_teams[closed_tasks_teams["total_tasks"]>2]
top_10_teams=closed_tasks_teams.tail(10)
bottom_10_teams=closed_tasks_teams.head(10)
top_10_teams=top_10_teams.sort_values(by="closed_tasks_share", ascending=True)
bottom_10_teams=bottom_10_teams.sort_values(by="closed_tasks_share", ascending=False)

def CreatePage():
    
    st.title("Статистика по закрытию задач")

    st.markdown("""---""")

    fig_top_10_teams = px.bar(
            top_10_teams,
            x="closed_tasks_share",
            y="team",
            orientation="h",
            color_discrete_sequence=["#039BE5"] * len(top_10_teams),
            template="plotly_white",
            labels={'closed_tasks_share': 'Процент задач со статусом "Закрыто"', 'team':'Команда'},
            width=900, height=600
        )

    fig_top_10_teams.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(b=100),
            xaxis=(dict(showgrid=True, ticksuffix="%")),
            title={
            'text': '<b>Топ-10 команд с наибольшим процентом задач со статусом "Закрыто" *</b>',
            'font': dict(size=20),
            'y':0.96,
            'x':0.61,
            'xanchor': 'center',
            'yanchor': 'top'} 
        )

    fig_top_10_teams.add_annotation(dict(font=dict(size=12),
                                        x=0,
                                        y=-0.17,
                                        showarrow=False,
                                        text="*В статистику включены только те команды, у которых было 3 и более задачи",
                                        textangle=0,
                                        xanchor='left',
                                        yanchor='bottom',
                                        xref="paper",
                                        yref="paper"))

    st.plotly_chart(fig_top_10_teams)

    fig_bottom_10_teams = px.bar(
            bottom_10_teams,
            x="closed_tasks_share",
            y="team",
            orientation="h",
            color_discrete_sequence=["#039BE5"] * len(bottom_10_teams),
            template="plotly_white",
            labels={'closed_tasks_share': 'Процент задач со статусом "Закрыто"', 'team':'Команда'},
            width=900, height=600
        )

    fig_bottom_10_teams.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(b=100),
            xaxis=(dict(showgrid=True, ticksuffix="%")),
            title={
            'text': '<b>Топ-10 команд с наименьшим процентом задач со статусом "Закрыто" *</b>',
            'font': dict(size=20),
            'y':0.96,
            'x':0.6,
            'xanchor': 'center',
            'yanchor': 'top'} 
        )

    fig_bottom_10_teams.add_annotation(dict(font=dict(size=12),
                                        x=0,
                                        y=-0.17,
                                        showarrow=False,
                                        text="*В статистику включены только те команды, у которых было 3 и более задачи",
                                        textangle=0,
                                        xanchor='left',
                                        yanchor='bottom',
                                        xref="paper",
                                        yref="paper"))

    st.plotly_chart(fig_bottom_10_teams)

    return True
import streamlit as st
import plotly.express as px
import pandas as pd

total_bugs_monthly=pd.read_excel("VkusVill_analysis_results.xlsx", sheet_name="total_bugs_monthly", index_col=0)
total_bugs_monthly=total_bugs_monthly.reset_index().sort_values(by="month", ascending=False)
months=["Июнь*", "Май", "Апрель", "Март", "Февраль", "Январь"]
total_bugs_monthly["month_name"]=months

total_bugs_microservices=pd.read_excel("VkusVill_analysis_results.xlsx", sheet_name="total_bugs_microservices", index_col=0)
total_bugs_microservices=total_bugs_microservices.reset_index()
total_bugs_microservices=total_bugs_microservices.head(10)
total_bugs_microservices=total_bugs_microservices.sort_values(by="bugs_number", ascending=True)

stage_time=pd.read_excel("VkusVill_analysis_results.xlsx", sheet_name="stage_time", index_col=0)
stage_time=stage_time.reset_index()
stage_time=stage_time.sort_values(by="time_diff", ascending=False)
stage_time["time_diff"]=stage_time["time_diff"].round(1)

def CreatePage():
    
    st.title("Общая статистика")

    st.markdown("""---""")

    fig_total_bugs_monthly = px.bar(
            total_bugs_monthly,
            x="bugs_number",
            y="month_name",
            orientation="h",
            color_discrete_sequence=["#039BE5"] * len(total_bugs_monthly),
            template="plotly_white",
            labels={'bugs_number': 'Количество багов', 'month_name':'Месяц'},
            width=700, height=500
        )
    
    fig_total_bugs_monthly.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=True)),
            title={
            'text': "<b>Количество багов в месяц</b>",
            'font': dict(size=20),
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}
        )
    
    fig_total_bugs_monthly.add_annotation(dict(font=dict(size=14),
                                        x=0,
                                        y=-0.3,
                                        showarrow=False,
                                        text="*29 и 30 июня отсутствуют в статистике по июню",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

    fig_total_bugs_microservices = px.bar(
            total_bugs_microservices,
            x="bugs_number",
            y="microservice",
            orientation="h",
            color_discrete_sequence=["#039BE5"] * len(total_bugs_microservices),
            template="plotly_white",
            labels={'bugs_number': 'Количество багов', 'microservice':'Микросервис'},
            width=800, height=600
        )

    fig_total_bugs_microservices.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=True)),
            title={
            'text': "<b>Топ-10 микросервисов по количеству багов</b>",
            'font': dict(size=20),
            'y':0.96,
            'x':0.57,
            'xanchor': 'center',
            'yanchor': 'top'}
        )

    fig_stage_time = px.bar(
            stage_time,
            x="stage",
            y="time_diff",
            orientation="v",
            color_discrete_sequence=["#039BE5"] * len(stage_time),
            template="plotly_white",
            labels={'time_diff': 'Среднее количество часов', 'stage':'Стадия решения бага'},
            width=850, height=600
        )

    fig_stage_time.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)),
            title={
            'text': "<b>Средняя длительность каждой стадии решения бага</b>",
            'font': dict(size=20),
            'y':0.945,
            'x':0.53,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis_tickangle=90
        )


    st.plotly_chart(fig_total_bugs_monthly)
    st.plotly_chart(fig_total_bugs_microservices)
    st.plotly_chart(fig_stage_time)

    return True
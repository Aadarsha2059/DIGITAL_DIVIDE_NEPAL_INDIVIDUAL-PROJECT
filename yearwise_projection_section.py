    # elif analysis_type == "Yearwise Projection":
    #     st.markdown('<h2 class="sub-header">📅 Yearwise Projection Analysis (2001-2021)</h2>', unsafe_allow_html=True)
        
    #     st.markdown("""
    #     <div class="budget-card">
    #         <h3>📊 Historical Trends & Metric Analysis</h3>
    #         <p>Analyze metric trends from 2001 to 2021 across all districts. Add or remove metrics dynamically to update charts. 
    #         District rankings are consistent with Budget Allocation for uniformity.</p>
    #     </div>
    #     """, unsafe_allow_html=True)
        
    #     # Get all districts and calculate their priority scores for consistent ranking
    #     all_districts = sorted(df_combined['District'].unique())
        
    #     # Calculate priority scores to maintain same ranking as Budget Allocation
    #     improvement_areas = ["Internet Access", "Electricity Access", "Digital Literacy", "Telecommunications", "Media Access"]
    #     priority_scores, _, _ = calculate_advanced_budget_allocation(
    #         df_combined, 1000000, "Balanced Development", improvement_areas, all_districts
    #     )
        
    #     # Create district ranking based on priority scores (same as Budget Allocation)
    #     if priority_scores:
    #         ranked_districts = [item['District'] for item in priority_scores]
    #     else:
    #         ranked_districts = all_districts
        
    #     # Metric selection
    #     st.markdown("### 🎯 Select Metrics to Analyze")
        
    #     col1, col2 = st.columns([3, 1])
        
    #     with col1:
    #         available_metrics = {
    #             'Internet_Access_Rate': '🌐 Internet Access Rate',
    #             'Electricity_Access_Rate': '⚡ Electricity Access Rate',
    #             'Telephone_Access_Rate': '📞 Telephone Access Rate',
    #             'TV_Access_Rate': '📺 TV Access Rate',
    #             'Radio_Access_Rate': '📻 Radio Access Rate',
    #             'Literacy_Rate_Total': '📚 Literacy Rate'
    #         }
            
    #         selected_metrics = st.multiselect(
    #             "Choose metrics to display (add or remove to update charts):",
    #             list(available_metrics.keys()),
    #             default=['Internet_Access_Rate', 'Electricity_Access_Rate', 'Literacy_Rate_Total'],
    #             format_func=lambda x: available_metrics[x],
    #             help="Select one or more metrics. Charts will update automatically."
    #         )
        
    #     with col2:
    #         show_all_districts = st.checkbox(
    #             "Show All Districts",
    #             value=False,
    #             help="Show all districts or top 6 by priority"
    #         )
            
    #         if not show_all_districts:
    #             num_districts = st.slider(
    #                 "Number of Districts:",
    #                 min_value=3,
    #                 max_value=len(ranked_districts),
    #                 value=min(6, len(ranked_districts)),
    #                 help="Select how many top-priority districts to display"
    #             )
    #         else:
    #             num_districts = len(ranked_districts)
        
    #     if selected_metrics:
    #         # Select districts to display (maintaining priority ranking)
    #         display_districts = ranked_districts[:num_districts]
            
    #         st.markdown(f"### 📊 Yearwise Trends for Top {num_districts} Districts (by Priority Ranking)")
    #         st.info(f"📌 Showing districts ranked by priority (same as Budget Allocation): {', '.join(display_districts)}")
            
    #         # Create interactive line chart for each metric
    #         for metric in selected_metrics:
    #             st.markdown(f"#### {available_metrics[metric]}")
                
    #             # Prepare data for the metric
    #             metric_data = []
    #             for district in display_districts:
    #                 district_data = df_combined[df_combined['District'] == district]
    #                 yearly_data = district_data.groupby('Year')[metric].mean().reset_index()
    #                 yearly_data['District'] = district
    #                 metric_data.append(yearly_data)
                
    #             if metric_data:
    #                 combined_metric_data = pd.concat(metric_data, ignore_index=True)
                    
    #                 # Create line chart
    #                 fig = px.line(
    #                     combined_metric_data,
    #                     x='Year',
    #                     y=metric,
    #                     color='District',
    #                     markers=True,
    #                     title=f"{available_metrics[metric]} Trends (2001-2021)",
    #                     labels={metric: 'Percentage (%)', 'Year': 'Census Year'},
    #                     color_discrete_sequence=px.colors.qualitative.Set2
    #                 )
                    
    #                 fig.update_traces(
    #                     mode='lines+markers',
    #                     line=dict(width=3),
    #                     marker=dict(size=10)
    #                 )
                    
    #                 fig.update_layout(
    #                     hovermode='x unified',
    #                     template='plotly_white',
    #                     height=500,
    #                     xaxis=dict(
    #                         tickmode='array',
    #                         tickvals=[2001, 2011, 2021],
    #                         ticktext=['2001', '2011', '2021']
    #                     ),
    #                     yaxis=dict(range=[0, 105]),
    #                     legend=dict(
    #                         orientation="v",
    #                         yanchor="top",
    #                         y=1,
    #                         xanchor="left",
    #                         x=1.02
    #                     )
    #                 )
                    
    #                 st.plotly_chart(fig, use_container_width=True)
                    
    #                 # Calculate and display highest and lowest values
    #                 col1, col2 = st.columns(2)
                    
    #                 with col1:
    #                     # Highest value across all years and districts
    #                     max_row = combined_metric_data.loc[combined_metric_data[metric].idxmax()]
    #                     st.markdown(f"""
    #                     <div class="priority-low">
    #                         <strong>🏆 Highest Value:</strong><br>
    #                         <strong>{max_row['District']}</strong> in <strong>{int(max_row['Year'])}</strong><br>
    #                         <span style="font-size: 1.5rem; font-weight: bold;">{max_row[metric]:.1f}%</span>
    #                     </div>
    #                     """, unsafe_allow_html=True)
                    
    #                 with col2:
    #                     # Lowest value across all years and districts
    #                     min_row = combined_metric_data.loc[combined_metric_data[metric].idxmin()]
    #                     st.markdown(f"""
    #                     <div class="priority-high">
    #                         <strong>⚠️ Lowest Value:</strong><br>
    #                         <strong>{min_row['District']}</strong> in <strong>{int(min_row['Year'])}</strong><br>
    #                         <span style="font-size: 1.5rem; font-weight: bold;">{min_row[metric]:.1f}%</span>
    #                     </div>
    #                     """, unsafe_allow_html=True)
                    
    #                 st.markdown("---")
            
    #         # Summary Statistics Table
    #         st.markdown("### 📋 Summary Statistics by District")
            
    #         summary_data = []
    #         for district in display_districts:
    #             district_info = {'District': district}
                
    #             # Get district rank
    #             district_rank = ranked_districts.index(district) + 1
    #             district_info['Priority Rank'] = f"#{district_rank}"
                
    #             for metric in selected_metrics:
    #                 district_data = df_combined[df_combined['District'] == district]
                    
    #                 # Get values for each year
    #                 val_2001 = district_data[district_data['Year'] == 2001][metric].mean()
    #                 val_2011 = district_data[district_data['Year'] == 2011][metric].mean()
    #                 val_2021 = district_data[district_data['Year'] == 2021][metric].mean()
                    
    #                 # Calculate growth
    #                 growth_2001_2021 = val_2021 - val_2001 if not pd.isna(val_2001) and not pd.isna(val_2021) else 0
                    
    #                 metric_short = metric.replace('_Access_Rate', '').replace('_Total', '').replace('_', ' ')
    #                 district_info[f'{metric_short} 2001'] = f"{val_2001:.1f}%" if not pd.isna(val_2001) else "N/A"
    #                 district_info[f'{metric_short} 2011'] = f"{val_2011:.1f}%" if not pd.isna(val_2011) else "N/A"
    #                 district_info[f'{metric_short} 2021'] = f"{val_2021:.1f}%" if not pd.isna(val_2021) else "N/A"
    #                 district_info[f'{metric_short} Growth'] = f"{growth_2001_2021:+.1f}%" if growth_2001_2021 != 0 else "N/A"
                
    #             summary_data.append(district_info)
            
    #         summary_df = pd.DataFrame(summary_data)
    #         st.dataframe(summary_df, use_container_width=True, height=400)
            
    #         # Download option
    #         st.markdown("### 📥 Download Analysis Data")
    #         col1, col2 = st.columns(2)
            
    #         with col1:
    #             csv = summary_df.to_csv(index=False)
    #             st.download_button(
    #                 label="📥 Download Summary as CSV",
    #                 data=csv,
    #                 file_name=f"yearwise_analysis_{datetime.now().strftime('%Y%m%d')}.csv",
    #                 mime="text/csv"
    #             )
            
    #         with col2:
    #             # Prepare detailed data for download
    #             detailed_data = []
    #             for district in display_districts:
    #                 for year in [2001, 2011, 2021]:
    #                     district_year_data = df_combined[
    #                         (df_combined['District'] == district) & 
    #                         (df_combined['Year'] == year)
    #                     ]
    #                     if not district_year_data.empty:
    #                         row = {'District': district, 'Year': year}
    #                         for metric in selected_metrics:
    #                             row[metric] = district_year_data[metric].mean()
    #                         detailed_data.append(row)
                
    #             detailed_df = pd.DataFrame(detailed_data)
    #             csv_detailed = detailed_df.to_csv(index=False)
    #             st.download_button(
    #                 label="📥 Download Detailed Data as CSV",
    #                 data=csv_detailed,
    #                 file_name=f"yearwise_detailed_{datetime.now().strftime('%Y%m%d')}.csv",
    #                 mime="text/csv"
    #             )
            
    #         # Comparative Growth Analysis
    #         st.markdown("### 📊 Comparative Growth Analysis")
            
    #         # Calculate average growth rates
    #         growth_data = []
    #         for district in display_districts:
    #             district_data = df_combined[df_combined['District'] == district]
    #             district_growth = {'District': district}
                
    #             for metric in selected_metrics:
    #                 val_2001 = district_data[district_data['Year'] == 2001][metric].mean()
    #                 val_2021 = district_data[district_data['Year'] == 2021][metric].mean()
                    
    #                 if not pd.isna(val_2001) and not pd.isna(val_2021) and val_2001 > 0:
    #                     growth_rate = ((val_2021 - val_2001) / val_2001) * 100
    #                     district_growth[metric] = growth_rate
    #                 else:
    #                     district_growth[metric] = 0
                
    #             growth_data.append(district_growth)
            
    #         growth_df = pd.DataFrame(growth_data)
            
    #         # Create bar chart for growth rates
    #         if len(selected_metrics) > 0:
    #             fig_growth = go.Figure()
                
    #             colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
                
    #             for i, metric in enumerate(selected_metrics):
    #                 fig_growth.add_trace(go.Bar(
    #                     name=available_metrics[metric],
    #                     x=growth_df['District'],
    #                     y=growth_df[metric],
    #                     marker_color=colors[i % len(colors)],
    #                     text=growth_df[metric].round(1),
    #                     textposition='auto',
    #                 ))
                
    #             fig_growth.update_layout(
    #                 title="Growth Rate Comparison (2001-2021)",
    #                 xaxis_title="District",
    #                 yaxis_title="Growth Rate (%)",
    #                 barmode='group',
    #                 template='plotly_white',
    #                 height=500,
    #                 legend=dict(
    #                     orientation="h",
    #                     yanchor="bottom",
    #                     y=1.02,
    #                     xanchor="right",
    #                     x=1
    #                 )
    #             )
                
    #             st.plotly_chart(fig_growth, use_container_width=True)
        
    #     else:
    #         st.warning("⚠️ Please select at least one metric to display the analysis.")
    
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime


def show_yearwise_projection(df_combined, analysis_type, calculate_advanced_budget_allocation):
    """
    Streamlit section for Year-wise Projection Analysis.
    Call this function inside your main app where the other tabs/sections are.
    """
    if analysis_type != "Yearwise Projection":
        return

    st.markdown('<h2 class="sub-header">Yearwise Projection Analysis (2001-2021)</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="budget-card">
        <h3>Historical Trends & Metric Analysis</h3>
        <p>Analyze metric trends from 2001 to 2021 across all districts. Add or remove metrics dynamically to update charts. 
        District rankings are consistent with Budget Allocation for uniformity.</p>
    </div>
    """, unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # 1. Consistent district ranking (same as Budget Allocation section)
    # ------------------------------------------------------------------
    all_districts = sorted(df_combined['District'].unique())

    improvement_areas = ["Internet Access", "Electricity Access", "Digital Literacy",
                         "Telecommunications", "Media Access"]

    priority_scores, _, _ = calculate_advanced_budget_allocation(
        df_combined, 1_000_000, "Balanced Development", improvement_areas, all_districts
    )

    ranked_districts = [item['District'] for item in priority_scores] if priority_scores else all_districts

    # ------------------------------------------------------------------
    # 2. Metric & district selection
    # ------------------------------------------------------------------
    st.markdown("### Select Metrics to Analyze")

    col1, col2 = st.columns([3, 1])

    available_metrics = {
        'Internet_Access_Rate': 'Internet Access Rate',
        'Electricity_Access_Rate': 'Electricity Access Rate',
        'Telephone_Access_Rate': 'Telephone Access Rate',
        'TV_Access_Rate': 'TV Access Rate',
        'Radio_Access_Rate': 'Radio Access Rate',
        'Literacy_Rate_Total': 'Literacy Rate'
    }

    with col1:
        selected_metrics = st.multiselect(
            "Choose metrics to display (add/remove to update charts):",
            options=list(available_metrics.keys()),
            default=['Internet_Access_Rate', 'Electricity_Access_Rate', 'Literacy_Rate_Total'],
            format_func=lambda x: available_metrics[x],
            help="Select one or more metrics. Charts will update automatically."
        )

    with col2:
        show_all = st.checkbox("Show All Districts", value=False,
                               help="Uncheck to limit to top-priority districts")

        if show_all:
            num_districts = len(ranked_districts)
        else:
            num_districts = st.slider(
                "Number of top-priority districts",
                min_value=3,
                max_value=len(ranked_districts),
                value=min(6, len(ranked_districts))
            )

    if not selected_metrics:
        st.warning("Please select at least one metric.")
        st.stop()

    display_districts = ranked_districts[:num_districts]

    st.markdown(f"### Year-wise Trends – Top {num_districts} Priority Districts")
    st.info(f"District order follows Budget Allocation priority: {', '.join(display_districts)}")

    # ------------------------------------------------------------------
    # 3. Line charts for each selected metric
    # ------------------------------------------------------------------
    for metric in selected_metrics:
        st.markdown(f"#### {available_metrics[metric]}")

        data_parts = []
        for district in display_districts:
            subset = df_combined[df_combined['District'] == district]
            yearly = subset.groupby('Year')[metric].mean().reset_index()
            yearly['District'] = district
            data_parts.append(yearly)

        chart_df = pd.concat(data_parts, ignore_index=True)

        fig = px.line(
            chart_df,
            x='Year',
            y=metric,
            color='District',
            markers=True,
            title=f"{available_metrics[metric]} Trends (2001-2021)",
            labels={metric: "Percentage (%)", "Year": "Census Year"},
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_traces(mode='lines+markers', line=dict(width=3), marker=dict(size=10))
        fig.update_layout(
            hovermode='x unified',
            template='plotly_white',
            height=520,
            xaxis=dict(tickmode='array', tickvals=[2001, 2011, 2021],
                       ticktext=['2001', '2011', '2021']),
            yaxis=dict(range=[0, 105]),
            legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02)
        )
        st.plotly_chart(fig, use_container_width=True)

        # Highest & lowest highlights
        col_a, col_b = st.columns(2)
        max_row = chart_df.loc[chart_df[metric].idxmax()]
        min_row = chart_df.loc[chart_df[metric].idxmin()]

        with col_a:
            st.markdown(f"""
            <div class="priority-low">
                <strong>Highest:</strong><br>
                <strong>{max_row['District']}</strong> ({int(max_row['Year'])})<br>
                <span style="font-size:1.5rem;font-weight:bold;">{max_row[metric]:.1f}%</span>
            </div>
            """, unsafe_allow_html=True)

        with col_b:
            st.markdown(f"""
            <div class="priority-high">
                <strong>Lowest:</strong><br>
                <strong>{min_row['District']}</strong> ({int(min_row['Year'])})<br>
                <span style="font-size:1.5rem;font-weight:bold;">{min_row[metric]:.1f}%</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

    # ------------------------------------------------------------------
    # 4. Summary table
    # ------------------------------------------------------------------
    st.markdown("### Summary Statistics by District")

    summary_rows = []
    for district in display_districts:
        row = {
            "District": district,
            "Priority Rank": f"#{ranked_districts.index(district) + 1}"
        }
        sub = df_combined[df_combined['District'] == district]

        for metric in selected_metrics:
            v2001 = sub[sub['Year'] == 2001][metric].mean()
            v2011 = sub[sub['Year'] == 2011][metric].mean()
            v2021 = sub[sub['Year'] == 2021][metric].mean()
            growth = (v2021 - v2001) if pd.notna(v2001) and pd.notna(v2021) else None

            name = metric.replace("_Access_Rate", "").replace("_Rate_Total", "").replace("_", " ")
            row[f"{name} 2001"] = f"{v2001:.1f}%" if pd.notna(v2001) else "N/A"
            row[f"{name} 2011"] = f"{v2011:.1f}%" if pd.notna(v2011) else "N/A"
            row[f"{name} 2021"] = f"{v2021:.1f}%" if pd.notna(v2021) else "N/A"
            row[f"{name} Growth"] = f"{growth:+.1f}%" if growth is not None and growth != 0 else "N/A"

        summary_rows.append(row)

    summary_df = pd.DataFrame(summary_rows)
    st.dataframe(summary_df, use_container_width=True, height=400)

    # ------------------------------------------------------------------
    # 5. Download buttons
    # ------------------------------------------------------------------
    st.markdown("### Download Analysis Data")
    d1, d2 = st.columns(2)

    with d1:
        st.download_button(
            "Download Summary Table (CSV)",
            data=summary_df.to_csv(index=False).encode(),
            file_name=f"yearwise_summary_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

    with d2:
        detailed_rows = []
        for district in display_districts:
            for year in [2001, 2011, 2021]:
                rec = df_combined[(df_combined['District'] == district) & (df_combined['Year'] == year)]
                if not rec.empty:
                    r = {"District": district, "Year": year}
                    r.update({m: rec[m].mean() for m in selected_metrics})
                    detailed_rows.append(r)
        detailed_df = pd.DataFrame(detailed_rows)
        st.download_button(
            "Download Detailed Data (CSV)",
            data=detailed_df.to_csv(index=False).encode(),
            file_name=f"yearwise_detailed_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

    # ------------------------------------------------------------------
    # 6. Growth comparison bar chart
    # ------------------------------------------------------------------
    st.markdown("### Growth Rate Comparison (2001-2021)")

    growth_rows = []
    for district in display_districts:
        row = {"District": district}
        sub = df_combined[df_combined['District'] == district]
        for metric in selected_metrics:
            v1 = sub[sub['Year'] == 2001][metric].mean()
            v2 = sub[sub['Year'] == 2021][metric].mean()
            if pd.notna(v1) and pd.notna(v2) and v1 > 0:
                row[metric] = ((v2 - v1) / v1) * 100
            else:
                row[metric] = 0
        growth_rows.append(row)

    growth_df = pd.DataFrame(growth_rows)

     # only show if we have data
    if not growth_df.empty:
        fig = go.Figure()
        colors = px.colors.qualitative.Plotly

        for i, metric in enumerate(selected_metrics):
            fig.add_trace(go.Bar(
                name=available_metrics[metric],
                x=growth_df['District'],
                y=growth_df[metric],
                marker_color=colors[i % len(colors)],
                text=growth_df[metric].round(1).astype(str) + "%",
                textposition="auto"
            ))

        fig.update_layout(
            title="Growth Rate Comparison (2001-2021)",
            xaxis_title="District",
            yaxis_title="Growth Rate (%)",
            barmode="group",
            template="plotly_white",
            height=550,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------------------
# How to use this file in your main app:
# ----------------------------------------------------------------------
# In your main Streamlit script (e.g. app.py) just do:
#
# from yearwise_projection_section import show_yearwise_projection
#
# # ... inside your tab or wherever you choose the analysis type:
# show_yearwise_projection(df_combined, analysis_type, calculate_advanced_budget_allocation)
#
# ----------------------------------------------------------------------
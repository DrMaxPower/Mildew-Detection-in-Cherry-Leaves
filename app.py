import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics


app = MultiPage(app_name="Farmy & Foods")  

app.add_page("box1: Quick Project Summary", page_summary_body)
app.add_page("box2: Leaves Visualizer", page_leaves_visualizer_body)
app.add_page("box3: Mildew Detection", page_mildew_detector_body)
app.add_page("box4: Project Hypothesis", page_project_hypothesis_body)
app.add_page("box5: ML Performance Metrics", page_ml_performance_metrics)




app.run()
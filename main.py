from helpers.analyzer import FrameAnalizer
from aquarel import load_theme

theme = load_theme("boxy_dark")
theme.apply()
dataset_name = 'GRAPE_QUALITY'
additional_pivot_operation = ['sum']
grape_analizer = FrameAnalizer(dataset_name)
# # Q1
grape_analizer.displayRegionSummary()
#
# # Q2
grape_analizer.highAttributeGrape()

# # Q3
grape_analizer.displayVarietySummery()

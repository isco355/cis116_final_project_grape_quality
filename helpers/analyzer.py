import pandas as pd
import helpers.bars as barCharts
import helpers.radar as radarChart
import helpers.table as TableCharts
import helpers.scatter as ScatterCharts


class FrameAnalizer:
    def __init__(self, dataset_name):
        self.datasets_path = './datasets'
        self.dataset_name = f'{dataset_name}.csv'
        self.data_frame = pd.DataFrame()

        self.categories_order = ['Premium', 'High', 'Medium', 'Low']

        self.grape_attributes = ["sugar_content_brix",
                                 "acidity_ph",  "berry_size_mm"]
        self.grow_factor = ['soil_moisture_percent',
                            'rainfall_mm', 'sun_exposure_hours']
        self.loadDataset()

    def loadDataset(self):
        file_path = f'{self.datasets_path}/{self.dataset_name}'
        self.data_frame = pd.read_csv(file_path)
        self.size = self.data_frame.shape[0]

    def pivot(self, index, columns, agg_functions=['size']):
        pivot_table = self.data_frame.pivot_table(
            index=index, values=columns, aggfunc=agg_functions)

        pivot_table.columns = pivot_table.columns.droplevel(level=0)
        return pivot_table

    def displayRegionSummary(self):
        # dataframe bar setup
        pivot_table = self.data_frame.pivot_table(
            index='region',  columns='quality_category', aggfunc=['size'], fill_value=0)
        pivot_table.columns = pivot_table.columns.droplevel(level=0)
        # dataframe groupbar setup
        pivot_table = pivot_table.loc[:, self.categories_order]
        pivot_table = pivot_table.sort_values(
            by=self.categories_order[1:3], ascending=[False, False])

        TableCharts.displayTable(pivot_table, 'region')
        barCharts.groupBar(pivot_table)
        barCharts.displayBar(self.data_frame, self.categories_order)

    def factorGraph(self, radar_points, radar_name):
        pivot_table = self.pivot(
            'quality_category', radar_points, ['mean']).round(2)

        pivot_table = pivot_table.loc[self.categories_order, :]

        TableCharts.displayTable(pivot_table, f'table_{radar_name}')
        radarChart.radarChart(pivot_table, f'radar_{radar_name}')
        ScatterCharts.multipleScatter(
            radar_points, self.data_frame, 'quality_category', radar_name, self.categories_order)

    def highAttributeGrape(self):
        self.factorGraph(self.grape_attributes, 'grape_attributes')

    def displayVarietySummery(self):
        self.factorGraph(self.grow_factor, 'grow_factor')

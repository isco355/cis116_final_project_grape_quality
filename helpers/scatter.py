import matplotlib.pyplot as plt
import helpers.plt as pltHelper

from matplotlib.ticker import MaxNLocator


def displaScatter(ax, data_frame, y_attribute, sub_dots, category_order):

    x_attribute = 'harvest_date'
    colors = pltHelper.colorRange()
    data_frame = data_frame.sort_values(by=x_attribute)

    for index, category in enumerate(category_order):
        category_mask = data_frame['quality_category'] == category
        df = data_frame.loc[category_mask, :]
        y = df[y_attribute]
        x = df[x_attribute]
        color = colors[index]

        ax.scatter(x, y,  label=category,
                   alpha=1, edgecolors='none',
                   color=color)
        ax.tick_params(labelrotation=45)

    ax.xaxis.set_major_locator(MaxNLocator(nbins=20))
    ax.set_ylabel(y_attribute)
    ax.set_xlabel(x_attribute)

    ax.legend()


def multipleScatter(attributes, data_frame, sub_dots, file_name, category_order):
    pltHelper.default_setup(plt)
    fig,  axs = plt.subplots(len(attributes))
    fig.set_figheight(25)
    fig.set_figwidth(30)
    for index, ax in enumerate(axs):
        y_name = attributes[index]
        displaScatter(ax, data_frame, y_name, sub_dots, category_order)
    # plt.show()
    pltHelper.saveChart(plt, f'scatter_{file_name}')

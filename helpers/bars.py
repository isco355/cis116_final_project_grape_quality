
import matplotlib.pyplot as plt
import helpers.plt as pltHelper


def displayBar(data_frame, x):

    plt.figure(figsize=(10, 10))
    pltHelper.default_setup(plt)
    variety_counts = data_frame['quality_category'].value_counts(
    ).reset_index()
    variety_counts.set_index('quality_category', inplace=True)

    variety_counts = variety_counts.loc[x, :]
    x = variety_counts.index
    y = variety_counts['count']
    plt.bar(x, y,  alpha=0.9, color=pltHelper.colorRange())
    for i, value in enumerate(y):
        plt.text(i, value + 1, str(value), ha='center')

    title = 'category_bars'
    plt.ylabel('count')
    pltHelper.saveChart(plt, title)


def groupBar(pivot_table):
    pltHelper.default_setup(plt)
    ax = pivot_table.plot(kind='bar', figsize=(14, 8),
                          color=pltHelper.colorRange(), label='')

    plt.tight_layout()

    for container in ax.containers:
        ax.bar_label(container)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.xticks(rotation=45)

    # plt.show()

    plt.ylabel('count')
    title = 'group_bar'
    # plt.title(title)
    pltHelper.saveChart(plt, title)

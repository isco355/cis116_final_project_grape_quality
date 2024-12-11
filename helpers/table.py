import matplotlib.pyplot as plt

import helpers.plt as pltHelper


def displayTable(df, title):
    # df.columns = df.columns.droplevel(level=0)

    fig, ax = plt.subplots()

    # fig, ax = plt.subplots(figsize=(8, 4))  # Set the figure size

    # Hide axes
    ax.axis('off')
    fig.set_figheight(10)
    fig.set_figwidth(18)

    # Create a table from the DataFrame
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        rowLabels=df.index,
        cellLoc='center',
        loc='center')

    # Customize the table
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 2)

    colors = ['#f2f2f2', '#ffffff']
    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        if key[0] == 0:
            cell.set_fontsize(16)
            cell.set_text_props(weight='bold')
            cell.set_facecolor('#4CAF50')
            cell.set_color('white')
        else:  # Data rows
            cell.set_facecolor(colors[i % 2])
        cell.set_edgecolor('#dddddd')
        cell.set_linewidth(1.5)

    for key in table.get_celld().keys():
        cell = table.get_celld()[key]
        if key[0] == 0:  # Header row
            cell.set_facecolor('#4CAF50')
            cell.set_edgecolor('#4CAF50')
            cell.set_linewidth(2.5)

    for cell in table.get_celld().values():
        cell.set_facecolor('none')
        cell.set_edgecolor('none')
        # cell.set_facecolor('#ffffff')
        cell.set_alpha(0.7)
        cell.set_linewidth(1.5)
        cell.set_edgecolor('#dddddd')
        title = pltHelper.title(title)
        plt.title(title, fontsize=18, weight='bold')

    # plt.show()
    pltHelper.saveChart(plt, f'table_{title}')
    # Show the plot

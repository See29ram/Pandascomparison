import numpy as np
from IPython.display import display, HTML
def highlight_diff(data, color='yellow'):
    attr = 'background-color: {}'.format(color)
    other = data.xs('First', axis='columns', level=-1)
    return pd.DataFrame(np.where(data.ne(other, level=0), attr, ''),
                        index=data.index, columns=data.columns)

caption_styles = {
    'selector':'caption',
    'props':[('font-weight', 'bold'),('margin-bottom','25px'),('font-size','25px')]
}
select_styles = {  # for row hover use <tr> instead of <td>
    'selector': '',
    'props': [('border-collapse', 'collapse'),('margin', '100px auto')]
}

table_styles = {  # for row hover use <tr> instead of <td>
    'selector': 'table',
    'props': [('border-collapse', 'collapse'),('margin', '100px auto')]
}

tbody_styles = {  # for row hover use <tr> instead of <td>
    'selector': 'tbody',
    'props': [('border', '1px solid #A2DBFA')]
}
td_styles = {  # for row hover use <tr> instead of <td>
    'selector': 'td',
    'props': [('border', '1px solid #A2DBFA'),('padding','1em'),('border-bottom','2px solid #A2DBFA')]
}
th_styles = {  # for row hover use <tr> instead of <td>
    'selector': 'th',
    'props': [('border', '1px solid #A2DBFA'),('padding','1em'),('background-color','#39A2DB'),('border-bottom','2px solid #A2DBFA')]
}

# df_out = df_final.style.set_table_styles(
#    [{"selector": "", "props": [("border-collapse", "collapse"),("border-radius","1em")]},
#     {"selector": "table", "props": [("border-collapse", "collapse"),("border-radius","1em")]},
#       {"selector": "tbody td", "props": [("border", "1px solid grey"),("border-radius","1em")]},
#      {"selector": "th", "props": [("border", "1px solid grey"),("border-radius","1em")]}
#     ]
# ).apply(highlight_diff, axis=None)

#df_out = df_final.style.set_table_styles([select_styles,table_styles, tbody_styles,td_styles, th_styles]).set_caption("Confusion matrix for multiple cancer prediction models.").apply(highlight_diff, axis=None)

df_out = df_final.style.set_table_styles([caption_styles,select_styles,table_styles, tbody_styles,td_styles, th_styles]).set_caption("Test Case 1").apply(highlight_diff, axis=None)

df_html =df_out.render()
file = open('C:\\Users\\c29ra\\Downloads\\check.html','w')
file.write(df_html)
file.close()

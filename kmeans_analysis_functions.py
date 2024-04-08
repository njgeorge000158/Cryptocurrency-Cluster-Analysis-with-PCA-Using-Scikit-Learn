#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  kmeans_analysis_functions.py
 #
 #  File Description:
 #      This Python script, kmeans_analysis_functions.py, contains generic 
 #      Python functions for conducting k-means cluster analysis.  Here is the list:
 #
 #      return_optimal_k_with_wcss_elbow
 #      return_optimal_k_with_calinski_harabasz
 #      return_optimal_k_with_silhouette
 #      return_optimal_k_with_davies_bouldin
 #
 #      return_subplot_trace_list
 #      return_height_width_rows_columns
 #      return_cluster_plots
 #      return_max_row_and_column
 #      
 #      return_cluster_predictions
 #      return_k_clusters_2d_scatter_plot
 #      return_k_clusters_3d_scatter_plot
 #      
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  11/21/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import log_subroutines

import hvplot.pandas
import math

import pandas as pd
import plotly.graph_objects as go

from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import calinski_harabasz_score 
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score 


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'kmeans_analysis_functions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  return_optimal_k_with_wcss_elbow
 #
 #  Function Description:
 #      This function returns an optimal k value using the WCSS Elbow Method.
 #
 #
 #  Return Type: integer, series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          normalized_dataframe
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_optimal_k_with_wcss_elbow(normalized_dataframe):
    
    try:
        
        k_integer_list = list(range(2, 11))
    
        inertia_float_list = []
    
        for k_value in k_integer_list:
    
            kmeans_model = KMeans(n_clusters = k_value, random_state = 21, n_init = 100)

            kmeans_model.fit(normalized_dataframe)

            inertia_float_list.append(kmeans_model.inertia_)
    

        inertia_series \
            = pd.Series \
                (inertia_float_list, index = k_integer_list, name = 'WCSS Elbow')

        
        inertia_index_integer_list = list(inertia_series.index)
        
        percent_variance_float_list = []

        
        for index in inertia_index_integer_list:
        
            percent_variance_float_list.append \
                (100 * \
                    (1 - (inertia_series[index] / inertia_series[inertia_index_integer_list[0]])))
    
    
        threshold_integer = len(percent_variance_float_list) + 1

        optimal_k_integer = 0

        
        for index in range(1, threshold_integer):
                
            if abs(percent_variance_float_list[index] - percent_variance_float_list[index - 1]) \
                < threshold_integer:
                
                optimal_k_integer = index + 1
                    
                break
                
                
        return optimal_k_integer, inertia_series
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_optimal_k_with_wcss_elbow, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return an optimal k value.')
    
        return None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  return_optimal_k_with_calinski_harabasz
 #
 #  Function Description:
 #      This function returns an optimal k value using the Calinski-Harabasz Method.
 #
 #
 #  Return Type: integer, series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataFrame
 #          normalized_dataframe
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_optimal_k_with_calinski_harabasz(normalized_dataframe):
    
    try:

        k_integer_list = list(range(2, 11))

        inertia_float_list = []

        
        for k_value in k_integer_list:

            kmeans_model = KMeans(n_clusters = k_value, random_state = 21, n_init = 100)

            kmeans_model.fit(normalized_dataframe)

            inertia_float_list.append \
                (calinski_harabasz_score(normalized_dataframe, kmeans_model.labels_))

        
        inertia_series \
            = pd.Series \
                (inertia_float_list, index = k_integer_list, name = 'Calinski Harabasz')

        optimal_k_integer = inertia_series.idxmax()

        
        return optimal_k_integer, inertia_series
    
    except:
        
        log_subroutines.print_and_log_text \
            (f'The function, return_optimal_k_with_calinski_harabasz, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return an optimal k value.')
    
        return None        


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_optimal_k_with_silhouette
 #
 #  Function Description:
 #      This function returns an optimal k values using the Silhouette Method.
 #
 #
 #  Return Type: integer, series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          normalized_dataframe
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_optimal_k_with_silhouette(normalized_dataframe):
    
    try:
        
        k_integer_list = list(range(2, 11))
    
        inertia_float_list = []

        
        for k_value in k_integer_list:
    
            kmeans_model = KMeans(n_clusters = k_value, random_state = 21, n_init = 100)

            kmeans_model.fit(normalized_dataframe)

            inertia_float_list.append \
                (silhouette_score(normalized_dataframe, kmeans_model.labels_))

        
        inertia_series \
            = pd.Series \
                (inertia_float_list, index = k_integer_list, name = 'Silhouette')


        point_float = inertia_series.max()
    
        optimal_k_integer = inertia_series.index[inertia_series == point_float][0]
    
            
        return optimal_k_integer, inertia_series
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_optimal_k_with_silhouette, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return an optimal k value.')
    
        return None 


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  return_optimal_k_with_davies_bouldin
 #
 #  Function Description:
 #      This function returns an optimal k values using the Davies-Bouldin Method.
 #
 #
 #  Return Type: integer, series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          normalized_dataframe
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_optimal_k_with_davies_bouldin(normalized_dataframe):
    
    try:
    
        k_integer_list = list(range(2, 11))
    
        inertia_float_list = []
        
    
        for k_value in k_integer_list:
    
            kmeans_model = KMeans(n_clusters = k_value, random_state = 21, n_init = 100)

            kmeans_model.fit(normalized_dataframe)

            inertia_float_list.append \
                (davies_bouldin_score(normalized_dataframe, kmeans_model.labels_))
        
        inertia_series \
            = pd.Series \
                (inertia_float_list, index = k_integer_list, name = 'Davies Bouldin')

        optimal_k_integer = inertia_series.idxmax()
    
            
        return optimal_k_integer, inertia_series
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_optimal_k_with_davies_bouldin, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return an optimal k value.')
    
        return None  


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  return_subplot_trace_list
 #
 #  Function Description:
 #      This function returns a subplot trace list for display.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list
 #          inertia_series_list
 #                          The parameter is a list of inertia series.
 #  list
 #          line_colors_string_list
 #                          The parameter is a list of colors for the lines.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_subplot_trace_list \
        (inertia_series_list,
         line_colors_string_list):
    
    try:
    
        subplots_trace_list = []
    
        for index, inertia_series in enumerate(inertia_series_list):
    
            line_trace \
                = go.Scatter \
                    (x = inertia_series.index, 
                     y = inertia_series,
                     line = {'color': \
                                line_colors_string_list[index % len(line_colors_string_list)]},
                     mode = 'lines')

            marker_trace \
                = go.Scatter \
                    (x = inertia_series.index, 
                     y = inertia_series,
                     hovertemplate \
                        = 'Number of K-Clusters: <b>%{x}</b><br>'
                            + 'Score: <b>%{y}</b><br>'
                            + '<extra></extra>',
                     marker \
                         = {'color': 'darkblue',
                            'size': 10},
                     mode = 'markers')
        
            plot_trace_list = [line_trace, marker_trace]
        
            subplots_trace_list.append(plot_trace_list)
        
        
        return subplots_trace_list
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_subplot_trace_list, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return a subplot trace list.')
    
        return None          


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  return_height_width_rows_columns
 #
 #  Function Description:
 #      This function returns the height, width, rows, and columns from a list of k-values
 #
 #
 #  Return Type: integer, integer, integer, integer
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list
 #          optimal_k_integer_list
 #                          The parameter is a list of optimal K values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_height_width_rows_columns(optimal_k_integer_list):
        
    try:

        list_length_integer = len(optimal_k_integer_list)

        
        if list_length_integer == 1:
            
            height_integer = 500
            
            width_integer = 500
            
            rows_integer = 1
            
            columns_integer = 1
            
        elif list_length_integer == 2:
            
            height_integer = 500
            
            width_integer = 1000
            
            rows_integer = 1
            
            columns_integer = 2
            
        elif list_length_integer == 3:
            
            height_integer = 500
            
            width_integer = 1500
            
            rows_integer = 1
            
            columns_integer = 3   
            
        elif list_length_integer == 4:
            
            height_integer = 1000
            
            width_integer = 1000
            
            rows_integer = 2
            
            columns_integer = 2 
        
        else:

            log_subroutines.print_and_log_text \
                ('The program sent a list to function, return_height_width_rows_columns, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'with a length outside accepted parameters (1-4): '
                 + f'{list_length_integer}')
            
            height_integer = 0
            
            width_integer = 0
            
            rows_integer = 0
            
            columns_integer = 0
            
        
        return height_integer, width_integer, rows_integer, columns_integer
            
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_height_width_rows_columns, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return height, width, rows, and columns.')
    
        return 0, 0, 0, 0          


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  return_cluster_plots
 #
 #  Function Description:
 #      This function returns a group of k-cluster line plots for display.
 #
 #
 #  Return Type: Plotly figure
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list
 #          optimal_k_integer_list
 #                          The parameter is a list of optimal K values.
 #  list
 #          inertia_series_list
 #                          The parameter is a list of inertia series.
 #  list
 #          line_colors_string_list
 #                          The parameter is a list of colors for the lines.
 #  string
 #          figure_title_string
 #                          The parameter is a figure title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_cluster_plots \
        (optimal_k_integer_list, 
         inertia_series_list, 
         line_colors_string_list,
         figure_title_string):
    
    try:
        
        height_integer, width_integer, rows_integer, columns_integer \
            = return_height_width_rows_columns(optimal_k_integer_list)
        
        if height_integer == 0:
            
            return None
        
        
        subplots_trace_list \
            = return_subplot_trace_list(inertia_series_list, line_colors_string_list)

        titles_string_list = [n.name for n in inertia_series_list]

        plotly_layout \
            = go.Layout \
                (height = height_integer, width = width_integer, title_text = figure_title_string)

        plotly_figure \
            = make_subplots \
                (rows = rows_integer, 
                 cols = columns_integer, 
                 horizontal_spacing = 0.12,
                 vertical_spacing = 0.12,
                 subplot_titles = titles_string_list)
    
    
        for index, subplots_trace in enumerate(subplots_trace_list):
               
            if index < 2:
                    
                row_integer = 1
                    
                column_integer = index + 1
                
            else:
                
                row_integer = 2
                
                column_integer = index - 1
                
        
            for trace in subplots_trace:
        
                plotly_figure.add_trace \
                    (trace, 
                     row = row_integer, 
                     col = column_integer)
            
                plotly_figure.update_annotations \
                    (font = {'color': 'black', 'family': 'garamond', 'size': 20.0},
                     yshift = 10.0)
            
                plotly_figure.update_xaxes \
                    (row = row_integer, 
                     col = column_integer,
                     tick0 = 1.0,
                     dtick = 1.0,
                     tickmode = 'linear',
                     linecolor = 'black',
                     linewidth = 2.0,
                     mirror = True,
                     showline = True,
                     tickfont = {'color': 'black', 'family': 'garamond', 'size': 14.0})
            
                plotly_figure.update_yaxes \
                    (row = row_integer, 
                     col = column_integer,
                     linecolor = 'black',
                     linewidth = 2.0, 
                     mirror = True, 
                     showline = True, 
                     tickfont = {'color': 'black', 'family': 'garamond', 'size': 14.0})
            
            if index > 1:
                
                plotly_figure.update_xaxes \
                    (row = row_integer, 
                     col = column_integer,
                     title = {'text': 'Number of K-Clusters',
                             'font': {'color': 'black', 
                                      'family': 'garamond',
                                      'size': 18.0}})                
            
            if index % 2 == 0:
            
                plotly_figure.update_yaxes \
                    (row = row_integer, 
                     col = column_integer,
                     title = {'text': 'Score',
                             'font': {'color': 'black', 
                                      'family': 'garamond',
                                      'size': 18.0}})
            
            plotly_figure.add_vline \
                (row = row_integer, 
                 col = column_integer,
                 x = optimal_k_integer_list[index],
                 line_color = 'black',
                 line_dash = 'dash',
                 line_width = 2.0)
            

        plotly_figure.update_layout \
            (plotly_layout,
             showlegend = False, 
             title = {'font': {'color': 'black', 
                               'family': 'garamond', 
                               'size': 24.0}}) 

        log_subroutines.save_plotly_image(plotly_figure, figure_title_string)
    
        return plotly_figure.show()
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_cluster_plots, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return cluster plots for display.')
    
        return None             


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  return_max_row_and_column
 #
 #  Function Description:
 #      This function returns the number of rows and columns for a plotly figure.
 #
 #
 #  Return Type: integer, integer
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list
 #          k_integer_list
 #                          The parameter is a list of optimal K values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_max_row_and_column(k_integer_list):
    
    try:

        list_length_integer = len(k_integer_list)
        
        if list_length_integer <= 3 \
            or list_length_integer == 5 \
            or list_length_integer == 7:
        
            return 1, list_length_integer
        
        elif list_length_integer == 4 \
                or list_length_integer == 9:

            sqrt_list_length_integer = int(math.sqrt(list_length_integer))
            
            return sqrt_list_length_integer, sqrt_list_length_integer
        
        elif list_length_integer == 6:
            
            return 2, 3
        
        elif list_length_integer == 8:
        
            return 2, 4
        
        else:

            log_subroutines.print_and_log_text \
                ('The program sent a list to function, return_max_row_and_column, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'with a length outside accepted parameters (1-9): '
                 + f'{list_length_integer}')
        
            return 0, 0
        
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_max_row_and_column, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return the maximum rows and columns.')
    
        return 0, 0


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  return_cluster_predictions
 #
 #  Function Description:
 #      This function returns a k-means cluster predictions.
 #
 #
 #  Return Type: list of lists
 # 
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          normalized_dataframe
 #                          The parameter is a dataframe of normalized values.
 #  list
 #          k_integer_list
 #                          The parameter is a list of optimal K values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_cluster_predictions \
        (normalized_dataframe,
         k_integer_list):
    
    try:
        
        predictions_integer_list_list = []
        
        for k_value in k_integer_list:
        
            kmeans_model = KMeans(n_clusters = k_value, n_init = 100, random_state = 21)
        
            kmeans_model.fit(normalized_dataframe)
    
            cluster_predictions_integer_list = kmeans_model.predict(normalized_dataframe)
        
            predictions_integer_list_list.append(cluster_predictions_integer_list)

        
        return predictions_integer_list_list
        
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_cluster_predictions, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return the k-means cluster predictions.')
    
        return None


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  return_k_clusters_2d_scatter_plot
 #
 #  Function Description:
 #      This function returns a group of 2-D k-cluster scatter plots for display.
 #
 #
 #  Return Type: Plotly figure
 # 
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          normalized_dataframe
 #                          The parameter is a dataframe of normalized values.
 #  list
 #          k_integer_list
 #                          The parameter is a list of optimal K values.
 #  list
 #          colors_string_list
 #                          The parameter is a list of plot colors.
 #  string
 #          figure_title_string
 #                          The parameter is a figure title.
 #  string
 #          x_axis_name_string
 #                          The parameter is a dataframe column name for the x-axis.
 #  string
 #          y_axis_name_string
 #                          The parameter is a dataframe column name for the y-axis.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_k_clusters_2d_scatter_plot \
        (normalized_dataframe,
         k_integer_list, 
         colors_string_list,
         figure_title_string,
         x_axis_name_string, 
         y_axis_name_string):
    
    try:

        titles_string_list = [f'K-Clusters for K = {n}' for n in k_integer_list]

        max_rows_integer, max_columns_integer \
            = return_max_row_and_column(k_integer_list)

        if max_rows_integer == 0:
        
            return None

    
        plotly_layout \
            = go.Layout \
                (height = 500 * max_rows_integer,
                 width = 500 * max_columns_integer,
                 title_text = figure_title_string)

        plotly_figure \
            = make_subplots \
                (rows = max_rows_integer, 
                 cols = max_columns_integer, 
                 horizontal_spacing = 0.12,
                 vertical_spacing = 0.12,
                 subplot_titles = titles_string_list)

        index_integer = 0

        for row in range(1, max_rows_integer + 1):
        
            for column in range(1, max_columns_integer + 1):

                kmeans_model \
                    = KMeans \
                        (n_clusters = k_integer_list[index_integer], 
                         n_init = 100, 
                         random_state = 21)

                kmeans_model.fit(normalized_dataframe)

                cluster_centers_dataframe \
                    = pd.DataFrame \
                        (kmeans_model.cluster_centers_, 
                         columns = normalized_dataframe.columns)

    
                plotly_points_scatter_trace \
                    = go.Scatter \
                        (x = normalized_dataframe[x_axis_name_string],
                         y = normalized_dataframe[y_axis_name_string],
                         name = 'Points',
                         mode = 'markers',
                         marker = {'color': kmeans_model.labels_,
                                   'colorscale': colors_string_list,
                                   'line': {'color': 'black', 'width': 1.0},
                                   'opacity': 1.0,
                                   'size': 10.0},
                         text = normalized_dataframe.index,
                         hovertemplate = '<b>Cryptocurrency:</b> %{text}<br>'
                                         + '<b>x:</b> %{x}<br>'
                                         + '<b>y:</b> %{y}<br>'
                                         + '<extra></extra>',
                         showlegend = False)

                plotly_clusters_scatter_trace \
                    = go.Scatter \
                        (x = cluster_centers_dataframe[x_axis_name_string],
                         y = cluster_centers_dataframe[y_axis_name_string],
                         name = 'Clusters',
                         mode = 'markers',
                         marker = {'size': 50.0,
                                   'color': cluster_centers_dataframe.index,
                                   'colorscale': colors_string_list,
                                   'opacity': 0.4,
                                   'line': {'color': 'black', 'width': 1.5}},
                        text = [f'{n + 1}' for n in range(len(cluster_centers_dataframe))],
                        hovertemplate = '<b>Cluster %{text}</b><br>'
                                        + '<b>x:</b> %{x}<br>'
                                        + '<b>y:</b> %{y}<br>'
                                        + '<extra></extra>',
                        showlegend = False)
        

                plot_trace_list = [plotly_points_scatter_trace, plotly_clusters_scatter_trace]

                for plot_trace in plot_trace_list:
            
                    plotly_figure.add_trace(plot_trace, row = row, col = column)

                plotly_figure.update_annotations \
                    (font = {'color': 'black', 'family': 'garamond', 'size': 20.0}, yshift = 10.0)

                plotly_figure.update_xaxes \
                    (row = row, 
                     col = column,
                     linecolor = 'black',
                     linewidth = 2.0,
                     mirror = True,
                     showline = True,
                     tickfont = {'color': 'black', 'family': 'garamond', 'size': 14.0})

                plotly_figure.update_yaxes \
                    (row = row, 
                     col = column,
                     linecolor = 'black',
                     linewidth = 2.0, 
                     mirror = True, 
                     showline = True, 
                     tickfont = {'color': 'black', 'family': 'garamond', 'size': 14.0})

                if row == max_rows_integer:
                    
                    plotly_figure.update_xaxes \
                        (row = row, 
                         col = column,
                         title = x_axis_name_string.replace('_', ' ').title(),
                         titlefont = {'color': 'black', 'family': 'garamond', 'size': 18.0}) 

                if column == 1:
            
                    plotly_figure.update_yaxes \
                        (row = row, 
                         col = column,
                         title = y_axis_name_string.replace('_', ' ').title(),
                         titlefont = {'color': 'black', 'family': 'garamond', 'size': 18.0})

                index_integer += 1
      

        plotly_figure.update_layout \
            (plotly_layout,
             showlegend = True, 
             title = {'font': {'color': 'black', 'family': 'garamond', 'size': 24.0}})

        log_subroutines.save_plotly_image(plotly_figure, figure_title_string)

        
        return plotly_figure.show()
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_k_clusters_2d_scatter_plot, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return a K-Clusters scatter plot for display.')
    
        return None  


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  return_k_clusters_3d_scatter_plot
 #
 #  Function Description:
 #      This function returns a 3-D k-cluster scatter plot for display.
 #
 #
 #  Return Type: Plotly figure
 # 
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          normalized_dataframe
 #                          The parameter is a DataFrame of normalized values.
 #  list
 #          k_integer
 #                          The parameter is an optimal k value.
 #  list
 #          colors_string_list
 #                          The parameter is a list of plot colors.
 #  string
 #          figure_title_string
 #                          The parameter is a figure title.
 #  list
 #          column_names_string_list
 #                          The parameter is a list of dataframe column names 
 #                          for dimensions.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_k_clusters_3d_scatter_plot \
        (normalized_dataframe, 
         k_integer, 
         colors_string_list,
         figure_title_string,
         column_names_string_list):
    
    try:
    
        kmeans_model = KMeans(n_clusters = k_integer, n_init = 100, random_state = 21)
    
        kmeans_model.fit(normalized_dataframe)
    
        cluster_centers_dataframe \
            = pd.DataFrame \
                (kmeans_model.cluster_centers_, columns = normalized_dataframe.columns)
    

        plotly_points_scatter_trace \
            = go.Scatter3d \
                (x = normalized_dataframe[column_names_string_list[0]],
                 y = normalized_dataframe[column_names_string_list[1]],
                 z = normalized_dataframe[column_names_string_list[2]],
                 name = 'Points',
                 mode = 'markers',
                 marker = {'color': kmeans_model.labels_,
                           'colorscale': colors_string_list,
                           'line': {'color': 'black', 'width': 1.0},
                           'opacity': 1.0,
                           'size': 7.0},
                 text = normalized_dataframe.index,
                 hovertemplate = '<b>Cryptocurrency:</b> %{text}<br>'
                                 + '<b>x:</b> %{x}<br>'
                                 + '<b>y:</b> %{y}<br>'
                                 + '<b>z:</b> %{z}<br>'
                                 + '<extra></extra>',
                 showlegend = True)   
    
        plotly_clusters_scatter_trace \
            = go.Scatter3d \
                (x = cluster_centers_dataframe[column_names_string_list[0]],
                 y = cluster_centers_dataframe[column_names_string_list[1]],
                 z = cluster_centers_dataframe[column_names_string_list[2]],
                 name = 'Clusters',
                 mode = 'markers',
                 marker = {'size': 42.0,
                           'color': cluster_centers_dataframe.index,
                           'colorscale': colors_string_list,
                           'opacity': 0.4,
                           'line': {'color': 'black', 'width': 1.5}},
                 text = [f'{n + 1}' for n in range(len(cluster_centers_dataframe))],
                 hovertemplate = '<b>Cluster %{text}</b><br>'
                                 + '<b>x:</b> %{x}<br>'
                                 + '<b>y:</b> %{y}<br>'
                                 + '<b>z:</b> %{z}<br>'
                                 + '<extra></extra>',
                 showlegend = True)
    
        plotly_layout \
            = go.Layout \
                (height = 900,
                 width = 900,
                 title = {'x': 0.5,
                          'y': 0.85,
                          'text': figure_title_string,
                          'font': {'color': 'black', 'family': 'garamond', 'size': 28.0}},
                 scene = {'aspectmode': 'manual',
                          'aspectratio': {'x': 0.9, 'y': 0.9, 'z': 0.9},
                          'xaxis': \
                            {'title': {'text': column_names_string_list[0],
                                       'font': {'color': 'black', 'family': 'garamond', 'size': 18.0}},
                             'color': 'black',
                             'gridcolor': 'darkblue',
                             'linecolor': 'black',
                             'linewidth': 2.0,
                             'mirror': True,
                             'showbackground': True,
                             'showline': True,
                             'tickfont': {'color': 'black', 'family': 'garamond', 'size': 14}},
                        'yaxis': \
                            {'title': {'text': column_names_string_list[1],
                                       'font': {'color': 'black', 'family': 'garamond', 'size': 18.0}},
                             'color': 'black',
                             'gridcolor': 'darkblue',
                             'linecolor': 'black',
                             'linewidth': 2.0,
                             'mirror': True,
                             'showbackground': True,
                             'showline': True,
                             'tickfont': {'color': 'black', 'family': 'garamond', 'size': 14.0}},
                        'zaxis': \
                            {'title': {'text': column_names_string_list[2],
                                       'font': {'color': 'black', 'family': 'garamond', 'size': 18.0}},
                             'color': 'black',
                             'gridcolor': 'darkblue',
                             'linecolor': 'black',
                             'linewidth': 2.0,
                             'mirror': True,
                             'showbackground': True,
                             'showline': True,
                             'tickfont': {'color': 'black', 'family': 'garamond', 'size': 14.0}}},
                 legend = {'x': 1.2,
                           'y': 0.8,
                           'xanchor': 'right',
                           'yanchor': 'top',
                           'bgcolor': 'aliceblue',
                           'font': {'color': 'black', 'family': 'garamond', 'size': 20.0}})

        plotly_figure\
            = go.Figure(data = [plotly_points_scatter_trace, plotly_clusters_scatter_trace], layout = plotly_layout)
    
    
        log_subroutines.save_plotly_image(plotly_figure, figure_title_string)
    
        
        return plotly_figure.show()
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_k_clusters_3d_scatter_plot, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return a 3D K-Clusters scatter plot for display.')
    
        return None


# In[ ]:





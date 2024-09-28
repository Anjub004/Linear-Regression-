# 1. Fucntion to create piechart 

def create_piechart(data, column):
    """
    Objective
    ---------- 
    Create Pichart for Categorical varaibles present in Pandas Dataframe
    
    parameters
    ----------
    data: this is pandas dataframe
    column: this is column name which is used to create plot
        
    returns
    ----------
    this will show piechart
    
    """
    labels = list(data[column].value_counts().to_dict().keys())
    sizes = list(data[column].value_counts().to_dict().values())
   
    plt.pie(sizes, 
            labels=labels, 
            autopct='%1.2f%%',
            shadow=False, 
            startangle=45)
    
    plt.axis('equal')  
    plt.title("Piechart - {}".format(column))
    plt.show()
    

# 2. Fucntion to check missing data 
    
def missing_data(df, plot_missing=True):
    """
    Objective
    ----------
    it shows the missing data in each column with 
    total missing values, percentage of missing value and
    its data type in descending order.
    
    parameters
    ----------
    df: pandas dataframe
        input data frame 
    
    returns
    ----------
    missing_data: output data frame(pandas dataframe)
    
    """
    
    total = df.isnull().sum().sort_values(ascending=False)
    
    percent = round((df.isnull().sum()/df.isnull().count()  * 100).sort_values(ascending=False),2)
    
    data_type = df.dtypes
    missing_data = pd.concat([total,percent,data_type],
                             axis=1,
                             keys=['Total','Percent','Data_Type']).sort_values("Total", 
                                                                               axis = 0,
                                                                               ascending = False)


    if plot_missing:

        plt.figure(figsize=(15,5))
        sns.heatmap(df.isnull(), cbar = False, yticklabels=False, cmap="magma" )
        print()

        
    return missing_data.head(missing_data.shape[0])

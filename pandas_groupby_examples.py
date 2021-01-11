# Example 1: Group by similar to SQL:
#Simple examples:
df.groupby('A').B.mean()
df.groupby('A').B.max()
df.groupby('A').B.agg(['min', 'max'])
df.groupby(['Name', 'Fruit']).agg({'Number': "sum"})



grouped.agg({'C_sum' : lambda x: x['C'].sum(),
             'C_std': lambda x: x['C'].std(),
             'D_sum' : lambda x: x['D'].sum()},
             'D_sumifC3': lambda x: x['D'][x['C'] == 3].sum(), ...)


# Example 2: apply the sae function on all of the remaining columns
response_data_weekly = response_data.groupby(['member_uuid', 'metric_week'])[['metric_value', 'baseline_metric_value', 'lusm_score']].median().reset_index()


# Example 3:
def my_func(df):
        
        # Create a pandas series
        d = {}
        d['Lab'+str(i)] = 0
        d['Low'+str(i)] = 0
        d['High'+str(i)] = 0
        
        df_lab = df[df['lab_name']== Top_proc[i]]
        
        if len(df_lab)>0:
            
            d['Lab'+str(i)] = 1
            a = df_lab.PC_result.values[0] # The assumption is that each patient has only done one of each lab
            
            if a==-1:
                d['Low'+str(i)] = 1
            
            elif a==1:
                d['High'+str(i)] = 1

        return pd.Series(d) #, index=['a_sum', 'a_max', 'b_mean', 'c_d_prodsum'])
    
    
    
    F_df = df.groupby(['PC_enc']).apply(my_func).reset_index()#.rename(columns={'lab_name':'lab_name', 0:'F'+str(i)}) 

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

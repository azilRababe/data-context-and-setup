import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        # pass  # YOUR CODE HERE

        csv_path=os.path.join('/home/rababeazil/code/azilRababe/data-context-and-setup','data','csv')
        csv_path=os.path.join('/')
        pd.read_csv(os.path.join(csv_path, 'olist_sellers_dataset.csv')).head()
        file_names=os.listdir(csv_path)
        file_names.remove('.keep')
        key_names=[name.replace('.csv', '').replace('_dataset','').replace('olist_','') for name in file_names]
        # key_names.remove('.keep')
        pd.read_csv(os.path.join(csv_path,'product_category_name_translation.csv'))
        data={}
        for (keys,values) in zip(key_names,file_names):
            data[keys]=pd.read_csv(os.path.join(csv_path,values))


    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")







class Metrics:
    def __init__(self,**kwargs):
        """
        Set's Animations variables.

        Kwargs:
           data (pandas dataframe):
        """
        if 'data' in kwargs:
            try:
                df = kwargs['data']
                if not df.empty:
                    print(df.head())
                else:
                    raise ValueError()
            except ValueError:
                print("no dataframe")

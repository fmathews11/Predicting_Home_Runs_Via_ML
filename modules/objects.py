from sklearn.base import BaseEstimator
import pandas as pd

class InvalidDataError(Exception):
    pass

class InvalidInputError(Exception):
    pass

### Pipeline Transformers ###

class DataframeColumnSelector(BaseEstimator):

    """
    Creating an sklearn Pipeline and need to select particular columns from a pd.DataFrame?
    This is your object!

    Parameters
    ----------
    col_list: list
        List of columns to select from the input dataframe

    Methods
    ----------
    fit
     - params:
        X - pd.DataFrame

        Fit the transformer to a pd.DataFrame
    transform
        Transform the pd.DataFrame via returning a copy with only the columns passed in the col_list parameter
    fit_transform
        Calls the fit and transform methods in one method
    
    Attributes
    ----------
    columns
        Returns the list of columns the selector

        Can also be used to set or update the list of columns

        Example:

        >> sel = DataFrameColumnSelector(col_list = ['manufacturer','mpn'])
        >> print(sel.columns)

        ['manufacturer','mpn']

        >> sel.columns = ['manufacturer','mpn','product_description_clean']
        >> print(sel.columns)

        ['manufacturer','mpn','product_description_clean']

        df_new = sel.fit_transform(df)
    """

    def __init__(self,col_list: list):

        if isinstance(col_list,list):
            self.col_list = col_list
    
    def fit(self,X,y = None):

        if isinstance(X,pd.DataFrame):

            return self
        
        raise InvalidInputError("Must pass a pd.DataFrame into the .fit method")
    
    def transform(self,X,y = None) -> pd.DataFrame:

        if not isinstance(X,pd.DataFrame):

            raise InvalidInputError(f"Input type passed must be a pd.DataFrame.  User-supplied input was of type {type(X).__name__}")
        
        if not self.col_list:

            raise InvalidDataError('Cannot pass a blank list into DataFrameColumnSelector')

        #Make a copy of the input DataFrame so as to not disturb the original data
        to_return = X.copy()

        return to_return.loc[:,[i for i in self.col_list]]
    
    def fit_transform(self,X,y = None):
        return self.transform(X=X,y = y)

    @property
    def columns(self):
        print(self.col_list)
    
    @columns.setter
    def columns(self,input_list):

        if isinstance(input_list,list):

            self.col_list = input_list
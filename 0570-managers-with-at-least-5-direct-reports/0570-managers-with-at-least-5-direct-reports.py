import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df1 = employee.copy()
    df1 = df1.groupby("managerId")["id"].count().reset_index()
    df1 = df1.rename(columns = {"id" : "reports"})
    print(df1.head())
    df1 = df1[df1["reports"] >= 5]
    df = employee.merge(df1, left_on = "id", right_on = "managerId")
    print(df.head())
    return df[["name"]]
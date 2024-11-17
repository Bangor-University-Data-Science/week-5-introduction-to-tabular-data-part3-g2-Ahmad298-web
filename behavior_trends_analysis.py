import pandas as pd

def import_data(OnlineRetail: str) -> pd.DataFrame:
    """
    Import the dataset from an Excel or CSV file into a DataFrame.
    """
    if filename.endswith(".xlsx"):
        return pd.read_excel(OnlineRetail.xlsx)
    elif filename.endswith(".csv"):
        return pd.read_csv(filename)
    else:
        raise ValueError("Unsupported file format. Use .xlsx or .csv.")

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the data to remove rows with missing CustomerID and exclude rows
    with negative values in Quantity or UnitPrice.
    """
    df = df.dropna(subset=['CustomerID'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    return df

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    """
    Identify loyal customers based on a minimum purchase threshold.
    """
    customer_counts = df.groupby('CustomerID').size().reset_index(name='purchase_count')
    return customer_counts[customer_counts['purchase_count'] >= min_purchases]

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the total revenue per quarter.
    """
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['quarter'] = df['InvoiceDate'].dt.to_period('Q')
    revenue = df.groupby('quarter').apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum()).reset_index(name='total_revenue')
    return revenue

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """
    Identify the top_n products with the highest total quantity sold.
    """
    product_demand = df.groupby('StockCode')['Quantity'].sum().reset_index(name='total_quantity')
    return product_demand.sort_values(by='total_quantity', ascending=False).head(top_n)

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a summary showing the average quantity and average unit price for each product.
    """
    summary = df.groupby('StockCode').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    return summary

def answer_conceptual_questions() -> dict:
    """
    Answer the conceptual questions.
    """
    return {
        "Q1": {"A", "D"},
        "Q2": {"B"},
        "Q3": {"A", "B", "C"},
        "Q4": {"A", "B"},
        "Q5": {"A"}
    }

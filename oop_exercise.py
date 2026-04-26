class Dataset:
    """Base class for any dataset"""
    
    def __init__(self, name):
        self.name = name
        self.data = []
    
    def load(self):
        raise NotImplementedError("Subclasses must implement load()")
    
    def describe(self):
        return f"Dataset: {self.name}, Samples: {len(self.data)}"


class CSVDataset(Dataset):
    """A dataset loaded from a CSV-like list of rows"""
    
    def __init__(self, name, filepath):
        super().__init__(name)
        self.filepath = filepath
    
    def load(self):
        # Simulating loading data (no real file needed)
        self.data = [
            {"age": 25, "salary": 50000},
            {"age": 30, "salary": 60000},
            {"age": 35, "salary": 75000},
        ]
        print(f"Loaded {len(self.data)} records from {self.filepath}")
    
    def get_column(self, column_name):
        return [row[column_name] for row in self.data]


# --- Your job: write code below this line ---

# 1. Create a CSVDataset object with name="employees" and filepath="employees.csv"

Data1=CSVDataset("employees","employees.csv")



# 2. Call .load() on it
Data1.load()
# 3. Print the result of .describe()
print(Data1.describe())
# 4. Print the "salary" column using get_column()
print(Data1.get_column("salary"))
# 5. Create a second dataset with different name and filepath, load it, describe it
Data2= CSVDataset("company","company.csv")
Data2.load()
print(Data2.describe())
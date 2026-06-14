# OOP: Inheritance + Template Method Pattern
# Pattern: base class defines the skeleton (run()), subclasses fill in the steps
# Concepts: super().__init__(), method override, raise NotImplementedError

class DataPipeline:
    """Base class. Defines the run() skeleton — subclasses implement the steps."""

    def __init__(self, name: str, source: str):
        self.name = name
        self.source = source

    def extract(self):
        print(f"[{self.name}] Extracting from {self.source}")

    def transform(self):
        raise NotImplementedError("Subclass must implement transform()")

    def load(self):
        raise NotImplementedError("Subclass must implement load()")

    def run(self):
        self.extract()
        self.transform()
        self.load()


class SparkPipeline(DataPipeline):
    def __init__(self, name: str, source: str, partitions: int):
        super().__init__(name, source)      # call parent __init__
        self.partitions = partitions

    def transform(self):
        print(f"[{self.name}] Transforming with Spark ({self.partitions} partitions)")

    def load(self):
        print(f"[{self.name}] Loading to data lake")


class PandasPipeline(DataPipeline):
    def __init__(self, name: str, source: str, chunksize: int = 10_000):
        super().__init__(name, source)
        self.chunksize = chunksize

    def transform(self):
        print(f"[{self.name}] Transforming with Pandas (chunksize={self.chunksize})")

    def load(self):
        print(f"[{self.name}] Loading to Postgres")


if __name__ == "__main__":
    pipelines: list[DataPipeline] = [
        SparkPipeline("ETL-Spark", "oracle", partitions=100),
        PandasPipeline("ETL-Pandas", "csv", chunksize=5_000),
    ]

    for pipeline in pipelines:
        pipeline.run()
        print()

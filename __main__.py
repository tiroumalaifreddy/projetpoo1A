from estimators.estimators import Estimators
from transformers.transformers import Transformers

if __name__ == "__main__":
    estimators = Estimators()
    transformers = Transformers()
    estimators.fit()
    transformers.transform()

import mlflow


def calculate(X, y):
    return X / y 

if __name__ =='__main__':
    X = 20
    y = 10
    with mlflow.start_run():
        
        results = calculate(X ,y)
        print(f'My results is {results}')

        mlflow.log_param("X",X)
        mlflow.log_param("y",y)
        mlflow.log_param("results",results)

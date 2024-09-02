##Made By : ANIS BENINI 


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import Model
from keras.layers import Input, Dense

if __name__ == "__main__":
    
    # 2. Import the dataset
    data = pd.read_csv('/content/drive/MyDrive/data.csv')

    # 3. Check for missing values
    # Number of missing values for each column
    # Number of rows
    data_missing = data.isnull().sum()
    n_rows = data.shape[0]
    
    # Percentage of missing values for each column
    missing_percentage = data_missing / n_rows * 100
    print("Missing data is:")
    print(data_missing)
    print("Percentage of missing data is:")
    print(missing_percentage)

    # Remove columns with more than 75% missing values
    data = data.loc[:, missing_percentage <= 75]

    # Remove inconsistent data using a threshold percentage
    values = data["Value"].value_counts(normalize=True)
    print("Values are:")
    print(values)
    retained_values = values[values > 0.001].index.tolist()
    data = data[data["Value"].isin(retained_values)]

    print("Retained values are:")
    print(retained_values)

    # Method 2:
    data_missing = data.isnull().sum()
    for c in data.columns:
        if data_missing[c] > 0:
            if data[c].dtype == 'object':  # Check if the column contains non-numeric values
                print(c)
                mode_value = data[c].mode()[0]  # Calculate the mode
                print(mode_value)
                data[c].fillna(mode_value, inplace=True)  # Replace missing values with the mode
            else:
                print(c)
                mean_value = data[c].mean()  # Calculate the mean
                print(mean_value)
                data[c].fillna(mean_value, inplace=True)

    # Remove the 'Date' and 'Time' columns
    data = data.drop('Date', axis=1)
    data = data.drop('Time', axis=1)

    # Check categorical values
    sensorID = data.loc[:, "SensorID"].values
    sensorValue = data.loc[:, "Value"].values
    encodeValue = pd.get_dummies(data['Value'])
    data = pd.concat([data, encodeValue], axis=1)
    data = data.drop('Value', axis=1)
    encodeID = pd.get_dummies(data['SensorID'])
    data = pd.concat([data, encodeID], axis=1)
    data = data.drop('SensorID', axis=1)
    # Replace boolean values with integers
    data.replace({False: 0, True: 1}, inplace=True)
    data.head()

    # Split the dataset
    x = data.loc[:, 'ABSENT':]
    print('Inputs:\n', x, '\nShape:', x.shape)

    y = data.loc[:, 'ResidentID1':'TaskID1']
    print('Outputs:\n', y, '\nShape:', y.shape)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
    print("Size of X_train:", x_train.shape)
    print("Size of X_test:", x_test.shape)
    print("Size of y_train:", y_train.shape)
    print("Size of y_test:", y_test.shape)

    # Define the model inputs with the expected shape (43,)
    inputs = Input(shape=(43,))

    # Define the intermediate layers and the output layer
    hidden_layer1 = Dense(64, activation='sigmoid')(inputs)
    hidden_layer2 = Dense(64, activation='sigmoid')(hidden_layer1)
    output = Dense(2, activation='sigmoid')(hidden_layer2)

    # Create the model by specifying the inputs and outputs
    model = Model(inputs=inputs, outputs=output)

    # Display a summary of the model
    model.summary()

    # Compile the model with the accuracy metric
    model.compile(optimizer='adam', loss=keras.losses.MeanSquaredError(), metrics=['accuracy'])

    # Convert input data to float32
    x_train = x_train.astype(np.float32)
    x_test = x_test.astype(np.float32)

    # Convert output data to float32
    y_train = y_train.astype(np.float32)
    y_test = y_test.astype(np.float32)
    
    # Train the model
    history = model.fit(x_train, y_train, epochs=10, batch_size=32)

    # Retrieve training metrics
    loss = history.history['loss']
    accuracy = history.history['accuracy']
    epochs = range(1, len(loss) + 1)

    # Make predictions on the training data
    predictions = model.predict(x_train)

    # Evaluate the model
    loss_, accuracy_ = model.evaluate(x_test, y_test)
    print("Test loss:", loss_)
    print("Test accuracy:", accuracy_)

    # Plotting with Matplotlib
    # Plot the loss curve
    plt.plot(epochs, loss, label='Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss During Training')
    plt.legend()
    plt.show()

    # Plot the accuracy curve
    plt.plot(epochs, accuracy, label='Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Accuracy During Training')
    plt.legend()
    plt.show()

    # Plot predictions vs. true values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_train, predictions)
    plt.xlabel("True Values")
    plt.ylabel("Predictions")
    plt.title("True Values vs. Predictions")
    plt.show()

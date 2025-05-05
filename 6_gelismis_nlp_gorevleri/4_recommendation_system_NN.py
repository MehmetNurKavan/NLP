#%% Import libraries

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

#%% Create a simple dataset (user - item - rating)

# Users: 0 to 4
# Items: 0 to 5
# Ratings are between 1 and 5

user_ids = np.array([0,1,2,3,4,0,1,2,3,4])  
item_ids = np.array([0,1,2,3,4,1,2,3,4,5])
ratings  = np.array([5,4,3,2,1,4,5,2,3,4])  

#%% Split data into training and test sets

user_ids_train, user_ids_test, item_ids_train, item_ids_test, ratings_train, ratings_test = train_test_split(
    user_ids, 
    item_ids, 
    ratings, 
    test_size=0.2, 
    random_state=42,
)

#%% Define the neural network model

def create_model(num_users, num_items, embedding_dim):
    # Input layers
    user_input = Input(shape=(1,), name="user")
    item_input = Input(shape=(1,), name="item")
    
    # Embedding layers
    user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim, name="user_embedding")(user_input)
    item_embedding = Embedding(input_dim=num_items, output_dim=embedding_dim, name="item_embedding")(item_input)
    
    # Flatten vectors
    user_vecs = Flatten()(user_embedding)
    item_vecs = Flatten()(item_embedding)
    
    # Compute dot product (similarity)
    dot_product = Dot(axes=1)([user_vecs, item_vecs])
    
    # Optional dense layer (can be removed)
    output = Dense(1)(dot_product)
    
    # Create and compile the model
    model = Model(inputs=[user_input, item_input], outputs=output)
    model.compile(optimizer=Adam(learning_rate=0.01), loss="mean_squared_error")
    
    return model

#%% Train the model

num_users = len(np.unique(user_ids))  # 5 unique users
num_items = len(np.unique(item_ids))  # 6 unique items
embedding_size = 8  # latent factor size

model = create_model(num_users, num_items, embedding_size)

# Train using user and item ids as input, ratings as target
model.fit([user_ids_train, item_ids_train], ratings_train, epochs=40, verbose=1, validation_split=0.1)

#%% Test - Evaluation

loss = model.evaluate([user_ids_test, item_ids_test], ratings_test)
print(f"Test Loss (MSE): {loss:.4f}")

#%% Recommendation test

user_id = np.array([0])
item_id = np.array([5])

predicted_rating = model.predict([user_id, item_id])
print(f"Predicted rating for user: {user_id[0]}, item: {item_id[0]} : {predicted_rating[0][0]:.2f}")

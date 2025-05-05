#%% Import libraries

from surprise import Dataset, KNNBasic, accuracy
from surprise.model_selection import train_test_split

#%% Load the built-in MovieLens 100k dataset

data = Dataset.load_builtin("ml-100k")

#%% Split the data into training and testing sets (80% train, 20% test)

train_set, test_set = train_test_split(data, test_size=0.2)

#%% Define similarity options and create the KNN model

sim_option = {
    "name": "cosine",       # Use cosine similarity
    "user_based": True      # Set to True for user-based filtering
}

model = KNNBasic(sim_options=sim_option)  # Create the KNN model
model.fit(train_set)  # Train the model with training data

#%% Evaluate the model on the test set

predictions = model.test(test_set)
accuracy.rmse(predictions)

#%% Function to get top-N recommendations for each user

def get_top_n(predictions, n=10):
    top_n = {}

    # Group all predictions by user
    for uid, iid, true_r, est, _ in predictions:
        if uid not in top_n:
            top_n[uid] = []
        top_n[uid].append((iid, est))

    # Sort the predictions for each user and retrieve the top-N items
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

#%% Generate top-10 recommendations for each user

top_n = get_top_n(predictions, n=10)

#%% Show top-10 recommendations for a specific user (e.g., user "1")

user_id = "1"
print(f"Top 10 recommendations for user {user_id}:")

for item_id, rating in top_n[user_id]:
    print(f"Item ID: {item_id}, Predicted Rating: {rating:.2f}")

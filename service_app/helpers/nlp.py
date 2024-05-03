import os
import csv
import sys
import nltk
import logging

from fuzzywuzzy import fuzz
from operator import itemgetter
from sentence_transformers import SentenceTransformer, util

nltk.download('punkt')
# Load a pre-trained Sentence Transformer model
MODEL = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
# Create a logger
logger = logging.getLogger(__name__)


class NLP:
    def __init__(self):
        logger.info("Reading CSV Data")
        self._user_data = self.csv_reader('users.csv')
        self._transaction_data = self.csv_reader('transactions.csv')

    # Load user data from CSV file into a dictionary
    def csv_reader(self, filename):
        logger.info("Reading file: %s", filename)
        csv_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'input_files', filename)
        data = []
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def match_users(self, transaction_id):
        matched_users = []
        for user in self._user_data:
            ratio = fuzz.ratio(user["id"].lower(), transaction_id.lower())
            if ratio >= 70:  # Adjust this threshold as needed
                matched_users.append({"id": user["id"], "name": user["name"], "match_metric": ratio})

        # Sort users by match ratio in descending order
        matched_users.sort(key=itemgetter("match_metric"), reverse=True)

        return matched_users

    def similar_transactions(self, input_string):
        input_embedding = MODEL.encode(input_string, convert_to_tensor=True)
        transaction_embeddings = MODEL.encode([transaction["description"] for transaction in self._transaction_data],
                                              convert_to_tensor=True)

        # Calculate cosine similarity between input and transaction embeddings
        similarities = util.pytorch_cos_sim(input_embedding, transaction_embeddings)[0].tolist()

        # Combine similarities with transaction data
        similar_transactions = [
            {"id": self._transaction_data[i]["id"], "description": self._transaction_data[i]["description"],
             "embeddings": transaction_embeddings[i].tolist(), "similarity": similarities[i]} for
            i in range(len(self._transaction_data))]

        # Sort transactions by similarity in descending order
        similar_transactions.sort(key=lambda x: x["similarity"], reverse=True)

        return {
            "total_number_of_tokens_used": len(nltk.word_tokenize(input_string)),
            "transactions": similar_transactions
        }

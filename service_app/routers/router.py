from fastapi import APIRouter, HTTPException, Query

from service_app.helpers.nlp import NLP

router = APIRouter()

NLP = NLP()


@router.get("/api/v1/match_users", tags=["Match Users"],
            description="This API endpoint is designed to match users with their payments based on a transaction ID "
                        "input. The endpoint takes a transaction ID as a string input and returns a list of users who "
                        "could be considered as matching the transaction with their ID. The matching logic is based on "
                        "fuzzy string matching, allowing for consideration of typos or variations in the transaction ID"
                        " input.",
            summary="Match users with transactions"
            )
def match_users_endpoint(transaction_id: str = Query(..., title="Transaction ID",
                                                     description="The transaction ID for which users are to be matched."
                                                     )):
    """
    Match users with their payments based on a transaction ID input.

    Parameters:
    - transaction_id: The transaction ID for which users are to be matched.

    Returns:
    - total_matches: The total number of matched users.
    - users: A list of dictionaries containing information about matched users.
    """
    if not transaction_id:
        raise HTTPException(status_code=422, detail="Transaction ID cannot be empty.")

    matched_users = NLP.match_users(transaction_id )

    response = {
        "total_matches": len(matched_users),
        "users": matched_users
    }

    return response


@router.get("/api/v1/similar_transactions",
            tags=["Similar Transactions"],
            summary="Find transactions with similar descriptions",
            description="List of transactions with similar descriptions"
            )
def similar_transactions_endpoint(input_string: str = Query(..., title="Input String",
                                                            description="The input string to find similar transactions."
                                                            )):
    """
    Find transactions with descriptions similar to the input string in a semantical way.

    This endpoint uses a pre-trained language model to generate embeddings from transaction descriptions and calculates
    the cosine similarity between the input string embedding and transaction embeddings. Transactions with descriptions
    similar to the input string are returned, sorted in order of relevance.

    Parameters:
    - input_string: The input string for which similar transactions are to be found.

    Returns:
    - total_number_of_tokens_used: Total number of tokens used
    - transactions: A list of dictionaries containing information about transactions with similar descriptions. Each
    dictionary includes the transaction ID, description, embedding and similarity score indicating the degree of
    similarity between the transaction description and the input string.
    """
    if not input_string:
        raise HTTPException(status_code=422, detail="Input String cannot be empty.")
    return NLP.similar_transactions(input_string)

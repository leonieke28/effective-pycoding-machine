from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Helper to get quote from a quote ID"""
    # use a list comprehension to filter out the quote where id matches the input qid
    quotes_filtered = [quote for quote in quotes if quote["id"] == qid]
    # if a match is found, it returns the first quote (there should ideally be only one per id)
    # otherwise it returns None
    return quotes_filtered[0] if quotes_filtered else None


def _quote_exists(new_quote):
    """Helper to check existence of a quote"""
    # use a list comprehension to check if any quote in quotes matches the new quote
    return any(
        quote
        for quote in quotes
        if quote["quote"] == new_quote.get("quote")
        and quote["movie"] == new_quote.get("movie")
    )


@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    return jsonify({"quotes": quotes})  # return the list of quotes as a json response


@app.route("/api/quotes/<int:qid>", methods=["GET"])
def get_quote(qid):
    quote = _get_quote(qid)
    if quote is None:
        abort(404)  # if no quote is found for the qid, return a 404 not found error
    return jsonify(
        {"quotes": [quote]}
    )  # return the quote wrapped in a list as a json response


@app.route("/api/quotes", methods=["POST"])
def create_quote():
    if not request.json or not "quote" in request.json or not "movie" in request.json:
        abort(
            400
        )  # if quote or movie field is missing in json request, return a 400 bad request error
    if _quote_exists(request.json):
        abort(400)  # if the quote already exists, return a 400 bad request error
    quote = {
        "id": quotes[-1]["id"]
        + 1,  # set the id as one more than the id of the last quote in the list
        "movie": request.json["movie"],
        "quote": request.json["quote"],
    }
    quotes.append(quote)  # add the new quote to the quotes list
    return (
        jsonify({"quote": quote}),
        201,
    )  # return the created quote as a json response with a 201 created status code


@app.route("/api/quotes/<int:qid>", methods=["PUT"])
def update_quote(qid):
    quote = _get_quote(qid)
    if quote is None:
        abort(404)  # if no quote is found for the qid, return a 404 not found error
    if not request.json:
        abort(400)  # if no json request is found, return a 400 bad request error
    quote["quote"] = request.json.get("quote", quote["quote"])
    quote["movie"] = request.json.get("movie", quote["movie"])
    return jsonify({"quote": quote})  # return the updated quote as a json response


@app.route("/api/quotes/<int:qid>", methods=["DELETE"])
def delete_quote(qid):
    quote = _get_quote(qid)
    if quote is None:
        abort(404)  # if no quote is found for the qid, return a 404 not found error
    quotes.remove(quote)  # remove the quote from the quotes list
    return jsonify({"result": True}), 204

from flask import Blueprint, request, jsonify
from app.services.vectorstore_service import get_vectorstore

query_bp = Blueprint("query_bp", __name__)

@query_bp.route("/query", methods=["POST"])
def query_data():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query text missing"}), 400

    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()
    results = retriever.get_relevant_documents(query)

    unique_results = list({doc.page_content: doc for doc in results}.values())
    unique_results = unique_results[:5]

    return jsonify({
        "query": query,
        "results": [r.page_content for r in unique_results]
    })

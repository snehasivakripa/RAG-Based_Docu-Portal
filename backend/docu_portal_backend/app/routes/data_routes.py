from flask import Blueprint, request, jsonify
from app.services.loaders import load_website
from app.services.vectorstore_service import store_documents

data_bp = Blueprint("data_bp", __name__)

@data_bp.route("/load", methods=["POST"])
def load_data():
    data = request.json
    urls = data.get("urls", [])

    if not urls:
        return jsonify({"error": "No URLs provided"}), 400

    documents = load_website(urls)
    store_documents(documents)
    return jsonify({"message": "✅ Data successfully stored in ChromaDB!"})

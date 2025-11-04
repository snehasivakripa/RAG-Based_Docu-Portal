import os
from flask import Blueprint, request, jsonify
from app.services.loaders import load_pdf
from app.services.vectorstore_service import store_documents
from app.utils.config import UPLOAD_FOLDER

upload_bp = Blueprint("upload_bp", __name__)

@upload_bp.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    documents = load_pdf([file_path])
    store_documents(documents)

    return jsonify({"message": f"✅ PDF '{file.filename}' uploaded and stored successfully!"})

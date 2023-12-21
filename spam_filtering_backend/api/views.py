"""Views for the API app"""
import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import joblib


@csrf_exempt
def authenticate(request):
    """Authentification view to validate a token from the frontend."""

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            token = data.get("token", "")
            valid = os.environ.get("AUTH_TOKEN", "") == token
            return JsonResponse({"validated": valid})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in request"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def classify(request):
    """Classify view for classifying e-mail texts with a count vectorizer."""
    if request.method == "POST":
        model = joblib.load("spam_filtering_backend/data/spam_classifier_model.joblib")
        count_vectorizer = joblib.load(
            "spam_filtering_backend/data/count_vectorizer.joblib"
        )
        data = json.loads(request.body.decode("utf-8"))
        input_array = []
        input_array.append(data.get("content", ""))
        input_features = count_vectorizer.transform(input_array)
        prediction = model.predict(input_features)
        return JsonResponse({"prediction": int(prediction[0])})
    return JsonResponse({"error": "Invalid request method"}, status=405)

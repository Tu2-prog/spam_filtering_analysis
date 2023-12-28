"""Views for the API app"""
import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import joblib
from api.classifier import NaiveBayesClassifier


@csrf_exempt
def authenticate(request):
    """Authentification view to validate a token from the frontend.
    :param request: A request object containing neccessary data for the authentification.
    :return A Response object that returns the result of the authentication in the JSON format.
    """

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
    """Classify view for classifying e-mail texts with a count vectorizer.
    :param request: A http request containing the neccessary data to do the computations.
    :return: A Response object that returns the result of the classification in the JSON format.
    """
    if request.method == "POST":
        model = joblib.load("spam_filtering_backend/data/spam_classifier_model.joblib")
        count_vectorizer = joblib.load(
            "spam_filtering_backend/data/count_vectorizer.joblib"
        )

        # Loading parameters for the naive bayes classifiers
        parameters_ham = joblib.load(
            "spam_filtering_backend/data/parameters_ham.joblib"
        )
        parameters_spam = joblib.load(
            "spam_filtering_backend/data/parameters_spam.joblib"
        )
        p_ham = joblib.load("spam_filtering_backend/data/p_ham.joblib")
        p_spam = joblib.load("spam_filtering_backend/data/p_spam.joblib")

        data = json.loads(request.body.decode("utf-8"))
        selected_option = data.get("classifier", "")
        selected_option = int(selected_option)
        if selected_option == 0:
            input_array = []
            input_array.append(data.get("content", ""))
            input_features = count_vectorizer.transform(input_array)
            prediction = model.predict(input_features)
            return JsonResponse({"prediction": int(prediction[0])})
        input_prompt = data.get("content", "")
        naive_bayes_classifier = NaiveBayesClassifier(
            parameters_spam, parameters_ham, p_spam, p_ham
        )
        prediction = naive_bayes_classifier.classify(input_prompt)
        return JsonResponse({"prediction": prediction})
    return JsonResponse({"error": "Invalid request method"}, status=405)

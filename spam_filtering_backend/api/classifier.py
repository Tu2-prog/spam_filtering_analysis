"""Module containing classifiers that are going to be used in the context of this project."""
import re


class NaiveBayesClassifier:
    """Naive Bayes Classifier trained to classify email texts."""

    def __init__(self, parameters_spam, parameters_ham, p_spam, p_ham):
        """
        Constructor initializing the classifier for the text analysis.
        :param parameters_spam: Dataset containing email texts which are spam.
        :param parameters_ham: Dataset containing email texts which are not spam.
        :param p_spam: Dataset containing the probabilities for the email texts which are spam.
        :param p_ham: Dataset containing the probabilities for the email texts which are not spam.
        """

        self.parameters_spam = parameters_spam
        self.parameters_ham = parameters_ham
        self.p_spam = p_spam
        self.p_ham = p_ham

    def classify(self, message):
        """Method responsible for classifying the input prompt.
        :param message: Message string that is used to classify.
        :return: A boolean stating if the classified message is a spam message or not.
        """
        message = re.sub("\W", " ", message)
        message = message.lower().split()

        p_spam_given_message = self.p_spam
        p_ham_given_message = self.p_ham

        for word in message:
            if word in self.parameters_spam:
                p_spam_given_message *= self.parameters_spam[word]

            if word in self.parameters_ham:
                p_ham_given_message *= self.parameters_ham[word]

        return p_ham_given_message < p_spam_given_message

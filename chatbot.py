import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(file_path):
    data = pd.read_csv(file_path)
    questions = data["instruction"].astype(str).tolist()
    answers = data["response"].astype(str).tolist()
    return questions, answers

def train_model(questions):
    vectorizer = TfidfVectorizer(stop_words='english')
    question_vectors = vectorizer.fit_transform(questions)
    return vectorizer, question_vectors

def get_response(user_input, vectorizer, question_vectors, answers):
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, question_vectors)

    score = similarity.max()

    if score < 0.3:
        return "Sorry, I didn't understand your question."

    index = similarity.argmax()
    return answers[index]

def main():
    print("AI Customer Support Chatbot")
    print("-----------------------------")

    questions, answers = load_data("Customer_Support_Dataset.csv")
    vectorizer, question_vectors = train_model(questions)

    while True:
        user_input = input("\nAsk a question (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = get_response(user_input, vectorizer, question_vectors, answers)
        print("Bot:", response)

if __name__ == "__main__":
    main()
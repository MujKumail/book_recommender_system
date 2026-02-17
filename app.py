from flask import Flask,render_template,request
import pickle
import numpy as np
import csv
import difflib
from datetime import datetime


popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_ratings'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template(
        'recommend.html',
        book_list=list(pt.index)
    )


@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')

    # 🔴 If book not found
    if user_input not in pt.index:
        suggestions = difflib.get_close_matches(user_input, pt.index, n=3)

        return render_template(
            'recommend.html',
            error="Book not found in dataset!",
            suggestions=suggestions,
            book_list=list(pt.index),
            selected_book=user_input
        )

    # 🟢 If book exists
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]

        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return render_template(
        'recommend.html',
        data=data,
        book_list=list(pt.index),
        selected_book = user_input
    )


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Save to CSV file
    with open('messages.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now(),
            name,
            email,
            message
        ])

    return render_template('contact.html', success=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



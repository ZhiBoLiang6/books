from flask import Flask, jsonify
from books import Book

"""
接口说明：
1.返回的是json数据
2.结构如下
{
    resCode: 0,非0即错误
    data: # 数据位置,一般为数组
    message: '对本次请求的说明'
}
"""


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    book = Book()
    arrData = book.get_books_infos_limit()
    return jsonify(arrData)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")

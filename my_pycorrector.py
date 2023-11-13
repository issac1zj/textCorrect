from flask import Flask, request
from flask_cors import CORS
import pycorrector

#github 地址
# https://github.com/shibing624/pycorrector

app = Flask(__name__)
CORS(app, supports_credentials=True)
pycorrector.set_custom_confusion_path_or_dict("./error_words")


@app.route("/correct", methods=["POST"])
def run():
    text = request.get_json().get("text", "")
    if text:
        corrected_sent, detail = pycorrector.correct(text)
        return {"corrected_sent": corrected_sent, "detail": detail}
    else:
        return {}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2345)


text1 = "少先队员因该为老人让坐"
text2 = "横需贺港停靠里跟号航空母舰"
text3 = "岩国陆战队航空站"
corrected_sent, detail = pycorrector.correct(text3)
print(corrected_sent, detail)



error_words_map = dict()
error_words_map['kc130'] = "KC-130"

# pycorrector.set_custom_confusion_path_or_dict(error_words_map)
pycorrector.set_custom_confusion_path_or_dict("./error_words")
corrected_sent, detail = pycorrector.correct("kc130为战斗机加油")
print(corrected_sent, detail)

corrected_sent, detail = pycorrector.correct("zg停靠尼米字号航空母舰")
print(corrected_sent, detail)

#  加载自己的错误词典
# import pycorrector

# error_sentences = [
#     '买iphonex，要多少钱',
#     '共同实际控制人萧华、霍荣铨、张旗康',
# ]
# for line in error_sentences:
#     print(pycorrector.correct(line))
#
# print('*' * 42)
# pycorrector.set_custom_confusion_path_or_dict('./my_custom_confusion.txt')
# for line in error_sentences:
#     print(pycorrector.correct(line))
#
#
#  训练自己的语言模型
#
# from pycorrector import Corrector
# import os
#
# pwd_path = os.path.abspath(os.path.dirname(__file__))
# lm_path = os.path.join(pwd_path, './people2014corpus_chars.klm')
# model = Corrector(language_model_path=lm_path)
#
# corrected_sent, detail = model.correct('少先队员因该为老人让坐')
# print(corrected_sent, detail)
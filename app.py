from flask import Flask,render_template,request

app = Flask(__name__)

def whoNotHere(data):
    student_list = []
    with open('input/学生名单_郑霞琴', 'r', encoding='utf-8') as f:
        text = f.readlines()
        for line in text:
            student_list.append(line.strip().replace(" ",""))

    # 没有接龙的孩子
    no_here_stu = []
    # 接龙多次的
    repeat_here_stu = []
    for student in student_list:
        # 取出名字
        name = student[-2:]
        if str(data).count(name) == 0:
            no_here_stu.append(student)
        if str(data).count(name) > 1:
            repeat_here_stu.append(student)

    result = ""
    if (len(no_here_stu) != 0 ):
        result = result + "没有接龙的孩子：<br>"
        for student in no_here_stu:
            result = result + student + "<br>"

    if (len(repeat_here_stu) != 0 ):
        result = result + "重复接龙的孩子：<br>"
        for student in repeat_here_stu:
            result = result + student + "<br>"

    return  result

@app.route('/',methods = ["GET","POST"])
def index():  # put application's code here
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        data = request.form.get("接龙文本")
        result = whoNotHere(data)
        return result


if __name__ == '__main__':
    app.run(debug=True)

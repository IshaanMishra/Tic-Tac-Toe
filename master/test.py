
import json
path=r"C:\Users\ishaa\Downloads\dev\Tic-Tac-Toe\master\test.json"
f=open(path)
data = json.load(f)


k=data['quiz']['maths']['q2']['question']
#quiz.maths.q2.question)
print(k)
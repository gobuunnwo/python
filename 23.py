# __init__メソッドは、インスタンスを生成した直後に処理を実行することができる。
# __init__メソッドは、「クラス名()」でインスタンスを生成した直後に自動で呼び出される。
# Planet()というインスタンスが作成されると、class Planet:def __init__(self):〜が実行される。
# name,~はインスタンス変数

# __init__メソッド
class Planet:
    def __init__(self):
        self.name="Earth"
        self.age=12345
        self.gravity=9.8
        self.number=23456

lohit=Planet()
print(f"This object is {lohit.name}")
print(f"This object is {lohit.age}")
print(f"This object is {lohit.gravity}")
print(f"This object is {lohit.number}")

mune=Planet()
print(f"This object is {mune.name}")
print(f"This object is {mune.age}")
print(f"This object is {mune.gravity}")
print(f"This object is {mune.number}")


try:
    1 / 1
except (ZeroDivisionError, TypeError) as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("没异常")
finally:
    print("一定执行")

# 异常来自于另一个ZeroDivisionError
# raise主动抛出异常
# assert只会抛出一个异常，调试作用
try:
    1/0
except:
    assert 1/2 <0
    raise ValueError("值不正确") from ZeroDivisionError



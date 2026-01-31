import logging
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print("cannot divide by zero")
    logging.error("ZeroDivisionError occurred")
except ValueError:
    print("invalid input! enter numbers only")
    logging.error("valueError occurred")
except Exception as e:
    print("unexpected error")
    logging.error("unexpected error:{e}")
else:
    print("calculation successfully")
finally:
    print("program finished")
try:
    x=int("abc")
except ValueError as e:
    print("simulated error")
    logging.error(f"simulated ValueError:{e}")
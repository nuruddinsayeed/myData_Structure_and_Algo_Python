try:
    file = open('decorators_function_log.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()
finally:
    print("process finished")
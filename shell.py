from modules import basic

while True:
    text = input('Stripe >>')
    print(text)
    result, error = basic.run(text)

    if error: print(error.as_string())
    else: print(result)
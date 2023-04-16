import base

while True:
    text = input('Stripe >>>  ')
    result, error = base.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)

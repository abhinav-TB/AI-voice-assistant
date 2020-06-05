import io
from base64 import b64encode
import eel

eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

eel.start('index.html', size=(1000, 600),debug=True)
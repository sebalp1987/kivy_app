import cv2
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import STRING


def predict_output(test):
    model = load_model('model.h5')
    test = [test]
    print(test)
    mushrooms = {'destroying_angel': 0, 'kantarell': 1, 'steinsopp': 2}
    poisson = STRING.poisson
    safe = STRING.safe
    info = STRING.explain_type

    X = []  # images
    nrows = 150
    ncolumns = 150
    print(test)
    for image in test:
        X.append(cv2.resize(cv2.imread(image, cv2.IMREAD_COLOR), (nrows, ncolumns), interpolation=cv2.INTER_CUBIC))

    X = np.array(X)
    print(X)
    datagen = ImageDataGenerator(rescale=1. / 255)

    prediction = model.predict(datagen.flow(X, batch_size=1))
    prediction = [item for sublist in prediction for item in sublist]
    pred_score = max(prediction)
    ind_max = np.argmax(prediction)
    type_m = ""
    danger = "[color=e9ff33]We did not find this mushroom in our database.[/color]"
    for key, val in mushrooms.items():
        if val == ind_max:
            type_m = key
            info = info.get(val)
            if type_m in poisson:
                danger = "[color=ff3333]Dangerous Mushroom[/color]"
            elif type_m in safe:
                danger = "[color=33ff36]Safe Mushroom[/color]"
            break

    return type_m + ' with probability ' + str(round(pred_score, 2)), danger, info

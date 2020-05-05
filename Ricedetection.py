
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

from PIL import Image
sys.modules['Image'] = Image 
from PIL import Image
print(Image.__file__)

#initializing the CNN
classifier = Sequential()

#convolution
classifier.add(Convolution2D(32,3,3, input_shape = (64,64,3), activation = 'relu'))

#pooling
classifier.add(MaxPool2D(pool_size=(2,2)))
#flattening
classifier.add(Flatten())
#fully connected input layer
classifier.add(Dense(output_dim = 128, activation = 'relu'))
#fully connected input layer
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))
classifier.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('train_set', target_size=(64, 64), batch_size=32, class_mode='binary')
test_set = train_datagen.flow_from_directory('test_set', target_size=(64, 64), batch_size=32, class_mode='binary')
classifier.fit_generator(training_set, samples_per_epoch=170, nb_epoch = 30, validation_data=test_set, nb_val_samples=60)
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('ricetest/testimage5.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'healthy'
else:
    prediction = 'disease'
print(prediction)

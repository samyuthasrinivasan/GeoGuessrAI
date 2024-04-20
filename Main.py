from AI import AI
from Perceptron import Perceptron
import geoguessingGraphics
# import Perceptron
# import AI
import cv2 as cv
import sys
import os
from zipfile import ZipFile
from geoguessingGraphics import Graphics


class Main():
  DIRECTORY_NAME = "FOLDER/"

  def create_perceptron(self, name, height, width):
    return Perceptron(name, height, width)

  def create_AI(self):
    return AI()

  # works hypothetically, need to test out with actual dataset
  def generate_dataset(self, folder, ai):
    DIRECTORY = self.DIRECTORY_NAME + folder
    list_of_metas = os.listdir(DIRECTORY)
    country_metas = {}
    list_of_perceptrons = []
    list_of_metas.remove(".DS_Store")
    for meta in list_of_metas:
      # ai.add_perceptron(folder.split('_')[0], self.create_perceptron(meta.split('_')[0]))
      list_of_imgs = []
      NEW_DIRECTORY = DIRECTORY + str(meta)
      files_in_folder = os.listdir(NEW_DIRECTORY)
      if ".DS_Store" in files_in_folder:
        files_in_folder.remove(".DS_Store")
      for f in files_in_folder:
        # sets rgb array from the file
        img = cv.imread(cv.samples.findFile(NEW_DIRECTORY + "/" + str(f)))
        sizes = str(meta).split("_")[1].split("x")
        img = cv.resize(img, (int(sizes[0]), int(sizes[1]))) # resizing
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # img = img[0:, 90:150] # cropping image
        # displays the image
        if img is None:
          sys.exit("Could not read the image.")

        list_of_imgs.append(img)

      height = int(meta.split('_')[1].split('x')[0])
      width = int(meta.split('_')[1].split('x')[1])
      per = self.create_perceptron(meta.split('_')[0], height, width)
      per.train(list_of_imgs, num_epochs=100, learning_rate=0.01)
      list_of_perceptrons.append(per)
      country_metas.update({meta.split('_')[0]: list_of_imgs})
    ai.add_perceptron(folder.split('/')[0], list_of_perceptrons)

    return country_metas
  

  # start here
main = Main()
ZIP_FILE = "FOLDER.zip"
COUNTRY_PATHS = ["SENEGAL/", "SPAIN/"]

# with ZipFile(ZIP_FILE, 'r') as zip:
#       zip.extractall()
#       print('Done')


ai = main.create_AI()

for country in COUNTRY_PATHS:
  dataset = main.generate_dataset(country, ai)

img = cv.imread(cv.samples.findFile("Picture1.jpeg"))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#img = cv.resize(img, (800, 2800))
prediction = ai.predict(img)[0]
print(prediction[1])

predicted_country = "NONE"
for country in COUNTRY_PATHS:
  list_of_metas = os.listdir("FOLDER/" + country)
  for meta in list_of_metas:
    if meta.split("_")[0] == prediction[0].get_name():
      predicted_country = country.split("/")[0]

print(predicted_country)
graphics = Graphics()
graphics.go(predicted_country)

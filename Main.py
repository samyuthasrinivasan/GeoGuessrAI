import geoguessingGraphics
import Perceptron
import AI
import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import os
from zipfile import ZipFile


class Main():
  DIRECTORY_NAME = "/content/FOLDER/"

  def create_perceptron(self, name, dataset):
    return Perceptron(name, dataset)

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
      DIRECTORY = DIRECTORY + str(meta)
      files_in_folder = os.listdir(DIRECTORY)
      if ".DS_Store" in files_in_folder:
        files_in_folder.remove(".DS_Store")
      for f in files_in_folder:
        # sets rgb array from the file
        img = cv.imread(cv.samples.findFile(DIRECTORY + "/" + str(f)))
        sizes = str(meta).split("_")[1].split("x")
        img = cv.resize(img, (int(sizes[0]), int(sizes[1]))) # resizing
        # img = img[0:, 90:150] # cropping image
        # displays the image
        if img is None:
          sys.exit("Could not read the image.")

        list_of_imgs.append(img)

      list_of_perceptrons.append(self.create_perceptron(meta.split('_')[0], list_of_imgs))
      country_metas.update({meta.split('_')[0]: list_of_imgs})
    ai.add_perceptron(folder.split('/')[0], list_of_perceptrons)

    return country_metas
  

  # start here
main = Main()
ZIP_FILE = "/content/FOLDER.zip"
COUNTRY_PATHS = ["COUNTRY/"]
META_PATHS = ["NAME_HXW/"]

with ZipFile(ZIP_FILE, 'r') as zip:
      zip.extractall()
      print('Done')

ai = main.create_AI()

for country in COUNTRY_PATHS:
  dataset = main.generate_dataset(country, ai)
  print(ai.get_dictionary())

prediction = ai.predict()

graphics = geoguessingGraphics()
graphics.go(prediction)
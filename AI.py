# import cv2

# for i in range(35):
#     #read image
#     original_image = cv2.imread(f"spain/bollard/BOLLARD#{i+1}.png")
#     newImage = cv2.resize(original_image, (100,200))
#     cv2.imwrite("BOLLARD#{i+1}.png", newImage)

class AI():

  def __init__(self):
    self.registeredCountries = {}

  def predict(self): # need to fix, for loop is looping through countries and is calling the method on the inner dictionary with the metas instead of singular metas
    list_of_tuples = []
    for country in self.registeredCountries:
      for dict_meta in self.registeredCountries.get(country):
        for meta in self.registeredCountries.get(country).get(dict_meta):
          list_of_tuples.append(tuple(dict_meta, meta.get_confidence()))

    return list_of_tuples

  def add_perceptron(self, country, perceptron):
    self.registeredCountries.update({country: perceptron})

  def get_dictionary(self):
    return self.registeredCountries

from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from playsound import playsound

class Another(Exception):
    pass
print("SEE THE IMAGE AND GIVE CONNECTIONS TO THE COMPONENT AND CHECK THE APPROPRIATE VALUES")
while True:
    try:
        prompt=input("Enter the test on (DC Machine or Transformer): ")
        if prompt[0]=="T" or prompt[0]=="t":
            image = mpimg.imread("Screenshot 2023-12-18 221926.png")
            plt.imshow(image)
            plt.show()    
            import transformer
        elif prompt[0]=="D" or prompt[0]=="d":
            image = mpimg.imread("image.jpg")
            plt.imshow(image)
            plt.show()
            import MOTORs
        else:
            raise Another
    except Another:
        print("Enter valid input only")
from PIL import Image, ImageColor
#from IPython.display import display

#image = Image.new(mode="RGB", size=(10,10), color="black")
image= Image.open("../data/dog.jpg")
#image(copy) = Image.open("path")
#w,h=image.size
#copyaccess=image.load()
#image.show()
#image.save(name,format="png")
#img_map=list(image.getdata())
#pix_col=ImageColor.getrgb(a) rgb values of passed color
print(bin(10))

def CanbeHidden(h,w,h2,w2):
    if h*w >= 4*h2*w2:
        return 1
    else:
        return 0
with Image.open("../data/x.png") as image:
    access=image.load()
    secret=Image.open("../data/dog.jpg")
    secretaccess=secret.load()
    maskw,maskh=image.size
    secretw,secreth=secret.size
    print(secret.size)
    image.show()
    secret.show()
    if CanbeHidden(maskh,maskw,secreth,secretw):
        print("Can be hidden")
        for color in range(3):
            for ki in range(secretw):
                for j in range(secreth):
                    #print(ki,j)
                    bincolor=bin(secretaccess[(ki,j)][color]).strip('0b')
                    bincolor=(8-len(bincolor))*'0'+bincolor
                    pixelnum=j*secretw+ki
                    pixelnum*=4
                    for i in range(4):
                        row=pixelnum//maskw
                        col=pixelnum%maskw
                        pixelnum+=1
                        tupl=list(access[(col,row)])
                        colorvalue=bin(tupl[color]).strip('0b')
                        colorvalue=(8-len(colorvalue))*'0'+colorvalue
                        colorvalue=colorvalue[0:6]+bincolor[2*i:2*i+2]
                        tupl[color]=int(colorvalue,2)
                        tupl=tuple(tupl)
                        access[(col,row)]=tupl
        image.save('out',format="png")
        image.show()           
    else:
        print("Sizes do not match, can't be hidden")
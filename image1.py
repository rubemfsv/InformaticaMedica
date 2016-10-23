import cv2
import decimal
import math

#Nao foram considerados no calculo os pixels pretos ja que o objetivo era apenas analisar o tumor
#Devem ser criados dois arquivos txt para armazenar os resultados e colocados os seus devidos caminhos

rows = cols = 0
grayColors = 140

def ReadImage():
    dados = open('C:\\Users\\Eduarda\\Desktop\\Telemedicina\\Nodulo segmentado\\dados.txt','w')
    image = cv2.imread("C:\\Users\\Eduarda\\Desktop\\Telemedicina\\Nodulo segmentado\\nodulo19.png")
    quant = 0
    grayScale = []
    global rows
    global cols
    rows = image.shape[0]
    cols = image.shape[1]
    for row in range(rows):
        grayScaleC = []
        for col in range(cols):
            pixel = image[row][col]
            (r, g, b) = pixel.tolist()                
            gray = (0.3*r)+(0.59*g)+(0.11*b)
            gray = int(gray)
            if r != 0 or g != 0 or b != 0:                
                gray = (0.3*r)+(0.59*g)+(0.11*b)
                grayScaleC.append(gray)
                dados.writelines(str(row))
                dados.writelines("  ")
                dados.writelines(str(col))
                dados.writelines(" GrayScale: ")
                dados.writelines(str(gray))
                dados.writelines("\n")
                image[row,col] = (255,0,0)                  
                quant=quant+1
            else:
                grayScaleC.append(0)
        grayScale.append(grayScaleC)
    dados.close()    
    cv2.imshow("Segmento da imagem analisado", image)
    cv2.imwrite("newImage.png", image)
    cv2.waitKey(0)
    return grayScale

def GLCM(grayScale):
    glcm = [] 
    global grayColors
    global rows
    global cols
    for i in range(grayColors):
        glcmC = []
        for j in range(grayColors):
            glcmC.append(0)
        glcm.append(glcmC)
    for i in range(rows):
        for j in range(cols-1):
            if grayScale[i][j]!=0 and grayScale[i][j+1]!=0:
                glcm[int(grayScale[i][j])-1][int(grayScale[i][j+1])-1] = glcm[int(grayScale[i][j])-1][int(grayScale[i][j+1])-1] + 1    
    return glcm

def histogramIntensity(grayScale):
    histogram = []
    global rows
    for i in range(rows):
        histogram.append(0)
    for i in range(rows):
        for j in range(cols):
            if int(grayScale[i][j]) != 0 :
                histogram[int(grayScale[i][j])] = histogram[int(grayScale[i][j])] + 1
    return histogram    

def grayScaleNormalized(glcm):
    global grayColors
    for i in range(grayColors):
        for j in range(grayColors):
            glcm[i][j] = decimal.Decimal(glcm[i][j])/decimal.Decimal(grayColors)
    return glcm

def angularSecondMoment(glcm):
    glcmNormalized = grayScaleNormalized(glcm)
    angular = 0
    global grayColors
    for i in range(grayColors):
        for j in range(grayColors):
            angular = angular + (glcmNormalized[i][j]*glcmNormalized[i][j])
    return angular

def  sumMean(glcm):
    global grayColors
    sumAux = 0
    for i in range(grayColors):
        for j in range(grayColors):
            sumAux = sumAux + ((i+j)*glcm[i][j])
    return sumAux

def maximumProbability(glcm):
    maxValue = 0
    global grayColors
    for i in range(grayColors):
        for j in range(grayColors):
            if(glcm[i][j]>maxValue):
                maxValue = glcm[i][j]
    return maxValue   

def mean(histogram):
    meanValue = 0
    global rows
    for i in range(rows):
        meanValue = meanValue + (i*histogram[i])
    return meanValue 

def energy(histogram):
    energyValue = 0
    global rows
    for i in range(rows):
        energyValue = energyValue + (histogram[i]**2)
    return energyValue

def entropy(histogram):
    entropyValue = 0
    global rows
    for i in range(rows):
        entropyValue = entropyValue + (histogram[i]*math.log1p(histogram[i]))
    entropyValue = entropyValue*(-1)
    return entropyValue

def kurtosis(histogram):
    kValue = aux1 = aux2 = 0
    fMean = mean(histogram) 
    global rows
    for i in range(rows):
        aux1 = aux1 + (((i - fMean)**4)*histogram[i])
    for i in range(rows):
        aux2 = aux2 +(((i - fMean)**2)*histogram[i])
    kValue = decimal.Decimal(aux1)/((decimal.Decimal(aux2))**2)
    return kValue
    
#Open the file
results = open('C:\\Users\\Eduarda\\Desktop\\Telemedicina\\Nodulo segmentado\\results.txt','w')

#Funcoes com a matriz de concorrencia

grayScale = ReadImage()  
glcm = GLCM(grayScale)
glcm = grayScaleNormalized(glcm)

#Angular Second Moment
ASM = angularSecondMoment(glcm)
results.writelines("Angular Second Moment: ")
results.writelines(str(ASM))
results.writelines("\n")

#Sum Mean
SumMeanValue = sumMean(glcm)
results.writelines("Sum Mean: ")
results.writelines(str(SumMeanValue))
results.writelines("\n")

#Maximal Probability
maximal = maximumProbability(glcm)
results.writelines("Maximal Probability: ")
results.writelines(str(maximal))
results.writelines("\n")


#Funcoes com o histograma de intensidade
histogram = histogramIntensity(grayScale)

#Mean
meanValue = mean(histogram)
results.writelines("Mean: ")
results.writelines(str(meanValue))
results.writelines("\n")

#Energy
energyValue = energy(histogram)
results.writelines("Energy: ")
results.writelines(str(energyValue))
results.writelines("\n")

#Entropy
entropyValue = entropy(histogram)
results.writelines("Entropy: ")
results.writelines(str(entropyValue))
results.writelines("\n")

#Kurtosis
kurtosisValue = kurtosis(histogram)
results.writelines("Kurtosis: ")
results.writelines(str(kurtosisValue))
results.writelines("\n")










         

    

    

import cv2
import codecs 

def render(fileName,XScale,YScale):
    color = ['赢','要','静','餐','餐','愿','性','命','元','爱','亲','龙','厅','三','二','一','一']
    base = cv2.imread(fileName,cv2.IMREAD_GRAYSCALE)
    img = cv2.resize( base,( int(base.shape[0]*XScale) , int(base.shape[1]*YScale) ) )
    Y = []
    for y in range(0,img.shape[1]):
        X = []
        for x in range(0,img.shape[0]):
            a = img[x,y]//15-1
            if ( a == -1 ):
                a = 0
            X.append(color[a])
        Y.append(X)
    return Y

import numpy as np
import math


def oteleme(d,h,l,x,y,z):
    matrix1 = np.array([[1, 0, 0, d], [0, 1, 0, h], [0, 0, 1,l],[0,0,0,1]])
    matrix2 = np.array([x,y,z,1])
    result = np.dot(matrix1, matrix2)
    print("Oteleme Sonucu : " + str(result))
    return result

def olcekleme(d,h,l,x,y,z):
    matrix1 = np.array([[d, 0, 0, 0], [0, h, 0, 0], [0, 0, l,0],[0,0,0,1]])
    matrix2 = np.array([x,y,z,1])
    result = np.dot(matrix1, matrix2)
    print("Oteleme Sonucu : " + str(result))
    return result

def dondurmeZ(angle,x,y,z):
    matrix1 = np.array([[math.cos(angle), -math.sin(angle), 0, 0], [math.sin(angle), math.cos(angle), 0, 0], [0, 0, 1,0],[0,0,0,1]])
    matrix2 = np.array([x,y,z,1])
    result = np.dot(matrix1, matrix2)
    print("Oteleme Sonucu : " + str(result))
    return result

def dondurmeY(angle,x,y,z):
    matrix1 = np.array([[math.cos(angle), 0, math.sin(angle), 0], [0, 1, 0, 0], [-math.sin(angle), 0, math.cos(angle),0],[0,0,0,1]])
    matrix2 = np.array([x,y,z,1])
    result = np.dot(matrix1, matrix2)
    print("Oteleme Sonucu : " + str(result))
    return result

def dondurmeX(angle,x,y,z):
    matrix1 = np.array([[1,0,0,0], [0,math.cos(angle),-math.sin(angle),0], [0,math.sin(angle),math.cos(angle),0],[0,0,0,1]])
    matrix2 = np.array([x,y,z,1])
    result = np.dot(matrix1, matrix2)
    print("Oteleme Sonucu : " + str(result))
    return result

araDeger = oteleme(5,1,2,1,2,3)
olcekleme(5,1,2,araDeger[0],araDeger[1],araDeger[2])
dondurmeZ(90,15,24,1)


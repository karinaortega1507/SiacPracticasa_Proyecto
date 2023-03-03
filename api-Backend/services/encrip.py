# #import sys
# #sys.path.append(r'C:\path\to\clr') 
# Reemplaza la ruta con la ruta de acceso real al módulo clr
# #import clr

# import ctypes

# # Carga la DLL
# dll = ctypes.cdll.LoadLibrary("E:/DOCUMENTOS/DIGOTEC/projects/WorkSpace/Veltrix_React_v4.2.0/Admin/api-Backend/services/SiacWebDll.dll")

# #encrip (”c¥¥aneE",'D')
# #encrip(p_usrcodigo,'E')
# # Define la firma de la función en Python
# encripf = dll.classGeneral
# encripf.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
# encripf.restype = ctypes.c_char_p

# # Usa la función en Python
# texto = "prueba"
# texto_encriptado = encripf(texto.encode(), b"E").decode()
# texto_desencriptado = encripf(texto_encriptado.encode(), b"D").decode()
# print(texto_encriptado)  # Imprime el texto encriptado
# print(texto_desencriptado)  # Imprime el texto desencriptado 
################################################################################################################################
# import ctypes

# # Carga la biblioteca DLL utilizando ctypes
# dll = ctypes.WinDLL('E:/DOCUMENTOS/DIGOTEC/projects/WorkSpace/Veltrix_React_v4.2.0/Admin/api-Backend/services/SiacWebDll.dll')

# # Obtiene una referencia a la clase ClassGeneral
# class_general = getattr(dll, 'ClassGeneral')

# # Obtiene una referencia a la función Encrip
# encrip = getattr(class_general, 'Encrip')

# # Define los tipos de datos de los argumentos y el valor de retorno
# encrip.argtypes = [ctypes.c_char_p, ctypes.c_char]
# encrip.restype = ctypes.c_char_p

# # Ejemplo de uso
# texto = 'Hola mundo'
# sProceso = b'E'
# texto_encriptado = encrip(texto.encode(), sProceso)
# print(texto_encriptado.decode())
####################################################################################################################
# from ctypes import *

# import sys

# import os

# import clr

# sys.path.append(r"C:\RIchard\Digotec\CLIENTES\FutureSoft\SiacWebDll.dll")
# clr.AddReference(r"C:\RIchard\Digotec\CLIENTES\FutureSoft\SiacWebDll.dll")
# from SiacWebDLL import ClassGeneral
# obj = ClassGeneral()
# print(obj.encrip('1', 'E'))
###########################################################################
import clr
clr.AddReference ('SiacWebDll')
clr.AddReference ('Microsoft.VisualBasic')

from System import Activador
from SiacWebDll import ClassGeneral

classGeneraltype = clr.GetClrType(ClassGeneral)
obj = Activador.CreateInstance(classGeneraltype)

encriptado = obj.Encrip("fsbs","E")

print(encriptado)
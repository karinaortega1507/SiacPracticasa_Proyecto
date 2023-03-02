#import sys
#sys.path.append(r'C:\path\to\clr') # Reemplaza la ruta con la ruta de acceso real al módulo clr
#import clr

import ctypes

# Carga la DLL
dll = ctypes.cdll.LoadLibrary("E:/DOCUMENTOS/DIGOTEC/projects/WorkSpace/Veltrix_React_v4.2.0/Admin/api-Backend/services/SiacWebDll.dll")

#encrip (”c¥¥aneE",'D')
#encrip(p_usrcodigo,'E')
# Define la firma de la función en Python
encripf = dll.classGeneral
encripf.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
encripf.restype = ctypes.c_char_p

# Usa la función en Python
texto = "prueba"
texto_encriptado = encripf(texto.encode(), b"E").decode()
texto_desencriptado = encripf(texto_encriptado.encode(), b"D").decode()
print(texto_encriptado)  # Imprime el texto encriptado
print(texto_desencriptado)  # Imprime el texto desencriptado


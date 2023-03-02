import ctypes

# Carga la biblioteca DLL utilizando ctypes
dll = ctypes.WinDLL('E:/DOCUMENTOS/DIGOTEC/projects/WorkSpace/Veltrix_React_v4.2.0/Admin/api-Backend/services/SiacWebDll.dll')

# Obtiene una referencia a la clase ClassGeneral
class_general = getattr(dll, 'ClassGeneral')

# Obtiene una referencia a la función Encrip
encrip = getattr(class_general, 'Encrip')

# Define los tipos de datos de los argumentos y el valor de retorno
encrip.argtypes = [ctypes.c_char_p, ctypes.c_char]
encrip.restype = ctypes.c_char_p

# Ejemplo de uso
texto = 'Hola mundo'
sProceso = b'E'
texto_encriptado = encrip(texto.encode(), sProceso)
print(texto_encriptado.decode())

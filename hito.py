
class Registro:
    def __init__(self, nombre, apellidos, pais, numero):
        self.validar_nombre(nombre)
        self.validar_apellidos(apellidos)
        self.validar_pais(pais)
        self.validar_numero(numero)

        self.nombre = nombre
        self.apellidos = apellidos
        self.pais = pais
        self.numero = numero
        self.carrito = Carrito()
    print('hola, registrate para acceder a nuestra tienda')
    def validar_nombre(self, nombre):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena no vacía.")

    def validar_apellidos(self, apellidos):
        if not apellidos or not isinstance(apellidos, str):
            raise ValueError("Los apellidos deben ser una cadena no vacía.")

    def validar_pais(self, pais):
        if not pais or not isinstance(pais, str):
            raise ValueError("El país debe ser una cadena no vacía.")

    def validar_numero(self, numero):
        if not (numero.isdigit() and len(numero) == 9):
            raise ValueError("Debe introducir un número de 9 dígitos.")

    def agregar_al_carrito(self, producto, precio):
        self.carrito.agregar_producto(producto, precio)

    def mostrar_carrito(self):
        self.carrito.mostrar_carrito()

    def realizar_pago(self):
        metodo_pago = input("Seleccione el método de pago (visa, mastercard): ")

        if metodo_pago.lower() == 'visa':
            numero_tarjeta = input("Ingrese el número de tarjeta: ")
            print("Procesando pago con tarjeta...")

            try:
                ValidadorTarjeta.validar_numero(numero_tarjeta)
                print("Pago realizado con tarjeta.")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif metodo_pago.lower() == 'mastercard':
            numero_tarjeta = input("Ingrese el número de tarjeta: ")
            print("Procesando pago con tarjeta...")

            try:
                ValidadorTarjeta.validar_numero(numero_tarjeta)
                print("Pago realizado con tarjeta.")
            except ValueError as e:
                print(f"Error: {str(e)}")

        else:
            print("Método de pago no válido. Por favor, seleccione 'visa' o 'mastercard'.")


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, precio):
        self.productos.append({'producto': producto, 'precio': precio})

    def mostrar_carrito(self):
        print("Contenido del carrito:")
        for item in self.productos:
            producto = item['producto']
            precio = item['precio']
            print(f"{producto} - Precio: ${precio:.2f}")


        total = sum(item['precio'] for item in self.productos)
        print(f"subtotal a pagar: ${total:.2f}")
        if pais == 'españa':
            total *= 1.21
        else:
            total *= 1.15
        print(f'total con impuestos incluidos {total:.2f}')

class ValidadorTarjeta:
    @staticmethod
    def validar_numero(numero_tarjeta):
        if not numero_tarjeta.isdigit() or len(numero_tarjeta) != 16:
            raise ValueError("Número de tarjeta inválido. Debe tener 16 dígitos.")
        else:
            print('numero correcto')




class Seguimiento:
    def __init__(self):
        self.enviar_sms = None
        self.enviar_correo=None
    def solicitar_envio_sms(self):
        respuesta = input("¿Quieres que te enviemos un SMS? (si/no): ")
        if respuesta.lower() == 'si':
            self.enviar_sms = True
            print("SMS enviado.")
        elif respuesta.lower() == 'no':
            self.enviar_sms = False
            print("No se enviará SMS.")
        else:
            print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")

    def solicitar_correo(self):
        respuesta = input("¿Quieres que te enviemos un correo? (si/no): ")
        if respuesta.lower() == 'si':
            self.enviar_correo = True
            print("correo enviado.")
        elif respuesta.lower() == 'no':
            self.enviar_correo = False
            print("No se enviará correo electronico.")
        else:
            print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")




productos = {
    'camiseta': 10.90,
    'pantalon': 29.99,
    'zapatillas': 109.99
}


nombre = input('Escriba su nombre: ')
apellidos = input('Escriba su apellido: ')
pais = input('¿Cuál es su país?: ')
numero = input('¿Cuál es su número de teléfono?: ')

try:
    usuario1 = Registro(nombre, apellidos, pais, numero)
    print("Registro exitoso.")
    print(f'Bienvenido a nuestra tienda, {usuario1.nombre}')


    print("\nProductos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto} - Precio: ${precio:.2f}")


    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == 'salir':
            break
        try:

            precio = productos[producto]
            usuario1.agregar_al_carrito(producto, precio)
        except KeyError:
            print("Error: Producto no válido.")

    usuario1.mostrar_carrito()
    usuario1.realizar_pago()
    seguimiento_usuario = Seguimiento()
    seguimiento_usuario.solicitar_envio_sms()
    seguimiento_usuario.solicitar_correo()


except ValueError as e:
    print(f"Error : {str(e)}")



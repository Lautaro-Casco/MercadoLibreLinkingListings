# Roadmap de Sincronización de Stock en Mercado Libre

## 1. Introducción
- **Objetivo:** Desarrollar una aplicación en Python que sincronice el stock de dos publicaciones existentes en Mercado Libre, creadas manualmente, utilizando la API de Mercado Libre.
- **Funcionalidad clave:** Detectar cambios en el stock de cualquiera de las publicaciones y actualizar la otra para mantener la sincronización en tiempo real, permitiendo que ambas publicaciones reflejen el mismo stock a pesar de ofrecer diferentes medios de pago o condiciones (por ejemplo, una con cuotas y otra sin cuotas).

## 2. Requisitos Previos
- Conocimientos básicos de Python y manejo de APIs.
- Ambiente de desarrollo configurado (Python 3.x, IDE o editor de código).
- Credenciales de acceso a la API de Mercado Libre: Client ID, Client Secret, Token de Acceso y Token de Refresco.
- IDs de las dos publicaciones ya existentes en Mercado Libre que se desean sincronizar.

## 3. Registro en Mercado Libre Developers
- Crear una cuenta en [Mercado Libre Developers](https://developers.mercadolibre.com.ar).
- Registrar una aplicación para obtener:
  - Client ID
  - Client Secret
  - Redirection URI
- Seguir el flujo OAuth 2.0 para generar el Token de Acceso y el Token de Refresco.

## 4. Configuración del Entorno
- Crear y activar un entorno virtual en Python.
- Instalar las bibliotecas requeridas, tales como:
  - `requests` para realizar peticiones HTTP.
  - (Opcional) `python-dotenv` para gestionar variables de entorno.

Ejemplo de comandos:
python -m venv env source env/bin/activate pip install requests python-dotenv
## 5. Estructura del Proyecto

## 6. Implementación del Script

### 6.1. Autorización y Conexión a la API
- Implementar el flujo OAuth 2.0 usando las credenciales para obtener y refrescar el token de acceso.
- Crear funciones en `ml_api.py` para:
  - Obtener el stock actual de una publicación (método GET).
  - Actualizar el stock de una publicación (método PUT o PATCH) en función de los cambios detectados.

### 6.2. Lógica de Sincronización de Stock
- Leer el stock actual de ambas publicaciones existentes (usando sus IDs definidos en el archivo de configuración o variables de entorno).
- Comparar los valores de stock para identificar ventas o cambios en cualquiera de las publicaciones.
- Calcular el stock central (valor actualizado después de una venta o ajuste) y actualizar ambas publicaciones en consecuencia.
- Implementar manejo de errores y registrar logs para monitorear las actualizaciones y detectar problemas.

### 6.3. Ciclo de Ejecución
- Diseñar el script para que ejecute la sincronización a intervalos definidos (por ejemplo, cada pocos minutos).
- Opcional: Configurar el script para que funcione como un servicio o tarea programada (por ejemplo, con cron en Linux o el Programador de tareas en Windows) para asegurar la ejecución continua.

## 7. Pruebas y Validación
- Probar cada función individualmente:
  - Verificar que la obtención del stock desde la API funcione correctamente.
  - Confirmar que la actualización de stock en cada publicación se realiza de forma efectiva.
- Realizar pruebas de integración para asegurar que la sincronización completa entre las dos publicaciones funcione sin inconvenientes.
- Agregar manejo de excepciones y mensajes de error para poder identificar y resolver problemas durante la ejecución.

## 8. Despliegue
- Alojar el script en un servidor o utilizar un servicio en la nube para ejecutar el proceso de sincronización de manera continua.
- Implementar mecanismos de monitoreo y registro (logs) para verificar el correcto funcionamiento en producción.
- Realizar pruebas en un ambiente de producción controlado con bajo volumen de ventas antes de escalar.

## 9. Mantenimiento y Futuras Mejoras
- Monitorear cambios en la API de Mercado Libre y actualizar el script según sea necesario.
- Incorporar un sistema de alertas para detectar desviaciones o fallos en la sincronización.
- Explorar la posibilidad de agregar una interfaz gráfica o notificaciones para facilitar la supervisión manual y la administración del proceso.

## Lab 1.1: Directorio telefónico con clases, listas y ciccionarios

## Objetivo:

Desarrollar un directorio telefónico utilizando clases para representar los contactos, listas para almacenarlos y diccionarios para optimizar las búsquedas. El programa debe permitir agregar, buscar, eliminar y mostrar contactos, además de incluir validaciones y persistencia de datos.

## Requerimientos

1. Clase ```Contacto```:

    * ```Atributos```: Nombre, Teléfono, Cumpleaños, Correo.

    * ```Métodos```: ```__str__``` para mostrar la información del contacto.

2. Clase Directorio:

    * ```Atributos```:

        * Una lista para almacenar objetos de la clase Contacto.

        * Un diccionario para indexar los contactos por número de teléfono.

    * ```Métodos```:

        * ```agregar_contacto```: Agrega un nuevo contacto.

        * ```buscar_por_telefono```: Busca un contacto por número de teléfono.

        * ```eliminar_contacto```: Elimina un contacto por número de teléfono.

        * ```mostrar_contactos```: Muestra todos los contactos ordenados por nombre.

        * ```guardar_datos```: Guarda los contactos en un archivo ```JSON``` o ```csv```.

        * ```cargar_datos```: Carga los contactos desde un archivo ```JSON``` o ```csv```.

3. Validaciones:

    * Validar que el número de teléfono tenga 10 dígitos.

    * Validar que el correo electrónico tenga un formato válido.

4. Persistencia de datos: Guardar y cargar los contactos en un archivo ```JSON``` o ```csv```.

## Pasos a Seguir
1. Crear la Clase ```Contacto```:

    * Define una clase llamada Contacto con los siguientes atributos:

        * nombre: Nombre y apellido del contacto.

        * telefono: Número de teléfono del contacto.

        * cumpleanos: Fecha de cumpleaños del contacto.

        * correo: Correo electrónico del contacto.

    * Implementa el método ```__str__``` para mostrar la información del contacto de manera formateada.

2. Crear la Clase ```Directorio```:

    * Define una clase llamada ```Directorio``` con los siguientes atributos:

        * ```contactos```: Una lista para almacenar objetos de la clase Contacto.

        * ```indice_telefonos```: Un diccionario para indexar los contactos por número de teléfono.

    * Implementa los siguientes métodos:

        * ```agregar_contacto```: Agrega un nuevo contacto a la lista y al diccionario.

        * ```buscar_por_telefono```: Busca un contacto por número de teléfono usando el diccionario.

        * ```eliminar_contacto```: Elimina un contacto de la lista y del diccionario.

        * ```mostrar_contactos```: Muestra todos los contactos ordenados por nombre.

        * ```guardar_datos```: Guarda los contactos en un archivo ```JSON``` o ```csv```.

        * ```cargar_datos```: Carga los contactos desde un archivo ```JSON``` o ```csv```.

3. Implementar Validaciones

    * Crea funciones para validar el número de teléfono y el correo electrónico:

      * ```validar_telefono```: Verifica que el número de teléfono tenga 10 dígitos.

      * ```validar_correo```: Verifica que el correo electrónico tenga un formato válido.

    * Usa estas funciones en el método ```agregar_contacto``` para asegurar que los datos ingresados sean correctos.

4. Implementar Persistencia de Datos

    * En el método ```guardar_datos```, convierte la lista de contactos en un formato ```JSON``` o ```csv``` y guárdala en un archivo.

    * En el método ```cargar_datos```, carga los contactos desde un archivo ```JSON``` o ```csv``` y reconstruye la lista y el diccionario.

5. Crear la Interfaz de Usuario

    * Implementa un menú interactivo que permita al usuario realizar las siguientes operaciones:

        * Agregar un nuevo contacto.

        * Buscar un contacto por teléfono.

        * Eliminar un contacto.

        * Mostrar todos los contactos.

        * Guardar datos.

        * Cargar datos.

        * Salir.

    * Usa un bucle ```while``` para mantener el programa en ejecución hasta que el usuario elija la opción de salir.

6. Pruebas y Depuración

    * Prueba el programa con diferentes casos de uso:

        * Agregar contactos con datos válidos e inválidos.

        * Buscar contactos existentes y no existentes.

        * Eliminar contactos.

        * Guardar y cargar datos.

    * Depura los errores que encuentres durante las pruebas.

## Actividades

  1. Diseño de clases: Definir las clases ```Contacto``` y ```Directorio``` con sus atributos y métodos.

  2. Implementación de métodos: Implementar los métodos de la clase ```Directorio``` para gestionar los contactos.

  3. Validaciones: Implementar las funciones de validación y úsalas en el método agregar_contacto.

  4. Persistencia de datos: Implementar los métodos ```guardar_datos``` y ```cargar_datos```.

  5. Interfaz de Usuario: Crear un menú interactivo para que el usuario pueda usar el directorio.

  6. Pruebas: Probar todas las funcionalidades del programa y corrige los errores.

## Entregables

  1. Código fuente: SUbir al repositorio el archivo ```Python``` con el código completo del programa.

  2. Documentación: En el respectivo ```README.md``` de **Github Classroom** escribir un breve informe describiendo las funcionalidades implementadas y los desafíos encontrados.

  


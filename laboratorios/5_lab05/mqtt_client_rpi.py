import paho.mqtt.client as mqtt
import time

# Configuración
broker = "192.168.1.100"  # Reemplaza con la IP del broker MQTT
puerto = 1883
topic_out = "output/hola"
topic_in = "input/hola"

# Callback cuando se recibe un mensaje
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en '{msg.topic}': {msg.payload.decode()}")

# Crear cliente MQTT
cliente = mqtt.Client()

# Asignar función de recepción
cliente.on_message = on_message

# Conectar al broker
cliente.connect(broker, puerto, 60)

# Suscribirse al tópico de escucha
cliente.subscribe(topic_in)

# Iniciar recepción en segundo plano
cliente.loop_start()

# Publicar en el tópico de envío
cliente.publish(topic_out, "Hola desde el cliente")
print(f"Mensaje enviado a '{topic_out}'")

# Esperar recepción
time.sleep(5)

# Detener y cerrar conexión
cliente.loop_stop()
cliente.disconnect()

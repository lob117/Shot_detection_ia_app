# 🎯 Interfaz del Sistema de Detección de Disparos y Red de Sensores

![Estado](https://img.shields.io/badge/Estado-Activo-success)
![Hardware](https://img.shields.io/badge/Hardware-ESP32-blue)
![Red](https://img.shields.io/badge/Protocolo-UDP-orange)
![Modelo](https://img.shields.io/badge/AI-CRNN-yellow)

Este documento describe la estructura, componentes y arquitectura de interconectividad de la interfaz de usuario diseñada para el monitoreo de un sistema distribuido de detección de disparos, basado en módulos de captura de audio y un modelo **CRNN** (*Convolutional Recurrent Neural Network*).

---

## 📑 Tabla de Contenidos
1. [Arquitectura del Ecosistema e Integración](#-arquitectura-del-ecosistema-e-integración)
2. [Representación del Entorno y Estado de los Sensores](#-representación-del-entorno-y-estado-de-los-sensores)
3. [Panel de Control: Monitoreo en Tiempo Real](#-panel-de-control-monitoreo-en-tiempo-real)
4. [Configuraciones: Ajustes del Sistema](#-configuraciones-ajustes-del-sistema-y-seguimiento-de-estado)
5. [Arquitectura de Conectividad y Procesamiento Multihilo](#-arquitectura-de-conectividad-y-procesamiento-multihilo)

---

## 🚀 Arquitectura del Ecosistema e Integración

El sistema opera mediante la orquestación de tres componentes fundamentales. La ejecución principal se gestiona desde el archivo **`main.py`**, el cual centraliza la recepción de datos y la inferencia.

Este proyecto integra y depende de los siguientes repositorios especializados:

1.  **🧠 Núcleo de Inteligencia Artificial:**
    * **Repositorio:** [Red Neuronal Detección de Disparos UNIMAGDALENA](https://github.com/devhuday/Red_neuronal_deteccion_de_disparos_UNIMAGDALENA/tree/main/Tesis%20IA)
    * **Función:** Proporciona la arquitectura de la red **CRNN** y los pesos entrenados para la clasificación de eventos acústicos.
2.  **🎙️ Captura de Audio de Alta Precisión:**
    * **Repositorio:** [ESP32 Mic INMP441](https://github.com/lob117/esp32_mic_inmp441)
    * **Función:** Proporciona el firmware base para los módulos sensores. Gestiona la configuración del protocolo I2S y la transmisión UDP de baja latencia necesaria para el streaming de audio.

**Flujo de Ejecución:**
Para iniciar el sistema de monitoreo, asegúrese de que los módulos ESP32 estén transmitiendo y ejecute: main.py

## 📑 Tabla de Contenidos
1. [Representación del Entorno y Estado de los Sensores](#-representación-del-entorno-y-estado-de-los-sensores)
2. [Panel de Control: Monitoreo en Tiempo Real](#-panel-de-control-monitoreo-en-tiempo-real)
3. [Configuraciones: Ajustes del Sistema](#-configuraciones-ajustes-del-sistema-y-seguimiento-de-estado)
4. [Arquitectura de Conectividad y Procesamiento Multihilo](#-arquitectura-de-conectividad-y-procesamiento-multihilo)

---

## 🗺️ Representación del Entorno y Estado de los Sensores

El entorno físico de monitoreo se visualiza mediante una cuadrícula o sistema de coordenadas bidimensional, permitiendo ubicar espacialmente cada módulo de forma precisa.

### Estados Visuales de los Nodos:
* ⚪ **INACTIVO (Desconectado):** Leyenda indicando falta de conexión; representación gráfica en color **gris**.
* **ACTIVO (Conectado):** Leyenda de conexión establecida. Adopta un color identificativo único por nodo:
    * 🟢 **Sensor 1:** Verde
    * 🟣 **Sensor 2:** Morado
    * 🔵 **Sensor 3:** Azul
* 🔴 **DETECCIÓN:** Al registrarse un evento clasificado como disparo, el indicador visual del sensor cambia inmediatamente a color **rojo**.
<img width="1917" height="902" alt="Captura de pantalla 2025-05-13 224441" src="https://github.com/user-attachments/assets/1d3ea224-4986-4430-8100-39e1bfaa5354" />

---

## 📊 Panel de Control: Monitoreo en Tiempo Real

Esta sección gestiona la sincronización de los módulos y la presentación de los resultados del análisis acústico (*Referencia: Figura 21*).

* 🎙️ **Recolección de Datos:** Cada módulo recolecta ventanas de datos de audio de **4 segundos** antes de enviarlos para su inferencia en la red neuronal.
* 🧠 **Evaluación del Modelo CRNN:** Los resultados de cada registro de audio se clasifican en dos posibles estados:
    * `¡ALERTA!` (Disparo detectado)
    * `Normal`
* 📈 **Probabilidades de Predicción:** El sistema expone la probabilidad matemática asociada a cada evaluación para medir el nivel de certeza del modelo.
* 📜 **Historial de Eventos:** Se mantiene un registro continuo por cada sensor que facilita la auditoría del sistema, incluyendo:
    * Marca de tiempo exacta (*Timestamp*)
    * Resultado de la detección
    * Probabilidad asociada
<img width="1919" height="992" alt="Captura de pantalla 2025-05-13 224457" src="https://github.com/user-attachments/assets/a8c8f878-5cff-484f-98ed-480da0180ce0" />

---

## ⚙️ Configuraciones: Ajustes del Sistema y Seguimiento de Estado

Interfaz diseñada para brindar un control granular sobre los parámetros operativos de la red y el modelo predictivo (*Referencia: Figura 22*).

| Funcionalidad | Descripción |
| :--- | :--- |
| **Umbral de Probabilidad** | Input numérico (0 a 1) que ajusta la sensibilidad del sistema. Define la probabilidad mínima requerida para disparar una alerta. |
| **Timeout del Sensor** | Límite de espera (en segundos) sin recibir datos antes de emitir una alerta por posible fallo o desconexión del equipo. |
| **Gestor de Modelos** | Botón 📁 que abre un explorador de archivos para cargar y actualizar dinámicamente los modelos CRNN de inferencia. |
| **Control Manual** | Botones de encendido/apagado individuales para habilitar o deshabilitar la recepción de datos de los Sensores 1, 2 y 3. |
| **Gestión de Visibilidad** | Botón `Ocultar Detalles / Mostrar Detalles` para alternar la visualización de coordenadas espaciales y direcciones IP en el Gráfico. |

<img width="1919" height="985" alt="Captura de pantalla 2025-05-13 224853" src="https://github.com/user-attachments/assets/5e694a56-cf1b-4794-b054-94aa040131a6" />

---

## 📡 Arquitectura de Conectividad y Procesamiento Multihilo

El sistema opera como una malla distribuida y cooperativa, garantizando baja latencia, eficiencia energética y orden cronológico en la ingesta de datos.

### 🌐 Capa de Red
* **Protocolo de Comunicación (UDP):** Se seleccionó UDP sobre TCP o MQTT por su ligereza y mínima latencia. Se sacrifica una confiabilidad absoluta a cambio de una alta velocidad de despliegue y un consumo de recursos muy reducido en los ESP32.
* **Gestión de Direcciones:** Cada nodo ESP32 se identifica mediante un par `IP:Puerto` específico, permitiendo múltiples flujos simultáneos hacia la estación central.

### 🧵 Procesamiento Concurrente
> *"En sistemas de audio en tiempo real, sin conectividad determinista no hay procesamiento fiable."*

* **Arquitectura Multihilo:** Separación de responsabilidades para evitar bloqueos. 
    * *Hilo Productor:* Captura constante del flujo de audio.
    * *Hilo Consumidor:* Procesa la información sin interrumpir la escucha continua.
* **Colas FIFO:** Se utilizan buffers intermedios (*First-In, First-Out*) para absorber diferencias de velocidad de procesamiento y garantizar que los paquetes de audio conserven su estricto orden cronológico.

<img width="876" height="539" alt="Captura de pantalla 2025-05-27 021728" src="https://github.com/user-attachments/assets/f9644b42-f665-4f28-af65-e535ff24cb6e" />

### 🎛️ Pipeline de Señal Digital (DSP)
Antes de ingresar a la CRNN, las ventanas de audio (4s a 22050 Hz) son refinadas:
1.  **Normalización de amplitud:** Coloca todas las señales en un rango homogéneo.
2.  **Reducción de ruido ambiental:** Estima el perfil de ruido inicial y lo atenúa.
3.  **Filtrado de Wiener:** Maximiza la relación señal-ruido en entornos complejos (viento, tráfico, voces) sin distorsionar la señal.

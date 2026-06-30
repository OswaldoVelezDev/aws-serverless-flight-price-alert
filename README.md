# ✈️ AWS Serverless Flight Price Alert System

Este proyecto implementa una solución serverless sobre Amazon Web Services (AWS) que monitorea precios simulados de vuelos y envía automáticamente una notificación por correo electrónico cuando detecta una disminución en la tarifa.

La solución fue desarrollada utilizando una arquitectura basada en eventos (Event-Driven Architecture), integrando AWS Lambda, Amazon EventBridge, Amazon DynamoDB, Amazon SNS y Amazon SES para automatizar el procesamiento y el envío de notificaciones sin necesidad de administrar servidores.

## 📸 Evidencias del Proyecto

Haga clic en los siguientes enlaces para ver las capturas de pantalla del despliegue técnico:

1. [📂 Arquitectura del Sistema](Evidencias/Diagrama_AWS.png)
2. [📂 Configuración de Permisos IAM](Evidencias/se_agregan_los_permisos.png)
3. [📂 Base de Datos DynamoDB](Evidencias/tablas_pobladas.png)
4. [📂 Lógica en AWS Lambda](evidencias/escribimos_la_funcion_lambda.png)
5. [📂 Disparador EventBridge](Evidencias/trigger_y_conexion_verificados.png)
6. [📂 Prueba de Envío SES](Evidencias/mostrando_correos_SES.png)
7. [📂 Alertas SNS y SES](Evidencias/correo_llegando_tanto_SNS_y_SES.png)
8. [📂 Análisis de Costos](Evidencias/costo_estimado.png)

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Servicios Cloud:** AWS Lambda, DynamoDB, SES, SNS, EventBridge.
- **Seguridad:** IAM Roles con políticas de mínimo privilegio.

- [📄 Descargar Documentación completa en pdf](./Documentacion_Tecnica_Avianca.pdf)

## 🛠️ Galería Técnica Completa
Para revisar el despliegue detallado de los 30 pasos de configuración, puede acceder directamente a la carpeta de evidencias:

👉 **[Ver todas las evidencias técnicas (30 capturas)](./Evidencias/)**
---
*© 2026 Oswaldo Velez - cloud architect*

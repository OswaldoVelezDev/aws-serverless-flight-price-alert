# ✈️ Proyect: ✈️ AWS Serverless Flight Price Alert System

This project is a serverless solution built on Amazon Web Services (AWS) that monitors simulated flight prices and automatically sends email notifications when a lower fare is detected.

The application uses an event-driven architecture powered by Amazon EventBridge, AWS Lambda, Amazon DynamoDB, Amazon SNS and Amazon SES, providing a scalable, low-cost and fully managed cloud solution without the need to manage servers.

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

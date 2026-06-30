# ✈️ AWS Serverless Flight Price Alert System

> A serverless application built on AWS that monitors simulated flight prices and automatically notifies users by email when a lower fare is detected.

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=awslambda)
![Amazon DynamoDB](https://img.shields.io/badge/Amazon-DynamoDB-4053D6?logo=amazondynamodb)
![Amazon EventBridge](https://img.shields.io/badge/Amazon-EventBridge-FF4F8B)
![Amazon SNS](https://img.shields.io/badge/Amazon-SNS-FF9900)
![Amazon SES](https://img.shields.io/badge/Amazon-SES-232F3E)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---
## 📖 Project Overview

This project implements a **serverless cloud solution** on **Amazon Web Services (AWS)** that monitors simulated flight prices and automatically notifies users by email when a lower fare is detected.

The application follows an **Event-Driven Architecture**, where Amazon EventBridge triggers AWS Lambda functions responsible for processing flight data, evaluating price changes, storing information in Amazon DynamoDB, and sending notifications through Amazon SNS and Amazon SES.

The solution was designed to demonstrate how AWS managed services can be integrated to build scalable, cost-effective, and fully serverless applications without managing traditional servers.

### Business Scenario

Many travelers miss airline promotions because checking ticket prices manually is time-consuming and inefficient.

This project simulates an automated monitoring service that continuously evaluates flight prices and immediately notifies subscribed users whenever a lower price is available.

---
# 🏗️ Solution Architecture

The application is built following a **serverless event-driven architecture** using fully managed AWS services.

Instead of relying on traditional servers, the system reacts automatically to scheduled events, processes flight information, stores data, and sends email notifications without requiring infrastructure management.

This architecture provides:

- High scalability
- Low operational cost
- Automatic execution
- Minimal infrastructure management
- Easy maintenance
- High availability

The following AWS services are integrated to build the complete solution:

| AWS Service | Purpose |
|------------|---------|
| Amazon EventBridge | Triggers scheduled events to start the monitoring process. |
| AWS Lambda | Executes the application logic and processes flight information. |
| Amazon DynamoDB | Stores user subscriptions and flight monitoring data. |
| Amazon SNS | Publishes notification events. |
| Amazon SES | Sends email alerts to subscribed users. |
| AWS IAM | Manages permissions and secure access between AWS services. |

## 📐 Architecture Diagram

> The complete architecture diagram will be added in the next section.

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

import boto3
import random
import json
from datetime import datetime, timedelta

# Inicializamos los recursos de AWS
dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')
sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        tabla_sub = dynamodb.Table('Suscripciones_Avianca')
        tabla_historial = dynamodb.Table('Historial_Precios')
        
        response = tabla_sub.scan()
        items = response.get('Items', [])
        
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")

        for item in items:
            # 1. Filtro de Estado
            estado_usuario = str(item.get('Estado', 'Activo')).strip().capitalize()
            email = str(item.get('Email_Viajero', '')).strip()
            
            if estado_usuario != 'Activo':
                continue 

            # 2. Datos de la Suscripción
            id_sub = item['Suscripcion_id']
            ruta_real = str(item.get('Ruta', 'SIN-RUTA')).strip()
            umbral = float(item.get('Umbral_Precio', 0))
            estado_alerta = str(item.get('alerta_enviada', 'No')).strip().capitalize()
            
            # 3. Simulación de Precios
            internacionales = ['MAD', 'MIA', 'MEX', 'EZE', 'JFK']
            es_internacional = any(ciudad in ruta_real for ciudad in internacionales)
            
            if es_internacional:
                precio_actual = random.randint(1800000, 4200000)
            else:
                precio_actual = random.randint(180000, 650000)
            
            # 4. Historial
            tabla_historial.put_item(
                Item={
                    'Ruta': ruta_real,
                    'timestamp': datetime.now().isoformat(),
                    'precio_detectado': precio_actual
                }
            )

            # 5. Lógica de Alerta
            if precio_actual <= umbral:
                if estado_alerta == 'No':
                    
                    # --- CONSTRUCCIÓN DEL LINK CON RUTA ---
                    # Extraemos los códigos
                    codigos = ruta_real.split('-')
                    origen = codigos[0] if len(codigos) > 0 else "BOG"
                    destino = codigos[1] if len(codigos) > 1 else "MDE"

                    #definimos una fecha
                    fecha_vuelo = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
                    
                    # Link que pre-carga el origen y destino en la búsqueda de Avianca
                    link_compra_directa = f"https://www.avianca.com/es/ofertas-vuelos/?origin={origen}&destination={destino}"
                    # Envío por SES
                    ses.send_email(
                        Source='Avianca Ofertas <oswaldovelez1995@gmail.com>',
                        Destination={'ToAddresses': [email]},
                        Message={
                            'Subject': {'Data': f'✈️ ¡OFERTA DETECTADA! {ruta_real} bajó de precio'},
                            'Body': {
                                'Html': {
                                    'Data': f"""
                                    <html>
                                        <body style="margin:0; padding:0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
                                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #f4f4f4; padding: 20px;">
                                                <tr>
                                                    <td align="center">
                                                        <table width="600" border="0" cellspacing="0" cellpadding="0" style="background-color: #ffffff; border-radius: 10px; overflow: hidden;">
                                                            <tr bgcolor="#E30613">
                                                                <td align="center" style="padding: 25px;">
                                                                    <h1 style="color: #ffffff; margin: 0; font-size: 26px;">AVIANCA MONITOR</h1>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td style="padding: 40px 30px; text-align: center;">
                                                                    <h2 style="color: #333333;">¡Es el momento de volar!</h2>
                                                                    <p style="color: #666666; font-size: 16px;">Nuestro sistema ha detectado una tarifa especial para tu ruta <b>{origen}</b> a <b>{destino}</b>.</p>
                                                                    
                                                                    <div style="margin: 30px 0; padding: 25px; border: 2px solid #E30613; border-radius: 15px; background-color: #fffafa;">
                                                                        <p style="margin: 0; color: #666666; font-size: 14px; text-transform: uppercase;">Mejor precio hoy ({fecha_hoy})</p>
                                                                        <p style="margin: 10px 0; color: #28a745; font-size: 36px; font-weight: bold;">${precio_actual:,.0f} COP</p>
                                                                    </div>

                                                                    <p style="color: #333333; font-size: 14px; margin-bottom: 25px;">Haz clic abajo para ver los vuelos disponibles en esta ruta.</p>

                                                                    <a href="{link_compra_directa}" target="_blank" style="background-color: #E30613; color: #ffffff; padding: 18px 40px; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 18px; display: inline-block;">
                                                                        COMPRAR AHORA
                                                                    </a>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td bgcolor="#333333" style="padding: 20px; color: #ffffff; font-size: 11px; text-align: center;">
                                                                    Este es un sistema automatizado.<br>
                                                                    *Verifica la disponibilidad de la tarifa seleccionando tu fecha de viaje.<br>
                                                                    © 2026 Oswaldo Velez - Cloud Architecture
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </body>
                                    </html>
                                    """
                                }
                            }
                        }
                    )

                    # Notificación SNS
                    sns.publish(
                        TopicArn='arn:aws:sns:us-east-1:012504445420:Alertas_Ventas_Avianca', 
                        Message=f"OFERTA ENVIADA: {email} | Ruta: {ruta_real} | Precio: ${precio_actual:,.0f}",
                        Subject="Alerta Comercial Avianca"
                    )
                    
                    tabla_sub.update_item(
                        Key={'Suscripcion_id': id_sub, 'Ruta': ruta_real},
                        UpdateExpression="set alerta_enviada = :r",
                        ExpressionAttributeValues={':r': 'Si'}
                    )
            
            else:
                if estado_alerta == 'Si':
                    tabla_sub.update_item(
                        Key={'Suscripcion_id': id_sub, 'Ruta': ruta_real},
                        UpdateExpression="set alerta_enviada = :r",
                        ExpressionAttributeValues={':r': 'No'}
                    )

        return {"status": "success", "message": "Procesamiento con link de ruta finalizado"}

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {"status": "error", "message": str(e)}

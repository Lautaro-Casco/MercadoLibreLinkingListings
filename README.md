# Mercado Libre Stock Synchronizer
## 🇬🇧 English

A Python application that synchronizes stock between two Mercado Libre publications of the same product.

### Prerequisites
- Python 3.x
- Mercado Libre Developer account
- Two existing publications on Mercado Libre

### Installation
1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Copy `.env.example` to `.env` and fill in your Mercado Libre credentials:
```bash
cp .env.example .env
```

### Configuration
Edit the `.env` file with your credentials:
- ML_CLIENT_ID: Your Mercado Libre application client ID
- ML_CLIENT_SECRET: Your Mercado Libre application client secret
- ML_REDIRECT_URI: Your application's redirect URI
- ML_ACCESS_TOKEN: Your Mercado Libre access token
- ML_REFRESH_TOKEN: Your Mercado Libre refresh token
- ML_PUBLICATION_1_ID: ID of the first publication
- ML_PUBLICATION_2_ID: ID of the second publication
- SYNC_INTERVAL: Synchronization interval in minutes

### Usage
Run the synchronization service:
```bash
python sync_service.py
```

The service will:
- Check stock levels every X minutes (defined in SYNC_INTERVAL)
- Synchronize stock levels if they differ
- Log all activities and errors

---

## 🇪🇸 Español

Una aplicación Python que sincroniza el stock entre dos publicaciones de Mercado Libre del mismo producto.

### Prerrequisitos
- Python 3.x
- Cuenta de desarrollador de Mercado Libre
- Dos publicaciones existentes en Mercado Libre

### Instalación
1. Clonar este repositorio
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```
3. Copiar `.env.example` a `.env` y completar con tus credenciales de Mercado Libre:
```bash
cp .env.example .env
```

### Configuración
Editar el archivo `.env` con tus credenciales:
- ML_CLIENT_ID: ID de cliente de tu aplicación de Mercado Libre
- ML_CLIENT_SECRET: Secreto de cliente de tu aplicación de Mercado Libre
- ML_REDIRECT_URI: URI de redirección de tu aplicación
- ML_ACCESS_TOKEN: Token de acceso de Mercado Libre
- ML_REFRESH_TOKEN: Token de actualización de Mercado Libre
- ML_PUBLICATION_1_ID: ID de la primera publicación
- ML_PUBLICATION_2_ID: ID de la segunda publicación
- SYNC_INTERVAL: Intervalo de sincronización en minutos

### Uso
Ejecutar el servicio de sincronización:
```bash
python sync_service.py
```

El servicio:
- Verificará los niveles de stock cada X minutos (definido en SYNC_INTERVAL)
- Sincronizará los niveles de stock si son diferentes
- Registrará todas las actividades y errores 
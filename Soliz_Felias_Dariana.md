# 🚀 Sistema de Publicación Inteligente en Redes Sociales

Sistema completo de generación automática de contenido con IA y publicación multi-plataforma usando OpenAI GPT y APIs de redes sociales.

## LINK DEL REPOSITORIO
https://github.com/DarianaSoliz/llm_topicos.git

## 📋 Descripción del Proyecto

Este proyecto es una **API REST inteligente** que permite:

- 🤖 **Generación automática de contenido** usando OpenAI GPT-3.5 Turbo
- 🎨 **Creación de imágenes** con DALL-E 3
- 📱 **Publicación automática** en Facebook, Instagram y LinkedIn
- 🌍 **Optimización por plataforma** (contenido específico para cada red social)
- 💬 **Comandos en lenguaje natural** ("Publica en Instagram sobre nuestro nuevo producto")
- 📊 **API REST completa** con FastAPI

## ⭐ Características Principales

### 🎯 Funcionalidades Core
- **Publicación directa**: Publica texto e imágenes en Facebook, Instagram y LinkedIn
- **Generador inteligente**: Crea contenido optimizado para cada plataforma
- **DALL-E Integration**: Genera imágenes automáticamente con IA
- **Comandos naturales**: Procesa instrucciones en lenguaje cotidiano
- **Preview de contenido**: Vista previa antes de publicar
- **Diagnóstico**: Verifica configuración de tokens y APIs

### 🌐 Plataformas Soportadas
- **Facebook**: Texto e imágenes
- **Instagram**: Imágenes con caption
- **LinkedIn**: Texto e imágenes (personal y organizacional)

### 🧠 Inteligencia Artificial
- **OpenAI GPT-3.5 Turbo**: Generación de contenido
- **DALL-E 3**: Creación de imágenes
- **Prompts especializados**: Optimización por plataforma
- **Control de tonalidad**: Profesional, casual, viral, etc.

## 🛠️ Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- Cuenta de OpenAI con API key
- Tokens de acceso para Facebook/Instagram y LinkedIn

### 1. Clonar el Proyecto
```bash
git clone <repository-url>
cd top
```

### 2. Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Copia el archivo de ejemplo:
```bash
copy .env.example .env
```

Edita el archivo `.env` con tus credenciales:

```env
# OpenAI
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-3.5-turbo

# Facebook e Instagram
PAGE_ID=tu-page-id
IG_USER_ID=tu-instagram-user-id
PAGE_ACCESS_TOKEN=tu-facebook-access-token

# LinkedIn
LINKEDIN_CLIENT_ID=tu-linkedin-client-id
LINKEDIN_CLIENT_SECRET=tu-linkedin-client-secret
LINKEDIN_ACCESS_TOKEN=tu-linkedin-access-token
LINKEDIN_PERSONAL_ID=tu-linkedin-personal-id
LINKEDIN_ORG_ID=tu-linkedin-organization-id

# Configuración
LOG_LEVEL=INFO
```

## 🔑 Obtener Credenciales de APIs

### OpenAI API Key
1. Ve a [OpenAI Platform](https://platform.openai.com/)
2. Crea una cuenta o inicia sesión
3. Ve a "API Keys" y crea una nueva key
4. Copia la key al archivo `.env`

### Facebook/Instagram API
1. Ve a [Facebook Developers](https://developers.facebook.com/)
2. Crea una app
3. Agrega los productos "Facebook Login" e "Instagram Basic Display"
4. Obtén:
   - `PAGE_ID`: ID de tu página de Facebook
   - `IG_USER_ID`: Instagram User ID (debe empezar con '17' y tener 17 dígitos)
   - `PAGE_ACCESS_TOKEN`: Token de acceso de página con permisos de publicación

### LinkedIn API
1. Ve a [LinkedIn Developers](https://www.linkedin.com/developers/)
2. Crea una aplicación
3. Solicita acceso a "Share on LinkedIn" y "Sign In with LinkedIn"
4. Obtén:
   - `LINKEDIN_CLIENT_ID`: Client ID de tu app
   - `LINKEDIN_CLIENT_SECRET`: Client Secret
   - `LINKEDIN_ACCESS_TOKEN`: Token de acceso del usuario
   - `LINKEDIN_PERSONAL_ID`: Tu LinkedIn ID personal

## 🚀 Ejecutar el Proyecto

### 1. Iniciar la API
```bash
python run_api.py
```

La API estará disponible en: `http://localhost:8000`

### 2. Verificar Configuración
Visita: `http://localhost:8000/diagnostics`

### 3. Ver Documentación Interactiva
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📖 Guía de Uso

### 🤖 Comando Inteligente (Recomendado)

El endpoint más poderoso permite usar **lenguaje natural**:

```bash
POST http://localhost:8000/smart-publish
Content-Type: application/json

{
    "command": "Quiero publicar en Instagram sobre nuestro nuevo café con una imagen moderna",
    "test_mode": false
}
```

**Ejemplos de comandos:**
- `"Publica en Facebook e Instagram sobre el evento de mañana"`
- `"Crea un post para LinkedIn sobre nuestra empresa con imagen profesional"`
- `"Comparte en todas las redes sociales sobre nuestro lanzamiento"`
- `"Publica en Instagram sobre tecnología con imagen futurista"`

### 📝 Generación de Contenido

Para generar contenido sin publicar automáticamente:

```bash
POST http://localhost:8000/generate-content
Content-Type: application/json

{
    "heading": "Lanzamiento de nuestro nuevo producto",
    "material": "Estamos emocionados de presentar nuestra nueva aplicación...",
    "platforms": ["facebook", "instagram", "linkedin"],
    "auto_publish": false,
    "image_url": "https://example.com/image.jpg"
}
```

### 👁️ Vista Previa

Para ver cómo se verá el contenido antes de publicar:

```bash
POST http://localhost:8000/preview-content
Content-Type: application/json

{
    "heading": "Evento de tecnología 2025",
    "material": "Te invitamos a nuestro evento...",
    "platforms": ["facebook", "instagram", "linkedin"]
}
```

### 🎯 Publicación Directa

#### Instagram
```bash
POST http://localhost:8000/publish/instagram
Content-Type: application/json

{
    "image_url": "https://example.com/image.jpg",
    "caption": "¡Mira nuestro nuevo producto! #Innovation #Tech"
}
```

#### Facebook (Texto)
```bash
POST http://localhost:8000/publish/facebook/text
Content-Type: application/json

{
    "message": "¡Grandes noticias! Lanzamos nuestro nuevo producto."
}
```

#### Facebook (Imagen)
```bash
POST http://localhost:8000/publish/facebook/image
Content-Type: application/json

{
    "image_url": "https://example.com/image.jpg",
    "caption": "¡Mira nuestro nuevo producto!"
}
```

#### LinkedIn (Texto)
```bash
POST http://localhost:8000/publish/linkedin/text
Content-Type: application/json

{
    "message": "Orgullosos de anunciar nuestro nuevo hito empresarial."
}
```

#### LinkedIn (Imagen)
```bash
POST http://localhost:8000/publish/linkedin/image
Content-Type: application/json

{
    "image_url": "https://example.com/image.jpg",
    "message": "Imagen de nuestro evento corporativo."
}
```

## 🧪 Ejecutar Pruebas

El proyecto incluye un sistema completo de pruebas:

```bash
# Ver casos de prueba disponibles
python tests/test_all_cases.py --list

# Ejecutar caso específico
python tests/test_all_cases.py --caso corporativo

# Ejecutar todos los casos
python tests/test_all_cases.py --all

# Modo interactivo
python tests/test_all_cases.py --interactive
```

### Casos de Prueba Incluidos

1. **Corporativo**: Anuncio de milestone empresarial
2. **Producto**: Lanzamiento de nueva aplicación
3. **Evento**: Invitación a conferencia

## 📁 Estructura del Proyecto

```
top/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias de Python
├── run_api.py               # Punto de entrada de la API
├── .env.example             # Plantilla de variables de entorno
├── facebook_token.json      # (generado automáticamente)
├── docs/                    # Documentación técnica
│   ├── clase-02-desarrollo.md
│   └── prompts.md
├── src/                     # Código fuente principal
│   ├── config.py           # Configuración y variables de entorno
│   ├── api/
│   │   ├── __init__.py
│   │   └── main.py         # Endpoints de la API REST
│   └── services/           # Lógica de negocio
│       ├── __init__.py
│       ├── llm_adapter.py           # Adaptador de OpenAI GPT
│       ├── content_publisher.py     # Publicador de contenido
│       ├── intelligent_publisher.py # Procesador de comandos naturales
│       ├── facebook_service.py      # Servicio de Facebook
│       ├── instagram_service.py     # Servicio de Instagram
│       └── linkedin_service.py      # Servicio de LinkedIn
├── tests/                   # Sistema de pruebas
│   ├── test_all_cases.py   # Casos de prueba unificados
│   └── test_producto.py    # Caso específico de producto
├── temp_images/            # Imágenes temporales (generado automáticamente)
└── logs/                   # Archivos de log (generado automáticamente)
```

## 🎨 Optimización por Plataforma

### Facebook
- **Estilo**: Conversacional y cercano
- **Límite**: 63,206 caracteres
- **Emojis**: Uso moderado (1-3 por post)
- **Hashtags**: Máximo 5, enfocados en engagement
- **Objetivo**: Generar interacción y comentarios

### Instagram
- **Estilo**: Visual, inspirador y moderno
- **Límite**: 2,200 caracteres
- **Emojis**: Uso abundante para impacto visual
- **Hashtags**: 5-10, combinando populares y específicos
- **Especial**: Incluye `suggested_image_prompt` para DALL-E
- **Objetivo**: Narrativa visual y engagement

### LinkedIn
- **Estilo**: Profesional, informativo y valioso
- **Límite**: 3,000 caracteres
- **Emojis**: Uso mínimo, solo para énfasis estratégico
- **Hashtags**: 3-5, enfocados en sector profesional
- **Objetivo**: Compartir conocimiento, networking, valor corporativo

## 🔧 Funcionalidades Técnicas

### Generación Inteligente de Contenido
- **Prompts especializados** por cada plataforma
- **Control de temperatura** para creatividad variable
- **Validación automática** de límites de caracteres
- **Limpieza de formato** JSON automática

### Integración DALL-E 3
- **Generación automática** de imágenes basada en contenido
- **Prompts optimizados** para redes sociales
- **Descarga y conversión** a URLs públicas
- **Integración con Facebook API** para almacenamiento

### Manejo de Errores
- **Logging completo** de todas las operaciones
- **Recuperación automática** ante fallos de API
- **Validación de tokens** y configuración
- **Mensajes de error** informativos

## 🐛 Solución de Problemas

### Error: "OPENAI_API_KEY no configurada"
1. Verifica que el archivo `.env` existe
2. Confirma que `OPENAI_API_KEY` está configurado correctamente
3. Reinicia el servidor después de cambios en `.env`

### Error en Instagram: "Invalid IG User ID"
1. El `IG_USER_ID` debe empezar con '17' y tener exactamente 17 dígitos
2. Obtén el ID correcto desde Facebook Graph API Explorer
3. Verifica que la cuenta de Instagram está conectada a la página de Facebook

### Error en LinkedIn: "Insufficient privileges"
1. Verifica que tu app tiene permisos "Share on LinkedIn"
2. El `LINKEDIN_ACCESS_TOKEN` debe tener scope `w_member_social`
3. Regenera el token si es necesario

### Error: "Image URL not accessible"
1. Asegúrate de que las URLs de imágenes sean públicamente accesibles
2. Facebook e Instagram requieren HTTPS
3. Verifica que el servidor de imágenes permite hotlinking

## 📊 Monitoreo y Logs

Los logs se guardan automáticamente en:
- **Consola**: Información en tiempo real
- **Archivos**: `logs/` (cuando esté configurado)

### Niveles de Log
- `INFO`: Operaciones normales
- `ERROR`: Errores de API o procesamiento
- `DEBUG`: Información detallada de desarrollo

## 🚀 Despliegue en Producción

### Variables de Entorno Adicionales
```env
# Producción
ENVIRONMENT=production
DEBUG=false
HOST=0.0.0.0
PORT=8000

# Seguridad
ALLOWED_HOSTS=tu-dominio.com
CORS_ORIGINS=https://tu-frontend.com
```

### Docker (Opcional)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "run_api.py"]
```

## 🤝 Contribución

1. Fork del proyecto
2. Crear rama para feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 🆘 Soporte

Para preguntas o problemas:

1. **Documentación**: Revisa este README y la documentación en `/docs`
2. **Issues**: Crea un issue en GitHub con detalles del problema
3. **Logs**: Incluye logs relevantes en tus reportes de problemas
4. **Configuración**: Verifica `/diagnostics` para problemas de configuración

## 🎯 Roadmap

### Versión Actual (1.0)
- ✅ Publicación en Facebook, Instagram, LinkedIn
- ✅ Generación de contenido con GPT-3.5
- ✅ Integración DALL-E 3
- ✅ Comandos en lenguaje natural
- ✅ API REST completa

### Próximas Versiones
- 🔄 Soporte para Twitter/X
- 🔄 Programación de publicaciones
- 🔄 Analytics y métricas
- 🔄 Interface web
- 🔄 Webhooks para notificaciones
- 🔄 Soporte para videos
- 🔄 Integración con más modelos de IA

---

⭐ **¡Si este proyecto te fue útil, no olvides darle una estrella en GitHub!** ⭐
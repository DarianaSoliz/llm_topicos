import requests
from src.config import PAGE_ID, PAGE_ACCESS_TOKEN


def facebook_post_text(message: str):
    """
    Publica un mensaje de texto en Facebook.
    
    Args:
        message (str): Mensaje de texto a publicar
        
    Returns:
        dict: Respuesta de la API de Facebook con el resultado de la publicación
    """
    url = (
        f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
        f"?message={message}"
        f"&access_token={PAGE_ACCESS_TOKEN}"
    )

    response = requests.post(url)
    return response.json()


def facebook_post_image(image_url: str, caption: str):
    """
    Publica una imagen con caption en Facebook.
    cccccc
    Args:c
        image_url (str): URL de la imagen a publicmagen
        
    Returns:
        dict: Respuesta de la API de Facebook con el resultado de la publicación
    """
    url = (
        f"https://graph.facebook.com/v19.0/{PAGE_ID}/photos"
        f"?url={image_url}"
        f"&caption={caption}"
        f"&access_token={PAGE_ACCESS_TOKEN}"
    )

    response = requests.post(url)
    return response.json()

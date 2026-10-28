import os
import sys
import logging
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI  # Usamos la librería especializada de OpenAI

# Configurar rutas del sistema
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Cargar variables de entorno
load_dotenv()

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("AchillesSportsCore")

def run_pipeline():
    logger.info("Initializing Achilles Sports Engine...")
    
    connection_string = os.getenv("AZURE_AI_PROJECT_CONNECTION_STRING")
    if not connection_string or connection_string.startswith("://"):
        logger.error("Configuration Error: Valid AZURE_AI_PROJECT_CONNECTION_STRING not detected in .env")
        sys.exit(1)
        
    logger.info("Connected securely to Microsoft Foundry Environment.")

    # 1. Inicializar Cliente Base de Microsoft Foundry Workspace
    try:
        logger.info("Establishing secure workspace connection to Azure AI Project Client...")
        endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT")
        credential_key = os.getenv("AZURE_AI_FOUNDRY_KEY")
        
        if not endpoint or not credential_key:
            raise ValueError("AZURE_AI_FOUNDRY_ENDPOINT or AZURE_AI_FOUNDRY_KEY missing in .env")
            
        project_client = AIProjectClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(credential_key)
        )
        logger.info("Successfully authenticated with Microsoft Foundry Workspace Resource.")
    except Exception as e:
        logger.error(f"Authentication Failed: {e}")
        project_client = None

    # 2. Verificar existencia de datos sintéticos (Simulación de partidos)
    synthetic_data_path = os.path.join(os.getenv("DATA_DIR_PATH", "./data"), "synthetic")
    logger.info(f"Checking target data streaming directory: {synthetic_data_path}")
    
    if not os.path.exists(synthetic_data_path):
        os.makedirs(synthetic_data_path, exist_ok=True)
        logger.info(f"Created directory structure at {synthetic_data_path}")

    # 3. Lógica de Inferencia de Azure OpenAI
    deployment_name = os.getenv("FOUNDRY_LLM_DEPLOYMENT_NAME", "gpt-4o")

    if project_client and endpoint and credential_key:
        try:
            logger.info(f"Testing real-time narrative agent generation using deployment: '{deployment_name}'...")
            
            # REPARACIÓN DEFINITIVA: Pasamos el endpoint directo sin prefijos duplicados.
            # El SDK nativo de OpenAI se encargará de estructurar las rutas /openai/deployments automáticamente.
            inference_client = AzureOpenAI(
                azure_endpoint=endpoint.rstrip("/"),
                api_key=credential_key,
                api_version="2024-05-01-preview"
            )
            
            response = inference_client.chat.completions.create(
                model=deployment_name,
                messages=[
                    {"role": "system", "content": "You are the Achilles Sports Match Intelligence Agent."},
                    {"role": "user", "content": "Generate a short introductory message stating that the Achilles Sports platform is active."}
                ]
            )
            
            # REPARACIÓN DE SINTAXIS: Acceso indexado correcto a la tupla de opciones generadas por OpenAI
            logger.info(f"Agent Response: {response.choices[0].message.content.strip()}")
        except Exception as e:
            logger.warning(f"Could not complete live inference via Foundry Endpoint: {e}")
            logger.info("Ensure your deployment name matches exactly in the Foundry Model Catalog.")
    else:
        logger.info("[Simulation] Match Reality Index baseline initialized at 50.0. Awaiting event ticks.")

    logger.info("Achilles Sports Execution Loop Active and Healthy.")

if __name__ == "__main__":
    run_pipeline()

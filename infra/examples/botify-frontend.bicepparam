using '../../apps/frontend/azuredeploy-frontend-private.bicep'

param resourceNameSuffix='btfy-dev-use2'
param uiContainerImage = 'retaildevcrews/botify-frontend:beta'
param existingAcrName='acrbtfydev001'

param uiConfigurationValues = [
  'SPEECH_ENGINE=azure'
  'AZURE_OPENAI_MODEL_NAME=${readEnvironmentVariable('AZURE_OPENAI_WHISPER_MODEL_NAME', 'whisper')}'
  //"azure"
  'AZURE_SPEECH_VOICE_NAME=${readEnvironmentVariable('AZURE_SPEECH_VOICE_NAME', 'en-US-AvaMultilingualNeural')}'
  //'AZURE_SPEECH_REGION=${readEnvironmentVariable('AZURE_SPEECH_REGION', 'eastus2')}'
  //"openai"
  'AZURE_OPENAI_WHISPER_MODEL_NAME=${readEnvironmentVariable('AZURE_OPENAI_WHISPER_MODEL_NAME', 'whisper')}'
  'AZURE_OPENAI_TTS_VOICE_NAME=${readEnvironmentVariable('AZURE_OPENAI_TTS_VOICE_NAME', 'nova')}'
  'AZURE_OPENAI_TTS_MODEL_NAME=${readEnvironmentVariable('AZURE_OPENAI_TTS_MODEL_NAME', 'tts')}'
  'AZURE_SPEECH_CUSTOM_MODEL_ENDPOINT_ID=${readEnvironmentVariable('AZURE_SPEECH_CUSTOM_MODEL_ENDPOINT_ID', 'af382c02-4233-4014-acff-efea04ccff17')}'
]

param uiConfigurationSecretNames = [
  'AZURE_SPEECH_ENDPOINT=AzureSpeechEndpoint'
  'AZURE_SPEECH_KEY=AzureSpeechApiKey'
  'AZURE_OPENAI_ENDPOINT=AzureOpenAIEndpoint'
  'AZURE_OPENAI_API_KEY=AzureOpenAIApiKey'
  'API_KEY=ApimDevKey'
  'FAST_API_SERVER=BackendUrl'
]

// Optional parameters
param speechPublicAccessEnabled = true
/* param vaultSecrets = {
  AzureSpeechEndpoint : readEnvironmentVariable('AZURE_SPEECH_ENDPOINT', '')
  AzureSpeechApiKey: readEnvironmentVariable('AZURE_SPEECH_KEY', '')
}
 */

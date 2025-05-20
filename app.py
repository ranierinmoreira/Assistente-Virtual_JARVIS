# pip install speechRecognition
# pip install pyaudio
# pip install pyttsx3
# pip install -U google.generativeai
import speech_recognition as sr
import os
import pyttsx3
import google.generativeai as genai


# CONFIGURAÇÕES JARVIS


# Inicializar o engine de síntese de fala
engine = pyttsx3.init()

def falar(texto):
  # Faz o computador falar
  engine.say(texto)
  engine.runAndWait()

def apresentacao():
  # Apresentação
  print("Iniciando o Sistema. Software 100% carregado e operando. Me chamo Jarvis.")
  falar("Iniciando o Sistema. Software 100% carregado e operando. Me chamo Jarvis.")

# Função para ouvir e reconhecer fala:
def ouvir_microfone(primeira_vez):
  # Habilita microfone usuário
  microfone = sr.Recognizer()

  # Apresentação apenas na primeira vez
  if primeira_vez:
      apresentacao()
      primeira_vez = False

  # Usando o microfone
  with sr.Microphone() as source:
      # Chama um algoritmo de redução de ruídos no som
      microfone.adjust_for_ambient_noise(source)

      # Frase para o usuário dizer algo
      print("Como posso te ajudar?")
      falar("Como posso te ajudar?")

      # Armazena o que foi dito numa variável
      audio = microfone.listen(source)

  try:
      # Passa a variável para o algoritmo reconhecer os padrões
      frase = microfone.recognize_google(audio, language="pt-BR")

      if "Iniciar navegador" in frase:
          os.system("start chrome.exe")
          falar("Abrindo o navegador")
      elif "Iniciar calculadora" in frase:
          os.system("start calc.exe")
          falar("Abrindo a calculadora")
      elif "Iniciar Paint" in frase:
          os.system("start mspaint.exe")
          falar("Abrindo o Paint")
      elif "Iniciar bloco de notas" in frase:
          os.system("start notepad.exe")
          falar("Abrindo o bloco de notas")
      elif "Iniciar Excel" in frase:
          os.system("start Excel.exe")
          falar("Abrindo o Excel")
      elif "Iniciar Word" in frase:
          os.system("start winword.exe")
          falar("Abrindo o Word")
      elif "Iniciar CMD" in frase:
          os.system("start cmd.exe")
          falar("Abrindo o prompt de comando")
      elif "Pesquisar" in frase:
          falar("Estou pesquisando.")
          pesquisa = frase.split("Pesquisar", 1)[1].strip()
          if pesquisa:
              resposta = pesquisar_no_google(f"Responda de forma discursiva, com no máximo 30 palavras: {pesquisa}")
              falar(resposta)
          else:
              falar("Por favor, diga o que você quer pesquisar.")
      elif "Desligar o sistema" in frase:
          falar("Finalizando o sistema. Até logo.")
          return True
      else:
          falar(f"O comando {frase} não foi reconhecido, tente novamente.")
  except sr.UnknownValueError:
      print("Não entendi, repita o que deseja.")
      falar("Não entendi, repita o que deseja.")
  return False

# Função para pesquisar no Google usando a API de IA
def pesquisar_no_google(pesquisa):
  # Configurando a API do Google
  GOOGLE_AI_KEY = "SUA CHAVE API AKI"
  genai.configure(api_key=GOOGLE_AI_KEY)
  # Configurando a Temperatura das Respostas
  configurar_geracao = {
      "candidate_count": 1,
      "temperature": 0.8,
  }
  # Configurando os Níveis de Segurança das Respostas (Ofensivas, Raciais, Sexuais, etc.)
  configurar_seguranca = {
      "HARASSMENT": "BLOCK_NONE",
      "HATE": "BLOCK_NONE",
      "SEXUAL": "BLOCK_NONE",
      "DANGEROUS": "BLOCK_NONE",
  }
  # Definindo o Modelo Usado para Pesquisa
  model = genai.GenerativeModel(
      model_name="gemini-1.0-pro",
      generation_config=configurar_geracao,
      safety_settings=configurar_seguranca,
  )
  # Configurando o Histórico de Pesquisa
  chat = model.start_chat(history=[])
  response = chat.send_message(pesquisa)
  return response.text

# LOOP DE EXECUÇÃO DO JARBAS
primeira_vez = True
while True:
  if ouvir_microfone(primeira_vez):
      break
  primeira_vez = False
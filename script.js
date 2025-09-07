let isListening = false;
let startTime = Date.now();

// Atualizar uptime
setInterval(() => {
    const now = Date.now();
    const uptime = now - startTime;
    const hours = Math.floor(uptime / 3600000);
    const minutes = Math.floor((uptime % 3600000) / 60000);
    const seconds = Math.floor((uptime % 60000) / 1000);
    document.getElementById('uptime').textContent = 
        `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}, 1000);

function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    
    if (message) {
        addMessage(message, 'user');
        input.value = '';
        
        // Simular resposta do JARVIS
        setTimeout(() => {
            const responses = [
                "Entendido. Processando sua solicitação...",
                "Analisando os dados fornecidos...",
                "Executando comando conforme solicitado...",
                "Verificando informações no sistema...",
                "Comando processado com sucesso!",
                "Posso ajudá-lo com mais alguma coisa?",
                "Sistema operacional. Aguardando próximas instruções.",
                "Processamento concluído. Status: OK"
            ];
            const randomResponse = responses[Math.floor(Math.random() * responses.length)];
            addMessage(randomResponse, 'jarvis');
        }, 1000);
    }
}

function addMessage(text, sender) {
    const chatContainer = document.getElementById('chatContainer');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${sender}-message`;
    
    const prefix = sender === 'user' ? 'Você:' : 'JARVIS:';
    messageDiv.innerHTML = `<strong>${prefix}</strong> ${text}`;
    
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function toggleVoice() {
    const voiceIndicator = document.getElementById('voiceIndicator');
    isListening = !isListening;
    
    if (isListening) {
        voiceIndicator.classList.add('active');
        // Aqui você pode integrar com Web Speech API
        setTimeout(() => {
            voiceIndicator.classList.remove('active');
            isListening = false;
            addMessage("Comando de voz processado!", 'jarvis');
        }, 3000);
    } else {
        voiceIndicator.classList.remove('active');
    }
}

function clearChat() {
    const chatContainer = document.getElementById('chatContainer');
    chatContainer.innerHTML = '<div class="chat-message jarvis-message"><strong>JARVIS:</strong> Chat limpo. Como posso ajudá-lo?</div>';
}

function showSystemInfo() {
    addMessage("Sistema JARVIS v2.0.1 - Status: Operacional - Uptime: " + document.getElementById('uptime').textContent, 'jarvis');
}

function toggleTheme() {
    // Implementar mudança de tema se necessário
    addMessage("Função de tema em desenvolvimento...", 'jarvis');
}

// Adicionar algumas mensagens de boas-vindas
setTimeout(() => {
    addMessage("Sistema inicializado com sucesso. Todas as funcionalidades estão operacionais.", 'jarvis');
}, 2000);

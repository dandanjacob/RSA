# Implementação do RSA e Experiência Interativa de Criptografia

Este repositório contém uma implementação do algoritmo RSA para criptografia e descriptografia de mensagens. Além disso, há uma experiência prática para demonstração em que os participantes recebem mensagens criptografadas personalizadas e as descriptografam utilizando chaves privadas entregues presencialmente.

---

## Funcionalidades
1. **Gerar números primos:**
   - Adaptável para aceitar primos fornecidos manualmente ou gerados por outra abordagem (recomenda-se uma forma robusta de gerar primos grandes).

2. **Cálculo do MDC:**
   - Implementação do Algoritmo Estendido de Euclides para cálculo do MDC, utilizado no processo de geração de chaves.

3. **Gerador de chaves:**
    - Geração das chaves pública e privada a partir dos números primos fornecidos.

4. **Criptografar mensagens:** 
   - Função que aplica o algoritmo RSA para criptografar mensagens com base em uma chave pública.

5. **Descriptografar mensagens:** 
   - Função que utiliza a chave privada para reverter mensagens criptografadas ao formato original.



---

## Estrutura do Projeto

### Notebook Principal
O notebook principal contém:
- **Implementação completa do RSA:** Incluindo explicações detalhadas de cada etapa.

### Arquivo Python Interativo (`decrypt_message.py`)
Este arquivo (`.py`) permite que os participantes da apresentação insiram suas chaves privadas para descriptografar as mensagens personalizadas enviadas.

---

## Experiência Interativa

Durante a apresentação:
1. Uma **mensagem criptografada personalizada** é enviada para cada participante (nomes extraídos previamente da sua lista de contatos do WhatsApp).
2. **Chaves privadas em papel:** Os participantes recebem suas chaves privadas de forma física.
3. **Script fornecido:** Os participantes utilizam o script Python (`interacao.py`) para descriptografar suas mensagens personalizadas.

---

## Como Usar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/rsa-criptografia.git
   cd rsa-criptografia

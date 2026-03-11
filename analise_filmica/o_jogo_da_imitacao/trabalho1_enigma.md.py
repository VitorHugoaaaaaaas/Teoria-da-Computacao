import math

class EnigmaCompleta:
    def __init__(self):
        # Configurações Históricas (Rotor III e Refletor B)
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor_ii_fio = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        self.refletor_b = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.posicao = 0

    def calcular_espaco_de_busca(self):
        """Calcula o total de combinações possíveis (Atividade 1)"""
        # 1. Arranjo de 3 rotores entre 5 disponíveis
        rotores = math.perm(5, 3) 
        # 2. Posições iniciais (26^3)
        posicoes = 26 ** 3
        # 3. Plugboard (10 cabos conectando 20 letras)
        # Fórmula: 26! / ((26-20)! * 10! * 2^10)
        n, k = 26, 10
        plugboard = math.factorial(n) // (math.factorial(n - 2*k) * math.factorial(k) * (2**k))
        
        total = rotores * posicoes * plugboard
        return total

    def cifrar_caractere(self, letra):
        """Lógica de processamento de uma única letra"""
        if letra not in self.alfabeto:
            return letra
        
        # O rotor gira ANTES da letra ser processada
        self.posicao = (self.posicao + 1) % 26
        
        # 1. Entrada no Rotor (Substituição com deslocamento)
        idx_entrada = (self.alfabeto.index(letra) + self.posicao) % 26
        letra_rotor = self.rotor_ii_fio[idx_entrada]
        
        # 2. Refletor (Garante que A nunca é A)
        idx_refletor = self.alfabeto.index(letra_rotor)
        letra_refletida = self.refletor_b[idx_refletor]
        
        # 3. Volta pelo Rotor (Inverso)
        idx_volta = self.rotor_ii_fio.index(letra_refletida)
        letra_saida = self.alfabeto[(idx_volta - self.posicao) % 26]
        
        return letra_saida

    def processar(self, texto):
        """Cifra ou decifra uma frase completa"""
        self.posicao = 0 # Reset para o início da mensagem
        texto = texto.upper()
        return "".join([self.cifrar_caractere(c) for c in texto])

# --- EXECUÇÃO DO PROGRAMA ---
maquina = EnigmaCompleta()

# PARTE 1: Matemática
total_comb = maquina.calcular_espaco_de_busca()
print(f"--- ANALISE MATEMATICA ---")
print(f"Combinacoes totais da Enigma: {total_comb:,}")
print(f"Em notacao cientifica: {total_comb:.2e}")
print("-" * 30)

# PARTE 2: Simulação (Atividade 2)
print(f"--- SIMULACAO DE MENSAGEM ---")
msg_original = "BOA SORTE TURING"
msg_cifrada = maquina.processar(msg_original)
print(f"Original: {msg_original}")
print(f"Cifrada:  {msg_cifrada}")

# Teste de Reciprocidade (Decifrar)
msg_decifrada = maquina.processar(msg_cifrada)
print(f"Decifrada: {msg_decifrada} (Sucesso!)")

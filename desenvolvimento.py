import random
# from Crypto.Util.number import getPrime, inverse, GCD
from sympy import isprime
from math import gcd


class RSA:
    def __init__(self, bit_length=1024, generate_primes = True, first_prime = None, second_prime = None):
        self.bit_length = bit_length
        self.public_key = None
        self.private_key = None
        self.n = None
        self.generate_primes = generate_primes
        self.first_prime = first_prime
        self.second_prime = second_prime


    def extended_euclid(a, b):

        """
        Implementação do algoritmo estendido de Euclides do zero.
        
        Calcula o máximo divisor comum (MDC) entre a e b e os coeficientes de Bézout.
        
        Args:
            a (int): Primeiro número.
            b (int): Segundo número.
        
        Returns:
            tuple: (mdc, x, y), onde:
                mdc -> Máximo divisor comum entre a e b.
                x, y -> Coeficientes de Bézout tais que a * x + b * y = mdc.
        """
        x0, y0, x1, y1 = 1, 0, 0, 1  # Inicialização dos coeficientes de Bézout
        while b != 0:
            q = a // b  # Quociente da divisão inteira
            a, b = b, a % b  # Atualiza a e b usando o algoritmo de Euclides
            x0, x1 = x1, x0 - q * x1  # Atualiza os coeficientes x
            y0, y1 = y1, y0 - q * y1  # Atualiza os coeficientes y
        return a # a é o MDC, x0 e y0 são os coeficientes de Bézout
    
    def generate_prime(self):
        """Gera um número primo aleatório com o tamanho de bits especificado."""
        while True:
            num = random.getrandbits(self.bit_length // 2) # 2 números gerados, // significa div inteira
            if isprime(num): # verifica se os numeros são primos
                return num
    
    def generate_keys(self):
        """Gera as chaves pública e privada."""
        p=0
        q=0
        if self.generate_primes == True:  # Certifique-se de verificar o nome correto do atributo
            p = self.generate_prime()
            q = self.generate_prime()
        else:
            if self.first_prime is None or self.second_prime is None:
                raise ValueError("Você deve fornecer os dois números primos se 'generate_primes' for False.")
            p = self.first_prime
            q = self.second_prime
        
        self.n = p * q #parte 1 da chave pública
        phi = (p - 1) * (q - 1) # 
        
        # Escolha um 'e' tal que 1 < e < phi e gcd(e, phi) == 1
        # e = 65537  # Valor padrão usado na prática (é primo)
        e = 97
        if phi<=e:
            raise ValueError("Você precisa que e seja menor que phi. \n" +
                            "Por favor, selecione números primos maiores ou " +
                            "escolha uma chave e menor.")

        if RSA.extended_euclid(e, phi) != 1: #função que verifica o MDC entre dois números
            raise ValueError("e não é coprimo com φ(n), tente gerar os primos novamente.")
        
        # Calcula o 'd' (chave privada)
        d = pow(e, -1, phi)
        
        self.public_key = (e, self.n)
        self.private_key = (d, self.n)
    
    def encrypt(self, plaintext):
        """Criptografa uma mensagem, dividindo-a em blocos se necessário."""
        e, n = self.public_key
        max_block_size = (n.bit_length() - 1) // 8  # Calcula o tamanho máximo do bloco em bytes

        # Divide a mensagem em blocos menores que o tamanho máximo
        plaintext_bytes = plaintext.encode('utf-8')
        blocks = [plaintext_bytes[i:i + max_block_size] for i in range(0, len(plaintext_bytes), max_block_size)]

        # Criptografa cada bloco individualmente
        ciphertext_blocks = []
        for block in blocks:
            plaintext_int = int.from_bytes(block, byteorder='big')  # Converte o bloco para inteiro
            ciphertext = pow(plaintext_int, e, n)  # Criptografa o bloco
            ciphertext_blocks.append(ciphertext)

        return ciphertext_blocks  # Retorna a lista de blocos criptografados

    
    def decrypt(self, ciphertext_blocks):
        """
        Descriptografa uma lista de blocos criptografados.
        
        Args:
            ciphertext_blocks (list): Lista de blocos criptografados como inteiros.
        
        Returns:
            str: Mensagem descriptografada como string.
        """
        d, n = self.private_key

        # Descriptografa cada bloco
        plaintext_bytes = b""
        for block in ciphertext_blocks:
            plaintext_int = pow(block, d, n)  # Descriptografa o bloco
            block_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, byteorder='big')
            plaintext_bytes += block_bytes  # Junta os bytes de cada bloco

        return plaintext_bytes.decode('utf-8')  # Converte para string

    
    def get_public_key(self):
        """Retorna a chave pública."""
        return self.public_key
    
    def get_private_key(self):
        """Retorna a chave privada."""
        return self.private_key


# Demonstração de uso
if __name__ == "__main__":
    rsa = RSA(generate_primes=False, first_prime=23, second_prime=29)
    rsa.generate_keys()
    
    print("Chave pública:", rsa.get_public_key())
    print("Chave privada:", rsa.get_private_key())
    
    # mensagem = "Hello, RSA!"
    mensagem = "Piroca é muito bom, queria ter uma pra mamar todos os dias antes de ir dormir."
    print("\nMensagem original:", mensagem)
    
    criptografada = rsa.encrypt(mensagem)
    print("Mensagem criptografada:", criptografada)
    
    descriptografada = rsa.decrypt(criptografada)
    print("Mensagem descriptografada:", descriptografada)